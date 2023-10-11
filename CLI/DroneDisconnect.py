# Imports
import subprocess

# Provide Info of The Tool at The Start 
def tool_info():
    print("/---------------------------------------------")
    print("DroneDisconnect by Secure Skies")
    print("For: ZEIT3101 - IT Project 2")
    print("Group 6 - 2023")
    print("Members: ...")
    print("Version: 0.1")
    print("This Tool Was Built for Linux (Ubuntu and Kali)")
    print("This Tool Was Designed and Tested on Drone Zero-X Stratus+ (ZXMP-D1000)")
    print("/---------------------------------------------")

'''
def systemcheck():
    # Check OS
    ...

    # Check Dependencies

    # Check if aircrack-ng is installed [IF REQUIRED]
    try:
        subprocess.check_output(["aircrack-ng", "--version"], stderr=subprocess.STDOUT, universal_newlines=True)
        print("Aircrack-ng is installed.")
    except subprocess.CalledProcessError:
        print("Aircrack-ng is not installed.")
'''

# Select Adaptor
def select_adaptor():
    
    # Get List of Adapters
    def get_adapter_list():
        print("Getting List of Adapters...")
        adapter_info = subprocess.check_output("iw dev 2>&1 | grep Interface | awk '{print $2}'", shell=True, universal_newlines=True)
        if not adapter_info:
            # No Adapters Found
            return []
        else:
            return adapter_info.splitlines()

    # Print Adapter Options and Get User Input
    def adapter_options():
        adapter_list = get_adapter_list()
        if not adapter_list:
            print("No adapters found. Please ensure you have a wireless adapter connected and try again.")
                  
        print("Select an Adapter/Option:")
        print("R. Rescan for Adapters")
        print("E. Exit")
        if not adapter_list:
            print("No Adapters to Select")
        else:
            i = 1
            for adapter in adapter_list:
                print(str(i) + ". " + adapter)
                i += 1

        choice = input("Please Make a Selection: ")
        
        if choice == "r" or choice == "R":
            adapter_options()
        elif choice == "e" or choice == "E":
            exit()
        elif choice.isdigit() and int(choice) in range(1, i):
            print("Selected: " + adapter_list[int(choice)-1])
            return adapter_list[int(choice)-1]
        else:
            print("Invalid choice. Please try again.")
            adapter_options()

    # Initial Select_Adaptor Execution 
    selected_adapter = adapter_options()
    return selected_adapter

# Select Access Point
def select_ap():

    def disconnect_adapter_from_current_ap():
        current_adapter_status = subprocess.Popen("nmcli d show " + selected_adapter + " 2>&1 | grep 'GENERAL.STATE:' | awk '{print $3}'", stdout = subprocess.PIPE, shell = True, universal_newlines = True).stdout.read()
        print(str(current_adapter_status))
        if "disconnected" not in current_adapter_status:
            print("Adapter is connected/connecting to an Access Point already. Disconnecting from Access Point...")
            disconnect_adapter = subprocess.Popen("nmcli dev disconnect " + selected_adapter, stdout = subprocess.PIPE, shell = True)
            disconnect_adapter.wait()
            print("Adapter Disconnected. Now Scanning for Access Points...")
        else:
            print("Adapter is not connected to an Access Point. Scanning for Access Points...")

    # Get List of Access Points
    def get_ap_list():
        print("Getting List of Access Points...")
        disconnect_adapter_from_current_ap()
        # Potential Alternate Method: ap_info = subprocess.check_output("nmcli dev wifi list 2>&1 | grep -v 'SSID' | awk '{print $2}'", shell=True, universal_newlines=True)
        


    # Print Access Points Options and Get User Input
    def ap_options():
        ap_list = get_ap_list()
        if not ap_list:
            print("No Access Points found.")
                  
        print("Select an Access Point/Option:")
        print("R. Rescan for Access Points")
        print("E. Exit")
        if not ap_list:
            print("No Access Points to Select")
        else:
            i = 1
            for ap in ap_list:
                print(str(i) + ". " + ap)
                i += 1

        choice = input("Please Make a Selection: ")
        
        if choice == "r" or choice == "R":
            ap_options()
        elif choice == "e" or choice == "E":
            exit()
        elif choice.isdigit() and int(choice) in range(1, i):
            print("Selected: " + ap_list[int(choice)-1])
            return ap_list[int(choice)-1]
        else:
            print("Invalid choice. Please try again.")
            ap_options()

    # Initial Select_Adaptor Execution 
    selected_ap = ap_options()
    return selected_ap

     

# Run Start Tool
if __name__ == "__main__":
    tool_info()
    # systemcheck()
    selected_adapter = select_adaptor()
    selected_ap = select_ap()