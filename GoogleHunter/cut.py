#! /usr/bin/env python 
#coding=utf-8
import re
import urlparse
file1 = open("cache1.txt","r+")
file2 = open("cache2.txt","w")
while 1:
	url = file1.readline()
	if "page" in url: 		
		continue
	if( url == '' ):
		break
	parsedTuple = urlparse.urlparse(url)
	print parsedTuple[1]
	#con = str(re.findall("http://.*tw",url))
	#print con
	#content=str(con.replace("http://",""))
	#content1=str(content.replace("['",""))
	#content2=str(content1.replace("']",""))
	#print content2
	file2.write(parsedTuple[1])
	file2.write("\n")
file1.close()
file2.close()
