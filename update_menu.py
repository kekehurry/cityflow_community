import os
import json

workflows = {}

ignore_dir = [".git", ".github"]

public_folder = os.getcwd()

base_url = '/cityflow_community/'

if not os.path.exists(public_folder):
    os.mkdir(public_folder)

for d in os.listdir(public_folder):
    folder_path = os.path.join(public_folder, d)
    if os.path.isdir(folder_path) and not d in ignore_dir:
        files = []
        for file in os.listdir(folder_path):
            if file.endswith(".csflow.json"):
                files.append(base_url+d+'/'+file)
        # 排序可选
        workflows[d] = sorted(files)


with open('community_workflows.json', "w", encoding="utf-8") as f:
    json.dump(workflows, f, ensure_ascii=False, indent=2)