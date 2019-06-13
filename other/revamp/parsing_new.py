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
    error_lines = []
    mac_lines = []
    wmi_lines = []
    misc_lines = []
    for line in lines:
        start_point = line.find("0000:00:00.0: ")
        error_lines.append(line[start_point + 14:])

    for line in error_lines:
        if line.split(' ')[0] == 'mac':
            mac_lines.append(line)
            
        elif line.split(' ')[0] == 'wmi':
            wmi_lines.append(line)

        else:
            misc_lines.append(line)

    for line in mac_lines:
        flag_loc = line.find('flags')
        if flag_loc > 0:
            flag_end = line.find('peer_bw_rxnss_override')
            flag = int(line[flag_loc + 6:flag_end - 1], 16)

            flag_list = flag_decode(flag)
            print(flag_list)

            
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

if __name__ == "__main__":
    parse()
