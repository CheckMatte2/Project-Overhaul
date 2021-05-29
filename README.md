# Projects Overhaul
This was my Information Systems Security capstone project. Project Overhaul is an automated python script that will capture WPA/WPA2 Network handshakes and convert the data into a readable format so that the password cracking tool Hashcat can attempt to crack the hashses. If Hashcat is succesful in cracking any of the hashes it will send an automated SMS(using Twilio) to the user letting them know what password has been cracked and helpful tips on how to mitigate these kind of attack.

The tools required for this project to work are:

  * Hashcat (https://github.com/hashcat)
  
  * Twilio (https://www.twilio.com/)
  
  * aircrack-ng (https://www.aircrack-ng.org/)
  
  * hcxdumptool (https://github.com/ZerBea/)
  
  * hcxtools (https://github.com/ZerBea/)
  
 A couple of notes must be taken into account
 1. Must be ran with sudo priviledges
 2. You will need a twilio account as you need there tokens to send the SMS message
 3. Need a Wireless Adapter that is capable of packet capture and injection
 4. Once your capture is complete youll need to start up the second program in order to crack the hashes
 
 #Planned Updates
 * Merge both scripts into one whole script
 * Add other hash formats
 * Add other wireless features(NMAP, etc)
 * Add a start menu so user can select what they would like to do
