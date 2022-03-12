## Installation

Install the python dependencies

    pip install -r requirements.txt

## Usage

Run the following command in a terminal:

    py ./KeepWindowsAlive.py -fixed_duration false -wait_duration=28800 -poke_interval=600

All arguments are optional and default to the values above.

    fixed_duration: If set to true the duration of the script will be fixed to the wait_duration number of seconds.
                    If set to false the program will reset the end time to the last human interaction with the computerplus the wait_duration number of seconds.

    wait_duration: The number of seconds the program will be alive (default is 8hrs)
    poke_interval: The number of seconds that the program should wait to trigger and event and prevent windows to lock down the computer (default is 10 mins)


## Known issues

The script might stop taking effect after the sesion expires from vmware. No errors are shown but it might require to restart the process 
