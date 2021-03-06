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

    #Debug statement
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

def new_parse():
    p = re.compile(r'(?:[0-9a-fA-F]:?){12}')

    macads = []

    new_file = open('mac_address.txt', 'w')
    new_file.close()

    f = open("data.txt", "r")
    lines = f.readlines()
    f.close
    for line in lines:
        match = re.findall(p, line)
        if match:
            if match[0] not in macads:
                macads.append(match[0])


    file_mac_addr = []
    mac_addr_file = open('mac_address.txt', 'r+')
    read_mac_addr = mac_addr_file.readlines()
    for mac in read_mac_addr:
        file_mac_addr.append(mac)

    for addr in macads:
        if addr + '\n' not in file_mac_addr:
            mac_addr_file.write(addr + '\n')

    log_file = open('parsed_data.txt', 'w')
    log_file.close()
    if lines:
        for line in lines:
            log_file = open('parsed_data.txt', 'a')

            mac_addr = re.findall(p, line)
            mac_addr = mac_addr[0]
            asc = line.find(' associated')
            vht = line.find('vht peer')
            ht = line.find('ht peer')
            mcs = line.find('mcs')
            phm = line.find('phymode')
            ma = line.find(mac_addr)
            peer = line.find('peer')
            qos = line.find('qos')
            wmi = line.find('wmi')
            peer_assoc = line.find('peer assoc')
            m = line.find('mac')
            pc = line.find('peer create')
            dasc = line.find('disassociated')
            pd = line.find('peer delete')
            ampdu = line.find('ampdu')
            time = line[2:9]

            dev_recov = line.find('device successfully recovered')

            hif_err = line.find('Could not init hif')
            core_err = line.find('Could not init core')
            pmf_qos_warn = line.find('failed to enable PMF QOS')
            dynamic_bw_warn = line.find('failed to enable dynamic BW')
            adaptive_qcs_warn = line.find('failed to enable adaptive qcs')
            burst_warn = line.find('failed to disable burst')
            idle_ps_config_warn = line.find('failed to enable idle_ps_config')


            ieee80211_ampdu_mlme_action = ["IEEE80211_AMPDU_RX_START",
                                           "IEEE80211_AMPDU_RX_STOP",
                                           "IEEE80211_AMPDU_TX_START",
                                           "IEEE80211_AMPDU_TX_STOP_CONT",
                                           "IEEE80211_AMPDU_TX_STOP_FLUSH",
                                           "IEEE80211_AMPDU_TX_STOP_FLUSH_CONT",
                                           "IEEE80211_AMPDU_TX_OPERATIONAL"]

            if hif_err > 0:
                log_file.write('Could not initialize HIF.\nATH10K state changed to OFF.\n\n')

            elif core_err > 0:
                log_file.write('Could not initialize CORE.\nHIF power down started.\n\n')

            elif pmf_qos_warn > 0:
                log_file.write('Failed to enable parameter - PMF (Protected Management Frame) QoS (Quality of Service).\nStopping CORE.\n\n')

            elif dynamic_bw_warn > 0:
                log_file.write('Failed to enable dynamic bandwidth.\nStopping CORE.\n\n')

            elif adaptive_qcs_warn > 0:
                log_file.write('Failed to enable adaptive qcs.\nStopping CORE.\n\n')

            elif burst_warn > 0:
                log_file.write('Failed to disable burst.\nStopping CORE.\n\n')

            elif idle_ps_config_warn > 0:
                log_file.write('Failed to enable idle ps config.\nStopping CORE.\n\n')

            elif ma > 0 and m > 0 and pc > 0:
                station = line[pc + 44]
                peer = line[pc + 57]
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('New peer connection request from station with MAC address: ' + mac_addr + '\n')
                log_file.write('Station Number is: ' + station + ' out of 512\n')
                log_file.write('Peer Number is: ' + peer + ' out of 528\n\n')

            elif ma > 0 and asc > 0:
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('The station with MAC Address ' + mac_addr + ' has been associated with the AP\n\n')

            elif ma > 0 and ht > 0 and mcs > 0:
                peer_ht_rate = line.find('cnt') + 4
                nss = line.find('nss') + 4

                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('WMI Peer HT rate for ' + mac_addr + ' = ' + line[peer_ht_rate:peer_ht_rate + 2] + '\n')
                log_file.write('Number of Spatial Streams for ' + mac_addr + ' = ' + line[nss:nss + 2] + '\n')

            elif ma > 0 and vht > 0:
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('Channel with Station ' + station + ' has Very High Transmission Capabilites\n')
                log_file.write('Maximum Length of A-MPDU: ' + line[vht + 36: vht + 42] + ' bytes\n\n')

            elif ma > 0 and qos > 0 and peer > 0:
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('Peer with address ' + mac_addr + ' has QoS = ' + line[qos + 4] + '\n\n')

            elif ma > 0 and wmi > 0 and peer_assoc > 0:
                vdev = line.find('vdev') + 5
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('Peer (new) with address ' + mac_addr + ' and VDEV = ' + line[vdev] + ' has been associated.\n\n')

            elif ma > 0 and phm > 0:
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('The mode of the connection is: 802.' + line[phm + 8:phm + 12] + '\n')
                log_file.write('The channel transmission capability is: ' + line[phm + 16:phm + 18] + ' Mhz\n\n')

            elif ma > 0 and ampdu > 0:
                tid_loc = line.find('tid')
                action_loc = line.find('action')

                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('Target Identifier for ' + mac_addr + ' = ' + line[tid_loc + 4] + '\n\n')
                log_file.write('Following flag for A-MPDU (Aggregate MAC Protocol Data Unit) action for ' + mac_addr + ' was set:\n')
                log_file.write(ieee80211_ampdu_mlme_action[int(line[action_loc + 7])] + '\n\n')


            elif ma > 0 and dasc > 0:
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('The station with MAC Address ' + mac_addr + ' has been disassociated from the AP\n\n')

            elif ma > 0 and m > 0 and pd > 0:
                log_file.write('At time: ' + time + 's from startup\n')
                log_file.write('The peer created for the STA with address ' + mac_addr + ' has been deleted\n\n')


            elif ma > 0 and dev_recov > 0:
                log_file.write('INFO:\n')
                log_file.write(mac_addr + 'has been successfully recovered and has restarted.\nConnection has been reconfigured.\n\n\n')

            log_file.close()


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
                asc = line.find(' associated')
                vht = line.find('vht peer')
                ht = line.find('ht peer')
                mcs = line.find('mcs')
                phm = line.find('phymode')
                ma = line.find(addr)
                m = line.find('mac')
                peer = line.find('peer')
                qos = line.find('qos')
                wmi = line.find('wmi')
                peer_assoc = line.find('peer assoc')
                pc = line.find('peer create')
                dasc = line.find('disassociated')
                pd = line.find('peer delete')
                ampdu = line.find('ampdu')
                time = line[2:9]

                dev_recov = line.find('device successfully recovered')

                hif_err = line.find('Could not init hif')
                core_err = line.find('Could not init core')
                pmf_qos_warn = line.find('failed to enable PMF QOS')
                dynamic_bw_warn = line.find('failed to enable dynamic BW')
                adaptive_qcs_warn = line.find('failed to enable adaptive qcs')
                burst_warn = line.find('failed to disable burst')
                idle_ps_config_warn = line.find('failed to enable idle_ps_config')

                ieee80211_ampdu_mlme_action = ["IEEE80211_AMPDU_RX_START",
                                               "IEEE80211_AMPDU_RX_STOP",
                                               "IEEE80211_AMPDU_TX_START",
                                               "IEEE80211_AMPDU_TX_STOP_CONT",
                                               "IEEE80211_AMPDU_TX_STOP_FLUSH",
                                               "IEEE80211_AMPDU_TX_STOP_FLUSH_CONT",
                                               "IEEE80211_AMPDU_TX_OPERATIONAL"]

                if hif_err > 0:
                    sta_file.write('Could not initialize HIF.\nATH10K state changed to OFF.\n\n')

                if core_err > 0:
                    sta_file.write('Could not initialize CORE.\nHIF power down started.\n\n')

                if pmf_qos_warn > 0:
                    sta_file.write('Failed to enable parameter - PMF (Protected Management Frame) QoS (Quality of Service).\nStopping CORE.\n\n')

                if dynamic_bw_warn > 0:
                    sta_file.write('Failed to enable dynamic bandwidth.\nStopping CORE.\n\n')

                if adaptive_qcs_warn > 0:
                    sta_file.write('Failed to enable adaptive qcs.\nStopping CORE.\n\n')

                if burst_warn > 0:
                    sta_file.write('Failed to disable burst.\nStopping CORE.\n\n')

                if idle_ps_config_warn > 0:
                    sta_file.write('Failed to enable idle ps config.\nStopping CORE.\n\n')

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

                if ma > 0 and ht > 0 and mcs > 0:
                    peer_ht_rate = line.find('cnt') + 4
                    nss = line.find('nss') + 4

                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('WMI Peer HT rate for ' + addr + ' = ' + line[peer_ht_rate:peer_ht_rate + 2] + '\n')
                    sta_file.write('Number of Spatial Streams for ' + addr + ' = ' + line[nss:nss + 2] + '\n')

                if ma > 0 and vht > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('Channel with Station ' + station + ' has Very High Transmission Capabilites\n')
                    sta_file.write('Maximum Length of A-MPDU: ' + line[vht + 36: vht + 42] + ' bytes\n\n')

                if ma > 0 and qos > 0 and peer > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('Peer with address ' + addr + ' has QoS = ' + line[qos + 4] + '\n\n')

                if ma > 0 and wmi > 0 and peer_assoc > 0:
                    vdev = line.find('vdev') + 5
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('Peer (new) with address ' + addr + ' and VDEV = ' + line[vdev] + ' has been associated.\n\n')

                if ma > 0 and phm > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The mode of the connection is: 802.' + line[phm + 8:phm + 12] + '\n')
                    sta_file.write('The channel transmission capability is: ' + line[phm + 16:phm + 18] + ' Mhz\n\n')

                if ma > 0 and ampdu > 0:
                    tid_loc = line.find('tid')
                    action_loc = line.find('action')

                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('Target Identifier for ' + addr + ' = ' + line[tid_loc + 4] + '\n\n')
                    sta_file.write('Following flag for A-MPDU (Aggregate MAC Protocol Data Unit) action for ' + addr + ' was set:\n')
                    sta_file.write(ieee80211_ampdu_mlme_action[int(line[action_loc + 7])] + '\n\n')

                if ma > 0 and dasc > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The station with MAC Address ' + addr + ' has been disassociated from the AP\n\n')

                if ma > 0 and m > 0 and pd > 0:
                    sta_file.write('At time: ' + time + 's from startup\n')
                    sta_file.write('The peer created for the STA with address ' + addr + ' has been deleted\n\n\n')


                if ma > 0 and dev_recov > 0:
                    sta_file.write('INFO:\n')
                    sta_file.write(addr + 'has been successfully recovered and has restarted.\nConnection has been reconfigured.\n\n\n')
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
    new_parse()
    parse()
