#!/usr/bin/python

import string
import os
import sys

def stepper(start, end, step):
	while start <= end:
		yield start
		start += step

def write_line(b, count):
	print str(b) + "\t" + str(count)

def compute_bucket(n, bsize):
	return n//bsize*bsize + bsize

if __name__ == "__main__":
	buckets = {}
	bucket_size = 500
	max_value = -1
	if len(sys.argv) == 2:
		bucket_size = int(sys.argv[1][1:])
	for line in sys.stdin:
		parts = string.split(line, "\t")
		latencyMs = int(parts[0])
		if latencyMs > max_value:
			max_value = latencyMs
		latencyBucket = compute_bucket(latencyMs, bucket_size)
		if latencyBucket in buckets.keys():
			buckets[latencyBucket] += 1
		else:
			buckets[latencyBucket] = 1
	for b in stepper(bucket_size, compute_bucket(max_value, bucket_size), bucket_size):
		if b in buckets.keys():
			write_line(b, buckets[b])
		else:
			write_line(b, 0)

