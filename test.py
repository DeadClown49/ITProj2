from nicegui import ui
import os

@ui.page('/adapter_selector')
def adapter_selector_page():
    ui.label('Adapter selector:')
    ui.button('Back to main page', on_click=lambda: ui.open('/'))
    ui.button('Select adapter', on_click=lambda: os.system('start cmd /K "netsh wlan show interfaces | findstr ^"Name^""'))

@ui.page('/access_point_selector', dark=True)
def access_point_selector_page():
    ui.label('Welcome to the dark side')
    ui.link('Back to main page', '/')

@ui.page('/deauth')
def deauth_page():
    ui.label('Deauth page')
    ui.link('Back to main page', '/')

# Home Page
ui.button('Select Adapter', on_click=lambda: ui.open('/adapter_selector'))
ui.button('Select Access Point', on_click=lambda: ui.open('/access_point_selector'))
ui.button('Deauth', on_click=lambda: ui.open('/deauth'))

ui.run()
