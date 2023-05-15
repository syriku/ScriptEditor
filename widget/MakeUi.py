import subprocess
import platform

system = platform.system()

if system == "Windows":
    command = "MakeUi.bat"
elif system == "Linux":
    command = "MakeUi.sh"
elif system == "Darwin":
    command = "MakeUi.sh"
else:
    print("Unsupported system type")
    exit(1)

try:
    result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(e.stderr)
    exit(1)
