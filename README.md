# nscalc
New Scripting Calculator version 0.1.3

graphical docs are available under File -> Help

internal docs only currently in the form of code comments


# supported platforms

support for linux natively with setup scripts for dependancies

support for windows may need work

support for MacOSX is not planned



# installation


available only from github

command line git is `very` recommended but not technically required


for linux, download the source from https://github.com/Krayfighter/nscalc.git

then run
```
cd nscalc/setup # move into the application directory
./setup.sh # run setup script
cd ../ # move back into application directory
./main.py # should run the calculator
```

currently python3, and pip are required before the installation
scripts can handle the process, better support may come later




for windows ### experimental


Step 1, enable powershell scripts

this step will allow you to run complex powershell scripts to
simplify the process of installing later on.

first, open a powershell window as administrator by pressing the windows key
then typing "powershell", then right click and choose the option "run as administrator"
and click "allow" when it asks for permissions.

now, copy "set-executionpolicy unrestricted" into the powershell window (do not copy the quotation marks)

it will now ask you if you want to change the execution policy,
and you type "Y" (again without the quotation marks) and press enter

if no error in red text appear that means you were successfully,

do NOT close this window, as we will use it in the next step


real step 2, downloading and running the setup script

in the powershell window run

Invoke-WebRequest -Uri https://gist.githubusercontent.com/Krayfighter/34c61dc6b9355ba0b661ed336b487e4f/raw/c7dfbefbf91edd985d506e419c97790844b59e6d/setup_nscalc.ps1 -Outfile ./setup.ps1

then run

./setup.ps1

the script will ask you if you want to run scripts
when it does, type "A" and press enter

after it has completed, 

step 2, choosing download method

do you have git installed? if you do go to [download via git](#download-for-windows-via-git),
but if you do not know the answer to that quaestion, the answer is no
in that case use the following setup


go to [my github page](https://github.com/Krayfighter/nscalc.git)
and find the green button that says "code" in the top right

click it and choose the option at the bottom called "download zip"

a window will pop up, and save it to your downloads folder

once the download has completed, open the zipped folder that you just download
in it you should see "nscalc-main", drag that onto an empty space on your desktop 

then you are done downloading

# donalod for windows via git

open a new powershell instance and run
cd "$env:USERPROFILE\Desktop" (this time with the quotation marks) to move into the Desktop folder

the run
git clone https://github.com/Krayfighter/nscalc.git

and then
cd nscalc
to enter the nscalc directory

then you are done downloading


# running the setup scripts

Now that you have set the execution policy, and downloaded nscalc
you can run the setup scripts to do the rest of the work

open the nscalc folder, and then enter the setup folder

at the top of file explorer, there is a bar displaying the currently folder
### add picture here
if you click it it should all be highlighted blue, then type powershell into it

this will open a new powershell instance in that folder

now, type "setup.ps1" into powershell (again without the quotation marks)
this will start the setup script

if it completes without any error (red text) then you were successful

if there were errors anywhere in the installation process try doing
some troublshooting, and open a new issue on the github page [here](https://github.com/Krayfighter/nscalc.git)
