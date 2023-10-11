from nicegui import ui
import os
import subprocess
import tkinter as tk
from tkinter import messagebox

label_style = 'color: #6E93D6; font-size: 300%; font-weight: 300; text-align: center; padding: 20px;'
button_style = 'background-color: #3874c8; color: white; font-size: 20px; border-radius: 12px; padding: 14px 40px; margin: 10px;'

def on_select_adapter():
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
            messagebox.showinfo("No adapters found. Please ensure you have a wireless adapter connected and try again.")
            return None
        
        root = tk.Tk()
        root.title("Adapter Selector")
        root.geometry("300x300")

        tk.Label(root, text="Select an Adapter/Option:").pack()
	
        selected_adapter = tk.StringVar()
	
        for i, adapter in enumerate(adapter_list, start=1):
            tk.Radiobutton(root, text=adapter, variable=selected_adapter, value=adapter).pack()

        
        tk.Button(root, text="Select", command=root.quit).pack()

        root.mainloop()

        return selected_adapter.get()

    # Initial Select_Adaptor Execution 
    selected_adapter = None
    while selected_adapter is None:
        selected_adapter = adapter_options()
    
    if selected_adapter:
        messagebox.showinfo("Selected: " + selected_adapter)

def access_point_selector():
    accesspointlabel = ui.label('Access point selector:')
    accesspointlabel.style(label_style)
    button1access = ui.button('Back to main page', on_click=lambda: ui.open('/'))
    button1access.style(button_style)


def deauth():
    ui.label('Deauth page')
    ui.link('Back to main page', '/')

# Home Page
labelhome = ui.label('Secure Skies')
labelhome.style(label_style)

#call the adapter function on click
button1home = ui.button('Select Adapter', on_click=on_select_adapter)
button1home.style(button_style)

#Call the access point function on click
button2home = ui.button('Select Access Point', on_click=access_point_selector)
button2home.style(button_style)

#Call the deauth function on click
button3home = ui.button('Deauth', on_click=deauth)
button3home.style(button_style)

ui.run()
