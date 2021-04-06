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

shell_script = []

if not os.path.exists("temp"):
    os.mkdir("temp")

for module in submodules:
    # get commit id of sub module
    label = subprocess.check_output(["git", "ls-files", "-s", module]).decode()
    commit = label.split(" ")[1]
    
    if commit == TESTED.get(module):
        print("Skipping tested module: {} {}".format(module, commit))
        continue

    print("Generate test for {} {}".format(module, commit))

    shell_script.extend([
        "conda env create -n {} -f {}/environment.yml".format(module, module),
        "conda activate {}".format(module),
        "cd {}".format(module),
        "python test.py",
        "echo {} has passed test!".format(module),
        "cd ../"
    ])


f = open("temp/test.bat", "w")
f.write(os.linesep.join(shell_script))
f.close()

shell_script.insert(0, "eval \"$(conda shell.bash hook)\"")
f = open("temp/test.sh", "w")
f.write(os.linesep.join(shell_script))
f.close()