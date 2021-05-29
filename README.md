# Projects Overhaul

## Project Overhaul was created by Checkmatte

## NOTE THE SCRIPT WILL NEED CHANGES IN ORDER TO WORK

This was my Information Systems Security capstone project. Project Overhaul is an automated python script that will capture WPA/WPA2 Network handshakes and convert the data into a readable format so that the password cracking tool Hashcat can attempt to crack the hashses. If Hashcat is succesful in cracking any of the hashes it will send an automated SMS(using Twilio) to the user letting them know what password has been cracked and helpful tips on how to mitigate these kind of attack.

This Project was done on Kali Linux 2021

# Tools Needed

  * Hcxdumptool (https://github.com/ZerBea/)
  * Hcxtools (https://github.com/ZerBea/)
  * Hashcat (https://github.com/hashcat)
  * Twilio (https://www.twilio.com/)
  * Aircrack-ng (https://www.aircrack-ng.org/)

# Notes  
 A couple of notes must be taken into account
 1. Must be ran with sudo priviledges
 2. You will need a twilio account as you need there tokens to send the SMS message
 3. Need a Wireless Adapter that is capable of packet capture and injection
 4. Once your capture is complete youll need to start up the second program in order to crack the hashes
 
 # Planned Updates to script
 * Merge both scripts into one whole script
 * Option of using hashcat and or John the Ripper
 * Add other wireless features(NMAP, etc)
 * Add a start menu so user can select what they would like to do
 * Be able to crack WPA3 hashes
