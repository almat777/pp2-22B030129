import os

with open(r"ret.txt", 'r') as fp:
	lines = len(fp.readlines())
	print(lines)