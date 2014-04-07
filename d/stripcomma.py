#!/usr/bin/python

import fileinput

for line in fileinput.input():
	line = line.strip()
	n = line.find(',')
	if n != -1:
		line = line[0:n]
	print line