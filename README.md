# Projects
This was my Information Systems Security capstone project. Project Overhaul is an automated python script that will capture WPA/WPA2 Network handshakes and convert the data into a readable format so that the password cracking tool Hashcat can attempt to crack the hashses. If Hashcat is succesful in cracking any of the hashes it will send an automated SMS(using Twilio) to the user letting them know what password has been cracked and helpful tips on how to mitigate these kind of attack.

The tools required for this project to work are:

  hashcat (https://github.com/hashcat)
  
  Twilio (https://www.twilio.com/)
  
  aircrack-ng (https://www.aircrack-ng.org/)
  
  hcxdumptool (https://github.com/ZerBea/)
  
  hcxtools (https://github.com/ZerBea/)
  
