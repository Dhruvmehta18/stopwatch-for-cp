This stopwatch can be use during competitive programming for measuring time take in each question.
To become faster in Competitive programming this stopwatch canbe helpfull\
I have made dark theme for making UI of stopwatch\
I am using python version = 3.8.2

<img src="./Stopwatch.jpg" alt="Stopwatch"/>

For running this stopwatch
1. By python command
```json
    python stopwatch.py
```
2. By making exe file (for using in real time)\
    First install pyinstaller
```json
    pip install pyinstaller
```

if you want to make exe file as whole you use this commands,but the start time is more in in this command

```json   
    pyinstaller -w -F stopwatch.py
```
Or use this command for faster start time
```json
    pyinstaller -w stopwatch.py
```
Or use this command if you want to have the icon on the exe file
```json
    pyinstaller -w -i "[filepath_to_icon]" stopwatch.py
```
After making exe file. The exe file will be under dist folder