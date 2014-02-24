#! /usr/bin/env python 
#coding=utf-8
import os
d = {}
for line in open('cache2.txt'):
    d[line] = d.get(line, 0) + 1 
fd = open('result.txt', 'w')
for k, v in d.items():
    if v > 0: 
	#fd.write("\n")
        fd.write(k)
	print(k)
fd.close()
os.remove('cache1.txt')
os.remove('cache2.txt')
os.remove('cut.pyc')
os.remove('dele.pyc')
#import zzuu
