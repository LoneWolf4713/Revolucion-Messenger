# The Receiving End Of Program.
from scapy.all import sniff,Ether



def packet_process(packet):
	if(packet.src==mac and packet.dst==Ether().src):
		print("\t-",packet.load.decode("UTF-8"))  
print('''
      
█▀█ █▀▀ █░█ █▀█ █░░ █░█ █▀▀ █ █▀█ █▄░█   █▀▄▀█ █▀▀ █▀ █▀ █▀▀ █▄░█ █▀▀ █▀▀ █▀█
█▀▄ ██▄ ▀▄▀ █▄█ █▄▄ █▄█ █▄▄ █ █▄█ █░▀█   █░▀░█ ██▄ ▄█ ▄█ ██▄ █░▀█ █▄█ ██▄ █▀▄
      ''')
print('''					★				''')
print("				𝒓𝒆𝒄𝒆𝒊𝒗𝒊𝒏𝒈 𝒆𝒏𝒅				")
		

mac = input("Enter Sender MAC: ")
print("--Messages From",mac,"Will Be Displayed As Received--\n")
sniff(count=0,store=0,prn=packet_process)
