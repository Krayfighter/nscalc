# nscalc
New Scripting Calculator version 0.1.4

graphical docs are available under File -> Help

internal docs only currently in the form of code comments


# supported platforms

support for linux natively with setup scripts for dependancies

support for windows *** may need work ***

support for MacOSX is not planned



# installation


available only from github

command line git is `very` recommended but not technically required


### for linux, download the source

git clone https://github.com/Krayfighter/nscalc.git

then run
```
cd nscalc/setup # move into the application directory
./setup.sh # run setup script
cd ../ # move back into application directory
./main.py # should run the calculator
```

currently python3, and pip are required before the installation
scripts can handle the process, better support may come later




## for windows


### Step 1, enable powershell scripts

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


### step 2, downloading and running the setup script

in the powershell window run

Invoke-WebRequest -Uri https://gist.githubusercontent.com/Krayfighter/34c61dc6b9355ba0b661ed336b487e4f/raw/c7dfbefbf91edd985d506e419c97790844b59e6d/setup_nscalc.ps1 -Outfile ./setup.ps1

then run

./setup.ps1

the script will ask you if you want to run scripts
when it does, type "A" and press enter

after it has completed, 



if there were errors anywhere in the installation process please
some troublshooting, and open a new issue on the github page [here](https://github.com/Krayfighter/nscalc.git)


### Thank you for trying nscalc
