from psgtray import SystemTray
import PySimpleGUI as sg


tooltip = 'OpenTerminal'
menu = ['', ['Sair']]


def Tray():
	window = sg.Window('OpenTerminal', finalize=True, enable_close_attempted_event=True)
	tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.DEFAULT_BASE64_ICON)
	tray.show_message('OpenTerminal', 'Started!')