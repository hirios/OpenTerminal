# OpenTerminal
Open the terminal in the folder that has focus with shortcut [Windows]

![bandicam 2022-01-16 19-32-25-115](https://user-images.githubusercontent.com/35049559/149681385-33e791e4-82cc-4498-b0c2-b73d18fe264e.gif)

## Config
You can customize commands and hotkey in main.py:
```python
COMMAND_WT = f'{PATH_WINDOWS_TERMINAL} -d'
COMMAND_CMD = 'start cmd /K cd'
HOTKEY = 'ctrl+alt+t'
```

Using CMD
```python
if explorer_path:
    os.popen(f'{COMMAND_CMD} "{explorer_path}"')
else:
    os.popen(PATH_CMD)
```

Using Windows Terminal
```python
if explorer_path:
    os.popen(f'{COMMAND_WT} "{explorer_path}"')
else:
    os.popen(PATH_WT)
```

CMD is default terminal

## Use
```
python main.py
```
To open the terminal just press `ctrl+alt+t` like in linux distributions


