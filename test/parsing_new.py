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
                flag = line.find('flags')
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

                if ma > 0 and vht > 0 and flag > 0:
                    flag_end = line.find('peer_bw_rxnss_override')
                    flag = int(line[flag + 6:flag_end - 1], 16)

                    flag_list = flag_decode(flag)
                    
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('Channel with Station ' + station + ' has Very High Transmission Capabilites\n')
                    sta_file.write('Maximum Length of A-MPDU: ' + line[vht + 36: vht + 42] + ' bytes\n\n')
                    sta_file.write('Following are the flags enabled for this client:\n\n')

                    for f in flag_list:
                        sta_file.write(f + '\n')
                    sta_file.write('\n\n')
                    
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


def flag_decode(flag):
    wmi_peer_flags = {'WMI_PEER_AUTH': 0x00000001,
                      'WMI_PEER_QOS': 0x00000002,
                      'WMI_PEER_NEED_PTK_4_WAY': 0x00000004,
                      'WMI_PEER_NEED_GTK_2_WAY': 0x00000010,
                      'WMI_PEER_APSD': 0x00000800,
                      'WMI_PEER_HT': 0x00001000,
                      'WMI_PEER_40MHZ': 0x00002000,
                      'WMI_PEER_STBC': 0x00008000,
                      'WMI_PEER_LDPC': 0x00010000,
                      'WMI_PEER_DYN_MIMOPS': 0x00020000,
                      'WMI_PEER_STATIC_MIMOPS': 0x00040000,
                      'WMI_PEER_SPATIAL_MUX': 0x00200000,
                      'WMI_PEER_VHT': 0x02000000,
                      'WMI_PEER_80MHZ': 0x04000000,
                      'WMI_PEER_VHT_2G': 0x08000000,
                      'WMI_PEER_PMF': 0x10000000,
                      'WMI_PEER_160MHZ': 0x20000000
                      }

    flag_len = len(str(bin(flag)))
    flag_len -= 2

    flag_list = []
    
    for i in range (0, flag_len):
        flag_value = flag & (1 << i)
        if flag_value > 0:
            flag_list.append(flag_value)

    final_flag_list = get_flags(wmi_peer_flags, flag_list)
            
    return final_flag_list
                      

def get_flags(peer_flags_dict, flag_list):
    list_of_flags = []
    peer_flag_items = peer_flags_dict.items()

    for item in peer_flag_items:
        if item[1] in flag_list:
            list_of_flags.append(item[0])

    return list_of_flags


        
if __name__ == '__main__':
    parse()
