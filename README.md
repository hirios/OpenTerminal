# OpenTerminal
Open the terminal in the folder that has focus with shortcut [Windows]



## Config
You can customize commands and hotkey in main.py:
```python
COMMAND_WT = f'{PATH_WINDOWS_TERMINAL} -d'
COMMAND_CMD = 'start cmd /K cd'
HOTKEY = 'ctrl+alt+t'
```

The cmd is set as the default terminal
```python
os.popen(f'{COMMAND_CMD} "{explorer_path}"')
```


## Use
To open the terminal just press `ctrl+alt+t` like in linux distributions


