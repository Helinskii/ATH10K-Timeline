#!bin/bash /etc/rc.common
echo 0x2012 > /sys/module/ath10k_core/parameters/debug_mask
dmesg | grep ath10k | grep 'sta\+[[:space:]]\+\|peer' > /myscript/data.txt

