import os
import json
from utils.save import save_workflow
import argparse


source_folder = os.path.join(os.getcwd(), 'source')
workflows_folder = os.path.join(os.getcwd(), 'workflows')
base_url = 'https://kekehurry.github.io/cityflow_community'

def load_file(file_path,author,category):
    file = os.path.basename(file_path)
    with open('community_workflows.json', "r", encoding="utf-8") as f:
        workflows = json.load(f)
    with open(file_path, "r", encoding="utf-8") as f:
        data = json.load(f)
    data['author'] = author
    data = save_workflow(data, source_folder, base_url)
    ouput_folder = os.path.join(workflows_folder, category)
    if not os.path.exists(ouput_folder):
        os.makedirs(ouput_folder)
    with open(os.path.join(ouput_folder, file), "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)
    if category not in workflows:
        workflows[category] = []
    workflows[category].append(base_url+f"/workflows/{category}/{file}")
    return workflows

if __name__ == '__main__':
    # parse parameters from command line use --category and --file
    parser = argparse.ArgumentParser(description='Update community workflows.')
    parser.add_argument('--category', type=str, required=True, help='The category of the workflow.')
    parser.add_argument('--file', type=str, required=True, help='The path to the workflow file.')
    parser.add_argument('--author',type=str, required=True, help='The author of the workflow file.')
    args = parser.parse_args()
    category = args.category
    file_path = args.file
    author = args.author
    workflows = load_file(file_path,author,category)
    with open('community_workflows.json', "w", encoding="utf-8") as f:
        json.dump(workflows, f, ensure_ascii=False, indent=2)