import subprocess
import time

# PowerShell command to execute
powershell_command = r"netsh wlan show interfaces | findstr 'Name'"

previous_output = None

while True:
    try:
        # Run the PowerShell command
        result = subprocess.run(["powershell", "-Command", powershell_command], capture_output=True, text=True, shell=True)

        # Check for successful execution
        if result.returncode == 0:
            # Get the current output
            current_output = result.stdout

            # Check if the output has changed
            if current_output != previous_output:
                print("PowerShell Output:")
                print(current_output)
                previous_output = current_output

        else:
            # Print error message
            print("PowerShell Error:")
            print(result.stderr)
    except Exception as e:
        # Print exception message
        print("An error occurred:", e)

    # Wait for 10 seconds before the next iteration
    time.sleep(1)
