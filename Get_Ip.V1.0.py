#Tools Get IPS V.1.0
#!/usr/bin/python
# -*- coding: utf-8 -*
#JametKNTLS - h0d3_g4n - Moslem - Jenderal92 -Kiddenta
# Blog : https://www.blog-gan.org          
#DONATE ME :(
	# BTC = 31mtLHqhaXXyCMnT2EU73U8fwYwigiEEU1
	# PERFECT MONEY  = U22270614
#You can recode This Tools 
#But I beg you not to delete the author's name.


import requests,re,time,random ,os, sys, socket
from multiprocessing.dummy import Pool
from colorama import Fore
###
def Banner():
	host_name = socket.gethostname()
	host_ip = socket.gethostbyname(host_name)
	print "==================================================="
	print Fore.RED + "[!] Tools Get IPS V.1.0 |" + Fore.WHITE +" "+ Fore.GREEN + "PYTHON CODE" + Fore.WHITE
	print Fore.RED + "[!] Contact : " + Fore.WHITE+"ICQ : Shin403" +"|"+ "TELEGRAM : Shin_code"
	print Fore.RED + "[!] Host : " + Fore.WHITE+"Shin@"+host_name
	print Fore.RED + "[!] LocalHost : " + Fore.WHITE + host_ip
	print "===================================================" 
Banner()

###
print Fore.YELLOW + "1 .Api From usings.ru" + Fore.WHITE
print Fore.YELLOW + "2 .Api From abuseipdb.com" + Fore.WHITE
print Fore.YELLOW + "3. Api From bitverzo.com" + Fore.WHITE
print Fore.YELLOW + "4. Api From macrobyte.net" + Fore.WHITE
print Fore.YELLOW + "5. Api From viewsforcash.com" + Fore.WHITE

shinpilih = raw_input('\nChoose : ')
print "==========" 
def getipe1():
	SHINX = raw_input('Frist Page : ')
	CODEE = raw_input('Last Page : ')
	try:
		for page in range(int(SHINX), int(CODEE)):
			urls = 'http://usings.ru/bots.php?bot=&page='+str(page)
			SHINGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
			if 'IP' in SHINGET:
				REGEX = re.findall("[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}\.[0-9]{1,4}",SHINGET)
				for SHIN in REGEX:
					print(Fore.GREEN + '[Geting Ip--> ]' + Fore.WHITE + SHIN)
					open('result.txt','a').write(SHIN+'\n')
				else:
					print(Fore.RED + '[CODED BY SHIN_CODE --> ]' + Fore.WHITE)
	except:
		pass

def getipe2():
	SHINX = raw_input('Frist Page : ')
	CODEE = raw_input('Last Page : ')
	try:
		for page in range(int(SHINX), int(CODEE)):
			urls = 'https://www.abuseipdb.com/sitemap?page='+str(page)
			SHINGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
			if 'Reported IPs' in SHINGET:
				REGEX = re.findall('<a href="https://www.abuseipdb.com/check/(.*?)">',SHINGET)
				for SHIN in REGEX:
					print(Fore.GREEN + '[Geting Ip--> ]' + Fore.WHITE + SHIN)
					open('result.txt','a').write(SHIN+'\n')
				else:
					print(Fore.RED + '[CODED BY SHIN_CODE --> ]' + Fore.WHITE)
	except:
		pass

def getipe3():
	SHINX = raw_input('Frist Page : ')
	CODEE = raw_input('Last Page : ')
	try:
		for page in range(int(SHINX), int(CODEE)):
			urls = 'http://bitverzo.com/recent_ip?p='+str(page)
			SHINGET = requests.get(urls,headers={'User-Agent':'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'}, timeout=10).text
			if 'Recent IP reviews' in SHINGET:
				REGEX = re.findall('<a href="http://bitverzo.com/ip/(.*?)">',SHINGET)
				for SHIN in REGEX:
					print(Fore.GREEN + '[Geting Ip--> ]' + Fore.WHITE + SHIN)
					open('result.txt','a').write(SHIN+'\n')
				else:
					print(Fore.RED + '[CODED BY SHIN_CODE --> ]' + Fore.WHITE)
	except:
		pass

def getipe4():
	try:
		SHINX = raw_input('Frist Page : ')
		CODEE = raw_input('Last Page : ')
		ua = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
		}
		for page in range(int(SHINX), int(CODEE)):
			urls = "http://macrobyte.net/recent_ip?p="+str(page)
			SHINGET = requests.post(urls,headers=ua, timeout=10).text
			if 'Recent IP reviews' in SHINGET:
				REGEX = re.findall('<a href="http://macrobyte.net/ip/(.*?)">',SHINGET)
				for SHIN in REGEX:
					print(Fore.GREEN + '[Geting Ip--> ]' + Fore.WHITE + SHIN)
					open('result.txt','a').write(SHIN+'\n')
				else:
					print(Fore.RED + '[CODED BY SHIN_CODE --> ]' + Fore.WHITE)
	except:
		pass

def getipe5():
	try:
		SHINX = raw_input('Frist Page : ')
		CODEE = raw_input('Last Page : ')
		ua = {
		'User-Agent': 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)'
		}
		for page in range(int(SHINX), int(CODEE)):
			urls = "http://viewsforcash.com/recent_ip?p="+str(page)
			SHINGET = requests.post(urls,headers=ua, timeout=10).text
			if 'Recent IP reviews' in SHINGET:
				REGEX = re.findall('<a href="http://viewsforcash.com/ip/(.*?)">',SHINGET)
				for SHIN in REGEX:
					print(Fore.GREEN + '[Geting Ip--> ]' + Fore.WHITE + SHIN)
					open('result.txt','a').write(SHIN+'\n')
				else:
					print(Fore.RED + '[CODED BY SHIN_CODE --> ]' + Fore.WHITE)
	except:
		pass

def DELETE_DUPLICATE():
	with open('result.txt', 'r') as SHINXX:
		SHINXXX = list(dict.fromkeys(SHINXX.read().splitlines()))
		with open('result.txt.tmp','a') as new:
			new.write('\n'.join(SHINXXX))
			new.close()
		SHINXX.close()
	os.remove('result.txt')
	os.rename('result.txt.tmp','result.txt')

def Main():
	try:
		if shinpilih == '1':
			getipe1()
		elif shinpilih == '2':
			getipe2()
		elif shinpilih == '3':
			getipe3()
		elif shinpilih == '4':
			getipe4()
		elif shinpilih == '5':
			getipe5()
	except:
		pass

if __name__ == '__main__':
	Main()
	DELETE_DUPLICATE()