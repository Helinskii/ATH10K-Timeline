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
            i = i + 1

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
        if match:
            if match[0] not in macads:
                macads.append(match[0])


    mac_addr = []
    if macads != []:
        new_file = open('mac_address.txt', 'w')
        new_file.close()
        for addr in macads:
            sta_file = open('MAC Address - ' + addr, 'w')
            for line in lines:
                sta_file = open('MAC Address - ' + addr, 'a')
                asc = line.find('associated')
                vht = line.find('vht peer')
                phm = line.find('phymode')
                ma = line.find(addr)
                m = line.find('mac')
                pc = line.find('peer create')
                dasc = line.find('disassociated')
                pd = line.find('peer delete')
                time = line[2:9]

                if ma > 0 and m > 0 and pc > 0:
                    station = line[pc + 44]
                    peer = line[pc + 57]
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('New peer connection request from station with MAC address: ' + addr + '\n')
                    sta_file.write('Station Number is: ' + station + ' out of 512\n')
                    sta_file.write('Peer Number is: ' + peer + ' out of 528\n\n')

                if ma > 0 and asc > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The station with MAC Address ' + addr + ' has been associated with the AP\n\n')
                    new_file = open('mac_address.txt', 'r+')
                    for mac_line in new_file:
                        mac_addr.append(mac_line)

                    if addr + '\n' not in mac_addr:
                        new_file.write(addr + '\n')

                    new_file.close()

                if ma > 0 and vht > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('Channel with Station ' + station + ' has Very High Transmission Capabilites\n')
                    sta_file.write('Maximum Length of A-MPDU: ' + line[vht + 36: vht + 42] + ' bytes\n\n')

                if ma > 0 and phm > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The mode of the connection is: 802.' + line[phm + 8:phm + 12] + '\n')
                    sta_file.write('The channel transmission capability is: ' + line[phm + 16:phm + 18] + ' Mhz\n\n')

                if ma > 0 and dasc > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The station with MAC Address ' + addr + ' has been disassociated from the AP\n\n')

                if ma > 0 and m > 0 and pd > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The peer created for the STA with address ' + addr + ' has been deleted\n\n\n')

                sta_file.close()

    for addr in macads:
        sta_file = open('MAC Address - ' + addr, 'r')
        all_text = sta_file.read()
        print("\n\n")
        print(all_text)
        sta_file.close()

        new_file.close()


if __name__ == '__main__':
    parse()
    display_sta()
