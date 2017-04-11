from bottle import route, run, request, response
import urllib2
import shutil
import os
import sys
response = urllib2.urlopen('https://raw.githubusercontent.com/StevenBlack/hosts/master/alternates/fakenews-gambling-porn-social/hosts')
data = response.read()
filename = "hosts"
hostfile= open(filename, 'w')
hostfile.write(data)
hostfile.close()
response.close()
@route('/hello')
def hello():
	blocktheshit()
def blocktheshit():
	shutil.copy('C:\Windows\System32\drivers\etc\hosts', 'C:\AdBlock\hosts_backup') 
	shutil.copy('C:\AdBlock\hosts', 'C:\Windows\System32\drivers\etc')
	count()
@route('/unblock')
def unblock():
	shutil.copy('C:\AdBlock\hosts_backup\orignal\hosts', 'C:\Windows\System32\drivers\etc')
	count()
@route('/count')
def count():
	count = 0
	with open('C:\Windows\System32\drivers\etc\hosts') as fileObj:
		for line in fileObj:  
			for ch in line:
				if(ch=='0'):
					count = count + 1
					break
				else:
					break
	content1 = '''<!DOCTYPE html><html><head><link href="https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz" rel="stylesheet"></head><body><p style="font-family: 'Yanone Kaffeesatz', sans-serif; font-size: 48px;">'''
	content2 = str(count)
	content3 = '''</p></body></html>'''
	file="iframe.html"
	f = open(file, 'w')
	f.write(content1)
	f.write(content2)
	f.write(content3)
	f.close()
	return str(count)
@route('/query')
def query():
	flag=0
	content2='Not Matched'
	ifile="iframe2.html"
	fl = open(ifile, 'w')
	query = request.query.q
	content1 = '''<!DOCTYPE html><html><head><link href="https://fonts.googleapis.com/css?family=Yanone+Kaffeesatz" rel="stylesheet"></head><body><p style="font-family: 'Yanone Kaffeesatz', sans-serif; font-size: 48px;">'''
	content3 = '''</p></body></html>'''
	querycheck = '0.0.0.0 '+ query
	file = "C:\Windows\System32\drivers\etc\hosts"
	f3=open(file, 'r')
	for line in f3:
		if(querycheck in line):
			flag=1
			break
	if(flag==1):
		content2='Matched'
		fl.write(content1)
		fl.write(content2)
		fl.write(content3)
	else:	
		fl.write(content1)
		fl.write(content2)
		fl.write(content3)
	f3.close()
	return content2
@route('/blacklist')
def blacklist():
	j=0
	file2 = "C:\Windows\System32\drivers\etc\hosts"
	f2 = open(file2, 'a')
	url = request.query.url
	for i in range(0,len(url)):
		if(url[i]==','):
			data2 = '0.0.0.0 '+url[j : i]+'\n'
			j=i+1
			f2.write(data2)
	data2 = '0.0.0.0 '+url[j : i+1]+'\n'	
	f2.write(data2)
	f2.close()	
run(host='localhost', port=8383, debug=True)