# rotek_keygen2
Keygen for some Rotek modems with ESSID RT-WIFI-HHHH and RT-GPON-HHHH

Based on reverse engineering of the algorithm found in /bin/flash in some firmware or /lib/libapmib.so in others. (credit to drsnooker)
Seeds are derived from an unknown hardware ID number found in /dev/mtdblock0

seed1 has a range of 0..0x763d
seed2 has a range of 0..0x7663
seed3 has a range of 0..0x7673

Usage: python3 rotek_keygen2.py 16861 22903 133

Credit to drsnooker for his Matlab script that this was converted from: https://forum.hashkiller.io/index.php?threads/unpublished-wpa-key-algorithms.19944/post-353954
