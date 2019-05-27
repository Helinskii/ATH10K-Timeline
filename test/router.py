#!/usr/bin/python3

import sys
import subprocess

def display():
    subprocess.call(['./Router.sh'])

print('ATH10K Debug Log Timeline\n\n')

while True:
    print('Select an option below:\n')
    print('1. Fetch debug log\n2. Quit\n')
    option = input('Enter Option [1/2]: ')
    if option not in ['1', '2']:
        print('Invalid Option\n')
        continue
    else:
        break

print('\n')
if option == '1':
    print('\n')
    display()
elif option == '2':
    quit()
