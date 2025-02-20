import os
import json

# 修改为你的仓库信息
GITHUB_USER = "kekehurry"
REPO_NAME = "cityflow_community"
BRANCH = "main"
BASE_URL = f"https://raw.githubusercontent.com/{GITHUB_USER}/{REPO_NAME}/refs/heads/{BRANCH}"

workflows = {}

ignore_dir = [".git", ".github"]

for d in os.listdir(os.getcwd()):
    if os.path.isdir(d) and not d in ignore_dir:
        folder_path = os.path.join(os.getcwd(), d)
        if os.path.exists(folder_path):
            files = []
            for file in os.listdir(folder_path):
                if file.endswith(".csflow.json"):
                    url = f"{BASE_URL}/{d}/{file}"
                    files.append(url)
            # 排序可选
            workflows[d] = sorted(files)
        else:
            workflows[d] = []

with open("community_workflows.json", "w", encoding="utf-8") as f:
    json.dump(workflows, f, ensure_ascii=False, indent=2)