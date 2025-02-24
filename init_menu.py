import os
import shutil
import json
from utils.save import save_workflow



source_folder = os.path.join(os.getcwd(), 'source')
raw_folder = os.path.join(os.getcwd(), 'raw')
workflows_folder = os.path.join(os.getcwd(), 'workflows')

if os.path.exists(source_folder):
    shutil.rmtree(source_folder)
    
for folder in ['files','icons','images','html']:
    if not os.path.exists(os.path.join(source_folder,folder)): 
        os.makedirs(os.path.join(source_folder,folder))

base_url = 'https://kekehurry.github.io/cityflow_community'

workflows = {}
for d in os.listdir(raw_folder):
    folder_path = os.path.join(raw_folder, d)
    if os.path.isdir(folder_path):
        files = []
        for file in os.listdir(folder_path):
            if file.endswith(".csflow.json"):
                file_path = os.path.join(folder_path, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    data = json.load(f)
                    data = save_workflow(data, source_folder, base_url, admin=True)
                ouput_folder = os.path.join(workflows_folder, d)
                if not os.path.exists(ouput_folder):
                    os.makedirs(ouput_folder)
                with open(os.path.join(ouput_folder, file), "w", encoding="utf-8") as f:
                    json.dump(data, f, ensure_ascii=False, indent=2)
                files.append(base_url+f"/workflows/{d}/{file}")
        workflows[d] = sorted(files)


# Sort the workflows dictionary to prioritize 'showcase'
if 'showcase' in workflows:
    showcase_workflows = {'showcase': workflows.pop('showcase')}
    workflows = {**showcase_workflows, **workflows}

with open('community_workflows.json', "w", encoding="utf-8") as f:
    json.dump(workflows, f, ensure_ascii=False, indent=2)