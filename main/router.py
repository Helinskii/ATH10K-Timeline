#!/usr/bin/python3

import sys
import subprocess
import parsing_menu

def display():
    subprocess.call(['./Router.sh'])

print('ATH10K Debug Log Timeline\n\n')

while True:
    print('Select an option below:\n')
    print('1. Fetch debug log\n2. Display STAs\n3. Quit\n')
    option = input('Enter Option [1/2/3]: ')
    if option not in ['1', '2', '3']:
        print('Invalid Option\n')
        continue
    else:
        break

print('\n')
if option == '1':
    print('\n')
    display()
    parsing_menu.parse()
elif option == '2':
    parsing_menu.display_sta()

    while True:
        option = input("Select a MAC Address to display information for [1/2/3..]: ")
        try:
            val = int(option)
        except ValueError:
            print('Invalid Option\n')
            continue

        try:
            parsing_menu.display_macinfo(val)
            quit()
            
        except IndexError:
            print("Out of range\n")
            continue
        

elif option == '3':
    quit()
