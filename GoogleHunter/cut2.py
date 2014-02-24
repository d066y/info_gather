#! /usr/bin/env python 
#coding=utf-8
import re
file1 = open("1.txt","r+")
file2 = open("2.txt","w")
while 1:
	url = file1.readline()
	#if( url == 'page' ):
	#	print "123124"		
	#pattern = re.compile(r'.*\d+') 
	#str = 'page'
	#if(pattern.match(str)=="None")
	if "page" in url: 		
		continue
	if( url == '' ):
		break
#url="http://www.tatung.com.tw/b5/responsibility_iso_qa.asp"
	con = str(re.findall("http://.*tw",url))
	#print con
	content=str(con.replace("http://",""))
	content1=str(content.replace("['",""))
	content2=str(content1.replace("']",""))
	print content2
	file2.write(content2)
	file2.write("\n")
file1.close()
file2.close()

 

