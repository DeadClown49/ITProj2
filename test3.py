import subprocess

def run_wsl_command(command):
    wsl_command = f"wsl {command}"
    result = subprocess.run(wsl_command, capture_output=True, text=True, shell=True)
    return result.stdout

pc_info = run_wsl_command("uname -a")
print(pc_info)