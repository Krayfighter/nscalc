# this is the setup script fro nscalc on windows
# it may be made better in the future

pip install --upgrade pip
pip install pip-tools

pip install -r requirements.txt

# this will be used for creating a desktop shortcut in the future
# $MainPythonFile = $env:USERPROFILE\Desktop\nscalc\main.py
# set $ShortCutPath = $env:USERPROFILE\Desktop\nscalc.lnk
# set $ShellObject = New-Object -ComObject ("WScript.Shell")
# set $shortcut = $WscriptObj.CreateShortcut($ShellObject)
# $shortcut.TargetPath = $ShortCutPath
# $shortcut.Save()


