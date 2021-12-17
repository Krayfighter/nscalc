# nscalc
New Scripting Calculator version 0.1.5
Build -> Development

graphical docs are available under File -> Help

internal docs only currently in the form of code comments


# supported platforms

support for linux natively with setup scripts for dependancies

support for windows *** may need work ***

support for MacOSX is not planned



# installation


available only from github


### for linux distrobutions

git clone https://github.com/Krayfighter/nscalc.git


### arch linux

for setup run
```
cd nscalc/setup
./archlinux.sh
./setup.sh
cd ../
```

then
```
./main.py
```
to run the application


### deprecated (requires python and pip beforehand)

run
```
cd nscalc/setup # move into the application directory
./setup.sh # run setup script
cd ../ # move back into application directory
./main.py # should run the calculator
```




## for windows


### Step 1, enable powershell scripts

this step will allow you to run complex powershell scripts to
simplify the process of installing later on.

first, open a powershell window as administrator by pressing the windows key
then typing "powershell", then right click and choose the option "run as administrator"
and click "allow" when it asks for permissions.

now, copy "set-executionpolicy unrestricted" into the powershell window (do not copy the quotation marks)
then, press enter to run the command

it will now ask you if you want to change the execution policy,
and you type "Y" (again without the quotation marks) and press enter

if no error in red text appear that means you were successfully,

do NOT close this window, as we will use it in the next step


### step 2, downloading and running the setup script

now, copy the following
```
Invoke-WebRequest -Uri https://gist.githubusercontent.com/Krayfighter/34c61dc6b9355ba0b661ed336b487e4f/raw/a26f1066063f55b0566dbfd636685af227c8caaa/setup_nscalc.ps1 -Outfile ./setup.ps1
```
then paste it into powershell the
powershell window and press enter
<!-- 
then run

./setup.ps1 -->

this will ask you if you want to run scripts
when it does, type "A" and press enter

<!-- after it has completed,  -->

now, the installation should be complete



if there were errors anywhere in the installation process please
some troublshooting, and open a new issue on the github page [here](https://github.com/Krayfighter/nscalc.git)


### Thank you for trying nscalc
