import os
import json
import subprocess

if os.path.exists("tested.json"):
    TESTED = json.load(open("tested.json"))
else:
    TESTED = {}

# Get submodule folders
submodules = [folder for folder in os.listdir(".") if os.path.isdir(folder) and ".git" in os.listdir(folder)]
print("Found submodules:", submodules)

for module in submodules:
    # get commit id of sub module
    label = subprocess.check_output(["git", "ls-files", "-s", module]).decode()
    commit = label.split(" ")[1]
    TESTED[module] = commit

# Delete un-existed examples 
for key in TESTED.copy():
    if key not in submodules:
        del TESTED[key]

json.dump(TESTED, open("tested.json", "w"), indent=2)