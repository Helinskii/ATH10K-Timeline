#!/bin/bash
timeout 2 sshpass -p 'password' scp root@192.168.1.1:/myscript/data.txt /home/soumyarup/Qualcomm_Project
RESULT=$?
# echo $RESULT
if [ $RESULT -eq 124 ] || [ $RESULT -eq 1 ]; then
  echo "Unable to fetch file. Parsing from existing file."
else
  echo 'File Received: Starting to parse...'
fi


