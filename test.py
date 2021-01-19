import os

# Get submodule folders
folders = [folder for folder in os.listdir(".") if os.path.isdir(folder) and ".git" in os.listdir(folder)]
print("Found submodules:", folders)

shell_script = []

if not os.path.exists("temp"):
    os.mkdir("temp")

for folder in folders:
    shell_script.extend([
        "conda env create -n {} -f {}/environment.yml".format(folder, folder),
        "conda activate {}".format(folder),
        "cd {}".format(folder),
        "python test.py",
        "echo {} has passed test!".format(folder),
        "cd ../"
    ])


f = open("temp/test.bat", "w")
f.write(os.linesep.join(shell_script))
f.close()

shell_script.insert(0, "eval \"$(conda shell.bash hook)\"")
f = open("temp/test.sh", "w")
f.write(os.linesep.join(shell_script))
f.close()