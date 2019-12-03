#!/usr/bin/env python3

import urllib.request, urllib.error
from time import gmtime, strftime
import socket, sys, os, time
import requests

session = "c3b9e6b6-d5a7-44f6-b183-634e479afd5c"

class colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

def check_url(url):

	try:
		headers = {}
		headers['Cookie'] = "session=" + session
		req = urllib.request.Request(url, headers = headers)
		conn = urllib.request.urlopen(req)
	except urllib.error.HTTPError as e:
	    # Return code error (e.g. 404, 501, ...)
	    # ...
	    #print('HTTPError: {}'.format(e.code))
	    return False
	except urllib.error.URLError as e:
	    # Not an HTTP-specific error (e.g. connection refused)
	    # ...
	    #print('URLError: {}'.format(e.reason))
	    return False
	else:
	    # 200
	    # ...
	    return True

def check_ctfd():
	title = "Checking  CTFD url  ".ljust(50, '-') + " "	
	if (check_url("https://ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_twisore_account():
	title = "Checking Twisore Account  ".ljust(50, '-') + " "	

	f = requests.get("https://soundcloud.com/twisore")

	if ("twisore999@gmail.com" in f.text):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)


def check_sometimes():
	
	title = "Checking \"Sometimes\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://sometimes.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_emoji():
	
	title = "Checking \"Emoji\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://emoji.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)


def check_pingv1():
	
	title = "Checking \"PingV1\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://pingv1.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_authent():
	
	title = "Checking \"Authent\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://authent.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_diary():
	
	title = "Checking \"Journal intime\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://diary.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_moul1():
	
	title = "Checking \"Comme dans un moul'1\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://moulin.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_moul2():
	
	title = "Checking \"Comme dans un moul'2\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://moulin.ctf.ineat.fr/")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_nothumans():

	title = "Checking \"Not-Humans\" chall  ".ljust(50, '-') + " "
	host = "nothumans.ctf.ineat.fr"
	port = 8080

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(3)
		s.connect((host, port))
		  			
		s.send(b'test' + b'\n');
		result = s.recv(1024).strip();
		
		if not len(result) :
			print(title + colors.FAIL + "[KO]" + colors.ENDC)
		elif (b"UGGC" in result):
			print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
		else:
			print(title + colors.FAIL + "[KO]" + colors.ENDC)	

		s.close()	

	except socket.error:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def print_header():
	print("".ljust(55, '#'))
	print(("Date du test :   " + strftime("%d-%m-%Y %H:%M:%S", gmtime()).center(57, ' ')))
	print("".ljust(55, '#'))


def check_file(path):
    r = requests.head(path)
    return r.status_code == requests.codes.ok

def check_weblogs():

	title = "Checking \"Web Logs\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/992e48ac905e0f8331f5da2fc2528adc/dump_web_logs.pcap?token=.eJyrVipJTcyNz0xRsjLUUSotTi2CsdMyc1LBbKNaAObFC-k.Xbi1Vw.mm3ETGFM8e2zbAOucmOjv7AEhCs")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_cat_eyes():

	title = "Checking \"Cat eyes\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/a4ef5b3688b2f7047122ff768b25734f/cats_eyes.png")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_image_speaks():

	title = "Checking \"L’image parle d’elle même\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/a9c6f402ece956ed6c0ed98e1caec601/the_image_speaks_for_itself.bmp")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_space_trip():

	title = "Checking \"Voyage dans l'espace\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/4670931b9beef2721951e1c8ffff98f6/challenge.png")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)


def check_elliot():

	title = "Checking \"Elliot\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/33ff5f7f983b2b8390a53a0e55d83aaa/Private-data.zip")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_OPrikube():

	title = "Checking \"OP'rikube\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/318a29e8a3dfbcd114c0d3450fbcbaca/oprikube.kdbx")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)


def check_president():

	title = "Checking \"Allô, président?\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/c138c701d32e4fa00f5e056fc25b94e5/president.pcap")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_cookie():

	title = "Checking \"Recette spéciale\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/48d2002b7552e77017aedd1f87d2ac80/chall_cookies.txt")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)


def check_chat():

	title = "Checking \"Trouvez le chat\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/314084e70f7f52085d529f76dc1c377d/chat.zip")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_pencil():

	title = "Checking \"Coup de crayon\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/da64317bf658bb4e270ced6e8130399c/cestecrit.png")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_encodingUU():

	title = "Checking \"Encodage - UU\" chall  ".ljust(50, '-') + " "
	
	if (check_url("https://ctf.ineat.fr/files/8f475cede9a602bf968d4fcd7b484013/uuencode.txt")):
		print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
	else:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)


def check_ssh_logs():

        title = "Checking \"SSH logs\" chall  ".ljust(50, '-') + " "
        
        if (check_url("https://ctf.ineat.fr/files/bb3ce7df3d285c82657eac4f9905941e/ssh.log")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_base_jumper():

        title = "Checking \"Base Jumper\" chall  ".ljust(50, '-') + " "

        if (check_url("https://ctf.ineat.fr/files/702fac719effdf70dab6a72f4246684b/base-jumper.jpg")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_gogol():
        title = "Checking \"Gogol\" chall  ".ljust(50, '-') + " "

        if (check_url("https://gogol.ctf.ineat.fr")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)	


def check_g0g0l():
        title = "Checking \"G0g0l\" chall  ".ljust(50, '-') + " "

        if (check_url("https://g0g0l.ctf.ineat.fr")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_android_crackme_01():
        title = "Checking \"Android Crack Me 01\" chall  ".ljust(50, '-') + " "

        if (check_url("https://ctf.ineat.fr/files/7955be8dd8eaa9063aa541f2e3c8109f/android-crackme-01.apk")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_android_crackme_02():
        title = "Checking \"Android Crack Me 02\" chall  ".ljust(50, '-') + " "

        if (check_url("https://ctf.ineat.fr/files/921291455aa20d7f049b17f6fd863077/android-crackme-02.apk")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_android_crackme_03():
        title = "Checking \"Android Crack Me 03\" chall  ".ljust(50, '-') + " "

        if (check_url("https://ctf.ineat.fr/files/3dce4ab030af3be8e963a31d9c55facc/android-crackme-03.apk")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_android_crackme_04():
        title = "Checking \"Android Crack Me 04\" chall  ".ljust(50, '-') + " "

        if (check_url("https://ctf.ineat.fr/files/a2da8a63e5e1c6cdbe827de735ad18ee/android-crackme-04.apk")):
                print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
        else:
                print(title + colors.FAIL + "[KO]" + colors.ENDC)

def check_bashme():

	title = "Checking \"Bash Me\" chall  ".ljust(50, '-') + " "
	host = "bashme.ctf.ineat.fr"
	port = 2222

	try:
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		s.settimeout(3)
		s.connect((host, port))		  			
				
		result = s.recv(1024).strip();
				
		if (b"SSH-2.0-OpenSSH_7.6p1 Ubuntu-4ubuntu0.3" == result):
			print(title + colors.OKGREEN + "[OK]" + colors.ENDC)
		else:
			print(title + colors.FAIL + "[KO]" + colors.ENDC)	

		s.close()	

	except socket.error:
		print(title + colors.FAIL + "[KO]" + colors.ENDC)	


while True:
	os.system('clear') 

	print_header()
	print()
	check_ctfd()
	print()
	check_sometimes()
	check_emoji()
	check_pingv1()
	check_authent()
	check_diary()
	check_moul1()
	check_moul2()
	check_gogol()
	check_g0g0l()
	print()
	check_nothumans()
	check_bashme()
	print()
	check_weblogs()
	check_ssh_logs()
	check_cat_eyes()
	check_image_speaks()
	check_space_trip()
	check_elliot()
	check_OPrikube()
	check_president()
	check_cookie()
	check_chat()
	check_pencil()
	check_encodingUU()
	check_base_jumper()
	check_android_crackme_01()
	check_android_crackme_02()
	check_android_crackme_03()
	check_android_crackme_04()
	print()
	check_twisore_account()

	time.sleep(5*60)
