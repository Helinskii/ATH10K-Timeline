#!/usr/bin/python
import re
p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
macads = []
def parse():
  f = open("data.txt","r")
  lines = f.readlines()
  f.close
  for line in lines:
    match = re.findall(p,line)
    if match:
      for mac in match:
        if mac not in macads:
         macads.append(mac)
      
  if macads!=[]:
    for addr in macads:
      for line in lines:
	asc = line.find(" associated")
        vht = line.find("vht peer")
	phm = line.find("phymode")
        ma = line.find(addr)
	m = line.find("mac")
        pc = line.find("peer create")
	dasc = line.find("disassociated")
        pd = line.find("peer delete")
        time = line[2:9]
	if ma>0 and m>0 and pc>0:
	  station = line[pc+44]
          peer = line[pc+57]
          print("At time: " + time + "s from startup")
	  print("New peer connection request from station with MAC Adrress: " + addr)
          print("Station Number is: " + station + " out of 512")
          print("Peer Number is: " + peer + " out of 528\n")
	if ma>0 and asc>0:
          print("At time: " + time + "s from startup")
	  print("The station with MAC Address " + addr + " has been associated with the AP\n")
	if ma>0 and vht>0:
          print("At time: " + time + "s from startup")
	  print("Channel with Station " + station + " has Very High Transmission Capabilities")
	  print("Maximum Length of A-MPDU: " + line[vht+36:vht+42] + " bytes\n")
	if ma>0 and phm>0:
          print("At time: " + time + "s from startup")
	  print("The mode of the connection is: 802." + line[phm+8:phm+12])
	  print("The channel transmission capability is: "+ line[phm+16:phm+18] + " Mhz\n")
	if ma>0 and dasc>0:
          print("At time: " + time + "s from startup")
	  print("The station with MAC Address " + addr + " has been disassociated from the AP\n")
	if ma>0 and m>0 and pd>0:
          print("At time: " + time + "s from startup")
	  print("The peer created for the STA with address " + addr + " has been deleted\n\n")
    


parse()
