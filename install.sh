#!/bin/sh

echo "*******************************************"
echo "          Installing Requirements          "
echo "*******************************************"

pip3 install -r ./requirements.txt
script_full_path="$(pwd)/main.py"
chmod 775 $script_full_path
crontab -r
(crontab -l 2>/dev/null; echo "*/7 * * * * python3 ${script_full_path}") | crontab -
crontab -l
echo "Instalation completed!"
