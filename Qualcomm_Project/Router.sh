#!/bin/bash
sshpass -p 'password' scp root@192.168.1.1:/myscript/data.txt /home/soumyarup/Qualcomm_Project
echo 'File Received: Starting to parse'
./parsing.py

