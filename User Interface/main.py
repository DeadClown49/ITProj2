from nicegui import ui

#Main window for the GUI, intention is to add the return from the Wi-Fi detection (And hopefully a map here)
ui.label('CONTENT')
def Wifi_check():
    [ui.label(f'Line {i}') for i in range(100)]
#Header for the GUI
with ui.header(elevated=True).style('background-color: #3874c8').classes('items-center justify-between'):
    ui.label('Secure Skies Drone Detection and Attack system')
    ui.button(on_click=lambda: right_drawer.toggle(), icon='menu').props('flat color=white')
#Left drawer for the GUI, intetion is to use this area for the detection buttons and maybe more
with ui.left_drawer(top_corner=True, bottom_corner=True).style('background-color: #d7e3f4'):
    ui.label('Options')
    ui.button('Click me!', on_click=Wifi_check)
#Right drawer for the GUI
with ui.right_drawer(fixed=False).style('background-color: #ebf1fa').props('bordered') as right_drawer:
    ui.label('PLACEHOLDER OF A RIGHT SIDE MENU FOR NOW')
#Footer for the GUI (not sure if we need this)
with ui.footer().style('background-color: #3874c8'):
    ui.label('FOOTER')

ui.run()