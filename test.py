import os

# Get submodule folders
folders = [folder for folder in os.listdir(".") if os.path.isdir(folder) and ".git" in os.listdir(folder)]
print("Found submodules:", folders)

shell_script = ""

os.makedirs("temp", exist_ok=True)

for folder in folders:
    shell_script += "conda env create -n {} -f {}/environment.yml\n".format(folder, folder)
    shell_script += "conda activate {}\n".format(folder)
    shell_script += "cd {}\n".format(folder)
    shell_script += "python test.py"
    shell_script += "cd ../"

f = open("temp/test.bat", "w")
f.write(shell_script)
f.close()