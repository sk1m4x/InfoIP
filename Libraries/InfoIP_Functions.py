# /Libraries/InfoIP_Functions.py
# Classes, Methods, Variables.


# Development.
__OS__ 			=	"Ubuntu / Linux"
__name__		=	"InfoIP"
__author__		=	"sk1m4x"
__version__		=	"1.0"	
__subtitle__	=	"Advanced Geolocation"
__Py_Version__	=	"Python 2.7.8"
__last_update__	=	"12/02/2015"

# Colors.
Basic_Green 	=	"\033[0;32m"
Green			=	"\033[1;32m"
Green_Underline	=	"\033[4;32m"
Basic_Yellow	=	"\033[0;33m"
Yellow 			=	"\033[1;33m"
White			=	"\033[0;37m"
WhiteB			=	"\033[1;37m"
Basic_Red		=	"\033[0;31m"
Red				=	"\033[1;31m"
Cyan			=	"\033[1;36m"
Basic_Cyan		=	"\033[0;36m"
Blue			=	"\033[1;34m"
Basic_Blue		=	"\033[0;34m"
Light_Blue		=	"\033[0;94m"
Blue_Underline	=	"\033[4;34m"
Default			=	"\033[0m"
Underline		=	"\033[4;32m"

import sys
import time
import json
import requests
import socket
import os

class IP_Method:
	def start(self):
		try:
			history = open("Logs/IP_Method.log", "a").write("[ %s ]	%s	\n" % (time.strftime("%Y-%m-%d %H:%M"), sys.argv[2]))
			print "%s[ ! ] Check if a new version of InfoIP: http://www.github.com/sk1m4x/InfoIP%s" % (Basic_Yellow, Default)
			print "%s[ ? ] Need help?: $ python %s --help %s" % (Light_Blue, sys.argv[0], Default)
			print "%s[ ! ] %sIP Method%s (-i) started.%s" % (Basic_Blue, Blue, Basic_Blue, Default)
			print "%s[...] Searching for %s%s%s%s\n" % (Basic_Blue, Blue, Blue_Underline, sys.argv[2], Default)

			My_API	=	requests.get("http://ip-api.com/json/%s" % sys.argv[2])

			LoadJson	=	json.loads(My_API.content)
			Adv_API	=	requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true_or_false" % (LoadJson['lat'], LoadJson['lon']))


			print "%sBasic Information%s" % (Green, Basic_Green)
			print "%sCountry		:\t%s%s [%s]".decode('utf-8') % (Basic_Green, White, LoadJson['country'], LoadJson['countryCode'])
			print "%sCity		:\t%s%s - %s (%s)".decode('utf-8') % (Basic_Green, White, LoadJson['city'], LoadJson['region'], LoadJson['regionName'])
			print "%sTimezone	:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['timezone'])
			print "%sZip		:\t%s%s\n".decode('utf-8') % (Basic_Green, White, LoadJson['zip'])

			print "\033[1;32mInternet Information\033[0m"
			print "%sISP		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['isp'])
			print "%sOrg.		:\t%s%s\n".decode('utf-8') % (Basic_Green, White, LoadJson['as'])

			print "%sAdvanced Information%s" % (Green, Basic_Green)
			print "%sLat.		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'])
			print "%sLon.		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['lon'])
			print "%sCoord.		:\t%s%s,%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'], LoadJson['lon'])
			print "%sGoogle Maps 	:\t%swww.google.com.br/maps/place/%s,%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'], LoadJson['lon'])

			print "%sStreet Number\t:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][0]['long_name'])
			print "%sRoute		:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][1]['long_name'])
			print "%sNeighborhood	:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][2]['long_name'])
			#print "%sPostal-Code	:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][7]['long_name'])
			print Default
		except IndexError: print "%s\nYou did not enter a target:\n%s$ python %s -i 0.0.0.0\n%s" % (Red, Basic_Red, sys.argv[0], Default)
		except KeyError: print "\n%sIncorrect target, use only the IP:\n%s$ python %s -i 0.0.0.0\n%s" % (Red, Basic_Red, sys.argv[0], Default)

class Skype_Method:
	def start(self):
		try:
			history = open("Logs/Skype_Method.log", "a").write("[ %s ]	%s	\n" % (time.strftime("%Y-%m-%d %H:%M"), sys.argv[2]))
			print "%s[ ! ] Check if a new version of InfoIP: http://www.github.com/sk1m4x/InfoIP%s" % (Basic_Yellow, Default)
			print "%s[ ? ] Need help?: $ python %s --help %s" % (Light_Blue, sys.argv[0], Default)
			print "%s[ ! ] %sSkype Method%s (-s) started.%s" % (Basic_Cyan, Cyan, Basic_Cyan, Default)
			print "%s[...] Searching for %s%s%s%s\n" % (Basic_Blue, Blue, Blue_Underline, sys.argv[2], Default)
			Get_Skype	=	requests.get("http://api.predator.wtf/resolver/?arguments=%s" % sys.argv[2]).text.replace(u'\ufeff', '')
			My_API	=	requests.get("http://ip-api.com/json/%s" % Get_Skype)

			LoadJson	=	json.loads(My_API.content)
			Adv_API		=	requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true_or_false" % (LoadJson['lat'], LoadJson['lon']))

			print "%sBasic Information%s" % (Green, Basic_Green)
			print "%sCountry		:\t%s%s [%s]".decode('utf-8') % (Basic_Green, White, LoadJson['country'], LoadJson['countryCode'])
			print "%sCity		:\t%s%s - %s (%s)".decode('utf-8') % (Basic_Green, White, LoadJson['city'], LoadJson['region'], LoadJson['regionName'])
			print "%sTimezone	:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['timezone'])
			print "%sZip		:\t%s%s\n".decode('utf-8') % (Basic_Green, White, LoadJson['zip'])

			print "\033[1;32mInternet Information\033[0m"
			print "%sIP		:\t%s%s".decode('utf-8') % (Basic_Green, White, Get_Skype)
			print "%sISP		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['isp'])
			print "%sOrg.		:\t%s%s\n".decode('utf-8') % (Basic_Green, White, LoadJson['as'])

			print "%sAdvanced Information%s" % (Green, Basic_Green)
			print "%sLat.		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'])
			print "%sLon.		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['lon'])
			print "%sCoord.		:\t%s%s,%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'], LoadJson['lon'])
			print "%sGoogle Maps 	:\t%swww.google.com.br/maps/place/%s,%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'], LoadJson['lon'])

			print "%sStreet Number\t:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][0]['long_name'])
			print "%sRoute		:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][1]['long_name'])
			print "%sNeighborhood	:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][2]['long_name'])
			#print "%sPostal-Code	:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][7]['long_name'])
			print Default
		except IndexError: print "\n%sUsage:\n%s$ python %s -s USER_ACCOUNT%s\n" % (White, Basic_Green, sys.argv[0], Default)
		except KeyError: print "Unable to locate the user '%s'." % sys.argv[2]

class Host_Method:
	def start(self):
		try:
			history = open("Logs/Host_Method.log", "a").write("[ %s ]	%s	\n" % (time.strftime("%Y-%m-%d %H:%M"), sys.argv[2]))
			print "%s[ ! ] Check if a new version of InfoIP: http://www.github.com/sk1m4x/InfoIP%s" % (Basic_Yellow, Default)
			print "%s[ ? ] Need help?: $ python %s --help %s" % (Light_Blue, sys.argv[0], Default)
			print "%s[ ! ] %sHost Method%s (-h) started.%s" % (Basic_Green, Green, Basic_Green, Default)
			print "%s[...] Searching for %s%s%s%s\n" % (Basic_Blue, Blue, Blue_Underline, sys.argv[2], Default)
			My_API	=	requests.get("http://ip-api.com/json/%s" % socket.gethostbyname(sys.argv[2]))

			LoadJson	=	json.loads(My_API.content)
			Adv_API	=	requests.get("http://maps.googleapis.com/maps/api/geocode/json?latlng=%s,%s&sensor=true_or_false" % (LoadJson['lat'], LoadJson['lon']))
			print "%sBasic Information%s" % (Green, Basic_Green)
			print "%sCountry		:\t%s%s [%s]".decode('utf-8') % (Basic_Green, White, LoadJson['country'], LoadJson['countryCode'])
			print "%sCity		:\t%s%s - %s (%s)".decode('utf-8') % (Basic_Green, White, LoadJson['city'], LoadJson['region'], LoadJson['regionName'])
			print "%sTimezone	:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['timezone'])
			print "%sZip		:\t%s%s\n".decode('utf-8') % (Basic_Green, White, LoadJson['zip'])

			print "\033[1;32mInternet Information\033[0m"
			print "%sIP		:\t%s%s".decode('utf-8') % (Basic_Green, White, socket.gethostbyname(sys.argv[2]))
			print "%sISP		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['isp'])
			print "%sOrg.		:\t%s%s\n".decode('utf-8') % (Basic_Green, White, LoadJson['as'])

			print "%sAdvanced Information%s" % (Green, Basic_Green)
			print "%sLat.		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'])
			print "%sLon.		:\t%s%s".decode('utf-8') % (Basic_Green, White, LoadJson['lon'])
			print "%sCoord.		:\t%s%s,%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'], LoadJson['lon'])
			print "%sGoogle Maps 	:\t%swww.google.com.br/maps/place/%s,%s".decode('utf-8') % (Basic_Green, White, LoadJson['lat'], LoadJson['lon'])

			print "%sStreet Number\t:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][0]['long_name'])
			print "%sRoute		:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][1]['long_name'])
			print "%sNeighborhood	:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][2]['long_name'])
			#print "%sPostal-Code	:\t%s%s" % (Basic_Green, White, json.loads(Adv_API.content)['results'][0]['address_components'][7]['long_name'])
			print Default
		except IndexError: print "%sYou did not enter a target: %s$ python %s -h www.host.com%s" % (Red, Basic_Red, sys.argv[0], Default)

class Help:
	def Window(self):

		print "%sAbout InfoIP.%s" % (WhiteB, White)
		print """This tool is developed to make geographic tracking of a determined target.
Based on Application Programming Interface (API) Google and IP-Api (http://ip-api.com/).
It's possible determine a target IP, Skype account or Host.\n"""
		print "%sIP Tracking%s    (-i).%s" % (WhiteB, White, Default)
		print "%s$ python %s -i 0.0.0.0%s\n" % (Basic_Green, sys.argv[0], Default)

		print "%sHOST Tracking%s  (-h).%s" % (WhiteB, White, Default)
		print "%s$ python %s -h www.target.com%s\n" % (Basic_Green, sys.argv[0], Default)

		print "%sSKYPE Tracking%s (-s).%s" % (WhiteB, White, Default)
		print "%s$ python %s -s USER_ACCOUNT%s\n" % (Basic_Green, sys.argv[0], Default)

		print "%sOfficial Repository%s (GitHub):" % (WhiteB, White)
		print "http://github.com/sk1m4x/InfoIP/"
		print Default

	def Version(self):
		print "%sVersion:%s %s. %sLast update:%s %s %s\n" % (WhiteB, White, __version__, WhiteB, White, __last_update__, Default)

class Update:
	def Load(self):
		print "%sAtualizacao %s" % (White, Default)

class ReadFile:
	def View_Hosts(self):
		Filename = "Logs/Host_Method.log"
		print "%s%s%s:" % (WhiteB, Filename, Default)
		print "%s%s%s" % (White, open(Filename, "r").read(), Default)

	def View_Ips(self):
		Filename = "Logs/IP_Method.log"
		print "%s%s%s:" % (WhiteB, Filename, Default)
		print "%s%s%s" % (White, open(Filename, "r").read(), Default)

	def View_SUsers(self):
		Filename = "Logs/Skype_Method.log"
		print "%s%s%s:" % (WhiteB, Filename, Default)
		print "%s%s%s" % (White, open(Filename, "r").read(), Default)

# Enjoy. ;)
