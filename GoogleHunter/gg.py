#! /usr/bin/env python 
#coding=utf-8
import urllib2,urllib
import simplejson
import re                     
print "=========================================="
print "+              GoogleHunter              +" 
print "+             demon#F4ckTeam             +"
print "+          http://www.dawner.info        +"
print "+      EX.===>keyword:site:baidu.com     +"  
print "=========================================="  
fs = open('cache1.txt', 'w')
seachstr = raw_input("Google Keywords?:") 
pages =   int(raw_input("How many pages?:")) 
    
#seachstr = 'site:tatung.com.tw'                                  
for x in range(pages):    
	print "page:%s================================="%(x+1)
	if x!=0:
		fs.write("\n") 	
		fs.write("page:%s"%(x+1))
	else: 
		fs.write("page:%s"%(x+1))   
	page = x * 8                                          
	url = ('https://ajax.googleapis.com/ajax/services/search/web'                  
'?v=1.0&q=%s&rsz=8&start=%s') % (urllib.quote(seachstr),page)   
	try:        
# class urllib2.Request(url[, data][, headers][, origin_req_host][, unverifiable])        
		request = urllib2.Request(        
		url, None, {'Referer': 'http://www.sina.com'})        
		response = urllib2.urlopen(request)  
#urlopen返回的是文件对象                                          
# Process the JSON string.        
		results = simplejson.load(response)        
		infoaaa = results['responseData']['results']    
	except Exception,e:        
		print e    
	else:        
		for minfo in infoaaa:            
			print minfo['url']
			fs.write("\n")
			fs.write(minfo['url'])
#fs.write(all.replace(r'\n', '\n'))
fs.close()
import cut
import dele			
#while 1:
	#file = open("1.txt","r+")
	#text = file.readline()
	#content=url.replace("http://","")
	 
	



