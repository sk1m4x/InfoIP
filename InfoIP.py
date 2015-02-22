#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
InfoIP - Advanced Geolocation.

Author:
sk1m4x

Last Update:
12/02/2015

Tested on operating systems (It will not run on Windows, USE LINUX!):
*  Ubuntu (Linux)
*  Debian (Linux)

GitHub:
http://github.com/sk1m4x/InfoIP/

Facebook:
https://www.facebook.com/pages/Spade-Team/334797706721469?fref=photo
'''

# Development.
__OS__ 			=	"Ubuntu / Linux"
__name__		=	"InfoIP"
__author__		=	"sk1m4x"
__version__		=	"1.0"
__subtitle__	=	"Advanced Geolocation"
__Py_Version__	=	"Python 2.7.8"

# Colors.
Basic_Green 	=	"\033[0;32m"
Green			=	"\033[1;32m"
Green_Underline	=	"\033[4;32m"
Basic_Yellow	=	"\033[0;33m"
Yellow 			=	"\033[1;33m"
White			=	"\033[0;37m"
Basic_Red		=	"\033[0;31m"
Red				=	"\033[1;31m"
Cyan			=	"\033[1;36m"
Basic_Cyan		=	"\033[0;36m"
Blue			=	"\033[1;34m"
Basic_Blue		=	"\033[0;34m"
Blue_Underline	=	"\033[4;34m"
Default			=	"\033[0m"
Underline		=	"\033[4;32m"

# Run it.
try:
	import sys
	import json
	import requests
	import socket
	import os

	from Libraries.InfoIP_Functions import *

	if sys.platform != 'linux2':
		print "\nYou are using Linux? ;)\n"

	else:

		print """
	 %s██╗███╗   ██╗███████╗ ██████╗  %s██╗██████╗ 
	 %s██║████╗  ██║██╔════╝██╔═══██╗ %s██║██╔══██╗
	 %s██║██╔██╗ ██║█████╗  ██║   ██║ %s██║██████╔╝
	 %s██║██║╚██╗██║██╔══╝  ██║   ██║ %s██║██╔═══╝ 
	 %s██║██║ ╚████║██║     ╚██████╔╝ %s██║██║     
	 %s╚═╝╚═╝  ╚═══╝╚═╝      ╚═════╝  %s╚═╝╚═╝""" % (White, Basic_Blue, White, Basic_Blue, White, Basic_Blue, White, Basic_Blue, White, Basic_Blue, White, Basic_Blue)

		print "\n%s%s%s%s (%s) by %s (http://www.github.com/sk1m4x/)\n" % (Blue, Blue_Underline, __subtitle__, Basic_Blue, __version__, __author__)



		if sys.argv[1]		==	"-i": IP_Method().start()
		elif sys.argv[1]	==	"-s": Skype_Method().start()
		elif sys.argv[1]	==	"-h": Host_Method().start()
		elif sys.argv[1]	==	"--help": Help().Window()
		elif sys.argv[1]	==	"--version" or sys.argv[1] == "-v": Help().Version()
		elif sys.argv[1]	==	"--update": Update().Load()
		elif sys.argv[1]	==	"--hosts": ReadFile().View_Hosts()
		elif sys.argv[1]	==	"--ips": ReadFile().View_Ips()
		elif sys.argv[1]	==	"--skypes": ReadFile().View_SUsers()
		else:
			print "%sInvalid command: '%s'%s" % (Basic_Red, sys.argv[1], Default)
			print "%s$ python %s --help %s\n" % (White, sys.argv[0], Default)

except IndexError: Help().Window()
except ImportError: print "%sLibraries missing: %s$ python Check_Modules.py%s" % (Red, Basic_Red, Default)
