import os
import json
import subprocess

if os.path.exists("tested.json"):
    TESTED = json.load(open("tested.json"))
else:
    TESTED = {}

if not os.path.exists("temp"):
    os.mkdir("temp")


# Get submodule folders
submodules = [folder for folder in os.listdir(".") if os.path.isdir(folder) and ".git" in os.listdir(folder)]
print("Found submodules:", submodules)


# Check if all submodules has environment yaml
for module in submodules:
    env_files = ["environment.yml", "environment.windows.yml", "environment.macos.yml", "environment.linux.yml"]
    env_file_exists = False
    for env_file in env_files:
        if env_file in os.listdir(module):
            env_file_exists = True
            break
    if not env_file_exists:
        raise RuntimeError("environment yaml missing for {}".format(module))


# Generate test scripts for each platforms
shell_script_windows = ['echo start testing']
shell_script_macos = ['echo start testing']
shell_script_linux = ['echo start testing']

def generate_test(shell_script, os_type):
    for module in submodules:
        # get commit id of sub module
        label = subprocess.check_output(["git", "ls-files", "-s", module]).decode()
        commit = label.split(" ")[1]
        
        env_file_cross_platform = os.path.join(module, "environment.yml")
        if os.path.exists(env_file_cross_platform):
            env_file = env_file_cross_platform
        else:
            env_file = os.path.join(module, "environment.{}.yml".format(os_type))

        if not os.path.exists(env_file):
            print("Skipping os: {}".format(os_type))
            continue
        
        if commit == TESTED.get(module):
            print("Skipping tested module: {} {}".format(module, commit))
            continue

        print("Generate test for {} {} {}".format(module, commit, os_type))

        shell_script.extend([
            "conda env create -n {} -f {}".format(module, env_file),
            "conda activate {}".format(module),
            "cd {}".format(module),
            "python test.py",
            "echo {} has passed test!".format(module),
            "cd ../"
        ])


generate_test(shell_script_windows, 'windows')
generate_test(shell_script_macos, 'macos')
generate_test(shell_script_linux, 'linux')


f = open("temp/test.windows.bat", "w")
f.write(os.linesep.join(shell_script_windows))
f.close()

shell_script_macos.insert(0, "eval \"$(conda shell.bash hook)\"")
f = open("temp/test.macos.sh", "w")
f.write(os.linesep.join(shell_script_macos))
f.close()

shell_script_linux.insert(0, "eval \"$(conda shell.bash hook)\"")
f = open("temp/test.linux.sh", "w")
f.write(os.linesep.join(shell_script_linux))
f.close()