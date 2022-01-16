#from psgtray import SystemTray
#import PySimpleGUI as sg
from time import sleep
from explorer import Explorer
import keyboard
import os


LOCAL_APPDATA = os.environ['LOCALAPPDATA']
PATH_WT = os.path.join(LOCAL_APPDATA, 'Microsoft', 'WindowsApps', 'wt.exe')

# tooltip = 'OpenTerminal'
# menu = ['', ['Sair']]

# window = sg.Window('OpenTerminal', finalize=True, enable_close_attempted_event=True)
# tray = SystemTray(menu, single_click_events=False, window=window, tooltip=tooltip, icon=sg.DEFAULT_BASE64_ICON)
# tray.show_message('OpenTerminal', 'Started!')


explorer = Explorer()
while True:
	if keyboard.is_pressed('ctrl+alt+t'):
		explorer_path = explorer.current_path()

		if explorer_path:
			os.popen(f'{PATH_WT} -d "{explorer_path}"')
		else:
			os.popen(PATH_WT)

		sleep(0.2)
