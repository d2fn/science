#!/usr/bin/python

import string
import os
import sys

if __name__ == "__main__":
	means = {}
	i = 0
	for line in sys.stdin:
		parts = string.split(line, "\t")
		num = int(parts[0])
		key = parts[1][:-1]
		if key in means.keys():
			means[key][0] += num
			means[key][1] += 1
		else:
			means[key] = [num, 1]
		i = i + 1
#		if i%100 == 0:
#			print str(i) + "..."
	for key in means:
		n = means[key][1]
		mean = int(round(means[key][0]/n))
		print key + "\t" + str(mean) + "\t" + str(n)

