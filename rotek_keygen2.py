# keygen for some Rotek modems with ESSID RT-WIFI-HHHH and RT-GPON-HHHH
# Based on reverse engineering of the algorithm  found in /bin/flash in some firmware 
# or /lib/libapmib.so in others.
# 
# the seeds are derived from an unknown hardware ID number found in /dev/mtdblock0
#
# seed 1 has a range of 0..0x763d
# seed 2 has a range of 0..0x7663
# seed 3 has a range of 0..0x7673
#
# however the real life range seems to be much smaller with most seed2 around 22000 and seed3=133

import argparse

def rotek_keygen2(seed1, seed2, seed3):
	charset = 'aaaaabcdeeeeefghiiiijkmnpqrstuuuuuvwxyyyyzAAAABCDEEEEFGHJKLMNPQRSTUUUUVWXYYYYZ233445677889'

	pos = 18
	pwd = ["" for i in range(18)]
	while pos > 0:
		seed1 = 171*seed1 % int('763d', 16)
		seed2 = 172*seed2 % int('7663', 16)
		seed3 = 170*seed3 % int('7673', 16)
		total = seed1+seed2+seed3
		letter = charset[total % len(charset)]
		pwd[pos-1] = letter

		if pos < 18:
			if pwd[pos-1] == pwd[pos]:
				pos = pos + 1

		if pos < 17:
			if pwd[pos-1] == pwd[pos+1]:
				pos = pos + 1

		if pos < 16:
			if pwd[pos-1] == pwd[pos+2]:
				pos = pos + 1

		pos = pos-1

	psk = pwd[8:18]
	admin = pwd[0:8]
	print("PSK: %s" % "".join(psk))
	print("Admin: %s" % "".join(admin))

parser = argparse.ArgumentParser(description='Keygen for some Rotek modems with ESSID RT-WIFI-HHHH and RT-GPON-HHHH')
parser.add_argument('seed1', help='Seed1', type=int)
parser.add_argument('seed2', help='Seed2', type=int)
parser.add_argument('seed3', help='Seed3', type=int)
args = parser.parse_args()

rotek_keygen2(args.seed1, args.seed2, args.seed3)
