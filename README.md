# KeepVMwareActive

To be added

# KeepWindowsAlive

Prevents windows to lock the screen by launching an event in the keyboard. It has been tested in a virtual machine hosted by vmware.

## Installation

Install the python dependencies

    pip install -r requirements.txt

## Usage

Run the following command in a terminal:

    py ./KeepWindowsAlive.py -wait_duration=28800 -poke_interval=600

Both arguments are optional and default to the values above


## Known issues

The script might stop taking effect after the sesion expires from vmware. No errors are shown but it might require to restart the process 
