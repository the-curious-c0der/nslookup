#! /usr/bin/python

import os

import sys

print "-"*60
def resolver(x):
	a = os.popen("nslookup " + x)
	for line in a.readlines():
		if "Name" in line:
			print line
		if "Address" in line:
			print line
				


resolver(sys.argv[1])

	




















