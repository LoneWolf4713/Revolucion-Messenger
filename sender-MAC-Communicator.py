# The Sending End Of Program.
from scapy.all import Ether,sendp
  
print('''
      
█▀█ █▀▀ █░█ █▀█ █░░ █░█ █▀▀ █ █▀█ █▄░█   █▀▄▀█ █▀▀ █▀ █▀ █▀▀ █▄░█ █▀▀ █▀▀ █▀█
█▀▄ ██▄ ▀▄▀ █▄█ █▄▄ █▄█ █▄▄ █ █▄█ █░▀█   █░▀░█ ██▄ ▄█ ▄█ ██▄ █░▀█ █▄█ ██▄ █▀▄
      ''')
print('''					★				      		''')
print("				𝒕𝒓𝒂𝒏𝒔𝒎𝒊𝒕𝒕𝒊𝒏𝒈 𝒆𝒏𝒅			      	 	")
		
mac = input("Enter MAC of Receiver: ")
print()
while True:
    msg = input("\tmessage: ")
    a = Ether(dst=mac)/msg
    sendp(a,iface='eth0')
    
