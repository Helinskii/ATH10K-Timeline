#!/usr/bin/python3

import re

def display_macinfo(mac_number):
    mac_addr = []
    mac_file = open('mac_address.txt', 'r')
    for mac_line in mac_file:
        mac_addr.append(mac_line.rstrip('\n'))

    mac_file.close()
    mac_filename = 'MAC Address - ' + mac_addr[mac_number - 1]

    mac_file = open(mac_filename, 'r')
    mac_info = mac_file.read()
    print(mac_info)

def display_sta():
    mac_addr = []

    try:
        mac_file = open('mac_address.txt', 'r')
        print("List of MAC addresses found. Displaying now...\n\n")
        i = 1
        for mac_line in mac_file:
            print(str(i) + '. ', end = '')
            print(mac_line + '\n')

    except IOError:
        print("No MAC addresses found.\n")
        quit()

def parse():
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')
    macads = []

    f = open("data.txt", "r")
    lines = f.readlines()
    f.close
    for line in lines:
        match = re.findall(p, line)
        if match[0] not in macads:
            macads.append(match[0])

#    print(macads)
    i = 0
    edit_line = []
    for _ in lines:
        edit_line.append(lines[i][40:])
        i = i + 1

 #   for line in edit_line:
 #       print(line)

 mac_addr = []
 if macads != []:
     new_file = open('mac_address.txt', 'w')
     new_file.close()
     for addr in macads:
         sta_file = open('MAC address - ' + addr, 'a')

if __name__ == "__main__":
    parse()
