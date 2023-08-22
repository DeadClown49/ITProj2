from nicegui import ui
import subprocess
import threading
import time

# Functions

def run_powershell():
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

                    ui.label("Adapters:")
                    ui.label(current_output)

            else:
                # Print error message
                print("PowerShell Error:")
                print(result.stderr)
        except Exception as e:
            # Print exception message
            print("An error occurred:", e)

        # Wait for 1 second before the next iteration
        time.sleep(1)

# UI

@ui.page('/adapter_selector')
def adapter_selector_page():
    ui.label('Adapter selector:')
    ui.button('Back to main page', on_click=lambda: ui.open('/'))
    ui.button('Select adapter', on_click=lambda: threading.Thread(target=run_powershell).start())

# Home Page
ui.button('Select Adapter', on_click=lambda: ui.open('/adapter_selector'))

ui.run()
