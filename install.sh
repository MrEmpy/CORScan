#!/bin/bash

printf '\e[1;35m   __________  ____  _____                
  / ____/ __ \/ __ \/ ___/_________ _____ 
 / /   / / / / /_/ /\__ \/ ___/ __ `/ __ \
/ /___/ /_/ / _, _/___/ / /__/ /_/ / / / /
\____/\____/_/ |_|/____/\___/\__,_/_/ /_/ \n\n'

printf '\e[1;34m[*] Installing\n'
pip install -r requirements.txt
chmod +x corscan.py
cp corscan.py /usr/bin/corscan
chmod +x /usr/bin/corscan
printf '\e[1;31m[+] Finished! Execute "corscan"'
