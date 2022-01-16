from explorer import Explorer
#from menu_tray import Tray
from time import sleep
import keyboard
import os


## Set app in Windows System Tray
#Tray()

LOCALAPPDATA = os.environ['LOCALAPPDATA']
USERPROFILE = os.environ['USERPROFILE']

PATH_WT = os.path.join(LOCALAPPDATA, 'Microsoft', 'WindowsApps', 'wt.exe')
COMMAND_WT = f'{PATH_WT} -d'

PATH_CMD = f'start cmd /K cd "{USERPROFILE}"'
COMMAND_CMD = 'start cmd /K cd'

HOTKEY = 'ctrl+alt+t'


explorer = Explorer()

while True:
	if keyboard.is_pressed(HOTKEY):
		explorer_path = explorer.current_path()

		# IF A WINDOWS EXPLORER WINDOW IS IN FOCUS
		if explorer_path:
			# COMMAND_WT OR COMMAND_CMD
			os.popen(f'{COMMAND_CMD} "{explorer_path}"')
		else:
			# PATH_WT OR PATH_CMD
			os.popen(PATH_CMD)

		sleep(0.2)
