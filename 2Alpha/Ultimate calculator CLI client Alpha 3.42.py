# some required modules
import math
import random
# model ID
modID = str("PI-6400x702")
konlop = int(1)
adminpas = str("password")
adminusr = str("admin")
print ("Calculator mode: " + str(modID) + " \n")
# boot screen 
print ("|||||||||||||||||||||||")
print ("|   U L T I M A T E   |")
print ("| C A L C U L A T O R |")
print ("|                     |")
print ("| A L P H A   1       |")
print ("|                     |")
print ("|||||||||||||||||||||||")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
biospar = input("Press [ENTER] key to start (Enter B3 to enter BIOS)")
if (biospar == "B3"):
	bioloop = int(0)
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
	while (bioloop == 0):
		print ("====================================================================================>")
		print ("UCALC System Basic Input Output System")
		print ("Model ID: " + str(modID) + "\t\tLoop ID: " + str(konlop))
		print ("Administrator username: " + str(adminusr) + "\nType 'ADMU' to modify")
		print ("Administrator password: " + str(adminpas) + "\nType 'ADMP' to modify")	
		modibio = str(input("Enter a modification code\nType Q to exit: "))
		if (modibio == "ADMU"):
			print ("Administrator account")
			adminusr = str(input("Rename the administrator: "))
		if (modibio == "ADMP"):
			print ("Administrator password")
			adminpas = str(input("Change the password: "))
		if (modibio == "Q"):
			(bioloop == 1)
			if (bioloop == 1):
				if (bioloop == 1):
					print ("Cannot exit BIOS, Looping Error\nSorry :|")
		print ("Error, unknown command")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
'''
print ("Presentation build for:\nMrs. Nelson's pre-algebra class\nAt Walla Walla High School")
bootpas = input("Press [ENTER] key to start...")
print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
'''
# boot menu
print ("Ultimate calculator")
konloop = int(konlop)
#while konloop == 1: # please do not re-enable konloop unless you are going to fix it
print ("Copyleft Sean Walla Walla 2015-2018")
print ("\nReading from UCALC.UCALC_ROM")
print ("\n\n\n/=={Ultimate Calculator}==\\")
print ("| My calculators  [ID: 1] |")
print ("| Setup (old)     [ID: 2] |")
print ("| Wiki            [ID: 3] |")
print ("| Exit            [ID: 4] |")
print ("| Public calc     [ID: 5] |")
print ("| Games           [ID: 6] |")
print ("| Explorer        [ID: 7] |")
print ("| Accessories     [ID: 8] |")
print ("| Settings        [ID: 9] |")
print ("|                         |")
print ("\\                         /")
print (" \\=======================/")
print ("  \\ Version 0.01 alpha  /")
print ("   \\ developer copy    /")
print ("    \\=================/")
print (" ")
uCMainConsole = int(input("Please enter an ID to start "))
# use the typed ID's to access these 4 menus in the calculator
if uCMainConsole == 1:
	konloop == 0
	print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n| My calculators |")
	print ("Error! Cannot display calculators")
# this method contains all the calculations. This one is the most important
if uCMainConsole == 2:
	konloop == 0
	conloop = int(1)
	while conloop == 1:
		print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nUltimate Calculator setup")
		print ("Select a language:")
		print ("Languages starting with A")
		print (" ")
		print ("Languages starting with B")
		print (" ")
		print ("Languages starting with C")
		print ("Catalan, Chinese")
		print ("Languages starting with D")
		print ("Dutch")
		print ("Languages starting with E")
		print ("English")
		print ("Languages starting with F")
		print (" ")
		print ("Languages starting with G")
		print ("German")
		print ("Languages starting with H")
		print (" ")
		print ("Languages starting with I")
		print (" ")
		print ("Languages starting with J")
		print ("Japanese")
		print ("Languages starting with K")
		print ("Korean")
		print ("Languages starting with L")
		print (" ")
		print ("Languages starting with M")
		print (" ")
		print ("Languages starting with N")
		print (" ")
		print ("Languages starting with O")
		print (" ")
		print ("Languages starting with P")
		print (" ")
		print ("Languages starting with Q")
		print (" ")
		print ("Languages starting with R")
		print ("Russian")
		print ("Languages starting with S")
		print ("Spanish")
		print ("Languages starting with T")
		print (" ")
		print ("Languages starting with U")
		print (" ")
		print ("Languages starting with V")
		print (" ")
		print ("Languages starting with W")
		print (" ")
		print ("Languages starting with X")
		print (" ")
		print ("Languages starting with Y")
		print (" ")
		print ("Languages starting with Z")
		print ("Zulu")
		languageselect1 = str(input("Type in your language here: "))
		if languageselect1 == ("english"):
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nSelect calculator type:")
			print ("4 bit   | CAPABLE   | maximum value: 16")
			print ("8 bit   | CAPABLE   | maximum value: 255")
			print ("12 bit  | CAPABLE   | maximum value: 4096")
			print ("16 bit  | CAPABLE   | maximum value: 65,535")
			print ("18 bit  | CAPABLE   | maximum value: 262,144")
			print ("24 bit  | CAPABLE   | maximum value: 8,388,607")
			print ("26 bit  | CAPABLE   | maximum value: UNKNOWN")
			print ("31 bit  | CAPABLE   | maximum value: UNKNOWN")
			print ("32 bit  | CAPABLE   | maximum value: 4,294,967,295")
			print ("36 bit  | CAPABLE   | maximum value: UNKNOWN")
			print ("48 bit  | CAPABLE   | maximum value: 140,737,488,355,327")
			print ("60 bit  | CAPABLE   | maximum value: UNKNOWN")
			print ("64 bit  | CAPABLE   | maximum value: 9,223,372,036,854,775,807")
			print ("128 bit | INCAPABLE | maximum value: 170,141,183,460,469,231,731,687,303,715,884,105,728")
			print ("256 bit | INCAPABLE | maximum value: UNKNOWN")
			print ("512 bit | INCAPABLE | maximum value: UNKNOWN")
			print ("Type in the bit number to continue")
			calcbittype = int(input("My calculator has a maximum integer of "))
			if calcbittype == 4:
				print ("That is a pretty weak calculator. You may want to change that")
				print ("Continuing as 4 bit")
			if calcbittype == 8:
				print ("That is a pretty weak calculator. You may want to change that")
				print ("Continuing as 8 bit")
			if calcbittype == 12:
				print ("That is a pretty weak calculator. You may want to change that")
				print ("Continuing as 12 bit")
			if calcbittype == 16:
				print ("That is a pretty weak calculator. You may want to change that")
				print ("Continuing as 16 bit")
			if calcbittype == 18:
				print ("That is a pretty weak calculator. You may want to change that")
				print ("Continuing as 18 bit")
			if calcbittype == 24:
				print ("That is a pretty weak calculator. You may want to change that")
				print ("Continuing as 24 bit")
			if calcbittype == 26:
				print ("This number is not available.")
				print ("Continuing as 32 bit")
			if calcbittype == 31:
				print ("This number is not available.")
				print ("Continuing as 32 bit")
			if calcbittype == 32:
				print ("Continuing as 32 bit")
			if calcbittype == 36:
				print ("This number is not available.")
				print ("Continuing as 48 bit")
			if calcbittype == 48:
				print ("Continuing as 48 bit")
			if calcbittype == 60:
				print ("This number is not available.")
				print ("Continuing as 64 bit")
			if calcbittype == 64:
				print ("Continuing as 64 bit")
			if calcbittype == 128:
				print ("This version of Python is not capable of 128 bit values")
				print ("Continuing as 64 bit")
			if calcbittype == 256:
				print ("This version of Python is not capable of 256 bit values")
				print ("Continuing as 64 bit")
			if calcbittype == 512:
				print ("This version of Python is not capable of 512 bit values")
				print ("Continuing as 64 bit")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			setupPart3 = input("Press [ENTER] key to continue")
			print ("Setup complete!")
			finalizeSetup = input("Press [ENTER] key to finalize setup")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCalculator ultimate")
			print ("|==================================================================|")
			print ("| Select a mode                                                    |")
			print ("|                                                                  |")
			print ("| Currency                              [ID: 10] .                 |")
			print ("|------------------------------------------------------------------|")
			print ("| Modular division                      [ID: 11]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Addition                              [ID: 12]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Subtraction                           [ID: 13]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Multiplication                        [ID: 14]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Division                              [ID: 15]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Distributive                          [ID: 16]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Temperature                           [ID: 17]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Weight                                [ID: 18]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Distance                              [ID: 19]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Number graph                          [ID: 20]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Square root                           [ID: 21]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| RGB Colors                            [ID: 22]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Speed                                 [ID: 23]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Energy                                [ID: 24]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Days since                            [ID: 25]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Years since                           [ID: 26]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Days between                          [ID: 27]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Years between                         [ID: 28]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Percentage                            [ID: 29]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Addition with decimals                [ID: 30]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Subtraction with decimals             [ID: 31]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Multiplication with decimals          [ID: 32]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Division with decimals                [ID: 33]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Modular division with decimals        [ID: 34]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| First 100,000 digits of PI            [ID: 35]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Greater than                          [ID: 36]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Less than                             [ID: 37]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Greater than or equal to              [ID: 38]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Less than or equal to                 [ID: 39]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Not equal to                          [ID: 40]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Equal to                              [ID: 41]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Greater than (with decimals)          [ID: 42]                   |")
			print ("|------------------------------------------------------------------|")
			print ("| Less than or equal (with decimals)                     [ID: 43]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Greater than or equal to (with decimals)               [ID: 44]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Less than or equal to (with decimals)                  [ID: 46]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Greater than (with decimals)                           [ID: 47]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Not equal to (with decimals)                           [ID: 48]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Equal to (with decimals)                               [ID: 49]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Generate a random number                               [ID: 50]  |")
			print ("|------------------------------------------------------------------|")
			print ("| Generate a random number (with decimals)               [ID: 51]  |")
			print ("|------------------------------------------------------------------|")
			print ("|                                                                  |")
			print ("====================================================================")
			print ("\n\n")
			calcIDSes = int(input("Enter an ID to continue: "))
			if calcIDSes == 10:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Currency calculator")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 11:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Modular division")
				modivision1 = int(input("Enter first number to mod: "))
				modivision2 = int(input("Enter second number to mod: "))
				curanswer = (modivision1 % modivision2)
				print ("The remainder of " + str(modivision1) + " and " + str(modivision2) + " is " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 12:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Addition")
				add1 = int(input("Enter first number to add: "))
				add2 = int(input("\nEnter second number to add: "))
				add3 = int(input("\nEnter third number to add (if you only want to use 2 numbers, type 0): "))
				add4 = int(input("\nEnter fourth number to add (if you only want to use 2 numbers, type 0): "))
				add5 = int(input("\nEnter fifth number to add (if you only want to use 2 numbers, type 0): "))
				curanswer = (add1 + add2 + add3 + add4 + add5)
				print ("\n\nThe answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 13:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Subtract")
				minus1 = int(input("Enter first number to subtract: "))
				minus2 = int(input("\nEnter second number to subtract: "))
				minus3 = int(input("\nEnter third number to subtract (if you only want to use 2 numbers, type 0): "))
				minus4 = int(input("\nEnter fourth number to subtract (if you only want to use 2 numbers, type 0): "))
				minus5 = int(input("\nEnter fifth number to subtract (if you only want to use 2 numbers, type 0): "))
				curanswer = (minus1 - minus2 - minus3 - minus4 - minus5)
				print ("\n\nThe answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 14:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Multiply")
				multiply1 = int(input("Enter first number to multiply: "))
				multiply2 = int(input("Enter second number to multiply: "))
				curanswer = (multiply1 * multiply2)
				print ("\n\nThe answer is: " + str(curanswer)) 
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 15:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Divide")
				divided1 = int(input("Enter first number to divide: "))
				divided2 = int(input("Enter second number to divide: "))
				curanswer = (divided1 / divided2)
				print ("\n\nThe answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 16:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Distributive")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate distributive properties")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 17:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Temperature")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the temperature")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 18:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Weight")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate weight")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 19:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Distance")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate distance")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 20:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Graph")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to use graphing")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 21:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Square root")
				sqrtmain1 = int(input("Enter a number to find its square root: "))
				curanswer = (sqrtmain1 * sqrtmain1) 
				print ("The square root of " + str(sqrtmain1) + " is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 22:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("RGB Calculator")
				red1 = int(input("[RED] Enter a number 0-255 "))
				green1 = int(input("[GREEN] Enter a number 0-255 "))
				blue1 = int(input("[BLUE] Enter a number 0-255 "))
				print ("r: " + str(red1) + " g: " + str(green1) + " b: " + str(blue1))
				if (red1 == 0) and (green1 == 0) and (blue1 == 0):
					print ("The current color is [BLACK]")
				if (red1 == 255) and (green1 == 255) and (blue1 == 255):
					print ("The current color is [WHITE]")
				if (red1 == 255) and (green1 == 0) and (blue1 == 0):
					print ("The current color is [RED]")
				if (red1 == 0) and (green1 == 255) and (blue1 == 0):
					print ("The current color is [GREEN]")
				if (red1 == 0) and (green1 == 0) and (blue1 == 255):
					print ("The current color is [BLUE]")
				if (red1 == 255) and (green1 == 255) and (blue1 == 0):
					print ("The current color is [YELLOW]")
				if (red1 == 255) and (green1 == 0) and (blue1 == 255):
					print ("The current color is [MAGENTA]")
				if (red1 == 0) and (green1 == 255) and (blue1 == 255):
					print ("The current color is [CYAN]")
				print ("Thank you for using the RGB calculator!")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 23:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Speed calculator")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the speed")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 24:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Energy calculator")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the energy")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 25:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Days since")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the days since a date")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 26:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Years since")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the years since a year")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 27:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Days between")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the days between a date")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 28:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Years between")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the years between a date")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 29:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Percentage")
				percent1 = float(input("Enter a number to find its percentage"))
				curanswer = (percent1 / 1)
				print (str(percent1) + " is " + str(curanswer) + " percent of 100")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 30:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Addition (with decimals)")
				add1dec1 = float(input("Enter number 1: "))
				add2dec2 = float(input("Enter number 2: "))
				curanswer = (add1dec1 + add2dec2)
				print ("The current answer is: " + str(curanswer))
				add3dec3 = float(input("Enter number 3: "))
				curanswer = (add1dec1 + add2dec2 + add3dec3)
				print ("The current answer is: " + str(curanswer)) 
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 31:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Subtraction (with decimals)")
				subtract1dec1 = float(input("Enter number 1: "))
				subtract2dec2 = float(input("Enter number 2: "))
				curanswer = (subtract1dec1 - subtract2dec2)
				print ("The current answer is: " + str(curanswer))
				subtract3dec3 = float(input("Enter numer 3: "))
				curanswer = (subtract1dec1 - subtract2dec2 - subtract3dec3)
				print ("The current answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 32:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Multiplication (with decimals)")
				multiply1dec1 = float(input("Enter number 1: "))
				multiply2dec2 = float(input("Enter number 2: "))
				curanswer = (multiply1dec1 * multiply2dec2)
				print ("The current answer is: " + str(curanswer))
				multiply3dec3 = float(input("Enter number 3: "))
				curanswer = (multiply1dec1 * multiply2dec2 * multiply3dec3)
				print ("The current answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 33:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Division (with decimals)")
				div1dec1 = float(input("Enter number 1: "))
				div2dec2 = float(input("Enter number 2: "))
				curanswer = (div1dec1 / div2dec2)
				print ("The current answer is: " + str(curanswer))
				div3dec3 = float(input("Enter number 3: "))
				curanswer = (div1dec1 / div2dec2 / div3dec3)
				print ("The current answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 34:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 35:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("First 100K digits of Pi")
				print ("3.141592653589793238462643383279502884197169399375105820974944592307816406286 208998628034825342117067982148086513282306647093844609550582231725359408128481 117450284102701938521105559644622948954930381964428810975665933446128475648233 786783165271201909145648566923460348610454326648213393607260249141273724587006 606315588174881520920962829254091715364367892590360011330530548820466521384146 951941511609433057270365759591953092186117381932611793105118548074462379962749 567351885752724891227938183011949129833673362440656643086021394946395224737190 702179860943702770539217176293176752384674818467669405132000568127145263560827 785771342757789609173637178721468440901224953430146549585371050792279689258923 542019956112129021960864034418159813629774771309960518707211349999998372978049 951059731732816096318595024459455346908302642522308253344685035261931188171010 003137838752886587533208381420617177669147303598253490428755468731159562863882 353787593751957781857780532171226806613001927876611195909216420198938095257201 065485863278865936153381827968230301952035301852968995773622599413891249721775 283479131515574857242454150695950829533116861727855889075098381754637464939319 255060400927701671139009848824012858361603563707660104710181942955596198946767 837449448255379774726847104047534646208046684259069491293313677028989152104752 162056966024058038150193511253382430035587640247496473263914199272604269922796 782354781636009341721641219924586315030286182974555706749838505494588586926995 690927210797509302955321165344987202755960236480665499119881834797753566369807 426542527862551818417574672890977772793800081647060016145249192173217214772350 141441973568548161361157352552133475741849468438523323907394143334547762416862 518983569485562099219222184272550254256887671790494601653466804988627232791786 085784383827967976681454100953883786360950680064225125205117392984896084128488 626945604241965285022210661186306744278622039194945047123713786960956364371917 287467764657573962413890865832645995813390478027590099465764078951269468398352 595709825822620522489407726719478268482601476990902640136394437455305068203496 252451749399651431429809190659250937221696461515709858387410597885959772975498 930161753928468138268683868942774155991855925245953959431049972524680845987273 644695848653836736222626099124608051243884390451244136549762780797715691435997 700129616089441694868555848406353422072225828488648158456028506016842739452267 467678895252138522549954666727823986456596116354886230577456498035593634568174 324112515076069479451096596094025228879710893145669136867228748940560101503308 617928680920874760917824938589009714909675985261365549781893129784821682998948 722658804857564014270477555132379641451523746234364542858444795265867821051141 354735739523113427166102135969536231442952484937187110145765403590279934403742 007310578539062198387447808478489683321445713868751943506430218453191048481005 370614680674919278191197939952061419663428754440643745123718192179998391015919 561814675142691239748940907186494231961567945208095146550225231603881930142093 762137855956638937787083039069792077346722182562599661501421503068038447734549 202605414665925201497442850732518666002132434088190710486331734649651453905796 268561005508106658796998163574736384052571459102897064140110971206280439039759 515677157700420337869936007230558763176359421873125147120532928191826186125867 321579198414848829164470609575270695722091756711672291098169091528017350671274 858322287183520935396572512108357915136988209144421006751033467110314126711136 990865851639831501970165151168517143765761835155650884909989859982387345528331 635507647918535893226185489632132933089857064204675259070915481416549859461637 180270981994309924488957571282890592323326097299712084433573265489382391193259 746366730583604142813883032038249037589852437441702913276561809377344403070746 921120191302033038019762110110044929321516084244485963766983895228684783123552 658213144957685726243344189303968642624341077322697802807318915441101044682325 271620105265227211166039666557309254711055785376346682065310989652691862056476 931257058635662018558100729360659876486117910453348850346113657686753249441668 039626579787718556084552965412665408530614344431858676975145661406800700237877 659134401712749470420562230538994561314071127000407854733269939081454664645880 797270826683063432858785698305235808933065757406795457163775254202114955761581 400250126228594130216471550979259230990796547376125517656751357517829666454779 174501129961489030463994713296210734043751895735961458901938971311179042978285 647503203198691514028708085990480109412147221317947647772622414254854540332157 185306142288137585043063321751829798662237172159160771669254748738986654949450 114654062843366393790039769265672146385306736096571209180763832716641627488880 078692560290228472104031721186082041900042296617119637792133757511495950156604 963186294726547364252308177036751590673502350728354056704038674351362222477158 915049530984448933309634087807693259939780541934144737744184263129860809988868 741326047215695162396586457302163159819319516735381297416772947867242292465436 680098067692823828068996400482435403701416314965897940924323789690706977942236 250822168895738379862300159377647165122893578601588161755782973523344604281512 627203734314653197777416031990665541876397929334419521541341899485444734567383 162499341913181480927777103863877343177207545654532207770921201905166096280490 926360197598828161332316663652861932668633606273567630354477628035045077723554 710585954870279081435624014517180624643626794561275318134078330336254232783944 975382437205835311477119926063813346776879695970309833913077109870408591337464 144282277263465947047458784778720192771528073176790770715721344473060570073349 243693113835049316312840425121925651798069411352801314701304781643788518529092 854520116583934196562134914341595625865865570552690496520985803385072242648293 972858478316305777756068887644624824685792603953527734803048029005876075825104 747091643961362676044925627420420832085661190625454337213153595845068772460290 161876679524061634252257719542916299193064553779914037340432875262888963995879 475729174642635745525407909145135711136941091193932519107602082520261879853188 770584297259167781314969900901921169717372784768472686084900337702424291651300 500516832336435038951702989392233451722013812806965011784408745196012122859937 162313017114448464090389064495444006198690754851602632750529834918740786680881 833851022833450850486082503930213321971551843063545500766828294930413776552793 975175461395398468339363830474611996653858153842056853386218672523340283087112 328278921250771262946322956398989893582116745627010218356462201349671518819097 303811980049734072396103685406643193950979019069963955245300545058068550195673 022921913933918568034490398205955100226353536192041994745538593810234395544959 778377902374216172711172364343543947822181852862408514006660443325888569867054 315470696574745855033232334210730154594051655379068662733379958511562578432298 827372319898757141595781119635833005940873068121602876496286744604774649159950 549737425626901049037781986835938146574126804925648798556145372347867330390468 838343634655379498641927056387293174872332083760112302991136793862708943879936 201629515413371424892830722012690147546684765357616477379467520049075715552781 965362132392640616013635815590742202020318727760527721900556148425551879253034 351398442532234157623361064250639049750086562710953591946589751413103482276930 624743536325691607815478181152843667957061108615331504452127473924544945423682 886061340841486377670096120715124914043027253860764823634143346235189757664521 641376796903149501910857598442391986291642193994907236234646844117394032659184 044378051333894525742399508296591228508555821572503107125701266830240292952522 011872676756220415420516184163484756516999811614101002996078386909291603028840 026910414079288621507842451670908700069928212066041837180653556725253256753286 129104248776182582976515795984703562226293486003415872298053498965022629174878 820273420922224533985626476691490556284250391275771028402799806636582548892648 802545661017296702664076559042909945681506526530537182941270336931378517860904 070866711496558343434769338578171138645587367812301458768712660348913909562009 939361031029161615288138437909904231747336394804575931493140529763475748119356 709110137751721008031559024853090669203767192203322909433467685142214477379393 751703443661991040337511173547191855046449026365512816228824462575916333039107 225383742182140883508657391771509682887478265699599574490661758344137522397096 834080053559849175417381883999446974867626551658276584835884531427756879002909 517028352971634456212964043523117600665101241200659755851276178583829204197484 423608007193045761893234922927965019875187212726750798125547095890455635792122 103334669749923563025494780249011419521238281530911407907386025152274299581807 247162591668545133312394804947079119153267343028244186041426363954800044800267 049624820179289647669758318327131425170296923488962766844032326092752496035799 646925650493681836090032380929345958897069536534940603402166544375589004563288 225054525564056448246515187547119621844396582533754388569094113031509526179378 002974120766514793942590298969594699556576121865619673378623625612521632086286 922210327488921865436480229678070576561514463204692790682120738837781423356282 360896320806822246801224826117718589638140918390367367222088832151375560037279 839400415297002878307667094447456013455641725437090697939612257142989467154357 846878861444581231459357198492252847160504922124247014121478057345510500801908 699603302763478708108175450119307141223390866393833952942578690507643100638351 983438934159613185434754649556978103829309716465143840700707360411237359984345 225161050702705623526601276484830840761183013052793205427462865403603674532865 105706587488225698157936789766974220575059683440869735020141020672358502007245 225632651341055924019027421624843914035998953539459094407046912091409387001264 560016237428802109276457931065792295524988727584610126483699989225695968815920 560010165525637567856672279661988578279484885583439751874454551296563443480396 642055798293680435220277098429423253302257634180703947699415979159453006975214 829336655566156787364005366656416547321704390352132954352916941459904160875320 186837937023488868947915107163785290234529244077365949563051007421087142613497 459561513849871375704710178795731042296906667021449863746459528082436944578977 233004876476524133907592043401963403911473202338071509522201068256342747164602 433544005152126693249341967397704159568375355516673027390074972973635496453328 886984406119649616277344951827369558822075735517665158985519098666539354948106 887320685990754079234240230092590070173196036225475647894064754834664776041146 323390565134330684495397907090302346046147096169688688501408347040546074295869 913829668246818571031887906528703665083243197440477185567893482308943106828702 722809736248093996270607472645539925399442808113736943388729406307926159599546 262462970706259484556903471197299640908941805953439325123623550813494900436427 852713831591256898929519642728757394691427253436694153236100453730488198551706 594121735246258954873016760029886592578662856124966552353382942878542534048308 330701653722856355915253478445981831341129001999205981352205117336585640782648 494276441137639386692480311836445369858917544264739988228462184490087776977631 279572267265556259628254276531830013407092233436577916012809317940171859859993 384923549564005709955856113498025249906698423301735035804408116855265311709957 089942732870925848789443646005041089226691783525870785951298344172953519537885 534573742608590290817651557803905946408735061232261120093731080485485263572282 576820341605048466277504500312620080079980492548534694146977516493270950493463 938243222718851597405470214828971117779237612257887347718819682546298126868581 705074027255026332904497627789442362167411918626943965067151577958675648239939 176042601763387045499017614364120469218237076488783419689686118155815873606293 860381017121585527266830082383404656475880405138080163363887421637140643549556 186896411228214075330265510042410489678352858829024367090488711819090949453314 421828766181031007354770549815968077200947469613436092861484941785017180779306 810854690009445899527942439813921350558642219648349151263901280383200109773868 066287792397180146134324457264009737425700735921003154150893679300816998053652 027600727749674584002836240534603726341655425902760183484030681138185510597970 566400750942608788573579603732451414678670368809880609716425849759513806930944 940151542222194329130217391253835591503100333032511174915696917450271494331515 588540392216409722910112903552181576282328318234254832611191280092825256190205 263016391147724733148573910777587442538761174657867116941477642144111126358355 387136101102326798775641024682403226483464176636980663785768134920453022408197 278564719839630878154322116691224641591177673225326433568614618654522268126887 268445968442416107854016768142080885028005414361314623082102594173756238994207 571362751674573189189456283525704413354375857534269869947254703165661399199968 262824727064133622217892390317608542894373393561889165125042440400895271983787 386480584726895462438823437517885201439560057104811949884239060613695734231559 079670346149143447886360410318235073650277859089757827273130504889398900992391 350337325085598265586708924261242947367019390772713070686917092646254842324074 855036608013604668951184009366860954632500214585293095000090715105823626729326 453738210493872499669933942468551648326113414611068026744663733437534076429402 668297386522093570162638464852851490362932019919968828517183953669134522244470 804592396602817156551565666111359823112250628905854914509715755390024393153519 090210711945730024388017661503527086260253788179751947806101371500448991721002 220133501310601639154158957803711779277522597874289191791552241718958536168059 474123419339842021874564925644346239253195313510331147639491199507285843065836 193536932969928983791494193940608572486396883690326556436421664425760791471086 998431573374964883529276932822076294728238153740996154559879825989109371712621 828302584811238901196822142945766758071865380650648702613389282299497257453033 283896381843944770779402284359883410035838542389735424395647555684095224844554 139239410001620769363684677641301781965937997155746854194633489374843912974239 143365936041003523437770658886778113949861647874714079326385873862473288964564 359877466763847946650407411182565837887845485814896296127399841344272608606187 245545236064315371011274680977870446409475828034876975894832824123929296058294 861919667091895808983320121031843034012849511620353428014412761728583024355983 003204202451207287253558119584014918096925339507577840006746552603144616705082 768277222353419110263416315714740612385042584598841990761128725805911393568960 143166828317632356732541707342081733223046298799280490851409479036887868789493 054695570307261900950207643349335910602454508645362893545686295853131533718386 826561786227363716975774183023986006591481616404944965011732131389574706208847 480236537103115089842799275442685327797431139514357417221975979935968525228574 526379628961269157235798662057340837576687388426640599099350500081337543245463 596750484423528487470144354541957625847356421619813407346854111766883118654489 377697956651727966232671481033864391375186594673002443450054499539974237232871 249483470604406347160632583064982979551010954183623503030945309733583446283947 630477564501500850757894954893139394489921612552559770143685894358587752637962 559708167764380012543650237141278346792610199558522471722017772370041780841942 394872540680155603599839054898572354674564239058585021671903139526294455439131 663134530893906204678438778505423939052473136201294769187497519101147231528932 677253391814660730008902776896311481090220972452075916729700785058071718638105 496797310016787085069420709223290807038326345345203802786099055690013413718236 837099194951648960075504934126787643674638490206396401976668559233565463913836 318574569814719621084108096188460545603903845534372914144651347494078488442377 217515433426030669883176833100113310869042193903108014378433415137092435301367 763108491351615642269847507430329716746964066653152703532546711266752246055119 958183196376370761799191920357958200759560530234626775794393630746305690108011 494271410093913691381072581378135789400559950018354251184172136055727522103526 803735726527922417373605751127887218190844900617801388971077082293100279766593 583875890939568814856026322439372656247277603789081445883785501970284377936240 782505270487581647032458129087839523245323789602984166922548964971560698119218 658492677040395648127810217991321741630581055459880130048456299765112124153637 451500563507012781592671424134210330156616535602473380784302865525722275304999 883701534879300806260180962381516136690334111138653851091936739383522934588832 255088706450753947395204396807906708680644509698654880168287434378612645381583 428075306184548590379821799459968115441974253634439960290251001588827216474500 682070419376158454712318346007262933955054823955713725684023226821301247679452 264482091023564775272308208106351889915269288910845557112660396503439789627825 001611015323516051965590421184494990778999200732947690586857787872098290135295 661397888486050978608595701773129815531495168146717695976099421003618355913877 781769845875810446628399880600616229848616935337386578773598336161338413385368 421197893890018529569196780455448285848370117096721253533875862158231013310387 766827211572694951817958975469399264219791552338576623167627547570354699414892 904130186386119439196283887054367774322427680913236544948536676800000106526248 547305586159899914017076983854831887501429389089950685453076511680333732226517 566220752695179144225280816517166776672793035485154204023817460892328391703275 425750867655117859395002793389592057668278967764453184040418554010435134838953 120132637836928358082719378312654961745997056745071833206503455664403449045362 756001125018433560736122276594927839370647842645676338818807565612168960504161 139039063960162022153684941092605387688714837989559999112099164646441191856827 700457424343402167227644558933012778158686952506949936461017568506016714535431 581480105458860564550133203758645485840324029871709348091055621167154684847780 394475697980426318099175642280987399876697323769573701580806822904599212366168 902596273043067931653114940176473769387351409336183321614280214976339918983548 487562529875242387307755955595546519639440182184099841248982623673771467226061 633643296406335728107078875816404381485018841143188598827694490119321296827158 884133869434682859006664080631407775772570563072940049294030242049841656547973 670548558044586572022763784046682337985282710578431975354179501134727362577408 021347682604502285157979579764746702284099956160156910890384582450267926594205 550395879229818526480070683765041836562094555434613513415257006597488191634135 955671964965403218727160264859304903978748958906612725079482827693895352175362 185079629778514618843271922322381015874445052866523802253284389137527384589238 442253547265309817157844783421582232702069028723233005386216347988509469547200 479523112015043293226628272763217790884008786148022147537657810581970222630971 749507212724847947816957296142365859578209083073323356034846531873029302665964 501371837542889755797144992465403868179921389346924474198509733462679332107268 687076806263991936196504409954216762784091466985692571507431574079380532392523 947755744159184582156251819215523370960748332923492103451462643744980559610330 799414534778457469999212859999939961228161521931488876938802228108300198601654 941654261696858678837260958774567618250727599295089318052187292461086763995891 614585505839727420980909781729323930106766386824040111304024700735085782872462 713494636853181546969046696869392547251941399291465242385776255004748529547681 479546700705034799958886769501612497228204030399546327883069597624936151010243 655535223069061294938859901573466102371223547891129254769617600504797492806072 126803922691102777226102544149221576504508120677173571202718024296810620377657 883716690910941807448781404907551782038565390991047759414132154328440625030180 275716965082096427348414695726397884256008453121406593580904127113592004197598 513625479616063228873618136737324450607924411763997597461938358457491598809766 744709300654634242346063423747466608043170126005205592849369594143408146852981 505394717890045183575515412522359059068726487863575254191128887737176637486027 660634960353679470269232297186832771739323619200777452212624751869833495151019 864269887847171939664976907082521742336566272592844062043021411371992278526998 469884770232382384005565551788908766136013047709843861168705231055314916251728 373272867600724817298763756981633541507460883866364069347043720668865127568826 614973078865701568501691864748854167915459650723428773069985371390430026653078 398776385032381821553559732353068604301067576083890862704984188859513809103042 359578249514398859011318583584066747237029714978508414585308578133915627076035 639076394731145549583226694570249413983163433237897595568085683629725386791327 505554252449194358912840504522695381217913191451350099384631177401797151228378 546011603595540286440590249646693070776905548102885020808580087811577381719174 177601733073855475800605601433774329901272867725304318251975791679296996504146 070664571258883469797964293162296552016879730003564630457930884032748077181155 533090988702550520768046303460865816539487695196004408482065967379473168086415 645650530049881616490578831154345485052660069823093157776500378070466126470602 145750579327096204782561524714591896522360839664562410519551052235723973951288 181640597859142791481654263289200428160913693777372229998332708208296995573772 737566761552711392258805520189887620114168005468736558063347160373429170390798 639652296131280178267971728982293607028806908776866059325274637840539769184808 204102194471971386925608416245112398062011318454124478205011079876071715568315 407886543904121087303240201068534194723047666672174986986854707678120512473679 247919315085644477537985379973223445612278584329684664751333657369238720146472 367942787004250325558992688434959287612400755875694641370562514001179713316620 715371543600687647731867558714878398908107429530941060596944315847753970094398 839491443235366853920994687964506653398573888786614762944341401049888993160051 207678103588611660202961193639682134960750111649832785635316145168457695687109 002999769841263266502347716728657378579085746646077228341540311441529418804782 543876177079043000156698677679576090996693607559496515273634981189641304331166 277471233881740603731743970540670310967676574869535878967003192586625941051053 358438465602339179674926784476370847497833365557900738419147319886271352595462 518160434225372996286326749682405806029642114638643686422472488728343417044157 348248183330164056695966886676956349141632842641497453334999948000266998758881 593507357815195889900539512085351035726137364034367534714104836017546488300407 846416745216737190483109676711344349481926268111073994825060739495073503169019 731852119552635632584339099822498624067031076831844660729124874754031617969941 139738776589986855417031884778867592902607004321266617919223520938227878880988 633599116081923535557046463491132085918979613279131975649097600013996234445535 014346426860464495862476909434704829329414041114654092398834443515913320107739 441118407410768498106634724104823935827401944935665161088463125678529776973468 430306146241803585293315973458303845541033701091676776374276210213701354854450 926307190114731848574923318167207213727935567952844392548156091372812840633303 937356242001604566455741458816605216660873874804724339121295587776390696903707 882852775389405246075849623157436917113176134783882719416860662572103685132156 647800147675231039357860689611125996028183930954870905907386135191459181951029 732787557104972901148717189718004696169777001791391961379141716270701895846921 434369676292745910994006008498356842520191559370370101104974733949387788598941 743303178534870760322198297057975119144051099423588303454635349234982688362404 332726741554030161950568065418093940998202060999414021689090070821330723089662 119775530665918814119157783627292746156185710372172471009521423696483086410259 288745799932237495519122195190342445230753513380685680735446499512720317448719 540397610730806026990625807602029273145525207807991418429063884437349968145827 337207266391767020118300464819000241308350884658415214899127610651374153943565 721139032857491876909441370209051703148777346165287984823533829726013611098451 484182380812054099612527458088109948697221612852489742555551607637167505489617 301680961380381191436114399210638005083214098760459930932485102516829446726066 613815174571255975495358023998314698220361338082849935670557552471290274539776 214049318201465800802156653606776550878380430413431059180460680083459113664083 488740800574127258670479225831912741573908091438313845642415094084913391809684 025116399193685322555733896695374902662092326131885589158083245557194845387562 878612885900410600607374650140262782402734696252821717494158233174923968353013 617865367376064216677813773995100658952887742766263684183068019080460984980946 976366733566228291513235278880615776827815958866918023894033307644191240341202 231636857786035727694154177882643523813190502808701857504704631293335375728538 660588890458311145077394293520199432197117164223500564404297989208159430716701 985746927384865383343614579463417592257389858800169801475742054299580124295810 545651083104629728293758416116253256251657249807849209989799062003593650993472 158296517413579849104711166079158743698654122234834188772292944633517865385673 196255985202607294767407261676714557364981210567771689348491766077170527718760 119990814411305864557791052568430481144026193840232247093924980293355073184589 035539713308844617410795916251171486487446861124760542867343670904667846867027 409188101424971114965781772427934707021668829561087779440504843752844337510882 826477197854000650970403302186255614733211777117441335028160884035178145254196 432030957601869464908868154528562134698835544456024955666843660292219512483091 060537720198021831010327041783866544718126039719068846237085751808003532704718 565949947612424811099928867915896904956394762460842406593094862150769031498702 067353384834955083636601784877106080980426924713241000946401437360326564518456 679245666955100150229833079849607994988249706172367449361226222961790814311414 660941234159359309585407913908720832273354957208075716517187659944985693795623 875551617575438091780528029464200447215396280746360211329425591600257073562812 638733106005891065245708024474937543184149401482119996276453106800663118382376 163966318093144467129861552759820145141027560068929750246304017351489194576360 789352855505317331416457050499644389093630843874484783961684051845273288403234 520247056851646571647713932377551729479512613239822960239454857975458651745878 771331813875295980941217422730035229650808917770506825924882232215493804837145 478164721397682096332050830564792048208592047549985732038887639160199524091893 894557676874973085695595801065952650303626615975066222508406742889826590751063 756356996821151094966974458054728869363102036782325018232370845979011154847208 761821247781326633041207621658731297081123075815982124863980721240786887811450 165582513617890307086087019897588980745664395515741536319319198107057533663373 803827215279884935039748001589051942087971130805123393322190346624991716915094 854140187106035460379464337900589095772118080446574396280618671786101715674096 766208029576657705129120990794430463289294730615951043090222143937184956063405 618934251305726829146578329334052463502892917547087256484260034962961165413823 007731332729830500160256724014185152041890701154288579920812198449315699905918 201181973350012618772803681248199587707020753240636125931343859554254778196114 293516356122349666152261473539967405158499860355295332924575238881013620234762 466905581643896786309762736550472434864307121849437348530060638764456627218666 170123812771562137974614986132874411771455244470899714452288566294244023018479 120547849857452163469644897389206240194351831008828348024924908540307786387516 591130287395878709810077271827187452901397283661484214287170553179654307650453 432460053636147261818096997693348626407743519992868632383508875668359509726557 481543194019557685043724800102041374983187225967738715495839971844490727914196 584593008394263702087563539821696205532480321226749891140267852859967340524203 109179789990571882194939132075343170798002373659098537552023891164346718558290 685371189795262623449248339249634244971465684659124891855662958932990903523923 333364743520370770101084388003290759834217018554228386161721041760301164591878 053936744747205998502358289183369292233732399948043710841965947316265482574809 948250999183300697656936715968936449334886474421350084070066088359723503953234 017958255703601693699098867113210979889707051728075585519126993067309925070407 024556850778679069476612629808225163313639952117098452809263037592242674257559 989289278370474445218936320348941552104459726188380030067761793138139916205806 270165102445886924764924689192461212531027573139084047000714356136231699237169 484813255420091453041037135453296620639210547982439212517254013231490274058589 206321758949434548906846399313757091034633271415316223280552297297953801880162 859073572955416278867649827418616421878988574107164906919185116281528548679417 363890665388576422915834250067361245384916067413734017357277995634104332688356 950781493137800736235418007061918026732855119194267609122103598746924117283749 312616339500123959924050845437569850795704622266461900010350049018303415354584 283376437811198855631877779253720116671853954183598443830520376281944076159410 682071697030228515225057312609304689842343315273213136121658280807521263154773 060442377475350595228717440266638914881717308643611138906942027908814311944879 941715404210341219084709408025402393294294549387864023051292711909751353600092 197110541209668311151632870542302847007312065803262641711616595761327235156666 253667271899853419989523688483099930275741991646384142707798870887422927705389 122717248632202889842512528721782603050099451082478357290569198855546788607946 280537122704246654319214528176074148240382783582971930101788834567416781139895 475044833931468963076339665722672704339321674542182455706252479721997866854279 897799233957905758189062252547358220523642485078340711014498047872669199018643 882293230538231855973286978092225352959101734140733488476100556401824239219269 506208318381454698392366461363989101210217709597670490830508185470419466437131 229969235889538493013635657618610606222870559942337163102127845744646398973818 856674626087948201864748767272722206267646533809980196688368099415907577685263 986514625333631245053640261056960551318381317426118442018908885319635698696279 503673842431301133175330532980201668881748134298868158557781034323175306478498 321062971842518438553442762012823457071698853051832617964117857960888815032960 229070561447622091509473903594664691623539680920139457817589108893199211226007 392814916948161527384273626429809823406320024402449589445612916704950823581248 739179964864113348032475777521970893277226234948601504665268143987705161531702 669692970492831628550421289814670619533197026950721437823047687528028735412616 639170824592517001071418085480063692325946201900227808740985977192180515853214 739265325155903541020928466592529991435379182531454529059841581763705892790690 989691116438118780943537152133226144362531449012745477269573939348154691631162 492887357471882407150399500944673195431619385548520766573882513963916357672315 100555603726339486720820780865373494244011579966750736071115935133195919712094 896471755302453136477094209463569698222667377520994516845064362382421185353488 798939567318780660610788544000550827657030558744854180577889171920788142335113 866292966717964346876007704799953788338787034871802184243734211227394025571769 081960309201824018842705704609262256417837526526335832424066125331152942345796 556950250681001831090041124537901533296615697052237921032570693705109083078947 999900499939532215362274847660361367769797856738658467093667958858378879562594 646489137665219958828693380183601193236857855855819555604215625088365020332202 451376215820461810670519533065306060650105488716724537794283133887163139559690 583208341689847606560711834713621812324622725884199028614208728495687963932546 428534307530110528571382964370999035694888528519040295604734613113826387889755 178856042499874831638280404684861893818959054203988987265069762020199554841265 000539442820393012748163815853039643992547020167275932857436666164411096256633 730540921951967514832873480895747777527834422109107311135182804603634719818565 557295714474768255285786334934285842311874944000322969069775831590385803935352 135886007960034209754739229673331064939560181223781285458431760556173386112673 478074585067606304822940965304111830667108189303110887172816751957967534718853 722930961614320400638132246584111115775835858113501856904781536893813771847281 475199835050478129771859908470762197460588742325699582889253504193795826061621 184236876851141831606831586799460165205774052942305360178031335726326705479033 840125730591233960188013782542192709476733719198728738524805742124892118347087 662966720727232565056512933312605950577772754247124164831283298207236175057467 387012820957554430596839555568686118839713552208445285264008125202766555767749 596962661260456524568408613923826576858338469849977872670655519185446869846947 849573462260629421962455708537127277652309895545019303773216664918257815467729 200521266714346320963789185232321501897612603437368406719419303774688099929687 758244104787812326625318184596045385354383911449677531286426092521153767325886 672260404252349108702695809964759580579466397341906401003636190404203311357933 654242630356145700901124480089002080147805660371015412232889146572239314507607 167064355682743774396578906797268743847307634645167756210309860409271709095128 086309029738504452718289274968921210667008164858339553773591913695015316201890 888748421079870689911480466927065094076204650277252865072890532854856143316081 269300569378541786109696920253886503457718317668688592368148847527649846882194 973972970773718718840041432312763650481453112285099002074240925585925292610302 106736815434701525234878635164397623586041919412969769040526483234700991115424 260127343802208933109668636789869497799400126016422760926082349304118064382913 834735467972539926233879158299848645927173405922562074910530853153718291168163 721939518870095778818158685046450769934394098743351443162633031724774748689791 820923948083314397084067308407958935810896656477585990556376952523265361442478 023082681183103773588708924061303133647737101162821461466167940409051861526036 009252194721889091810733587196414214447865489952858234394705007983038853886083 103571930600277119455802191194289992272235345870756624692617766317885514435021 828702668561066500353105021631820601760921798468493686316129372795187307897263 735371715025637873357977180818487845886650433582437700414771041493492743845758 710715973155943942641257027096512510811554824793940359768118811728247215825010 949609662539339538092219559191818855267806214992317276316321833989693807561685 591175299845013206712939240414459386239880938124045219148483164621014738918251 010909677386906640415897361047643650006807710565671848628149637111883219244566 394581449148616550049567698269030891118568798692947051352481609174324301538368 470729289898284602223730145265567989862776796809146979837826876431159883210904 371561129976652153963546442086919756737000573876497843768628768179249746943842 746525631632300555130417422734164645512781278457777245752038654375428282567141 288583454443513256205446424101103795546419058116862305964476958705407214198521 210673433241075676757581845699069304604752277016700568454396923404171108988899 341635058515788735343081552081177207188037910404698306957868547393765643363197 978680367187307969392423632144845035477631567025539006542311792015346497792906 624150832885839529054263768766896880503331722780018588506973623240389470047189 761934734430843744375992503417880797223585913424581314404984770173236169471976 571535319775499716278566311904691260918259124989036765417697990362375528652637 573376352696934435440047306719886890196814742876779086697968852250163694985673 021752313252926537589641517147955953878427849986645630287883196209983049451987 439636907068276265748581043911223261879405994155406327013198989570376110532360 629867480377915376751158304320849872092028092975264981256916342500052290887264 692528466610466539217148208013050229805263783642695973370705392278915351056888 393811324975707133102950443034671598944878684711643832805069250776627450012200 352620370946602341464899839025258883014867816219677519458316771876275720050543 979441245990077115205154619930509838698254284640725554092740313257163264079293 418334214709041254253352324802193227707535554679587163835875018159338717423606 155117101312352563348582036514614187004920570437201826173319471570086757853933 607862273955818579758725874410254207710547536129404746010009409544495966288148 691590389907186598056361713769222729076419775517772010427649694961105622059250 242021770426962215495872645398922769766031052498085575947163107587013320886146 326641259114863388122028444069416948826152957762532501987035987067438046982194 205638125583343642194923227593722128905642094308235254408411086454536940496927 149400331978286131818618881111840825786592875742638445005994422956858646048103 301538891149948693543603022181094346676400002236255057363129462629609619876056 425996394613869233083719626595473923462413459779574852464783798079569319865081 597767535055391899115133525229873611277918274854200868953965835942196333150286 956119201229888988700607999279541118826902307891310760361763477948943203210277 335941690865007193280401716384064498787175375678118532132840821657110754952829 497493621460821558320568723218557406516109627487437509809223021160998263303391 546949464449100451528092508974507489676032409076898365294065792019831526541065 813682379198409064571246894847020935776119313998024681340520039478194986620262 400890215016616381353838151503773502296607462795291038406868556907015751662419 298724448271942933100485482445458071889763300323252582158128032746796200281476 243182862217105435289834820827345168018613171959332471107466222850871066611770 346535283957762599774467218571581612641114327179434788599089280848669491413909 771673690027775850268664654056595039486784111079011610400857274456293842549416 759460548711723594642910585090995021495879311219613590831588262068233215615308 683373083817327932819698387508708348388046388478441884003184712697454370937329 836240287519792080232187874488287284372737801782700805878241074935751488997891 173974612932035108143270325140903048746226294234432757126008664250833318768865 075642927160552528954492153765175149219636718104943531785838345386525565664065 725136357506435323650893679043170259787817719031486796384082881020946149007971 513771709906195496964007086766710233004867263147551053723175711432231741141168 062286420638890621019235522354671166213749969326932173704310598722503945657492 461697826097025335947502091383667377289443869640002811034402608471289900074680 776484408871134135250336787731679770937277868216611786534423173226463784769787 514433209534000165069213054647689098505020301504488083426184520873053097318949 291642532293361243151430657826407028389840984160295030924189712097160164926561 341343342229882790992178604267981245728534580133826099587717811310216734025656 274400729683406619848067661580502169183372368039902793160642043681207990031626 444914619021945822969099212278855394878353830564686488165556229431567312827439 082645061162894280350166133669782405177015521962652272545585073864058529983037 918035043287670380925216790757120406123759632768567484507915114731344000183257 034492090971243580944790046249431345502890068064870429353403743603262582053579 011839564908935434510134296961754524957396062149028872893279252069653538639644 322538832752249960598697475988232991626354597332444516375533437749292899058117 578635555562693742691094711700216541171821975051983178713710605106379555858890 556885288798908475091576463907469361988150781468526213325247383765119299015610 918977792200870579339646382749068069876916819749236562422608715417610043060890 437797667851966189140414492527048088197149880154205778700652159400928977760133 075684796699295543365613984773806039436889588764605498387147896848280538470173 087111776115966350503997934386933911978988710915654170913308260764740630571141 109883938809548143782847452883836807941888434266622207043872288741394780101772 139228191199236540551639589347426395382482960903690028835932774585506080131798 840716244656399794827578365019551422155133928197822698427863839167971509126241 054872570092407004548848569295044811073808799654748156891393538094347455697212 891982717702076661360248958146811913361412125878389557735719498631721084439890 142394849665925173138817160266326193106536653504147307080441493916936326237376 777709585031325599009576273195730864804246770121232702053374266705314244820816 813030639737873664248367253983748769098060218278578621651273856351329014890350 988327061725893257536399397905572917516009761545904477169226580631511102803843 601737474215247608515209901615858231257159073342173657626714239047827958728150 509563309280266845893764964977023297364131906098274063353108979246424213458374 090116939196425045912881340349881063540088759682005440836438651661788055760895 689672753153808194207733259791727843762566118431989102500749182908647514979400 316070384554946538594602745244746681231468794344161099333890899263841184742525 704457251745932573898956518571657596148126602031079762825416559050604247911401 695790033835657486925280074302562341949828646791447632277400552946090394017753 633565547193100017543004750471914489984104001586794617924161001645471655133707 407395026044276953855383439755054887109978520540117516974758134492607943368954 378322117245068734423198987884412854206474280973562580706698310697993526069339 213568588139121480735472846322778490808700246777630360555123238665629517885371 967303463470122293958160679250915321748903084088651606111901149844341235012464 692802880599613428351188471544977127847336176628506216977871774382436256571177 945006447771837022199910669502165675764404499794076503799995484500271066598781 360380231412683690578319046079276529727769404361302305178708054651154246939526 512710105292707030667302444712597393995051462840476743136373997825918454117641 332790646063658415292701903027601733947486696034869497654175242930604072700505 903950314852292139257559484507886797792525393176515641619716844352436979444735 596426063339105512682606159572621703669850647328126672452198906054988028078288 142979633669674412480598219214633956574572210229867759974673812606936706913408 155941201611596019023775352555630060624798326124988128819293734347686268921923 977783391073310658825681377717232831532908252509273304785072497713944833389255 208117560845296659055394096556854170600117985729381399825831929367910039184409 928657560599359891000296986446097471471847010153128376263114677420914557404181 590880006494323785583930853082830547607679952435739163122188605754967383224319 565065546085288120190236364471270374863442172725787950342848631294491631847534 753143504139209610879605773098720135248407505763719925365047090858251393686346 386336804289176710760211115982887553994012007601394703366179371539630613986365 549221374159790511908358829009765664730073387931467891318146510931676157582135 142486044229244530411316065270097433008849903467540551864067734260358340960860 553374736276093565885310976099423834738222208729246449768456057956251676557408 841032173134562773585605235823638953203853402484227337163912397321599544082842 166663602329654569470357718487344203422770665383738750616921276801576618109542 009770836360436111059240911788954033802142652394892968643980892611463541457153 519434285072135345301831587562827573389826889852355779929572764522939156747756 667605108788764845349363606827805056462281359888587925994094644604170520447004 631513797543173718775603981596264750141090665886616218003826698996196558058720 863972117699521946678985701179833244060181157565807428418291061519391763005919 431443460515404771057005433900018245311773371895585760360718286050635647997900 413976180895536366960316219311325022385179167205518065926351803625121457592623 836934822266589557699466049193811248660909979812857182349400661555219611220720 309227764620099931524427358948871057662389469388944649509396033045434084210246 240104872332875008174917987554387938738143989423801176270083719605309438394006 375611645856094312951759771393539607432279248922126704580818331376416581826956 210587289244774003594700926866265965142205063007859200248829186083974373235384 908396432614700053242354064704208949921025040472678105908364400746638002087012 666420945718170294675227854007450855237772089058168391844659282941701828823301 497155423523591177481862859296760504820386434310877956289292540563894662194826 871104282816389397571175778691543016505860296521745958198887868040811032843273 986719862130620555985526603640504628215230615459447448990883908199973874745296 981077620148713400012253552224669540931521311533791579802697955571050850747387 475075806876537644578252443263804614304288923593485296105826938210349800040524 840708440356116781717051281337880570564345061611933042444079826037795119854869 455915205196009304127100727784930155503889536033826192934379708187432094991415 959339636811062755729527800425486306005452383915106899891357882001941178653568 214911852820785213012551851849371150342215954224451190020739353962740020811046 553020793286725474054365271759589350071633607632161472581540764205302004534018 357233829266191530835409512022632916505442612361919705161383935732669376015691 442994494374485680977569630312958871916112929468188493633864739274760122696415 884890096571708616059814720446742866420876533479985822209061980217321161423041 947775499073873856794118982466091309169177227420723336763503267834058630193019 324299639720444517928812285447821195353089891012534297552472763573022628138209 180743974867145359077863353016082155991131414420509144729353502223081719366350 934686585865631485557586244781862010871188976065296989926932817870557643514338 206014107732926106343152533718224338526352021773544071528189813769875515757454 693972715048846979361950047772097056179391382898984532742622728864710888327017 372325881824465843624958059256033810521560620615571329915608489206434030339526 226345145428367869828807425142256745180618414956468611163540497189768215422772 247947403357152743681940989205011365340012384671429655186734415374161504256325 671343024765512521921803578016924032669954174608759240920700466934039651017813 485783569444076047023254075555776472845075182689041829396611331016013111907739 863246277821902365066037404160672496249013743321724645409741299557052914243820 807609836482346597388669134991978401310801558134397919485283043673901248208244 481412809544377389832005986490915950532285791457688496257866588599917986752055 455809900455646117875524937012455321717019428288461740273664997847550829422802 023290122163010230977215156944642790980219082668986883426307160920791408519769 523555348865774342527753119724743087304361951139611908003025587838764420608504 473063129927788894272918972716989057592524467966018970748296094919064876469370 275077386643239191904225429023531892337729316673608699622803255718530891928440 380507103006477684786324319100022392978525537237556621364474009676053943983823 576460699246526008909062410590421545392790441152958034533450025624410100635953 003959886446616959562635187806068851372346270799732723313469397145628554261546 765063246567662027924520858134771760852169134094652030767339184114750414016892 412131982688156866456148538028753933116023229255561894104299533564009578649534 093511526645402441877594931693056044868642086275720117231952640502309977456764 783848897346431721598062678767183800524769688408498918508614900343240347674268 624595239589035858213500645099817824463608731775437885967767291952611121385919 472545140030118050343787527766440276261894101757687268042817662386068047788524 288743025914524707395054652513533945959878961977891104189029294381856720507096 460626354173294464957661265195349570186001541262396228641389779673332907056737 696215649818450684226369036784955597002607986799626101903933126376855696876702 929537116252800554310078640872893922571451248113577862766490242516199027747109 033593330930494838059785662884478744146984149906712376478958226329490467981208 998485716357108783119184863025450162092980582920833481363840542172005612198935 366937133673339246441612522319694347120641737549121635700857369439730597970971 972666664226743111776217640306868131035189911227133972403688700099686292254646 500638528862039380050477827691283560337254825579391298525150682996910775425764 748832534141213280062671709400909822352965795799780301828242849022147074811112 401860761341515038756983091865278065889668236252393784527263453042041880250844 236319038331838455052236799235775292910692504326144695010986108889991465855188 187358252816430252093928525807796973762084563748211443398816271003170315133440 230952635192958868069082135585368016100021374085115448491268584126869589917414 913382057849280069825519574020181810564129725083607035685105533178784082900004 155251186577945396331753853209214972052660783126028196116485809868458752512999 740409279768317663991465538610893758795221497173172813151793290443112181587102 351874075722210012376872194474720934931232410706508061856237252673254073332487 575448296757345001932190219911996079798937338367324257610393898534927877747398 050808001554476406105352220232540944356771879456543040673589649101761077594836 454082348613025471847648518957583667439979150851285802060782055446299172320202 822291488695939972997429747115537185892423849385585859540743810488262464878805 330427146301194158989632879267832732245610385219701113046658710050008328517731 177648973523092666123458887310288351562644602367199664455472760831011878838915 114934093934475007302585581475619088139875235781233134227986650352272536717123 075686104500454897036007956982762639234410714658489578024140815840522953693749 971066559489445924628661996355635065262340533943914211127181069105229002465742 360413009369188925586578466846121567955425660541600507127664176605687427420032 957716064344860620123982169827172319782681662824993871499544913730205184366907 672357740005393266262276032365975171892590180110429038427418550789488743883270 306328327996300720069801224436511639408692222074532024462412115580435454206421 512158505689615735641431306888344318528085397592773443365538418834030351782294 625370201578215737326552318576355409895403323638231921989217117744946940367829 618592080340386757583411151882417743914507736638407188048935825686854201164503 135763335550944031923672034865101056104987272647213198654343545040913185951314 518127643731043897250700498198705217627249406521461995923214231443977654670835 171474936798618655279171582408065106379950018429593879915835017158075988378496 225739851212981032637937621832245659423668537679911314010804313973233544909082 491049914332584329882103398469814171575601082970658306521134707680368069532297 199059990445120908727577622535104090239288877942463048328031913271049547859918 019696783532146444118926063152661816744319355081708187547705080265402529410921 826485821385752668815558411319856002213515888721036569608751506318753300294211 868222189377554602722729129050429225978771066787384000061677215463844129237119 352182849982435092089180168557279815642185819119749098573057033266764646072875 743056537260276898237325974508447964954564803077159815395582777913937360171742 299602735310276871944944491793978514463159731443535185049141394155732938204854 212350817391254974981930871439661513294204591938010623142177419918406018034794 988769105155790555480695387854006645337598186284641990522045280330626369562649 091082762711590385699505124652999606285544383833032763859980079292284665950355 121124528408751622906026201185777531374794936205549640107300134885315073548735 390560290893352640071327473262196031177343394367338575912450814933573691166454 128178817145402305475066713651825828489809951213919399563324133655677709800308 191027204099714868741813466700609405102146269028044915964654533010775469541308 871416531254481306119240782118869005602778182423502269618934435254763357353648 561936325441775661398170393063287216690572225974520919291726219984440964615826 945638023950283712168644656178523556516412771282691868861557271620147493405227 694659571219831494338162211400693630743044417328478610177774383797703723179525 543410722344551255558999864618387676490397246116795901810003509892864120419516 355110876320426761297982652942588295114127584126273279079880755975185157684126 474220947972184330935297266521001566251455299474512763155091763673025946213293 019040283795424632325855030109670692272022707486341900543830265068121414213505 715417505750863990767394633514620908288893493837643939925690060406731142209331 219593620298297235116325938677224147791162957278075239505625158160313335938231 150051862689053065836812998810866326327198061127154885879809348791291370749823 057592909186293919501472119758606727009254771802575033773079939713453953264619 526999659638565491759045833358579910201271320458390320085387888163363768518208 372788513117522776960978796214237216254521459128183179821604411131167140691482 717098101545778193920231156387195080502467972579249760577262591332855972637121 120190572077140914864507409492671803581515757151405039761096384675556929897038 354731410022380258346876735012977541327953206097115450648421218593649099791776 687477448188287063231551586503289816422828823274686610659273219790716238464215 348985247621678905026099804526648392954235728734397768049577409144953839157556 548545905897649519851380100795801078375994577529919670054760225255203445398871 253878017196071816407812484784725791240782454436168234523957068951427226975043 187363326301110305342333582160933319121880660826834142891041517324721605335584 999322454873077882290525232423486153152097693846104258284971496347534183756200 301491570327968530186863157248840152663983568956363465743532178349319982554211 730846774529708583950761645822963032442432823773745051702856069806788952176819 815671078163340526675953942492628075696832610749532339053622309080708145591983 735537774874202903901814293731152933464446815121294509759653430628421531944572 711861490001765055817709530246887526325011970520947615941676872778447200019278 913725184162285778379228443908430118112149636642465903363419454065718354477191 244662125939265662030688852005559912123536371822692253178145879259375044144893 398160865790087616502463519704582889548179375668104647461410514249887025213993 687050937230544773411264135489280684105910771667782123833281026218558775131272 117934444820144042574508306394473836379390628300897330624138061458941422769474 793166571762318247216835067807648757342049155762821758397297513447899069658953 254894033561561316740327647246921250575911625152965456854463349811431767025729 566184477548746937846423373723898192066204851189437886822480727935202250179654 534375727416391079197295295081294292220534771730418447791567399173841831171036 252439571615271466900581470000263301045264354786590329073320546833887207873544 476264792529769017091200787418373673508771337697768349634425241994995138831507 487753743384945825976556099655595431804092017849718468549737069621208852437701 385375768141663272241263442398215294164537800049250726276515078908507126599703 670872669276430837722968598516912230503746274431085293430527307886528397733524 601746352770320593817912539691562106363762588293757137384075440646896478310070 458061344673127159119460843593582598778283526653115106504162329532904777217408 355934972375855213804830509000964667608830154061282430874064559443185341375522 016630581211103345312074508682433943215904359443031243122747138584203039010607 094031523555617276799416002039397509989762933532585557562480899669182986422267 750236019325797472674257821111973470940235745722227121252685238429587427350156 366009318804549333898974157149054418255973808087156528143010267046028431681923 039253529779576586241439270154974087927313105163611913757700892956482332364829 826302460797587576774537716010249080462430185652416175665560016085912153455626 760219268998285537787258314514408265458348440947846317877737479465358016996077 940556870119232860804113090462935087182712593466871276669487389982459852778649 956916546402945893506496433580982476596516514209098675520380830920323048734270 346828875160407154665383461961122301375945157925269674364253192739003603860823 645076269882749761872357547676288995075211480485252795084503395857083813047693 788132112367428131948795022806632017002246033198967197064916374117585485187848 401205484467258885140156272501982171906696081262778548596481836962141072171421 498636191877475450965030895709947093433785698167446582826791194061195603784539 785583924076127634410576675102430755981455278616781594965706255975507430652108 530159790807334373607943286675789053348366955548680391343372015649883422089339 997164147974693869690548008919306713805717150585730714881564992071408675825960 287605645978242377024246980532805663278704192676846711626687946348695046450742 021937394525926266861355294062478136120620263649819999949840514386828525895634 226432870766329930489172340072547176418868535137233266787792173834754148002280 339299735793615241275582956927683723123479898944627433045456679006203242051639 628258844308543830720149567210646053323853720314324211260742448584509458049408 182092763914000854042202355626021856434899414543995041098059181794888262805206 644108631900168856815516922948620301073889718100770929059048074909242714101893 354281842999598816966099383696164438152887721408526808875748829325873580990567 075581701794916190611400190855374488272620093668560447559655747648567400817738 170330738030547697360978654385938218722058390234444350886749986650604064587434 600533182743629617786251808189314436325120510709469081358644051922951293245007 883339878842933934243512634336520438581291283434529730865290978330067126179813 031679438553572629699874035957045845223085639009891317947594875212639707837594 486113945196028675121056163897600888009274611586080020780334159145179707303683 519697776607637378533301202412011204698860920933908536577322239241244905153278 095095586645947763448226998607481329730263097502881210351772312446509534965369 309001863776409409434983731325132186208021480992268550294845466181471555744470 966953017769043427203189277060471778452793916047228153437980353967986142437095 668322149146543801459382927739339603275404800955223181666738035718393275707714 204672383862461780397629237713120958078936384144792980258806552212926209362393 063731349664018661951081158347117331202580586672763999276357907806381881306915 636627412543125958993611964762610140556350339952314032311381965623632719896183 725484533370206256346422395276694356837676136871196292181875457608161705303159 072882870071231366630872275491866139577373054606599743781098764980241401124214 277366808275139095931340415582626678951084677611866595766016599817808941498575 497628438785610026379654317831363402513581416115190209649913354873313111502270 068193013592959597164019719605362503355847998096348871803911161281359596856547 886832585643789617315976200241962155289629790481982219946226948713746244472909 345647002853769495885959160678928249105441251599630078136836749020937491573289 627002865682934443134234735123929825916673950342599586897069726733258273590312 128874666045146148785034614282776599160809039865257571726308183349444182019353 338507129234577437557934406217871133006310600332405399169368260374617663856575 887758020122936635327026710068126182517291460820254189288593524449107013820621 155382779356529691457650204864328286555793470720963480737269214118689546732276 775133569019015372366903686538916129168888787640752549349424973342718117889275 993159671935475898809792452526236365903632007085444078454479734829180208204492 667063442043755532505052752283377888704080403353192340768563010934777212563908 864041310107381785333831603813528082811904083256440184205374679299262203769871 801806112262449090924264198582086175117711378905160914038157500336642415609521 632819712233502316742260056794128140621721964184270578432895980288233505982820 819666624903585778994033315227481777695284368163008853176969478369058067106482 808359804669884109813515865490693331952239436328792399053481098783027450017206 543369906611778455436468772363184446476806914282800455107468664539280539940910 875493916609573161971503316696830992946634914279878084225722069714887558063748 030886299511847318712477729191007022758889348693945628951580296537215040960310 776128983126358996489341024703603664505868728758905140684123812424738638542790 828273382797332688550493587430316027474906312957234974261122151741715313361862 241091386950068883589896234927631731647834007746088665559873338211382992877691 149549218419208777160606847287467368188616750722101726110383067178785669481294 878504894306308616994879870316051588410828235127415353851336589533294862949449 506186851477910580469603906937266267038651290520113781085861618888694795760741 358553458515176805197333443349523012039577073962377131603024288720053732099825 300897761897312981788194467173116064723147624845755192873278282512718244680782 421521646956781929409823892628494376024885227900362021938669648221562809360537 317804086372726842669642192994681921490870170753336109479138180406328738759384 826953558307739576144799727000347288018278528138950321798634521611106660883931 405322694490545552786789441757920244002145078019209980446138254780585804844241 640477503153605490659143007815837243012313751156228401583864427089071828481675 752712384678245953433444962201009607105137060846180118754312072549133499424761 711563332140893460915656155060031738421870157022610310191660388706466143889773 631878094071152752817468957640158104701696524755774089164456867771715850058326 994340167720215676772406812836656526412298243946513319735919970940327593850266 955747023181320324371642058614103360652453693916005064495306016126782264894243 739716671766123104897503188573216555498834212180284691252908610148552781527762 562375045637576949773433684601560772703550962904939248708840628106794362241870 474700836884267102255830240359984164595112248527263363264511401739524808619463 584078375355688562231711552094722306543709260679735100056554938122457548372854 571179739361575616764169289580525729752233855861138832217110736226581621884244 317885748879810902665379342666421699091405653643224930133486798815488662866505 234699723557473842483059042367714327879231642240387776433019260019228477831383 763253612102533693581262408686669973827597736568222790721583247888864236934639 616436330873013981421143030600873066616480367898409133592629340230432497492688 783164360268101130957071614191283068657732353263965367739031766136131596555358 499939860056515592193675997771793301974468814837110320650369319289452140265091 546518430993655349333718342529843367991593941746622390038952767381333061774762 957494386871697845376721949350659087571191772087547710718993796089477451265475 750187119487073873678589020061737332107569330221632062843206567119209695058576 117396163232621770894542621460985841023781321581772760222273813349541048100307 327510779994899197796388353073444345753297591426376840544226478421606312276964 696715647399904371590332390656072664411643860540483884716191210900870101913072 607104411414324197679682854788552477947648180295973604943970047959604029274629 920357209976195014034831538094771460105633344699882082212058728151072918297121 191787642488035467231691654185225672923442918712816323259696541354858957713320 833991128877591722611527337901034136208561457799239877832508355073019981845902 595835598926055329967377049172245493532968330000223018151722657578752405883224 908582128008974790932610076257877042865600699617621217684547899644070506624171 021332748679623743022915535820078014116534806564748823061500339206898379476625 503654982280532966286211793062843017049240230198571997894883689718304380518217 441914766042975243725168343541121703863137941142209529588579806015293875275379 903093887168357209576071522190027937929278630363726876582268124199338480816602 160372215471014300737753779269906958712128928801905203160128586182549441335382 078488346531163265040764242839087012101519423196165226842200371123046430067344 206474771802135307012409886035339915266792387110170622186588357378121093517977 560442563469499978725112544085452227481091487430725986960204027594117894258128 188215995235965897918114407765335432175759525553615812800116384672031934650729 680799079396371496177431211940202129757312516525376801735910155733815377200195 244454362007184847566341540744232862106099761324348754884743453966598133871746 609302053507027195298394327142537115576660002578442303107342955153394506048622 276496668762407932435319299263925373107689213535257232108088981933916866827894 828117047262450194840970097576092098372409007471797334078814182519584259809624 174761013825264395513525931188504563626418830033853965243599741693132289471987 830842760040136807470390409723847394583489618653979059411859931035616843686921 948538205578039577388136067954990008512325944252972448666676683464140218991594 456530942344065066785194841776677947047204195882204329538032631053749488312218 039127967844610013972675389219511911783658766252808369005324900459741094706877 291232821430463533728351995364827432583311914445901780960778288358373011185754 365995898272453192531058811502630754257149394302445393187017992360816661130542 625399583389794297160207033876781503301028012009599725222228080142357109476035 192554443492998676781789104555906301595380976187592035893734197896235893112598 390259831026719330418921510968915622506965911982832345550305908173073519550372 166587028805399213857603703537710517802128012956684198414036287272562321442875 430221090947272107347413497551419073704331827662617727599688882602722524713368 335345281669277959132886138176634985772893690096574956228710302436259077241221 909430087175569262575806570991201665962243608024287002454736203639484125595488 172727247365346778364720191830399871762703751572464992228946793232269361917764 161461879561395669956778306829031658969943076733350823499079062410020250613405 734430069574547468217569044165154063658468046369262127421107539904218871612761 778701425886482577522388918459952337629237791558574454947736129552595222657863 646211837759847370034797140820699414558071908021359073226923310083175951065901 912129479540860364075735875020589020870457967000705526250581142066390745921527 330940682364944159089100922029668052332526619891131184201629163107689408472356 436680818216865721968826835840278550078280404345371018365109695178233574303050 485265373807353107418591770561039739506264035544227515610110726177937063472380 499066692216197119425912044508464174638358993823994651739550900085947999013602 667426149429006646711506717542217703877450767356374215478290591101261915755587 023895700140511782264698994491790830179547587676016809410013583761357859135692 445564776446417866711539195135769610486492249008344671548638305447791433009768 048687834818467273375843689272431044740680768527862558516509208826381323362314 873333671476452045087662761495038994950480956046098960432912335834885999029452 640028499428087862403981181488476730121675416110662999555366819312328742570206 373835202008686369131173346973174121915363324674532563087134730279217495622701 468732586789173455837996435135880095935087755635624881049385299900767513551352 779241242927748856588856651324730251471021057535251651181485090275047684551825 209633189906852761443513821366215236889057878669943228881602837748203550601602 989400911971385017987168363374413927597364401700701476370665570350433812111357 641501845182141361982349515960106475271257593518530433287553778305750956742544 268471221961870917856078393614451138333564910325640573389866717812397223751931 643061701385953947436784339267098671245221118969084023632741149660124348309892 994173803058841716661307304006758838043211155537944060549772170594282151488616 567277124090338772774562909711013488518437411869565544974573684521806698291104 505800429988795389902780438359628240942186055628778842880212755388480372864001 944161425749990427200959520465417059810498996750451193647117277222043610261407 975080968697517660023718774834801612031023468056711264476612374762785219024120 256994353471622666089367521983311181351114650385489502512065577263614547360442 685949807439693233129712737715734709971395229118265348515558713733662912024271 430250376326950135091161295299378586468130722648600827088133353819370368259886 789332123832705329762585738279009782646054559855513183668884462826513379849166 783940976135376625179825824966345877195012438404035914084920973375464247448817 618407002356958017741017769692507781489338667255789856458985105689196092439884 156928069698335224022563457049731224526935419383700484318335719651662672157552 419340193309901831930919658292096965624766768365964701959575473934551433741370 876151732367720422738567427917069820454995309591887243493952409444167899884631 984550485239366297207977745281439941825678945779571255242682608994086331737153 889626288962940211210888442737656862452761213037101730078513571540453304150795 944777614359743780374243664697324713841049212431413890357909241603640631403814 983148190525172093710396402680899483257229795456404270175772290417323479607361 878788991331830584306939482596131871381642346721873084513387721908697510494284 376932502498165667381626061594176825250999374167288395174406693254965340310145 222531618900923537648637848288134420987004809622717122640748957193900291857330 746010436072919094576799461492929042798168772942648772995285843464777538690695 014898413392454039414468026362540211861431703125111757764282991464453340892097 696169909837265236176874560589470496817013697490952307208268288789073019001825 342580534342170592871393173799314241085264739094828459641809361413847583113613 057610846236683723769591349261582451622155213487924414504175684806412063652017 038633012953277769902311864802006755690568229501635493199230591424639621702532 974757311409422018019936803502649563695586642590676268568737211033915679383989 576556519317788300024161353956243777784080174881937309502069990089089932808839 743036773659552489130015663329407790713961546453408879151030065132193448667324 827590794680787981942501958262232039513125201410996053126069655540424867054998 678692302174698900954785072567297879476988883109348746442640071818316033165551 153427615562240547447337804924621495213325852769884733626918264917433898782478 927846891882805466998230368993978341374758702580571634941356843392939606819206 177333179173820856243643363535986349449689078106401967407443658366707158692452 118299789380407713750129085864657890577142683358276897855471768718442772612050 926648610205153564284063236848180728794071712796682006072755955590404023317874 944734645476062818954151213916291844429765106694796935401686601005519607768733 539651161493093757096855455938151378956903925101495326562814701199832699220006 639287537471313523642158926512620407288771657835840521964605410543544364216656 224456504299901025658692727914275293117208279393775132610605288123537345106837 293989358087124386938593438917571337630072031976081660446468393772580690923729 752348670291691042636926209019960520412102407764819031601408586355842760953708 655816427399534934654631450404019952853725200495780525465625115410925243799132 626271360909940290226206283675213230506518393405745011209934146491843332364656 937172591448932415900624202061288573292613359680872650004562828455757459659212 053034131011182750130696150983551563200431078460190656549380654252522916199181 995960275232770224985573882489988270746593635576858256051806896428537685077201 222034792099393617926820659014216561592530673794456894907085326356819683186177 226824991147261573203580764629811624401331673789278868922903259334986179702199 498192573961767307583441709855922217017182571277753449150820527843090461946083 521740200583867284970941102326695392144546106621500641067474020700918991195137 646690448126725369153716229079138540393756007783515337416774794210038400230895 185099454877903934612222086506016050035177626483161115332558770507354127924990 985937347378708119425305512143697974991495186053592040383023571635272763087469 321962219006426088618367610334600225547747781364101269190656968649501268837629 690723396127628722304114181361006026404403003599698891994582739762411461374480 405969706257676472376606554161857469052722923822827518679915698339074767114610 302277660602006124687647772881909679161335401988140275799217416767879923160396 356949285151363364721954061117176738737255572852294005436178517650230754469386 930787349911035218253292972604455321079788771144989887091151123725060423875373 484125708606406905205845212275453384800820530245045651766951857691320004281675 805492481178051983264603244579282973012910531838563682120621553128866856495651 261389226136706409395333457052698695969235035309422454386527867767302754040270 224638448355323991475136344104405009233036127149608135549053153902100229959575 658370538126196568314428605795669662215472169562087001372776853696084070483332 513279311223250714863020695124539500373572334680709465648308920980153487870563 349109236605755405086411152144148143463043727327104502776866195310785832333485 784029716092521532609255893265560067212435946425506599677177038844539618163287 961446081778927217183690888012677820743010642252463480745430047649288555340906 218515365435547412547615276977266776977277705831580141218568801170502836527554 321480348800444297999806215790456416195721278450892848980642649742709057912906 921780729876947797511244730599140605062994689428093103421641662993561482813099 887074529271604843363081840412646963792584309418544221635908457614607855856247 381493142707826621518554160387020687698046174740080832434366538235455510944949 843109349475994467267366535251766270677219418319197719637801570216993367508376 005716345464367177672338758864340564487156696432104128259564534984138841289042 068204700761559691684303899934836679354254921032811336318472259230555438305820 694167562999201337317548912203723034907268106853445403599356182357631283776764 063101312533521214199461186935083317658785204711236433122676512996417132521751 355326186768194233879036546890800182713528358488844411176123410117991870923650 718485785622102110400977699445312179502247957806950653296594038398736990724079 767904082679400761872954783596349279390457697366164340535979221928587057495748 169669406233427261973351813662606373598257555249650980726012366828360592834185 584802695841377255897088378994291054980033111388460340193916612218669605849157 148573356828614950001909759112521880039641976216355937574371801148055944229873 041819680808564726571354761283162920044988031540210553059707666636274932830891 688093235929008178741198573831719261672883491840242972129043496552694272640255 964146352591434840067586769035038232057293413298159353304444649682944136732344 215838076169483121933311981906109614295220153617029857510559432646146850545268 497576480780800922133581137819774927176854507553832876887447459159373116247060 109124460982942484128752022446259447763874949199784044682925736096853454984326 653686284448936570411181779380644161653122360021491876876946739840751717630751 684985635920148689294310594020245796962292456664488196757629434953532638217161 339575779076637076456957025973880043841580589433613710655185998760075492418721 171488929522173772114608115434498266547987258005667472405112200738345927157572 771521858994694811794064446639943237004429114074721818022482583773601734668530 074498556471542003612359339731291445859152288740871950870863221883728826282288 463184371726190330577714765156414382230679184738603914768310814135827575585364 359772165002827780371342286968878734979509603110889919614338666406845069742078 770028050936720338723262963785603865321643234881555755701846908907464787912243 637555666867806761054495501726079114293083128576125448194444947324481909379536 900820638463167822506480953181040657025432760438570350592281891987806586541218 429921727372095510324225107971807783304260908679427342895573555925272380551144 043800123904168771644518022649168164192740110645162243110170005669112173318942 340054795968466980429801736257040673328212996215368488140410219446342464622074 557564396045298531307140908460849965376780379320189914086581466217531933766597 011433060862500982956691763884605676297293146491149370462446935198403953444913 514119366793330193661766365255514917498230798707228086085962611266050428929696 653565251668888557211227680277274370891738963977225756489053340103885593112567 999151658902501648696142720700591605616615970245198905183296927893555030393468 121976158218398048396056252309146263844738629603984892438618729850777592879272 206855480721049781765328621018747676689724884113956034948037672703631692100735 083407386526168450748249644859742813493648037242611670426687083192504099761531 907685577032742178501000644198412420739640013960360158381056592841368457411910 273642027416372348821452410134771652960312840865841978795111651152982781462037 913985500639996032659124852530849369031313010079997719136223086601109992914287 124938854161203802041134018888721969347790449752745428807280350930582875442075 513481666092787935356652125562013998824962847872621443236285367650259145046837 763528258765213915648097214192967554938437558260025316853635673137926247587804 944594418342917275698837622626184636545274349766241113845130548144983631178978 448973207671950878415861887969295581973325069995140260151167552975057543781024 223895792578656212843273120220071673057406928686936393018676595825132649914595 026091706934751940897535746401683081179884645247361895605647942635807056256328 118926966302647953595109712765913623318086692153578860781275991053717140220450 618607537486630635059148391646765672320571451688617079098469593223672494673758 309960704258922048155079913275208858378111768521426933478692189524062265792104 362034885292626798401395321645879115157905046057971083898337186403802441751134 722647254701079479399695355466961972676325522991465493349966323418595145036098 034409221220671256769872342794070885707047429317332918852389672197135392449242 617864118863779096281448691786946817759171715066911148002075943201206196963779 510322708902956608556222545260261046073613136886900928172106819861855378098201 847115416363032626569928342415502360097804641710852553761272890533504550613568 414377585442967797701466029438768722511536380119175815402812081825560648541078 793359892106442724489861896162941341800129513068363860929410008313667337215300 835269623573717533073865333820484219030818644918409372394403340524490955455801 640646076158101030176748847501766190869294609876920169120218168829104087070956 095147041692114702741339005225334083481287035303102391969997859741390859360543 359969707560446013424245368249609877258131102473279856207212657249900346829388 687230489556225320446360263985422525841646432427161141981780248259556354490721 922658386366266375083594431487763515614571074552801615967704844271419443518327 569840755267792641126176525061596523545718795667317091331935876162825592078308 018520689015150471334038610031005591481785211038475454293338918844412051794396 997019411269511952656491959418997541839323464742429070271887522353439367363366 320030723274703740712398256202466265197409019976245205619855762576000870817308 328834438183107005451449354588542267857855191537229237955549433341017442016960 009069641561273229777022121795186837635908225512881647002199234886404395915301 846400471432118636062252701154112228380277853891109849020134274101412155976996 543887719748537643115822983853312307175113296190455900793806427669581901484262 799122179294798734890186847167650382732855205908298452980625925035212845192592 798659350613296194679625237397256558415785374456755899803240549218696288849033 256085145534439166022625777551291620077279685262938793753045418108072928589198 971538179734349618723292761474785019261145041327487324297058340847111233374627 461727462658241532427105932250625530231473875925172478732288149145591560503633 457542423377916037495250249302235148196138116256391141561032684495807250827343 176594405409826976526934457986347970974312449827193311386387315963636121862349 726140955607992062831699942007205481152535339394607685001990988655386143349578 165008996164907967814290114838764568217491407562376761845377514403147541120676 016072646055685925779932207033733339891636950434669069482843662998003741452762 771654762382554617088318981086880684785370553648046935095881802536052974079353 867651119507937328208314626896007107517552061443378411454995013643244632819334 638905093654571450690086448344018042836339051357815727397333453728426337217406 577577107983051755572103679597690188995849413019599957301790124019390868135658 553966194137179448763207986880037160730322054742357226689680188212342439188598 416897227765219403249322731479366923400484897605903795809469604175427961378255 378122394764614783292697654516229028170110043784603875654415173943396004891531 881757665050095169740241564477129365661425394936888423051740012992055685428985 389794266995677702708914651373689220610441548166215680421983847673087178759027 920917590069527345668202651337311151800018143412096260165862982107666352336177 400783778342370915264406305407180784335806107296110555002041513169637304684921 335683726540030750982908936461204789111475303704989395283345782408281738644132 271000296831194020332345642082647327623383029463937899837583655455991934086623 509096796113400486702712317652666371077872511186035403755448741869351973365662 177235922939677646325156202348757011379571209623772343137021203100496515211197 601317641940820343734851285260291333491512508311980285017785571072537314913921 570910513096505988599993156086365547740355189816673353588004821466509974143376 118277772335191074121757284159258087259131507460602563490377726337391446137703 802131834744730111303267029691733504770163210661622783002726928336558401179141 944780874825336071440329625228577500980859960904093631263562132816207145340610 422411208301000858726425211226248014264751942618432585338675387405474349107271 004975428115946601713612259044015899160022982780179603519408004651353475269877 760952783998436808690898919783969353217998013913544255271791022539701081063214 304851137829149851138196914304349750018998068164441212327332830719282436240673 319655469267785119315277511344646890550424811336143498460484905125834568326644 152848971397237604032821266025351669391408204994732048602162775979177123475109 750240307893575993771509502175169355582707253391189233407022383207758580213717 477837877839101523413209848942345961369234049799827930414446316270721479611745 697571968123929191374098292580556195520743424329598289898052923336641541925636 738068949420147124134052507220406179435525255522500874879008656831454283516775 054229480327478304405643858159195266675828292970522612762871104013480178722480 178968405240792436058274246744307672164527031345135416764966890127478680101029 513386269864974821211862904033769156857624069929637249309720162870720018983542 369036414927023696193854737248032985504511208919287982987446786412915941753167 560253343531062674525450711418148323988060729714023472552071349079839898235526 872395090936566787899238371257897624875599044322889538837731734894112275707141 095979004791930104674075041143538178246463079598955563899188477378134134707024 674736211204898622699188851745625173251934135203811586335012391305444191007362 844756751416105041097350585276204448919097890198431548528053398577784431393388 399431044446566924455088594631408175122033139068159659251054685801313383815217 641821043342978882611963044311138879625874609022613090084997543039577124323061 690626291940392143974027089477766370248815549932245882597902063125743691094639 325280624164247686849545532493801763937161563684785982371590238542126584061536 722860713170267474013114526106376538339031592194346981760535838031061288785205 154693363924108846763200956708971836749057816308515813816196688222204757043759 061433804072585386208356517699842677452319582418268369827016023741493836349662 935157685406139734274647089968561817016055110488097155485911861718966802597354 170542398513556001872033507906094642127114399319604652742405088222535977348151 913543857125325854049394601086579379805862014336607882521971780902581737087091 646045272797715350991034073642502038638671822052287969445838765294795104866071 739022932745542678566977686593992341683412227466301506215532050265534146099524 935605085492175654913483095890653617569381763747364418337897422970070354520666 317092960759198962773242309025239744386101426309868773391388251868431650102796 491149773758288891345034114886594867021549210108432808078342808941729800898329 753694064496990312539986391958160146899522088066228540841486427478628197554662 927881462160717138188018084057208471586890683691939338186427845453795671927239 797236465166759201105799566396259853551276355876814021340982901629687342985079 247184605687482833138125916196247615690287590107273310329914062386460833337863 825792630239159000355760903247728133888733917809696660146961503175422675112599 331552967421333630022296490648093458200818106180210022766458040027821333675857 301901137175467276305904435313131903609248909724642792845554991349000518029570 708291905255678188991389962513866231938005361134622429461024895407240485712325 662888893172211643294781619055486805494344103409068071608802822795968695013364 381426825217047287086301013730115523686141690837567574763723976318575703810944 339056456446852418302814810799837691851212720193504404180460472162693944578837 709010597469321972055811407877598977207200968938224930323683051586265728111463 799698313751793762321511125234973430524062210524423435373290565516340666950616 589287821870775679417608071297378133518711793165003315552382248773065344417945 341539520242444970341012087407218810938826816751204229940494817944947273289477 011157413944122845552182842492224065875268917227278060711675404697300803703961 878779669488255561467438439257011582954666135867867189766129731126720007297155 361302750355616781776544228744211472988161480270524380681765357327557860250584 708401320883793281600876908130049249147368251703538221961903901499952349538710 599735114347829233949918793660869230137559636853237380670359114424326856151210 940425958263930167801712866923928323105765885171402021119695706479981403150563 304514156441462316376380990440281625691757648914256971416359843931743327023781 233693804301289262637538266779503416933432360750024817574180875038847509493945 489620974048544263563716499594992098088429479036366629752600324385635294584472 894454716620929749549661687741412088213047702281611645604400723635158114972973 921896673738264720472264222124201656015028497130633279581430251601369482556701 478093579088965713492615816134690180696508955631012121849180584792272069187169 631633004485802010286065785859126997463766174146393415956953955420331462802651 895116793807457331575984608617370268786760294367778050024467339133243166988035 407323238828184750105164133118953703648842269027047805274249060349208295475505 400345716018407257453693814553117535421072655783561549987444748042732345788006 187314934156604635297977945507535930479568720931672453654720838168585560604380 197703076424608348987610134570939487700294617579206195254925575710903852517148 852526567104534981341980339064152987634369542025608027761442191431892139390883 454313176968510184010384447234894886952098194353190650655535461733581404554483 788475252625394966586999205841765278012534103389646981864243003414679138061902 805960785488801078970551694621522877309010446746249797999262712095168477956848 258334140226647721084336243759374161053673404195473896419789542533503630186140 095153476696147625565187382329246854735693580289601153679178730355315937836308 224861517777054157757656175935851201669294311113886358215966761883032610416465 171484697938542262168716140012237821377977413126897726671299202592201740877007 695628347393220108815935628628192856357189338495885060385315817976067947984087 836097596014973342057270460352179060564760328556927627349518220323614411258418 242624771201203577638889597431823282787131460805353357449429762179678903456816 988955351850447832561638070947695169908624710001974880920500952194363237871976 487033922381154036347548862684595615975519376541011501406700122692747439388858 994385973024541480106123590803627458528849356325158538438324249325266608758890 831870070910023737710657698505643392885433765834259675065371500533351448990829 388773735205145933304962653141514138612443793588507094468804548697535817021290 849078734780681436632332281941582734567135644317153796781805819585246484008403 290998194378171817730231700398973305049538735611626102399943325978012689343260 558471027876490107092344388463401173555686590358524491937018104162620850429925 869743581709813389404593447193749387762423240985283276226660494238512970945324 558625210360082928664972417491914198896612955807677097959479530601311915901177 394310420904907942444886851308684449370590902600612064942574471035354765785924 270813041061854621988183009063458818703875585627491158737542106466795134648758 677154383801852134828191581246259933516019893559516796893285220582479942103451 271587716334522299541883968044883552975336128683722593539007920166694133909116 875880398882886921600237325736158820716351627133281051818760210485218067552664 867390890090719513805862673512431221569163790227732870541084203784152568328871 804698795251307326634027851905941733892035854039567703561132935448258562828761 061069822972142096199350933131217118789107876687204454887608941017479864713788 246215395593333327556200943958043453791978228059039595992743691379377866494096 404877784174833643268402628293240626008190808180439091455635193685606304508914 228964521998779884934747772913279726602765840166789013649050874114212686196986 204412696528298108704547986155954533802120115564697997678573892018624359932677 768945406050821883822790983362716712449002676117849826437703300208184459000971 723520433199470824209877151444975101705564302954282181967000920251561584417420 593365814813490269311151709387226002645863056132560579256092733226557934628080 568344392137368840565043430739657406101777937014142461549307074136080544210029 560009566358897789926763051771878194370676149821756418659011616086540863539151 303920131680576903417259645369235080641744656235152392905040947995318407486215 121056183385456617665260639371365880252166622357613220194170137266496607325201 077194793126528276330241380516490717456596485374835466919452358031530196916048 099460681490403781982973236093008713576079862142542209641900436790547904993007 837242158195453541837112936865843055384271762803527912882112930835157565659994 474178843838156514843422985870424559243469329523282180350833372628379183021659 183618155421715744846577842013432998259456688455826617197901218084948033244878 725818377480552226815101137174536841787028027445244290547451823467491956418855 124442133778352142386597992598820328708510933838682990657199461490629025742768 603885051103263854454041918495886653854504057132362968106914681484786965916686 184275679846004186876229805556296304595322792305161672159196867584952363529893 578850774608153732145464298479231051167635774949462295256949766035947396243099 534331040499420967788382700271447849406903707324910644415169605325656058677875 741747211082743577431519406075798356362914332639781221894628744779811980722564 671466405485013100965678631488009030374933887536418316513498254669467331611812 336485439764932502617954935720430540218297487125110740401161140589991109306249 231281311634054926257135672181862893278613883371802853505650359195274140086951 092616754147679266803210923746708721360627833292238641361959412133927803611827 632410600474097111104814000362334271451448333464167546635469973149475664342365 949349684588455152415075637660508663282742479413606287604129064491382851945640 264315322585862404314183866959063324506300039221319264762596269151090445769530 144405461803785750303668621246227863975274666787012100339298487337501447560032 210062235802934377495503203701273846816306102657030087227546296679688089058712 767636106622572235222973920644309352432722810085997309513252863060110549791564 479184500461804676240892892568091293059296064235702106152464620502324896659398 732493396737695202399176089847457184353193664652912584806448019652016283879518 949933675924148562613699594530728725453246329152911012876377060557060953137752 775186792329213495524513308986796916512907384130216757323863757582008036357572 800275449032795307990079944254110872569318801466793559583467643286887696661009 739574996783659339784634695994895061049038364740950469522606385804675807306991 229047408987916687211714752764471160440195271816950828973353714853092893704638 442089329977112585684084660833993404568902678751600877546126798801546585652206 121095349079670736553970257619943137663996060606110640695933082817187642604357 342536175694378484849525010826648839515970049059838081210522111109194332395113 605144645983421079905808209371646452312770402316007213854372346126726099787038 565709199850759563461324846018840985019428768790226873455650051912154654406382 925385127631766392205093834520430077301702994036261543400132276391091298832786 392041230044555168405488980908077917463609243933491264116424009388074635660726 233669584276458369826873481588196105857183576746200965052606592926354829149904 576830721089324585707370166071739819448502884260396366074603118478622583105658 087087030556759586134170074540296568763477417643105175103673286924555858208237 203860178173940517513043799486882232004437804310317092103426167499800007301609 481458637448877852227307633049538394434538277060876076354209844500830624763025 357278103278346176697054428715531534001649707665719598504174819908720149087568 603778359199471934335277294728553792578768483230110185936580071729118696761765 505377503029303383070644891281141202550615089641100762382457448865518258105814 034532012475472326908754750707857765973254284445935304499207001453874894822655 644222369636554419422544133821222547749753549462482768053333698328415613869236 344335855386847111143049824839899180316545863828935379913053522283343013795337 295401625762322808113849949187614414132293376710656349252881452823950620902235 787668465011666009738275366040544694165342223905210831458584703552935221992827 276057482126606529138553034554974455147034493948686342945965843102419078592368 022456076393678416627051855517870290407355730462063969245330779578224594971042 018804300018388142900817303945050734278701312446686009277858181104091151172937 487362788787490746528556543474888683106411005102302087510776891878152562273525 155037953244485778727761700196485370355516765520911933934376286628461984402629 525218367852236747510880978150709897841308624588152266096355140187449583692691 779904712072649490573726428600521140358123107600669951853612486274675637589622 529911649606687650826173417848478933729505673900787861792535144062104536625064 046372881569823231750059626108092195521115085930295565496753886261297233991462 835847604862762702730973920200143224870758233735491524608560821032888297418390 647886992327369136004883743661522351705843770554521081551336126214291181561530 175888257359489250710887926212864139244330938379733386780613179523731526677382 085802470143352700924380326695174211950767088432634644274912755890774686358216 216604274131517021245858605623363149316464691394656249747174195835421860774871 105733845843368993964591374060338215935224359475162623918868530782282176398323 730618020424656047752794310479618972429953302979249748168405289379104494700459 086499187272734541350810198388186467360939257193051196864560185578245021823106 588943798652243205067737996619695547244058592241795300682045179537004347245176 289356677050849021310773662575169733552746230294303120359626095342357439724965 921101065781782610874531887480318743082357369919515634095716270099244492974910 548985151965866474014822510633536794973714251022934188258511737199449911509758 374613010550506419772153192935487537119163026203032858865852848019350922587577 559742527658401172134232364808402714335636754204637518255252494432965704386138 786590196573880286840189408767281671413703366173265012057865391578070308871426 151907500149257611292767519309672845397116021360630309054224396632067432358279 788933232440577919927848463333977773765590187057480682867834796562414610289950 848739969297075043275302997287229732793444298864641272534816060377970729829917 302929630869580199631241330493935049332541235507105446118259114111645453471032 988104784406778013807713146540009938630648126661433085820681139583831916954555 825942689576984142889374346708410794631893253910696395578070602124597489829356 461356078898347241997947856436204209461341238761319886535235831299686226894860 840845665560687695450127448663140505473535174687300980632278046891224682146080 672762770840240226615548502400895289165711761743902033758487784291128962324705 919187469104200584832614067733375102719565399469716251724831223063391932870798 380074848572651612343493327335666447335855643023528088392434827876088616494328 939916639921048830784777704804572849145630335326507002958890626591549850940797 276756712979501009822947622896189159144152003228387877348513097908101912926722 710377889805396415636236416915498576840839846886168437540706512103906250612810 766379904790887967477806973847317047525344215639038720123880632368803701794930 895490077633152306354837425681665336160664198003018828712376748189833024683637 148830925928337590227894258806008728603885916884973069394802051122176635913825 152427867009440694235512020156837777885182467002565170850924962374772681369428 435006293881442998790530105621737545918267997321773502936892806521002539626880 749809264345801165571588670044350397650532347828732736884086354000274067678382 196352222653929093980736739136408289872201777674716811819585613372158311905468 293608323697611345028175783020293484598292500089568263027126329586629214765314 223335179309338795135709534637718368409244442209631933129562030557551734006797 374061416210792363342380564685009203716715264255637185388957141641977238742261 059666739699717316816941543509528319355641770566862221521799115135563970714331 289365755384464832620120642433801695586269856102246064606933079384785881436740 700059976970364901927332882613532936311240365069865216063898725026723808740339 674439783025829689425689674186433613497947524552629142652284241924308338810358 005378702399954217211368655027534136221169314069466951318692810257479598560514 500502171591331775160995786555198188619321128211070944228724044248115340605589 595835581523201218460582056359269930347885113206862662758877144603599665610843 072569650056306448918759946659677284717153957361210818084154727314266174893313 417463266235422207260014601270120693463952056444554329166298666078308906811879 009081529506362678207561438881578135113469536630387841209234694286873083932043 233387277549680521030282154432472338884521534372725012858974769146080831440412 586818154004918777228786980185345453700652665564917091542952275670922221747411 206272065662298980603289167206874365494824610869736722554740481288924247185432 360575341167285075755205713115669795458488739874222813588798584078313506054829 055148278529489112190538319562422871948475940785939804790109419407067176443903 273071213588738504999363883820550168340277749607027684488028191222063688863681 104356952930065219552826152699127163727738841899328713056346468822739828876319 864570983630891778648708667618548568004767255267541474285102814580740315299219 781455775684368111018531749816701642664788409026268282444825802753209454991510 451851771654631180490456798571325752811791365627815811128881656228587603087597 496384943527567661216895926148503078536204527450775295063101248034180458405943 292607985443562009370809182152392037179067812199228049606973823874331262673030 679594396095495718957721791559730058869364684557667609245090608820221223571925 453671519183487258742391941089044411595993276004450655620646116465566548759424 736925233695599303035509581762617623184956190649483967300203776387436934399982 943020914707361894793269276244518656023955905370512897816345542332011497599489 627842432748378803270141867695262118097500640514975588965029300486760520801049 153788541390942453169171998762894127722112946456829486028149318156024967788794 981377721622935943781100444806079767242927624951078415344642915084276452000204 276947069804177583220909702029165734725158290463091035903784297757265172087724 474095226716630600546971638794317119687348468873818665675127929857501636341131 462753049901913564682380432997069577015078933772865803571279091376742080565549 362541")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 36:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Greater than calculator")
				isItGreater1 = int(input("Enter the first number: "))
				isItGreater2 = int(input("Enter the second number: "))
				if (isItGreater1 > isItGreater2):
					curanswer = isItGreater1
					lessThan = isItGreater2
				if (isItGreater1 < isItGreater2):
					curanswer = isItGreater2
					lessThan = isItGreater1
				print (str(curanswer) + " is greater than " + str(lessThan))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 37:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 38:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 39:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 40:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 41:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 42:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 43:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 44:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 45:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 46:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 47:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 48:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 49:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 50:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Random Number Generator")
				ranrange = int(input("How many random numbers do you want to generate (1-100 MAX recommended): "))
				rand1 = int(input("Enter the start number of the random range: "))
				rand2 = int(input("Enter the end number of the random range: "))
				staran = int
				staran = 0
				while not (staran == ranrange):
					ranrange - 1
					print (random.randint(rand1, rand2))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad) ")					
			if calcIDSes == 51:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Random Number Generator (with decimals)")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
if uCMainConsole == 3:
	konloop = int(0)
	while konloop == 0:
		print ("The ultimate math encyclopedia")
		print ("Volume 1")
		print ("\nUCalc exclusives")
		print ("Update log [ID: 10000]")
		print ("Version info [ID: 10001]")
		print ("Developer Data Folder ReadMe [ID: 10002]")
		print ("Source info [ID: 10003]")
		print ("Development goals [ID: 10004]")
		print ("Manufacturing guide [ID: 10005]")
		print ("Terms of use [ID: 10006]")
		print ("Credits [ID: 10007]")
		more1 = input("Press [ENTER] key for more")
		print ("\nProcessor setup")
		print ("4 bit-128 bit [ID: 20000]")
		print ("Weak calculators [ID: 20001]")
		print ("System compatibility [ID: 20002]")
		print ("4 bit computing [ID: 20003]")
		print ("8 bit computing [ID: 20004]")
		print ("12 bit computing [ID: 20005]")
		print ("16 bit computing [ID: 20006]")
		print ("18 bit computing [ID: 20007]")
		print ("24 bit computing [ID: 20008]")
		print ("26 bit computing [ID: 20009]")
		print ("31 bit computing  [ID: 20010]")
		print ("32 bit computing  [ID: 20011]")
		print ("36 bit computing  [ID: 20012]")
		print ("48 bit computing  [ID: 20013]")
		print ("60 bit computing  [ID: 20014]")
		print ("64 bit computing  [ID: 20015]")
		print ("128 bit computing  [ID: 20016]")
		print ("256 bit computing  [ID: 20017]")
		print ("512 bit computing  [ID: 20018]")
		print ("Variable names and their purpose for UCalc [ID: 20019]") 
		more1 = input("Press [ENTER] key for more")
		print ("\nGetting started with math [ID: 30000]")
		print ("Counting [ID: 30001]")
		print ("Names of numbers [ID: 30002]")
		print ("Superstitious numbers [ID: 30003]")
		print ("Slang numbers [ID: 30004]")
		print ("Roman numerals [ID: 30005]")
		print ("Multiples table [ID: 30006]")
		print ("IQ Definition [ID: 30007]")
		print ("Bit slicing definiton [ID: 30008]")
		more1 = input("Press [ENTER] key for more")
		print ("\nAlgebra")
		more1 = input("Press [ENTER] key for more")
		print ("\nCalculus")
		more1 = input("Press [ENTER] key for more")
		WikIDSelect = int(input("Enter an ID to start: "))
		if WikIDSelect == 10000:
			print ("Update log")
			print ("For Ucalc")
			more1 = input("Read more? [ENTER]")
			print ("UCalc pre-alpha CLI client 1")
			print ("\nThis is the very first version of the UCalc client")
			print ("It contains many features, but has some odd bugs")
			print ("There was only 1 pre-alpha version of this program, and was a simple private demonstration build to make sure all the added features workede")
			print ("It was moved to the alpha phase when it was deemed stable, and acquired a working update log")
			print ("Pre-alpha 1 added the following features:")
			print ("<*> Added Main Menu")
			print ("<*> Added language setup [ONLY ENGLISH]")
			print ("<*> processor setup")
			print ("<*> ID table for calculation operations")
			print ("<*> Random number generator (unstable, but still works)")
			print ("<*> Calculator room (unstable, but still runs)")
			print ("<*> Added modular division calculator")
			print ("<*> Added addition calculator")
			print ("<*> Added subtraction calculator")
			print ("<*> Added multiplication calculator")
			print ("<*> Added division calculator")
			print ("<*> Added greater than calculator")
			print ("<*> Added count 100,000 digits of Pi (easter egg)")
			print ("<*> Added RGB calculator")
			print ("<*> Added addition calculator")
			print ("<*> Added subtraction calculator")
			print ("<*> Added multiplication calculator")
			print ("<*> Added division calculator")
			print ("<*> Added wiki page (with no entries at the moment")
			print ("That is it for pre-alpha 1!")
			more1 = input("Read more? [ENTER]")
			print ("UCalc Alpha client 1")
			print ("\nUCalc jumped to the Alpha phase because of 2 reasons:")
			print ("<*> The program works in a stable state over 50% of the time")
			print ("<*> The update log was released")
			print ("<*> Added speed-dial calculator (the public calculator)")
			print ("<*> Increased documentation")
			print ("<*> Added more organized ID chart for math operations (it can now fit perfectly on a 1280x720 screen)")
			print ("<*> Fixed 3 critical bugs that prevent certain operations from running, and causing the program to crash")
			print ("<*> Added in new operaitons (Speed-dial only)")
			print ("<*> Added manufacturer list")
			print ("<*> Added boot-screens (modify to unlock)")
			more1 = input("Read more? [ENTER]")
			print ("UCalc Alpha client 2")
			print ("<*> increased documentation")
			print ("<*> added vote counter")
			print ("<*> added memory calculator")
			print ("<*> added game catalog")
			print ("Why didn't it go to beta? Not all the planned features are here yet, and it is still unstable at times")
			print ("Alpha 1 added the following features:")
			print ("<*> a working update log")
			print ("That is it for alpha 1!")
			noMore = input("End of update log. Press [ENTER to exit]")
			print ("Exiting update log")
			print ("Please wait...")
		if WikIDSelect == 10001:
			print ("UCalc Pro")
			print ("Demonstration build")
			print ("Alpha 1")
			print ("Version 0.01")
			print ("Copyleft Sean Walla Walla")
			print ("Written in Python 3")
			noMore = input("Press [ENTER] key to exit version info")
			print ("Exiting version info")
			print ("Please wait...")
		if WikIDSelect == 10002:
			print ("READ_ME.TXT | Calculator Notepad |")
			print ("''''''''''''''''''''''''''''''''''")
			print ("DevData subdirectory |")
			print ("=====================/")
			print (" ")
			print ("=========================================================================\\")
			print ("                                                                         |")
			print ("As a joke referrring to the old 8:3 file system, and the calculators     |")
			print ("we are succeeding in this project, during the pre-alpha phase, we        |")
			print ("made several .DAT files. These aren't used by anything, they are just    |")
			print ("notes. Try looking inside them with notepad, notepad++ or other text     |")
			print ("editors. Don't worry, simple modifications or overwrites to the contents |")
			print ("of the files will have NO effect on UCALC they are simply just notes     |")
			print ("                                                                 - Sean  |")
			print ("=========================================================================/")
			print (" ")
			print ("========================================\\")
			print ("N I C E _ A S C I I _ A R T _ S E A N   |")
			print ("A E T H E T I C _ B O T T O M _ T E X T |")
			print ("========================================/")
			print (" ")
			print ("===================================================================================\\")
			print ("Copyleft (>) Sean Walla Walla 2015-2018                                            |")
			print ("Modifications are allowed to the program as long as credit is given                |")
			print ("===================================================================================/")
			print (" ")
			noMore = input("Press [ENTER] key to close this file")
			print ("Closing document")
			print ("Please wait...")
		if WikIDSelect == 10003:
			print ("Source info")
			print ("Language: Python 3x (3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8)")
			print ("Tools used: \nPython 3.6.exe\nNotepad++\nNotepad.exe")
			print ("Lines of code: 3470")
			print ("Bytes: 394393")
			noMore = input("Press [ENTER] key to exit source info")
			print ("Closing")
			print ("Please wait")
		if WikIDSelect == 10004:
			print ("Development goals")
			print ("Here are our current development goals")
			print ("<*> Go over 10,239 lines of code (amount in the first version of Linux)")
			print ("<*> Reduce overall bug count to less than 50")
			print ("<*> Surpass the TI-30XS calculator in every way")
			print ("<*> Finish implementing all features")
			print ("Those are our current development goals!")
			noMore = input("Press [ENTER] key to exit source info")
			print ("Closing")
			print ("Please wait")
		if WikIDSelect == 10005:
			print ("Manufacturing guide")
			print ("===================")
			print ("Requirements:")
			print ("1280x720 or higher screen (FPS doesn't matter, as long as it is at least 24 FPS)")
			print ("64 bit processor")
			print ("256 Megabytes of RAM")
			print ("1024 Megabytes of disk space")
			print ("8 bit color or more")
			print ("No internet connection required PLEASE keep it this way")
			print ("Battery: at least 1500 mAh capacity (2600 mAh or higher recommended)")
			print ("Keypad:")
			print ("| 1 2 3 4 5 6 7 8 9 0 a b c d e f g h i j k l m n o p q r s t u v w x y z")
			print ("====================================================================================================")
		if WikIDSelect == 10006:
			print ("Terms of usage")
			print ("Please read and accept these conditions to use UCalc")
			more1 = input("Press [ENTER] for more")
			print ("Distribution")
			print ("You are allowed to download, modify, and share this software if you give credit. You can give it publically, to a friend, co-worker, neighbor, or anyone as long as you follow the TOU")
			print ("You cannot charge royalties for this product. It is free open-source software, and must remain free")
			print ("We do not want inappropriate builds. If you are to do that, distribute them privately. No racism, sexism, supremacy, or other bad stuff")
			more1 = input("Press [ENTER] for more")
			print ("Manufacturing")
			print ("You are allowed to manufacture your own versions of the hardware as long as you give credit and reach minimum system requirement")
			more1 = input("Press [ENTER] for more")
			print ("Credit")
			print ("Credit must be given to the original creators, even if you were to just make a minor edit. Plagiarism is NOT allowed")
			nomore = input("Press [ENTER] to agree and exit")
		if WikIDSelect == 10007:
			print ("C R E D I T S")
			print (" ")
			print (" ")
			more1 = input("Press [ENTER] key to start")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("Programmers")
			print ("\nSean P. Myrick")
			more1 = input("Press [ENTER] key for more")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("Beta testers")
			print ("\nSean P. Myrick")
			print ("Michael Whitney")
			print ("Colleen P. Myrick")
			more1 = input("Press [ENTER] key for more")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("Inspirations")
			print ("\nWindows 3.1 - Microsoft")
			print ("Windows 1.01 - Microsoft")
			print ("Wikipedia - Wikimedia foundation")
			print ("NASA - National American Space Agency")
			more1 = input("Press [ENTER] key for more")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("Sound producers")
			print ("\nSean Myrick")
			more1 = input("Press [ENTER] key for more")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
			print ("Special thanks to")
			print ("\nMichael Whitney - for showing interest")
			print ("Carrie Delfino - for teaching me how to program in python")
			print ("Colleen and Vern Myrick - for supporting me through my life")
			noMore = input("Press [ENTER] key to quit")
		if WikIDSelect == 20000:
			print ("Processor setup")
			print ("In computer science and engineering, the processor is one of the main parts of a computer")
			print ("The CPU (Central Processing Unit) works with information on your computer")
			print ("There are processors with different integer caps, such as 4 bit, 8 bit, 16 bit, 32 bit, etc")
			print ("These integer caps hold their own limits")
			print ("Here is a chart on how it works:")
			print ("|-----------------------------------------------------------------------|")
			print ("| CPU Integers                                                          |")
			print ("| 4 bit   | max = 16                                                    |")
			print ("| 8 bit   | max = 255                                                   |")
			print ("| 12 bit  | max = 4096                                                  |")
			print ("| 16 bit  | max = 65,535                                                |")
			print ("| 18 bit  | max = 262,144                                               |")
			print ("| 24 bit  | max = 8,388,607                                             |")
			print ("| 26 bit  | max = UNKNOWN                                               |")
			print ("| 31 bit  | max = UNKNOWN                                               |")
			print ("| 32 bit  | max = 4,294,967,295                                         |")
			print ("| 36 bit  | max = UNKNOWN                                               |")
			print ("| 48 bit  | max = 140,737,488,355,327                                   |")
			print ("| 60 bit  | max = UNKNOWN                                               |")
			print ("| 64 bit  | max = 9,223,372,036,854,775,807                             |")
			print ("| 128 bit | max = 170,141,183,460,469,231,731,687,303,715,884,105,728   |")
			print ("| 256 bit | max = UNKNOWN                                               |")
			print ("| 512 bit | max = UNKNOWN                                               |")
			print ("|-----------------------------------------------------------------------|")
			print ("Which brings us to the Weak Calculators section")
			noMore = input("Press [ENTER] key to exit")
			print ("Exiting")
			print ("Please wait...")
		if WikIDSelect == 20001:
			print ("Weak calculators")
			print ("| Please read 'Processor setup' first if you haven't already")
			print ("A weak calculator with uCalc is considered a calculator that")
			print ("Can't calculate high amounts of numbers")
			print ("Any calculator below 32 bit here is considered weak, as it can't do advanced calculations")
			print ("But then why did we include them? UCalc supports all types of math. If you would like to experience simple calculators, and what")
			print ("the worlds weakest calculator feels like, go ahead! If you would like to experience what the worlds most advanced calculator feels like")
			print ("be my guest! All numbers are allowed. No exceptions")
		if WikIDSelect == 20002:
			print ("Compatibility")
			print ("\nMicrosoft Windows")
			print ("Windows 2000")
			print ("Windows XP")
			print ("Windows Vista")
			print ("Windows 7")
			print ("Windows 8")
			print ("Windows 8.1")
			print ("Windows 10")
			print ("Windows Server 2003")
			print ("Windows Server 2008")
			print ("Windows Server 2012")
			print ("Windows Server 2016")
			print ("Windows Server 2019")
			print ("\nMacOS")
			print ("MacOS X 10.2")
			print ("MacOS X 10.3")
			print ("MacOS X 10.4")
			print ("MacOS X 10.5")
			print ("MacOS X 10.6")
			print ("MacOS X 10.7")
			print ("OS X 10.8")
			print ("OS X 10.9")
			print ("OS X 10.10")
			print ("OS X 10.11")
			print ("MacOS 10.12")
			print ("MacOS 10.13")
			print ("MacOS 10.14")
			print ("\nLinux")
			print ("\nUbuntu")
			print ("Ubuntu 4.04 and up")
			print ("Lubuntu 6.10 and up")
			print ("Xubuntu 6.10 and up")
			print ("\nFedora")
			print ("Fedora Core 3 and up")
			print ("\nMint")
			print ("Linux Mint 4 and up")
			print ("\nArch")
			print ("Unknown")
			print ("\nGentoo")
			print ("Unknown")
		if WikIDSelect == 20003:
			print ("In computer architecture, 4-bit integers, memory addresses, or other data units are those that are 4 bits wide. Also, ")
			print ("4-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size. A group ")
			print ("of four bits is also called a nibble and has 24 = 16 possible values.")
			print (" ")
			print ("Some of the first microprocessors had a 4-bit word length and were developed around 1970. The TMS 1000, the world's first ")
			print ("single-chip microprocessor, was a 4-bit CPU; it had a Harvard architecture, with an on-chip instruction ROM, 8-bit-wide ")
			print ("instructions and an on-chip data RAM with 4-bit words.[1] The first commercial microprocessor was the binary-coded decimal") 
			print ("(BCD-based) Intel 4004,[2][3] developed for calculator applications in 1971; it had a 4-bit word length, but had 8-bit ")
			print ("instructions and 12-bit addresses.")
			print (" ")
			print ("The HP Saturn processors, used in many Hewlett-Packard calculators between 1984 and 2003 (including the HP 48 series ")
			print ("of scientific calculators) are ''4-bit'' (or hybrid 64-/4-bit) machines; as the Intel 4004 did, they string multiple 4-bit") 
			print ("words together, e.g. to form a 20-bit memory address, and most of the registers are 64 bits wide, storing 16 ")
			print ("4-bit digits.[4][5][6]")
			print (" ")
			print ("The 4-bit processors were programmed in assembly language or Forth, e.g. ''MARC4 Family of 4 bit Forth CPU''[7] because of the ")
			print ("extreme size constraint on programs and because common programming languages (for microcontrollers, 8-bit and larger), such as") 
			print ("the C programming language, do not support 4-bit data types (C requires that the size of the char data type be at least 8 ")
			print ("bits,[8] and that all data types other than bitfields have a size that is a multiple of the character size[9][10][11]). ")
			print ("While larger than 4-bit values can be used by combining more than one manually, the language has to support the smaller ")
			print ("values used in the combining. If not, assembly is the only option.[dubious – discuss]")
			print (" ")
			print ("The 1970s saw the emergence of 4-bit software applications for mass markets like pocket calculators. During the ")
			print ("1980s 4-bit microprocessor were used in handheld electronic games to keep costs low.")
			print (" ")
			print ("In the 1970s and 1980s, a number of research and commercial computers used bit slicing, in which the CPU's arithmetic ")
			print ("logic unit (ALU) was built from multiple 4-bit-wide sections, each section including a chip such as an Am2901 or 74181 chip.")
			print (" ")
			print ("The Zilog Z80, although it is an 8-bit microprocessor, has a 4-bit ALU.[12][13]")
			more1 = input("Contents")
			print (" ")
			print ("1 Modern uses")
			print ("2 Details")
			print ("3 List of 4-bit processors")
			print ("4 See also")
			print ("5 References")
			print ("6 External links")
			print (" ")
			more1 = input("Modern uses")
			print (" ")
			print ("While 32- and 64-bit processors are more prominent in modern consumer electronics, 4-bit CPUs continue to be used ")
			print ("(usually as part of a microcontroller) in cost-sensitive applications that require minimal computing power. For example,") 
			print ("one bicycle computer specifies that it uses a ''4-bit 1-chip microcomputer''.[14] Other typical uses include coffee makers,") 
			print ("infrared remote controls,[15] and security alarms.[16]")
			print (" ")
			print ("Use of 4-bit processors has declined relative to 8-bit or even 32-bit processors, as they are hard to find cheaper in general") 
			print ("computer suppliers' stores. The simplest kinds are not available in any of them, and others are ''non-stock'' and more ")
			print ("expensive.[17] (A few expensive ones can be found, as of 2014, on eBay.)[18][19][20]")
			print (" ")
			print ("Electronics stores still carry, as of 2014, non-CPU/non-MCU 4-bit chips, such as counters.")
			print (" ")
			print ("As of 2015, most PC motherboards, especially laptop motherboards, use a 4-bit LPC bus (introduced in 1998) to connect the ")
			print ("southbridge to the motherboard firmware flash ROM (UEFI or BIOS) and the Super I/O chip.[21][22]")
			more1 = input("Details")
			print ("Main article: Nibble")
			print (" ")
			print ("With 4 bits, it is possible to create 16 different values. All single-digit hexadecimal numbers can be written with four bits. ")
			print ("Binary-coded decimal is a digital encoding method for numbers using decimal notation, with each decimal digit represented by ")
			print ("four bits.")
			print ("Binary 	Octal 	Decimal 	Hexadecimal")
			print ("0000 	0 	0 	0")
			print ("0001 	1 	1 	1")
			print ("0010 	2 	2 	2")
			print ("0011 	3 	3 	3")
			print ("0100 	4 	4 	4")
			print ("0101 	5 	5 	5")
			print ("0110 	6 	6 	6")
			print ("0111 	7 	7 	7")
			print ("1000 	10 	8 	8")
			print ("1001 	11 	9 	9")
			print ("1010 	12 	10 	A")
			print ("1011 	13 	11 	B")
			print ("1100 	14 	12 	C")
			print ("1101 	15 	13 	D")
			print ("1110 	16 	14 	E")
			print ("1111 	17 	15 	F")
			more1 = input("List of 4-bit processors")
			print ("16-pin DIP")
			print ("Intel C4004")
			print ("infrared remote control PCB")
			print ("an infrared remote control transmitter controlled by a NEC D63GS 4-bit microcontroller")
			print ("20-pin PSOP")
			print ("NEC D63GS: a 4-bit microcontroller for infrared remote control transmission")
			print ("card-edge PCB")
			print ("Olympia CD700 Desktop Calculator using the National Semiconductor MAPS MM570X bit-serial 4-bit microcontroller")
			print ("16-pin DIP")
			print ("National Semiconductor MM5700CA/D bit-serial 4-bit microcontroller")
			print (" ")
			print ("TMS 1000")
			print ("Intel 4004")
			print ("Intel 4040")
			print ("10NES")
			print ("Atmel MARC4 core[23][24] – (discontinued: ''Last ship date: March 7, 2015''[25])")
			print ("Samsung S3C7 (KS57 Series) 4-bit microcontrollers (RAM: 512 to 5264 nibbles, 6 MHz clock)")
			print ("Toshiba TLCS-47 series")
			print ("HP Saturn")
			print ("NEC μPD75X")
			print ("NEC μCOM-4")
			print ("NEC (now Renesas) µPD612xA (discontinued), µPD613x, μPD6x[15][26] and μPD1724x[27] infrared remote control transmitter ")
			print ("microcontrollers[28][29]")
			print ("EM Microelectronic-Marin EM6600 family,[30] EM6580,[31][32] EM6682,[33] etc.")
			print ("Epson S1C63 family")
			print ("National Semiconductor MAPS MM570X")
			noMore = input("Press [ENTER] key to exit")
		if WikIDSelect == 20005:
In computer architecture, 8-bit integers, memory addresses, or other data units are those that are 8 bits (1 octet) wide. Also, 8-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size. 8-bit is also a generation of microcomputers in which 8-bit microprocessors were the norm.

The IBM System/360 introduced byte-addressable memory with 8-bit bytes, as opposed to bit-addressable or decimal digit-addressable or word-addressable memory, although its general purpose registers were 32 bits wide, and addresses were contained in the lower 24 bits of those addresses. Different models of System/360 had different internal data path widths; the IBM System/360 Model 30 (1965) implemented the 32-bit System/360 architecture, but had an 8 bit native path width, and performed 32-bit arithmetic 8 bits at a time.[1]

The first widely adopted 8-bit microprocessor was the Intel 8080, being used in many hobbyist computers of the late 1970s and early 1980s, often running the CP/M operating system; it had 8-bit data words and 16-bit addresses. The Zilog Z80 (compatible with the 8080) and the Motorola 6800 were also used in similar computers. The Z80 and the MOS Technology 6502 8-bit CPUs were widely used in home computers and second- and third-generation game consoles of the 1970s and 1980s. Many 8-bit CPUs or microcontrollers are the basis of today's ubiquitous embedded systems.
Details

There are 28 (256) different possible values for 8 bits. When unsigned, it has possible values ranging from 0 to 255, when signed, it has -128 to 127.

Eight-bit CPUs use an 8-bit data bus and can therefore access 8 bits of data in a single machine instruction. The address bus is typically a double octet wide (i.e. 16-bit), due to practical and economical considerations. This implies a direct address space of only 64 kB on most 8-bit processors.
Notable 8-bit CPUs

The first commercial 8-bit processor was the Intel 8008 (1972) which was originally intended for the Datapoint 2200 intelligent terminal. Most competitors to Intel started off with such character oriented 8-bit microprocessors. Modernized variants of these 8-bit machines are still one of the most common types of processor in embedded systems.

Another notable 8-bit CPU is the MOS Technology 6502; it, and variants of it, were used in a number of personal computers such as the Apple I and Apple II, the Atari 8-bit family, the BBC Micro, and the Commodore PET and Commodore VIC-20, and in a number of video game consoles such as the Atari 2600 and the Nintendo Entertainment System.
Early or popular 8-bit processors (incomplete) Manufacturer 	Processor 	Year 	Comment
Intel 	8008 	1972 	Datapoint 2200 compatible
Signetics 	2650 	1973 	
Intel 	8080 	1974 	8008 source compatible
Motorola 	6800 	1974 	
Fairchild 	F8 	1975 	
MOS 	6502 	1975 	Similar to 6800, but incompatible
Microchip 	PIC 	1975 	Harvard architecture microcontroller
Electronic Arrays 	EA9002 	1976 	8-bit data, 12-bit addressing
RCA 	1802 	1976 	
Zilog 	Z80 	1976 	8080 binary compatible
Intel 	8085 	1977 	8080 binary compatible
Motorola 	6809 	1978 	6800 source compatible
Zilog 	Z8 	1978 	Harvard architecture microcontroller
Intel 	8051 	1980 	Harvard architecture microcontroller
MOS 	6510 	1982 	Enhanced 6502 custom-made for use in the Commodore 64
Ricoh 	2A03 	1982 	6502 clone minus BCD instructions for the Nintendo Entertainment System
Zilog 	Z180 	1985 	Z80 binary compatible
Motorola 	68HC11 	1985 	
Atmel 	AVR 	1996 	
Zilog 	EZ80 	1999 	Z80 binary compatible
Infineon 	XC800 	2005 	
Freescale 	68HC08 		
Hudson 	HuC6280 		
Motorola 	6803 		
NEC 	78K0[2] 		
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
In computer architecture, 12-bit integers, memory addresses, or other data units are those that are 12 bits (1.5 octets) wide. Also, 12-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.

Possibly the best-known 12-bit CPU is the PDP-8 and its relatives, such as the Intersil 6100 microprocessor produced in various incarnations from August 1963 to mid-1990. Many analog to digital converters (ADCs) have a 12-bit resolution. Some PIC microcontrollers use a 12-bit word size.

12 binary digits, or 3 nibbles (a 'tribble'), have 4096 (10000 octal, 1000 hexadecimal) distinct combinations. Hence, a microprocessor with 12-bit memory addresses can directly access 4096 words (4 Kw) of word-addressable memory. At a time when six-bit character codes were common a 12-bit word, which could hold two characters, was a convenient size. IBM System/360 instruction formats use a 12-bit displacement field which, added to the contents of a base register, can address 4096 bytes of memory.
List of 12-bit computer systems

    Digital Equipment Corporation
        PDP-5
        PDP-8
            DECmate, a personal computer based on the Intersil 6100
        PDP-12
        PDP-14
    Intersil IM6100 microprocessor (PDP-8-compatible)
    Control Data Corporation
        CDC 6600 - Peripheral Processor (PP)
        CDC 160 series computers
    National Cash Register NCR 315
    Scientific Data Systems SDS 92
    Ford Motor Company EEC I Automotive engine control unit
    PC12 minicomputer
    Ferranti Argus
    LINC, later commercialized by DEC as the LINC-8
    Electronic Arrays 9002 (12-bit addressing but 8-bit byte)
		if WikIDSelect == 20006:
In computer architecture, 16-bit integers, memory addresses, or other data units are those that are 16 bits (2 octets) wide. Also, 16-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size. 16-bit microcomputers are computers in which 16-bit microprocessors were the norm.

A 16-bit register can store 216 different values. The signed range of integer values that can be stored in 16 bits is −32,768 (−1 × 215) through 32,767 (215 − 1); the unsigned range is 0 through 65,535 (216 − 1). Since 216 is 65,536, a processor with 16-bit memory addresses can directly access 64 KB (65,536 bytes) of byte-addressable memory. If a system uses segmentation with 16-bit segment offsets, more can be accessed.
Contents

    1 16-bit architecture
        1.1 16/32-bit Motorola 68000 and Intel 386SX
    2 Intel 16-bit memory models
    3 16-bit application
    4 List of 16-bit CPUs
    5 See also
    6 References

16-bit architecture

The MIT Whirlwind (c. 1951)[1][2] was quite possibly the first-ever 16-bit computer. Other early (c. 1965–70) 16-bit computers include the IBM 1130,[3] the HP 2100,[4] the Data General Nova,[5] and the DEC PDP-11.[6] Early (c. 1973–75) multi-chip 16-bit microprocessors include the National Semiconductor IMP-16 and the Western Digital MCP-1600. Early (c. 1975–76) single-chip 16-bit microprocessors include the Panafacom MN1610,[7][8] National Semiconductor PACE, the HP BPC, and the TI TMS9900. Other notable 16-bit processors include the Intel 8086, the Intel 80286, the WDC 65C816, and the Zilog Z8000. The Intel 8088 was binary compatible with the Intel 8086, and was 16-bit in that its registers were 16 bits wide, and arithmetic instructions could operate on 16-bit quantities, even though its external bus was 8 bits wide.

A 16-bit integer can store 216 (or 65,536) distinct values. In an unsigned representation, these values are the integers between 0 and 65,535; using two's complement, possible values range from −32,768 to 32,767. Hence, a processor with 16-bit memory addresses can directly access 64 KB of byte-addressable memory.

16-bit processors have been almost entirely supplanted in the personal computer industry, and are used less than 32-bit (or 8-bit) CPUs in embedded applications.
16/32-bit Motorola 68000 and Intel 386SX

The Motorola 68000 is sometimes called 16-bit because its internal and external data buses were 16 bits wide; however, it could be considered a 32-bit processor in that the general purpose registers were 32 bits wide and most arithmetic instructions supported 32-bit arithmetic. The 68000 was a microcoded processor with three internal 16-bit ALUs. Only 24 bits of the program counter (PC) were available on original DIP packages, with up to 16 megabytes of addressable RAM. 68000 software is 32-bit in nature and forward-compatible with other 32-bit processors in the same family.[9] The 68008 was a version of the 68000 with 8-bit external data path and 1 megabyte addressing for the 48-pin DIP version and 4 megabyte for the 52-pin PLCC version. Several Apple Inc. Macintosh models; e.g., LC series, used 32-bit 68020 and 68030 processors on a 16-bit data bus to save cost.

Similar analysis applies to Intel's 80286 CPU replacement called the 386SX which is a 32-bit processor with 32-bit ALU and internal 32-bit data paths with a 16-bit external bus and 24-bit addressing of the processor it replaced.
Intel 16-bit memory models
Main article: Intel Memory Model
	
This article may be confusing or unclear to readers. Please help us clarify the article. There might be a discussion about this on the talk page. (August 2017) (Learn how and when to remove this template message)

Just as there are multiple data models for 64-bit architectures, the 16-bit Intel architecture allows for different memory models—ways to access a particular memory location. The reason for using a specific memory model is the size of the assembler instructions or required storage for pointers. Compilers of the 16-bit era generally had the following type-width characteristic:
16-bit data model Data model 	short 	int 	long 	Pointers
IP16L32 (near) 	16 	16 	32 	16
I16LP32 (far) 	16 	16 	32 	32

Tiny
    Code and data will be in the same segment (especially, the registers CS, DS, ES, SS will point to the same segment); near (16-bit) pointers are always used. Code, data and stack together cannot exceed 64 KB.
Small
    Code and data will be in different segments, and near pointers are always used. There will be 64 KB of space for code and 64 KB for data/stack.
Medium
    Code pointers will use far pointers (16:16 bit), enabling access to 1 MB. Data pointers remain to be of the near type.
Compact
    Data pointers will use far and code will use near pointers.
Large/huge
    Code and data pointers will be far.[10]

16-bit application

In the context of IBM PC compatible and Wintel platforms, a 16-bit application is any software written for MS-DOS, OS/2 1.x or early versions of Microsoft Windows which originally ran on the 16-bit Intel 8088 and Intel 80286 microprocessors. Such applications used a 20-bit or 24-bit segment or selector-offset address representation to extend the range of addressable memory locations beyond what was possible using only 16-bit addresses. Programs containing more than 216 bytes (65,536 bytes) of instructions and data therefore required special instructions to switch between their 64-kilobyte segments, increasing the complexity of programming 16-bit applications.
List of 16-bit CPUs
This list is incomplete; you can help by expanding it.

    Angstrem
        1801 series CPU
    Data General
        Nova
        Eclipse
    Digital Equipment Corporation
        PDP-11 (for LSI-11, see Western Digital, below)
            DEC J-11
            DEC T-11
    EnSilica
        eSi-1600
    Ferranti
        Ferranti F100-L
        Ferranti F200-L
    Freescale
        Freescale 68HC12
        Freescale 68HC16
    General Instrument
        CP1600
    Hewlett-Packard
        HP 21xx/2000/1000/98xx/BPC
        HP 3000
    Honeywell
        Honeywell Level 6/DPS 6
    IBM
        1130/1800
        System/7
        Series/1
        System/36
    Infineon
        XE166 family
        C166 family
        C167 family
        XC2000
    Intel
        Intel 8086/Intel 8088
        Intel 80186/Intel 80188
        Intel 80286
        Intel MCS-96
    Lockheed
        MAC-16
    Motorola
        Motorola 68000 (32-bit registers, 16-bit bus)
        Motorola 68010 (32-bit registers, 16-bit bus)
    National Semiconductor
        IMP-16
        PACE/INS8900
    NEC
        V20/V30
    Renesas
        Renesas M16C (16-bit registers, 24-bit address space)
    Ricoh
        Ricoh 5A22 (WDC 65816 clone used in SNES)
    Texas Instruments
        Texas Instruments TMS9900
        TI MSP430
    Western Design Center
        WDC 65816/65802
    Western Digital
        MCP-1600 (used in the DEC LSI-11)
    Xerox
        Alto
    Zilog
        Zilog Z8000


			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20007:
In computer architecture, 18-bit integers, memory addresses, or other data units are those that are 18 bits (2.25 octets) wide. Also, 18-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.

18 binary digits have 262144 (1000000 octal, 40000 hexadecimal) distinct combinations.

18 bits was a common word size for smaller computers in the 1960s, when large computers often used 36 bit words and 6-bit character sets were the norm.
Example computer architectures

Possibly the most well-known 18-bit computer architectures are the PDP-1, PDP-4, PDP-7, PDP-9 and PDP-15 minicomputers produced by Digital Equipment Corporation from 1960 to 1975.

The UNIVAC produced several 18-bit computers, including the UNIVAC 418 and several military systems.

The IBM 7700 Data Acquisition System was announced by IBM on December 2, 1963.

The BCL Molecular 18 was a group of systems designed and manufactured in the UK in the 1970s and 1980s.

The NASA Standard Spacecraft Computer NSSC-1 was developed as a standard component for the MultiMission Modular Spacecraft at the Goddard Space Flight Center (GSFC) in 1974.

The flying-spot store digital memory in the first experimental electronic switching systems used nine plates of optical memory that were read and written two bits at a time, producing a word size of 18 bits.
Character encoding

18-bit machines use a variety of character encodings.

The DEC Radix-50, called Radix 508 format, packs three characters plus two bits in each 18-bit word.[1]

The Teletype packs three characters in each 18-bit word; each character a 5-bit Baudot code and an upper-case bit.[2]

The DEC SIXBIT format packs three characters in each 18-bit word,[2] each 6-bit character obtained by stripping the high bits from the 7-bit ASCII code, which folds lowercase to uppercase letters. 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20008:
In computer architecture, 24-bit integers, memory addresses, or other data units are those that are 24 bits (3 octets) wide. Also, 24-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.

Notable 24-bit machines include the CDC 924 – a 24-bit version of the CDC 1604, CDC lower 3000 series, SDS 930 and SDS 940, the ICT 1900 series, and the Datacraft minicomputers/Harris H series.[1]

The term SWORD is sometimes used to describe a 24-bit data type with the S prefix referring to sesqui.[citation needed]

The IBM System/360, announced in 1964, was a popular computer system with 24-bit addressing and 32-bit general registers and arithmetic. The early 1980s saw the first popular personal computers, including the IBM PC/AT with an Intel 80286 processor using 24-bit addressing and 16-bit general registers and arithmetic, and the Apple Macintosh 128K with a Motorola 68000 processor featuring 24-bit addressing and 32-bit registers.

The eZ80 is a microprocessor and microcontroller family, with 24-bit registers and therefore 24-bit linear addressing, that is binary compatible with the 8/16-bit Z80.[citation needed]

The 65816 is a microprocessor and microcontroller family with 16-bit registers and 24-bit bank switched addressing. It is binary compatible with the 8-bit 6502.[2]

The range of unsigned integers that can be represented in 24 bits is 0 to 16,777,215 (FFFFFF16 in hexadecimal). The range of signed integers that can be represented in 24 bits is −8,388,608 to 8,388,607.

Several fixed-point digital signal processors have a 24-bit data bus, selected as the basic word length because it gave the system a reasonable precision for the processing audio (sound). In particular, the Motorola 56000 series has three parallel 24-bit data buses, one connected to each memory space: program memory, data memory X, and data memory Y.[3]

Engineering Research Associates (later merged into UNIVAC) designed a series of 24-bit drum memory machines including the Atlas, its commercial version the UNIVAC 1101, the ATHENA computer, the UNIVAC 1824 guidance computer, etc. Those designers selected a 24-bit word length because the Earth is roughly 40 million feet in diameter, and an intercontinental ballistic missile guidance computer needs to do the Earth-centered inertial navigation calculations to an accuracy of a few feet.[4][not in citation given] 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20009:
In computer architecture, 26-bit integers, memory addresses, or other data units are those that are 26 bits wide, and thus can represent values up to 64 mega (base 2). Two examples of computer processors that featured 26-bit memory addressing are certain second generation IBM System/370 mainframe computer models introduced in 1981 (and several subsequent models), which had 26-bit physical addresses but had only the same 24-bit virtual addresses as earlier models, and the first generations of ARM processors.
Contents

    1 History
        1.1 IBM System/370
        1.2 Early ARM processors
    2 External links

History
IBM System/370

As data processing needs continued to grow, IBM and their customers faced challenges directly addressing larger memory sizes. In what ended up being a short-term ''emergency'' solution, a pair of IBM's second wave of System/370 models, the 3033 and 3081, introduced 26-bit real memory addressing, increasing the System/370's amount of physical memory that could be attached by a factor of 4 from the previous 24-bit limit of 16 MB. IBM referred to 26-bit addressing as ''extended real addressing,'' and some subsequent models also included 26-bit support. However, only 2 years later, IBM introduced 31-bit memory addressing, expanding both physical and virtual addresses to 31 bits, with its System/370-XA models, and even the popular 3081 was upgradeable to XA standard.

Given 26-bit's brief history as the state-of-the-art in memory addressing available in IBM's model range, and given that virtual addresses were still limited to 24 bits, software exploitation of 26-bit mode was limited. The few customers that exploited 26-bit mode eventually adjusted their applications to support 31-bit addressing,[citation needed] and IBM dropped support for 26-bit mode after several years producing models supporting 24-bit, 26-bit, and 31-bit modes. The 26-bit mode is the only addressing mode that IBM removed from its line of mainframe computers descended from the System/360. All the other addressing modes, including now 64-bit mode, are supported in current model mainframes.
Early ARM processors

In the ARM processor architecture, 26-bit refers to the design used in the original ARM processors where the Program Counter (PC) and Processor Status Register (PSR) were combined into one 32-bit register (R15), the status flags filling the high 6 bits and the Program Counter taking up the lower 26 bits.

In fact, because the program counter is always word-aligned the lowest two bits are always zero which allowed the designers to reuse these two bits to hold the processor's mode bits too. The four modes allowed were USR26, SVC26, IRQ26, FIQ26; contrast this with the 32 possible modes available when the program status was separated from the program counter in more recent ARM architectures.

This design enabled more efficient program execution, as the Program Counter and status flags could be saved and restored with a single operation. This resulted in faster subroutine calls and interrupt response than traditional designs, which would have to do two register loads or saves when calling or returning from a subroutine.

Despite having a 32-bit ALU and word-length, processors based on ARM architecture version 1 and 2 had only a 26-bit PC and address bus, and were consequently limited to 64 MiB of addressable memory. This was still a vast amount of memory at the time, but because of this limitation, architectures since have included various steps away from the original 26-bit design.

The ARM architecture version 3 introduced a 32-bit PC and separate PSR, as well as a 32-bit address bus, allowing 4 GiB of memory to be addressed. The change in the PC/PSR layout caused incompatibility with code written for previous architectures, so the processor also included a 26-bit compatibility mode which used the old PC/PSR combination. The processor could still address 4 GB in this mode, but could not execute anything above address 0x3FFFFFC (64 MB). This mode was used by RISC OS running on the Acorn Risc PC to utilise the new processors while retaining compatibility with existing software.

ARM architecture version 4 made the support of the 26-bit addressing modes optional, and ARM architecture version 5 onwards has removed them entirely. 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20010:
In computer architecture, 31-bit integers, memory addresses, or other data units are those that are 31 bits wide.

In 1983, IBM introduced 31-bit addressing in the System/370-XA mainframe architecture as an upgrade to the 24-bit physical and virtual,[1] and transitional 24-bit-virtual/26-bit physical,[2][3] addressing of earlier models.[4][5] This enhancement allowed address spaces to be 128 times larger, permitting programs to address memory above 16 MB (referred to as ''above the line'').[6][1] Support for COBOL, FORTRAN and later on Linux/390 were included.
Contents

    1 Architecture
    2 Transition
    3 370/ESA architecture
    4 z/Architecture
    5 Linux/390
    6 References

Architecture

In the System/360, other than the 360/67, and early System/370 architectures, the general purpose registers were 32 bits wide, the machine did 32-bit arithmetic operations, and addresses were always stored in 32-bit words, so the architecture was considered 32-bit, but the machines ignored the top 8 bits of the address resulting in 24-bit addressing. With the XA extension, only the high order bit (bit 0) in the word was ignored for addressing. An exception is that mode-switching instructions also used bit 0. There were at least two reasons that IBM did not implement the 32-bit addressing of the 360/67

    The loop control instructions BXH and BXLE did signed comparisons.
    Much of the existing software used bit 0 as an end-of-list indicator.[7]

Transition

The transition was tricky: assembly language programmers, including IBM's own operating systems architects and developers, had been using the spare byte at the top of addresses for flags for almost twenty years.[8] IBM chose to provide two forms of addressing to minimize the pain: if the most significant bit (bit 0) of a 32-bit address was on, the next 31 bits were interpreted as the virtual address. If the most significant bit was off, then only the lower 24 bits were treated as the virtual address (just as with pre-XA systems). Thus programs could continue using the seven low-order bits of the top byte for other purposes as long as they left the top bit off. The only programs requiring modification were those that set the top (leftmost) bit of a word containing an address. This also affected address comparisons: The leftmost bit of a word is also interpreted as a sign-bit in 2's complement arithmetic, indicating a negative number if bit 0 is on. Programs that use signed arithmetic comparison instructions could get reversed results. Two equivalent addresses could be compared as non-equal if one of them had the sign bit turned on even if the remaining bits were identical. Most of this was invisible to programmers using high-level languages like COBOL[9] or FORTRAN,[3][10] and IBM aided the transition with dual mode hardware for a period of time.

Certain machine instructions in this 31-bit addressing mode alter the addressing mode bit as a possibly intentional side effect. For example, the original subroutine call instructions BAL, Branch and Link, and its register-register equivalent, BALR, Branch and Link Register, store certain status information, the instruction length code,[11] the condition code and the program mask, in the top byte of the return address. A BAS, Branch and Store, instruction was added to allow 31-bit return addresses. BAS, and its register-register equivalent, BASR, Branch and Store Register, was part of the instruction set of the System/360 Model 67, which was the only System/360 model to allow addresses longer than 24 bits. These instructions were maintained, but were modified and extended for 31-bit addressing.

Additional instructions in support of 24/31-bit addressing include two new register-register call/return instructions which also effect an addressing mode change (e.g. Branch and Save and Set Mode, BASSM,[12] the 24/31 bit version of a call where the linkage address including the mode is saved and a branch is taken to an address in a possibly different mode, and BSM, Branch and Set Mode, the 24/31 bit version of a return, where the return is directly to the previously saved linkage address and in its previous mode). Taken together, BASSM and BSM allow 24-bit calls to 31-bit (and return to 24-bit), 31-bit calls to 24-bit (and return to 31-bit), 24-bit calls to 24-bit (and return to 24-bit) and 31-bit calls to 31-bit (and return to 31-bit).

Like BALR 14,15 (the 24-bit-only form of a call), BASSM is used as BASSM 14,15, where the linkage address and mode are saved in register 14, and a branch is taken to the subroutine address and mode specified in register 15. Somewhat similarly to BCR 15,14 (the 24-bit-only form of an unconditional return), BSM is used as BSM 0,14, where 0 indicates that the current mode is not saved (the program is leaving the subroutine, anyway), and a return to the caller at the address and mode specified in register 14 is to be taken. Refer to IBM publication MVS/Extended Architecture System Programming Library: 31-Bit Addressing, GC28-1158-1, for extensive examples of the use of BAS, BASR, BASSM and BSM, in particular, pp. 29–30.
370/ESA architecture

In the 1990s IBM introduced 370/ESA architecture (later named 390/ESA and finally ESA/390 or System/390, in short S/390), completing the evolution to full 31-bit virtual addressing and keeping this addressing mode flag. These later architectures allow more than 2 GB of physical memory and allow multiple concurrent address spaces up to 2 GB each in size. As of mid-2006 there were too many programs unduly constrained by this multiple 31-bit addressing mode.[citation needed]
z/Architecture

IBM broke the 2 GB linear addressing barrier (''the bar'') in 2000 with the introduction of the first 64-bit z/Architecture system, the IBM zSeries Model 900.[1][13] Unlike the XA transition, z/Architecture does not reserve a top bit to identify earlier code. z/Architecture maintains compatibility with 24-bit and 31-bit code, even older code running concurrently with newer 64-bit code.
Linux/390

Since Linux/390 was first released for the existing 32-bit data/31-bit addressing hardware in 1999, initial mainframe Linux applications compiled in pre-z/Architecture mode are also limited to 31-bit addressing. This limitation disappeared with 64-bit hardware, 64-bit Linux on z Systems, and 64-bit Linux applications. The 64-bit Linux distributions still run 32-bit data/31-bit addressing programs. IBM's 31-bit addressing allows 31-bit code to make use of additional memory. However, at any one instant, a maximum of 2 GB is in each working address space. For non-64-bit Linux on processors with 31-bit addressing, it is possible to assign memory above the 2 GB bar as a RAM disk. 31-bit Linux kernel (not user-space) support was removed in version 4.1.[14] 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20011:
In computer architecture, 32-bit integers, memory addresses, or other data units are those that are 32 bits (4 octets) wide. Also, 32-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size. 32-bit microcomputers are computers in which 32-bit microprocessors are the norm.
Contents

    1 Range for storing integers
    2 Technical history
    3 Architectures
    4 Applications
    5 Images
    6 File formats
    7 See also
    8 References
    9 External links

Range for storing integers

A 32-bit register can store 232 different values. The range of integer values that can be stored in 32 bits depends on the integer representation used. With the two most common representations, the range is 0 through 4,294,967,295 (232 − 1) for representation as an (unsigned) binary number, and −2,147,483,648 (−231) through 2,147,483,647 (231 − 1) for representation as two's complement.

One important consequence is that a processor with 32-bit memory addresses can directly access at most 4 GiB of byte-addressable memory (though in practice the limit may be lower).
Technical history

Memory, as well as other digital circuits and wiring, was expensive during the first decades of 32-bit architectures (the 1960s to the 1980s).[1] Older 32-bit processor families (or simpler, cheaper variants thereof) could therefore have many compromises and limitations in order to cut costs. This could be a 16-bit ALU, for instance, or external (or internal) buses narrower than 32 bits, limiting memory size or demanding more cycles for instruction fetch, execution or write back.

Despite this, such processors could be labeled ''32-bit,'' since they still had 32-bit registers and instructions able to manipulate 32-bit quantities. For example, the original Motorola 68000 had a 16-bit data ALU and a 16-bit external data bus, but had 32-bit registers and a 32-bit based instruction set. Such designs were sometimes referred to as ''16/32-bit''.[2]

However, the opposite is often true for newer 32-bit designs. For example, the Pentium Pro processor is a 32-bit machine, with 32-bit registers and instructions that manipulate 32-bit quantities, but the external address bus is 36 bits wide, giving a larger address space than 4 GB, and the external data bus is 64 bits wide, primarily in order to permit a more efficient prefetch of instructions and data.[3]
Architectures

Prominent 32-bit instruction set architectures used in general-purpose computing include the IBM System/360 and IBM System/370 (which had 24-bit addressing) and the System/370-XA, ESA/370, and ESA/390 (which had 31-bit addressing), the DEC VAX, the NS320xx, the Motorola 68000 family (the first two models of which had 24-bit addressing), the Intel IA-32 32-bit version of the x86 architecture, and the 32-bit versions of the ARM,[4] SPARC, MIPS, PowerPC and PA-RISC architectures. 32-bit instruction set architectures used for embedded computing include the 68000 family and ColdFire, x86, ARM, MIPS, PowerPC, and Infineon TriCore architectures.
Applications

On the x86 architecture, a 32-bit application normally means software that typically (not necessarily) uses the 32-bit linear address space (or flat memory model) possible with the 80386 and later chips. In this context, the term came about because DOS, Microsoft Windows and OS/2[5] were originally written for the 8088/8086 or 80286, 16-bit microprocessors with a segmented address space where programs had to switch between segments to reach more than 64 kilobytes of code or data. As this is quite time-consuming in comparison to other machine operations, the performance may suffer. Furthermore, programming with segments tend to become complicated; special far and near keywords or memory models had to be used (with care), not only in assembly language but also in high level languages such as Pascal, compiled BASIC, Fortran, C, etc.

The 80386 and its successors fully support the 16-bit segments of the 80286 but also segments for 32-bit address offsets (using the new 32-bit width of the main registers). If the base address of all 32-bit segments is set to 0, and segment registers are not used explicitly, the segmentation can be forgotten and the processor appears as having a simple linear 32-bit address space. Operating systems like Windows or OS/2 provide the possibility to run 16-bit (segmented) programs as well as 32-bit programs. The former possibility exists for backward compatibility and the latter is usually meant to be used for new software development.
Images

In digital images/pictures, 32-bit usually refers to RGBA color space; that is, 24-bit truecolor images with an additional 8-bit alpha channel. Other image formats also specify 32 bits per pixel, such as RGBE.

In digital images, 32-bit sometimes refers to high-dynamic-range imaging (HDR) formats that use 32 bits per channel, a total of 96 bits per pixel. 32-bit-per-channel images are used to represent values brighter than what sRGB color space allows (brighter than white); these values can then be used to more accurately retain bright highlights when either lowering the exposure of the image or when it is seen through a dark filter or dull reflection.

For example, a reflection in an oil slick is only a fraction of that seen in a mirror surface. HDR imagery allows for the reflection of highlights that can still be seen as bright white areas, instead of dull grey shapes.
File formats
A 32-bit file format is a binary file format for which each elementary information is defined on 32 bits (or 4 bytes). An example of such a format is the Enhanced Metafile Format. 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20012:
In computer architecture, 36-bit integers, memory addresses, or other data units are those that are 36 bits (six six-bit characters) wide. Also, 36-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.

Prior to the introduction of computers, the state of the art in precision scientific and engineering calculation was the ten-digit, electrically powered, mechanical calculator, such as those manufactured by Friden, Marchant and Monroe. These calculators had a column of keys for each digit, and operators were trained to use all their fingers when entering numbers, so while some specialized calculators had more columns, ten was a practical limit. Computers, as the new competitor, had to match that accuracy. Decimal computers sold in that era, such as the IBM 650 and the IBM 7070, had a word length of ten digits, as did ENIAC, one of the earliest computers.

Early binary computers aimed at the same market therefore often used a 36-bit word length. This was long enough to represent positive and negative integers to an accuracy of ten decimal digits (35 bits would have been the minimum). It also allowed the storage of six alphanumeric characters encoded in a six-bit character code. Computers with 36-bit words included the MIT Lincoln Laboratory TX-2, the IBM 701/704/709/7090/7094, the UNIVAC 1103/1103A/1105 and 1100/2200 series, the General Electric GE-600/Honeywell 6000, the Digital Equipment Corporation PDP-6/PDP-10 (as used in the DECsystem-10/DECSYSTEM-20), and the Symbolics 3600 series.

Smaller machines like the PDP-1/PDP-9/PDP-15 used 18-bit words, so a double word was 36 bits.

These computers had addresses 15 to 18 bits in length. The addresses referred to 36-bit words, so the computers were limited to addressing between 32768 and 262144 words (196608 to 1572864 six-bit characters). The older 36-bit computers were limited to a similar amount of physical memory as well. Architectures that survived evolved over time to support larger virtual address spaces using memory segmentation or other mechanisms.

The common character packings included:

    six 5.32-bit DEC Radix-50 characters, plus four spare bits
    six 6-bit Fieldata or IBM BCD characters (ubiquitous in early usage)
    six 6-bit ASCII characters, supporting the upper-case unaccented letters, digits, space, and most ASCII punctuation characters. It was used on the PDP-6 and PDP-10 under the name sixbit.
    five 7-bit characters and 1 unused bit (the usual PDP-6/10 convention, called five-seven ASCII)[1][2]
    four 8-bit characters (7-bit ASCII plus 1 spare bit, or 8-bit EBCDIC), plus four spare bits
    four 9-bit characters[1][2] (the Multics convention).

Characters were extracted from words either using machine code shift and mask operations or with special-purpose hardware supporting 6-bit, 9-bit, or variable-length characters. The Univac 1100/2200 used the partial word designator of the instruction, the ''J'' field, to access characters. The GE-600 used special indirect words to access 6- and 9-bit characters. the PDP-6/10 had special instructions to access arbitrary-length byte fields.

The standard C programming language requires that the size of the char data type be at least 8 bits,[3] and that all data types other than bitfields have a size that is a multiple of the character size,[4] so standard C implementations on 36-bit machines would typically use 9-bit chars, although 12-bit, 18-bit, or 36-bit would also satisfy the requirements of the standard.[5]

By the time IBM introduced System/360, scientific calculations had shifted to floating point and mechanical calculators were no longer a competitor. The 360s also included instructions for variable length decimal arithmetic for commercial applications, so the practice of using word lengths that were a power of two quickly became commonplace, though some 36-bit computer systems are still sold as of 2014, e.g., the Unisys ClearPath Dorado series, which is the continuation of the UNIVAC 1100/2200 series of mainframe computers.

CompuServe was launched using 36-bit PDP-10 computers in the late 1960s. It continued using PDP-10 and DECSYSTEM-10-compatible hardware and retired the service in the late 2000s.
Other uses in electronics

The LatticeECP3 FPGAs from Lattice Semiconductor include multiplier slices that can be configured to support the multiplication of two 36-bit numbers.[6] The DSP block in Altera Stratix FPGAs can do 36-bit additions and multiplications.[7] 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20013:
In computer architecture, 48-bit integers can represent 281,474,976,710,656 (248 or 2.814749767×1014) discrete values. This allows an unsigned binary integer range of 0 through 281,474,976,710,655 (248 − 1) or a signed two's complement range of -140,737,488,355,328 (-247) through 140,737,488,355,327 (247 − 1). A 48-bit memory address can directly address every byte of 256 tebibytes of storage. 48-bit can refer to any other data unit that consumes 48 bits (6 octets) in width. Examples include 48-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.
Word size

Computers with 48-bit words include the AN/FSQ-32, CDC 1604/upper-3000 series, BESM-6, Ferranti Atlas, and Burroughs large systems (B5xxx-B8xxx, most of which additionally had a 3- or 4-bit type tag).
Addressing

The IBM System/38 and the AS/400, in its CISC variants, are 48-bit addressing systems. The address size used in logical block addressing was increased to 48 bits with the introduction of ATA-6. The Ext4 file system physically limits the file block count to 48 bits.

The minimal implementation of the x86-64 architecture provides 48-bit addressing encoded into 64 bits; future versions of the architecture can expand this without breaking properly written applications.

The media access control address (MAC address) of a computer uses a 48-bit address space. This can be changed to 64-bit addressing.
Images
See also: Deep color

In digital images, 48 bits per pixel, or 16 bits per each color channel (red, green and blue), is used for accurate processing. For the human eye, it is almost impossible to see any difference between such an image and a 24-bit image,[citation needed] but the existence of more shades of each of the three primary colors (65,536 as opposed to 256) means that more operations can be performed on the image without risk of noticeable banding or posterization.

    vte

Processor technologies
Models	

    Turing machine
        Universal Post–Turing Quantum Belt machine Stack machine Finite-state machine
        with datapath Hierarchical Queue automaton Register machines
        Counter Pointer Random-access Random-access stored program

Architecture	

    Von Neumann Harvard
        modified Dataflow Transport-triggered Cellular Endianness Memory access
        NUMA HUMA Load/store Register/memory Cache hierarchy Memory hierarchy
        Virtual memory Secondary storage Heterogeneous Fabric Multiprocessing Cognitive Neuromorphic

Instruction set
architectures	
Types	

    CISC RISC Application-specific EDGE
        TRIPS VLIW
        EPIC MISC OISC NISC ZISC comparison
        addressing modes

    x86 ARM MIPS Power
        PowerPC SPARC Itanium Unicore MicroBlaze RISC-V others

Execution	
Instruction pipelining	
Pipeline stall Operand forwarding Classic RISC pipeline
Hazards	

    Data dependency Structural Control False sharing

Out-of-order	

    Tomasulo algorithm
        Reservation station Re-order buffer Register renaming

Speculative	

    Branch prediction Memory dependence prediction

Parallelism	
Level	

    Bit
        Bit-serial Word Instruction Pipelining
        Scalar Superscalar Task
        Thread Process Data
        Vector Memory Distributed

Multithreading	

    Temporal Simultaneous
        Hyperthreading Speculative Preemptive Cooperative

Flynn's taxonomy	

    SISD SIMD
        SWAR SIMT MISD MIMD
        SPMD

Processor
Performance	

    Transistor count Instructions per cycle (IPC)
        Cycles per instruction (CPI) Instructions per second (IPS) Floating-point operations per second (FLOPS) Transactions per second (TPS) Synaptic updates per second (SUPS) Performance per watt (PPW) Cache performance metrics Computer performance by orders of magnitude

Types	

    Central processing unit (CPU) Graphics processing unit (GPU)
        GPGPU Vector Barrel Stream Coprocessor ASIC FPGA CPLD Multi-chip module (MCM) System in package (SiP)

By application	

    Microprocessor Microcontroller Mobile Notebook Ultra-low-voltage ASIP

Systems
on Chip	

    System-on-Chip (SoC) Multiprocessor (MPSoC) Programmable (PSoC) Network-on-Chip (NoC)

Hardware
accelerators	

    AI accelerator Vision processing unit (VPU) Physics processing unit (PPU) Digital signal processor (DSP) Tensor processing unit (TPU) Secure cryptoprocessor Network processor Baseband processor

Word size	

    1-bit 2-bit 4-bit 8-bit 16-bit 32-bit 48-bit 64-bit 128-bit 256-bit 512-bit others
        variable

Core count	

    Single-core Multi-core Manycore Heterogeneous architecture

Components	

    Core Cache
        CPU cache replacement policies coherence Bus Clock rate FIFO

Functional units	

    Arithmetic logic unt (ALU) Address generation unit (AGU) Floating-point unit (FPU) Memory management unit
        Load–store unit Translation lookaside buffer (TLB)

Logic	

    Combinational Sequential Glue Logic Gate
        Quantum Array

Registers	

    Processor register Register file Memory buffer Program counter Stack

Control unit	

    Instruction unit Data buffer Write buffer Microcode ROM Counter

Datapath	

    Multiplexer Demultiplexer Adder Multiplier
        CPU Binary decoder
        Address decoder Sum addressed decoder Barrel shifter

Circuitry	

    Integrated circuit
        3D Mixed signal Power management Boolean Digital Analog Quantum Switch

Power
management	

    PMU APM ACPI Dynamic frequency scaling Dynamic voltage scaling Clock gating Performance per watt (PPW)

Related	

    History of general-purpose CPUs Microprocessor chronology Processor design Digital electronics Hardware security module


			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20014:
			print (''In computer architecture, 60-bit integers, memory addresses, or other data units are those that are 60 bits wide. Also, '')
			print (''60-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.'')
			print ('' '')
			print (''Computers with 60-bit words include the CDC 6000 series, the CDC 7600, and some of the CDC Cyber series. '')
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20015:
In computer architecture, 64-bit computing is the use of processors that have datapath widths, integer size, and memory address widths of 64 bits (eight octets). Also, 64-bit computer architectures for central processing units (CPUs) and arithmetic logic units (ALUs) are those that are based on processor registers, address buses, or data buses of that size. From the software perspective, 64-bit computing means the use of code with 64-bit virtual memory addresses. However, not all 64-bit instruction sets support full 64-bit virtual memory addresses; x86-64 and ARMv8, for example, support only 48 bits of virtual address, with the remaining 16 bits of the virtual address required to be all 0's or all 1's, and several 64-bit instruction sets support fewer than 64 bits of physical memory address.

The term 64-bit describes a generation of computers in which 64-bit processors are the norm. 64 bits is a word size that defines certain classes of computer architecture, buses, memory and CPUs, and by extension the software that runs on them. 64-bit CPUs have been used in supercomputers since the 1970s (Cray-1, 1975) and in reduced instruction set computing (RISC) based workstations and servers since the early 1990s, notably the MIPS R4000, R8000, and R10000, the DEC Alpha, the Sun UltraSPARC, and the IBM RS64 and POWER3 and later POWER microprocessors. In 2003, 64-bit CPUs were introduced to the (formerly 32-bit) mainstream personal computer market in the form of x86-64 processors and the PowerPC G5, and were introduced in 2012[1] into the ARM architecture targeting smartphones and tablet computers, first sold on September 20, 2013, in the iPhone 5S powered by the ARMv8-A Apple A7 system on a chip (SoC).

A 64-bit register can store 264 (over 18 quintillion or 1.8×1019) different values. The range of integer values that can be stored in 64 bits depends on the integer representation used. With the two most common representations, the range is 0 through 18,446,744,073,709,551,615 (264 − 1) for representation as an (unsigned) binary number, and −9,223,372,036,854,775,808 (−263) through 9,223,372,036,854,775,807 (263 − 1) for representation as two's complement. Hence, a processor with 64-bit memory addresses can directly access 264 bytes (=16 exabytes) of byte-addressable memory.

With no further qualification, a 64-bit computer architecture generally has integer and addressing processor registers that are 64 bits wide, allowing direct support for 64-bit data types and addresses. However, a CPU might have external data buses or address buses with different sizes from the registers, even larger (the 32-bit Pentium had a 64-bit data bus, for instance[2]). The term may also refer to the size of low-level data types, such as 64-bit floating-point numbers.
Contents

    1 Architectural implications
    2 History
    3 Limits of processors
    4 64-bit data timeline
    5 64-bit address timeline
    6 64-bit operating system timeline
    7 64-bit applications
        7.1 32-bit vs 64-bit
        7.2 Pros and cons
        7.3 Software availability
    8 64-bit data models
    9 Current 64-bit architectures
    10 See also
    11 Notes
    12 References
    13 External links

Architectural implications

Processor registers are typically divided into several groups: integer, floating-point, single instruction, multiple data (SIMD), control, and often special registers for address arithmetic which may have various uses and names such as address, index, or base registers. However, in modern designs, these functions are often performed by more general purpose integer registers. In most processors, only integer or address-registers can be used to address data in memory; the other types of registers cannot. The size of these registers therefore normally limits the amount of directly addressable memory, even if there are registers, such as floating-point registers, that are wider.

Most high performance 32-bit and 64-bit processors (some notable exceptions are older or embedded ARM architecture (ARM) and 32-bit MIPS architecture (MIPS) CPUs) have integrated floating point hardware, which is often, but not always, based on 64-bit units of data. For example, although the x86/x87 architecture has instructions able to load and store 64-bit (and 32-bit) floating-point values in memory, the internal floating point data and register format is 80 bits wide, while the general-purpose registers are 32 bits wide. In contrast, the 64-bit Alpha family uses a 64-bit floating-point data and register format, and 64-bit integer registers.
History

Many computer instruction sets are designed so that a single integer register can store the memory address to any location in the computer's physical or virtual memory. Therefore, the total number of addresses to memory is often determined by the width of these registers. The IBM System/360 of the 1960s was an early 32-bit computer; it had 32-bit integer registers, although it only used the low order 24 bits of a word for addresses, resulting in a 16 MiB [16 × 10242 bytes] address space. 32-bit superminicomputers, such as the DEC VAX, became common in the 1970s, and 32-bit microprocessors, such as the Motorola 68000 family and the 32-bit members of the x86 family starting with the Intel 80386, appeared in the mid-1980s, making 32 bits something of a de facto consensus as a convenient register size.

A 32-bit address register meant that 232 addresses, or 4 GiB of random-access memory (RAM), could be referenced. When these architectures were devised, 4 GB of memory was so far beyond the typical amounts (4 MB) in installations, that this was considered to be enough headroom for addressing. 4.29 billion addresses were considered an appropriate size to work with for another important reason: 4.29 billion integers are enough to assign unique references to most entities in applications like databases.

Some supercomputer architectures of the 1970s and 1980s, such as the Cray-1,[3] used registers up to 64 bits wide, and supported 64-bit integer arithmetic, although they did not support 64-bit addressing. In the mid-1980s, Intel i860[4] development began culminating in a (too late[5] for Windows NT) 1989 release; the i860 had 32-bit integer registers and 32-bit addressing, so it was not a fully 64-bit processor, although its graphics unit supported 64-bit integer arithmetic.[6] However, 32 bits remained the norm until the early 1990s, when the continual reductions in the cost of memory led to installations with amounts of RAM approaching 4 GB, and the use of virtual memory spaces exceeding the 4 GB ceiling became desirable for handling certain types of problems. In response, MIPS and DEC developed 64-bit microprocessor architectures, initially for high-end workstation and server machines. By the mid-1990s, HAL Computer Systems, Sun Microsystems, IBM, Silicon Graphics, and Hewlett Packard had developed 64-bit architectures for their workstation and server systems. A notable exception to this trend were mainframes from IBM, which then used 32-bit data and 31-bit address sizes; the IBM mainframes did not include 64-bit processors until 2000. During the 1990s, several low-cost 64-bit microprocessors were used in consumer electronics and embedded applications. Notably, the Nintendo 64[7] and the PlayStation 2 had 64-bit microprocessors before their introduction in personal computers. High-end printers, network equipment, and industrial computers, also used 64-bit microprocessors, such as the Quantum Effect Devices R5000.[citation needed] 64-bit computing started to drift down to the personal computer desktop from 2003 onward, when some models in Apple's Macintosh lines switched to PowerPC 970 processors (termed G5 by Apple), and AMD released its first 64-bit x86-64 processor.
Limits of processors
	
This section needs additional citations for verification. Please help improve this article by adding citations to reliable sources. Unsourced material may be challenged and removed. (January 2010) (Learn how and when to remove this template message)

In principle, a 64-bit microprocessor can address 16 EiBs (16 × 10246 = 264 = 18,446,744,073,709,551,616 bytes, or about 18.4 exabytes) of memory. However, not all instruction sets, and not all processors implementing those instruction sets, support a full 64-bit virtual or physical address space.

The x86-64 architecture (as of 2016) allows 48 bits for virtual memory and, for any given processor, up to 52 bits for physical memory.[8][9] These limits allow memory sizes of 256 TiB (256 × 10244 bytes) and 4 PiB (4 × 10245 bytes), respectively. A PC cannot currently contain 4 pebibytes of memory (due to the physical size of the memory chips), but AMD envisioned large servers, shared memory clusters, and other uses of physical address space that might approach this in the foreseeable future. Thus the 52-bit physical address provides ample room for expansion while not incurring the cost of implementing full 64-bit physical addresses. Similarly, the 48-bit virtual address space was designed to provide more than 65,000 (216) times the 32-bit limit of 4 GiB (4 × 10243 bytes), allowing room for later expansion and incurring no overhead of translating full 64-bit addresses.

The Power ISA v3.0 allows 64 bits for an effective address, mapped to a segmented address with between 65 and 78 bits allowed, for virtual memory, and, for any given processor, up to 60 bits for physical memory.[10]

The Oracle SPARC Architecture 2015 allows 64 bits for virtual memory and, for any given processor, between 40 and 56 bits for physical memory.[11]

The ARM AArch64 Virtual Memory System Architecture allows 48 bits for virtual memory and, for any given processor, from 32 to 48 bits for physical memory.[12]
64-bit data timeline

1961
    IBM delivers the IBM 7030 Stretch supercomputer, which uses 64-bit data words and 32- or 64-bit instruction words.
1974
    Control Data Corporation launches the CDC Star-100 vector supercomputer, which uses a 64-bit word architecture (prior CDC systems were based on a 60-bit architecture).
    International Computers Limited launches the ICL 2900 Series with 32-bit, 64-bit, and 128-bit two's complement integers; 64-bit and 128-bit floating point; 32-bit, 64-bit, and 128-bit packed decimal and a 128-bit accumulator register. The architecture has survived through a succession of ICL and Fujitsu machines. The latest is the Fujitsu Supernova, which emulates the original environment on 64-bit Intel processors.
1976
    Cray Research delivers the first Cray-1 supercomputer, which is based on a 64-bit word architecture and will form the basis for later Cray vector supercomputers.
1983
    Elxsi launches the Elxsi 6400 parallel minisupercomputer. The Elxsi architecture has 64-bit data registers but a 32-bit address space.
1989
    Intel introduces the Intel i860 reduced instruction set computing (RISC) processor. Marketed as a ''64-Bit Microprocessor'', it had essentially a 32-bit architecture, enhanced with a 3D graphics unit capable of 64-bit integer operations.[13]
1993
    Atari introduces the Atari Jaguar video game console, which includes some 64-bit wide data paths in its architecture.[14]

64-bit address timeline

1991
    MIPS Computer Systems produces the first 64-bit microprocessor, the R4000, which implements the MIPS III architecture, the third revision of its MIPS architecture.[15] The CPU is used in SGI graphics workstations starting with the IRIS Crimson. Kendall Square Research deliver their first KSR1 supercomputer, based on a proprietary 64-bit RISC processor architecture running OSF/1.
1992
    Digital Equipment Corporation (DEC) introduces the pure 64-bit Alpha architecture which was born from the Prism project.[16]
1994
    Intel announces plans for the 64-bit IA-64 architecture (jointly developed with Hewlett-Packard) as a successor to its 32-bit IA-32 processors. A 1998 to 1999 launch date was targeted.
1995
    Sun launches a 64-bit SPARC processor, the UltraSPARC.[17] Fujitsu-owned HAL Computer Systems launches workstations based on a 64-bit CPU, HAL's independently designed first-generation SPARC64. IBM releases the A10 and A30 microprocessors, the first 64-bit PowerPC AS processors.[18] IBM also releases a 64-bit AS/400 system upgrade, which can convert the operating system, database and applications.
1996
    Nintendo introduces the Nintendo 64 video game console, built around a low-cost variant of the MIPS R4000. HP releases the first implementation of its 64-bit PA-RISC 2.0 architecture, the PA-8000.[19]
1998
    IBM releases the POWER3 line of full-64-bit PowerPC/POWER processors.[20]
1999
    Intel releases the instruction set for the IA-64 architecture. AMD publicly discloses its set of 64-bit extensions to IA-32, called x86-64 (later branded AMD64).
2000
    IBM ships its first 64-bit z/Architecture mainframe, the zSeries z900. z/Architecture is a 64-bit version of the 32-bit ESA/390 architecture, a descendant of the 32-bit System/360 architecture.
2001
    Intel ships its IA-64 processor line, after repeated delays in getting to market. Now branded Itanium and targeting high-end servers, sales fail to meet expectations.
2003
    AMD introduces its Opteron and Athlon 64 processor lines, based on its AMD64 architecture which is the first x86-based 64-bit processor architecture. Apple also ships the 64-bit ''G5'' PowerPC 970 CPU produced by IBM. Intel maintains that its Itanium chips would remain its only 64-bit processors.
2004
    Intel, reacting to the market success of AMD, admits it has been developing a clone of the AMD64 extensions named IA-32e (later renamed EM64T, then yet again renamed to Intel 64). Intel ships updated versions of its Xeon and Pentium 4 processor families supporting the new 64-bit instruction set.
    VIA Technologies announces the Isaiah 64-bit processor.[21]
2006
    Sony, IBM, and Toshiba begin manufacturing the 64-bit Cell processor for use in the PlayStation 3, servers, workstations, and other appliances. Intel released Core 2 Duo as the first mainstream x86-64 processor for its mobile, desktop, and workstation line. Prior 64-bit extension processor lines were not widely available in the consumer retail market (most of 64-bit Pentium 4/D were OEM), 64-bit Pentium 4, Pentium D, and Celeron were not into mass production until late 2006 due to poor yield issue (most of good yield wafers were targeted at server and mainframe while mainstream still remain 130 nm 32-bit processor line until 2006) and soon became low end after Core 2 debuted. AMD released their first 64-bit mobile processor and manufactured in 90 nm.
2011
    ARM Holdings announces ARMv8-A, the first 64-bit version of the ARM architecture.[22]
2012
    ARM Holdings announced their Cortex-A53 and Cortex-A57 cores, their first cores based on their 64-bit architecture, on 30 October 2012.[1][23]
2013
    Apple announces the iPhone 5S, the first 64‑bit smartphone, which uses their A7 ARMv8-A-based system-on-a-chip.
2014
    Google announces the Nexus 9, the first Android device to run on a 64-bit Tegra K1 processor.

64-bit operating system timeline

1985
    Cray releases UNICOS, the first 64-bit implementation of the Unix operating system.[24]
1993
    DEC releases the 64-bit DEC OSF/1 AXP Unix-like operating system (later renamed Tru64 UNIX) for its systems based on the Alpha architecture.
1994
    Support for the R8000 processor is added by Silicon Graphics to the IRIX operating system in release 6.0.
1995
    DEC releases OpenVMS 7.0, the first full 64-bit version of OpenVMS for Alpha. First 64-bit Linux distribution for the Alpha architecture is released.[25]
1996
    Support for the R4x00 processors in 64-bit mode is added by Silicon Graphics to the IRIX operating system in release 6.2.
1998
    Sun releases Solaris 7, with full 64-bit UltraSPARC support.
2000
    IBM releases z/OS, a 64-bit operating system descended from MVS, for the new zSeries 64-bit mainframes; 64-bit Linux on z Systems follows the CPU release almost immediately.
2001
    Linux becomes the first OS kernel to fully support x86-64 (on a simulator, as no x86-64 processors had been released yet).[26]
2001
    Microsoft releases Windows XP 64-Bit Edition for the Itanium's IA-64 architecture, although it was able to run 32-bit applications through an execution layer.
2003
    Apple releases its Mac OS X 10.3 ''Panther'' operating system which adds support for native 64-bit integer arithmetic on PowerPC 970 processors.[27] Several Linux distributions release with support for AMD64. FreeBSD releases with support for AMD64.
2005
    On January 4, Microsoft discontinues Windows XP 64-Bit Edition, as no PCs with IA-64 processors had been available since the previous September, and announces that it is developing x86-64 versions of Windows to replace it.[28] On January 31, Sun releases Solaris 10 with support for AMD64 and EM64T processors. On April 29, Apple releases Mac OS X 10.4 ''Tiger'' which provides limited support for 64-bit command-line applications on machines with PowerPC 970 processors; later versions for Intel-based Macs supported 64-bit command-line applications on Macs with EM64T processors. On April 30, Microsoft releases Windows XP Professional x64 Edition and Windows Server 2003 x64 Edition for AMD64 and EM64T processors.[29]
2006
    Microsoft releases Windows Vista, including a 64-bit version for AMD64/EM64T processors that retains 32-bit compatibility. In the 64-bit version, all Windows applications and components are 64-bit, although many also have their 32-bit versions included for compatibility with plug-ins.
2007
    Apple releases Mac OS X 10.5 ''Leopard'', which fully supports 64-bit applications on machines with PowerPC 970 or EM64T processors.
2009
    Microsoft releases Windows 7, which, like Windows Vista, includes a full 64-bit version for AMD64/Intel 64 processors; most new computers are loaded by default with a 64-bit version. It also releases Windows Server 2008 R2, which is the first 64-bit only operating system released by Microsoft. Apple releases Mac OS X 10.6, ''Snow Leopard'', which ships with a 64-bit kernel for AMD64/Intel64 processors, although only certain recent models of Apple computers will run the 64-bit kernel by default. Most applications bundled with Mac OS X 10.6 are now also 64-bit.[27]
2011
    Apple releases Mac OS X 10.7, ''Lion'', which runs the 64-bit kernel by default on supported machines. Older machines that are unable to run the 64-bit kernel run the 32-bit kernel, but, as with earlier releases, can still run 64-bit applications; Lion does not support machines with 32-bit processors. Nearly all applications bundled with Mac OS X 10.7 are now also 64-bit, including iTunes.
2013
    Apple releases iOS 7, which, on machines with AArch64 processors, has a 64-bit kernel that supports 64-bit applications.
2014
    Google releases Android Lollipop, the first version of the Android operating system with support for 64-bit processors.
2017
    Apple releases iOS 11, supporting only machines with AArch64 processors. It has a 64-bit kernel that only supports 64-bit applications. 32-bit applications are no longer compatible.

64-bit applications
32-bit vs 64-bit

A change from a 32-bit to a 64-bit architecture is a fundamental alteration, as most operating systems must be extensively modified to take advantage of the new architecture, because that software has to manage the actual memory addressing hardware.[30] Other software must also be ported to use the new abilities; older 32-bit software may be supported either by virtue of the 64-bit instruction set being a superset of the 32-bit instruction set, so that processors that support the 64-bit instruction set can also run code for the 32-bit instruction set, or through software emulation, or by the actual implementation of a 32-bit processor core within the 64-bit processor, as with some Itanium processors from Intel, which included an IA-32 processor core to run 32-bit x86 applications. The operating systems for those 64-bit architectures generally support both 32-bit and 64-bit applications.[31]

One significant exception to this is the AS/400, software for which is compiled into a virtual instruction set architecture (ISA) called Technology Independent Machine Interface (TIMI); TIMI code is then translated to native machine code by low-level software before being executed. The translation software is all that must be rewritten to move the full OS and all software to a new platform, as when IBM transitioned the native instruction set for AS/400 from the older 32/48-bit IMPI to the newer 64-bit PowerPC-AS, codenamed Amazon. The IMPI instruction set was quite different from even 32-bit PowerPC, so this transition was even bigger than moving a given instruction set from 32 to 64 bits.

On 64-bit hardware with x86-64 architecture (AMD64), most 32-bit operating systems and applications can run with no compatibility issues. While the larger address space of 64-bit architectures makes working with large data sets in applications such as digital video, scientific computing, and large databases easier, there has been considerable debate on whether they or their 32-bit compatibility modes will be faster than comparably priced 32-bit systems for other tasks.

A compiled Java program can run on a 32- or 64-bit Java virtual machine with no modification. The lengths and precision of all the built-in types, such as char, short, int, long, float, and double, and the types that can be used as array indices, are specified by the standard and are not dependent on the underlying architecture. Java programs that run on a 64-bit Java virtual machine have access to a larger address space.[32]

Speed is not the only factor to consider in comparing 32-bit and 64-bit processors. Applications such as multi-tasking, stress testing, and clustering – for high-performance computing (HPC) – may be more suited to a 64-bit architecture when deployed appropriately. For this reason, 64-bit clusters have been widely deployed in large organizations, such as IBM, HP, and Microsoft.

Summary:

    A 64-bit processor performs best with 64-bit software.
    A 64-bit processor has backward compatibility and will handle most 32-bit software.
    A 32-bit processor is incompatible with 64-bit software.

Pros and cons

A common misconception is that 64-bit architectures are no better than 32-bit architectures unless the computer has more than 4 GiB of random-access memory.[33] This is not entirely true:

    Some operating systems and certain hardware configurations limit the physical memory space to 3 GiB on IA-32 systems, due to much of the 3–4 GiB region being reserved for hardware addressing; see 3 GB barrier; 64-bit architectures can address far more than 4 GiB. However, IA-32 processors from the Pentium Pro onward allow a 36-bit physical memory address space, using Physical Address Extension (PAE), which gives a 64 GiB physical address range, of which up to 62 GiB may be used by main memory; operating systems that support PAE may not be limited to 4 GiB of physical memory, even on IA-32 processors. However, drivers and other kernel mode software, more so older versions, may be incompatible with PAE; this has been cited as the reason for 32-bit versions of Microsoft Windows being limited to 4 GiB of physical RAM[34] (although the validity of this explanation has been disputed[35]).
    Some operating systems reserve portions of process address space for OS use, effectively reducing the total address space available for mapping memory for user programs. For instance, 32-bit Windows reserves 1 or 2 GiB (depending on the settings) of the total address space for the kernel, which leaves only 3 or 2 GiB (respectively) of the address space available for user mode. This limit is much higher on 64-bit operating systems.
    Memory-mapped files are becoming more difficult to implement in 32-bit architectures as files of over 4 GiB become more common; such large files cannot be memory-mapped easily to 32-bit architectures, as only part of the file can be mapped into the address space at a time, and to access such a file by memory mapping, the parts mapped must be swapped into and out of the address space as needed. This is a problem, as memory mapping, if properly implemented by the OS, is one of the most efficient disk-to-memory methods.
    Some 64-bit programs, such as encoders, decoders and encryption software, can benefit greatly from 64-bit registers,[citation needed] while the performance of other programs, such as 3D graphics-oriented ones, remains unaffected when switching from a 32-bit to a 64-bit environment.[citation needed]
    Some 64-bit architectures, such as x86-64, support more general-purpose registers than their 32-bit counterparts (although this is not due specifically to the word length). This leads to a significant speed increase for tight loops since the processor does not have to fetch data from the cache or main memory if the data can fit in the available registers.

    Example in C:

int a, b, c, d, e;
for (a=0; a<100; a++)
{
  b = a;
  c = b;
  d = c;
  e = d;
}

    If a processor only has the ability to keep two or three values or variables in registers, it would need to move some values between memory and registers to be able to process variables d and e also; this is a process that takes many CPU cycles. A processor that is able to hold all values and variables in registers can loop through them with no need to move data between registers and memory for each iteration. This behavior can easily be compared with virtual memory, although any effects are contingent on the compiler.

The main disadvantage of 64-bit architectures is that, relative to 32-bit architectures, the same data occupies more space in memory (due to longer pointers and possibly other types, and alignment padding). This increases the memory requirements of a given process and can have implications for efficient processor cache use. Maintaining a partial 32-bit model is one way to handle this, and is in general reasonably effective. For example, the z/OS operating system takes this approach, requiring program code to reside in 31-bit address spaces (the high order bit is not used in address calculation on the underlying hardware platform) while data objects can optionally reside in 64-bit regions. Not all such applications require a large address space or manipulate 64-bit data items, so these applications do not benefit from these features.
Software availability

x86-based 64-bit systems sometimes lack equivalents of software that is written for 32-bit architectures. The most severe problem in Microsoft Windows is incompatible device drivers for obsolete hardware. Most 32-bit application software can run on a 64-bit operating system in a compatibility mode, also termed an emulation mode, e.g., Microsoft WoW64 Technology for IA-64 and AMD64. The 64-bit Windows Native Mode[36] driver environment runs atop 64-bit NTDLL.DLL, which cannot call 32-bit Win32 subsystem code (often devices whose actual hardware function is emulated in user mode software, like Winprinters). Because 64-bit drivers for most devices were unavailable until early 2007 (Vista x64), using a 64-bit version of Windows was considered a challenge. However, the trend has since moved toward 64-bit computing, more so as memory prices dropped and the use of more than 4 GB of RAM increased. Most manufacturers started to provide both 32-bit and 64-bit drivers for new devices, so unavailability of 64-bit drivers ceased to be a problem. 64-bit drivers were not provided for many older devices, which could consequently not be used in 64-bit systems.

Driver compatibility was less of a problem with open-source drivers, as 32-bit ones could be modified for 64-bit use. Support for hardware made before early 2007, was problematic for open-source platforms,[citation needed] due to the relatively small number of users.

64-bit versions of Windows cannot run 16-bit software. However, most 32-bit applications will work well. 64-bit users are forced to install a virtual machine of a 16- or 32-bit operating system to run 16-bit applications.[37]

Mac OS X 10.4 ''Tiger'' and Mac OS X 10.5 ''Leopard'' only had a 32-bit kernel, but they can run 64-bit user-mode code on 64-bit processors. Mac OS X 10.6 ''Snow Leopard'' had both 32- and 64-bit kernels, and, on most Macs, used the 32-bit kernel even on 64-bit processors. This allowed those Macs to support 64-bit processes while still supporting 32-bit device drivers; although not 64-bit drivers and performance advantages that can come with them. Mac OS X 10.7 ''Lion'' ran with a 64-bit kernel on more Macs, and OS X 10.8 ''Mountain Lion'' and later macOS releases only have a 64-bit kernel. On systems with 64-bit processors, both the 32- and 64-bit macOS kernels can run 32-bit user-mode code, and all versions of macOS include 32-bit versions of libraries that 32-bit applications would use, so 32-bit user-mode software for macOS will run on those systems.

Linux and most other Unix-like operating systems, and the C and C++ toolchains for them, have supported 64-bit processors for many years. Many applications and libraries for those platforms are open source, written in C and C++, so that if they are 64-bit-safe, they can be compiled into 64-bit versions. This source-based distribution model, with an emphasis on frequent releases, makes availability of application software for those operating systems less of an issue.
64-bit data models

In 32-bit programs, pointers and data types such as integers generally have the same length. This is not necessarily true on 64-bit machines.[38][39][40] Mixing data types in programming languages such as C and its descendants such as C++ and Objective-C may thus work on 32-bit implementations but not on 64-bit implementations.

In many programming environments for C and C-derived languages on 64-bit machines, int variables are still 32 bits wide, but long integers and pointers are 64 bits wide. These are described as having an LP64 data model. Another alternative is the ILP64 data model in which all three data types are 64 bits wide, and even SILP64 where short integers are also 64 bits wide.[41] However, in most cases the modifications required are relatively minor and straightforward, and many well-written programs can simply be recompiled for the new environment with no changes. Another alternative is the LLP64 model, which maintains compatibility with 32-bit code by leaving both int and long as 32-bit. LL refers to the long long integer type, which is at least 64 bits on all platforms, including 32-bit environments.
64-bit data models Data model 	short (integer) 	int 	long (integer) 	long long 	pointers,
size_t 	Sample operating systems
LLP64,
IL32P64 	16 	32 	32 	64 	64 	Microsoft Windows (x86-64 and IA-64) using Visual C++; and MinGW
LP64,
I32LP64 	16 	32 	64 	64 	64 	Most Unix and Unix-like systems, e.g., Solaris, Linux, BSD, macOS. Windows when using Cygwin; z/OS
ILP64 	16 	64 	64 	64 	64 	HAL Computer Systems port of Solaris to the SPARC64
SILP64 	64 	64 	64 	64 	64 	Classic UNICOS[41] (versus UNICOS/mp, etc.)

Many 64-bit platforms today use an LP64 model (including Solaris, AIX, HP-UX, Linux, macOS, BSD, and IBM z/OS). Microsoft Windows uses an LLP64 model. The disadvantage of the LP64 model is that storing a long into an int may overflow. On the other hand, converting a pointer to a long will “work” in LP64. In the LLP64 model, the reverse is true. These are not problems which affect fully standard-compliant code, but code is often written with implicit assumptions about the widths of data types. C code should prefer (u)intptr_t instead of long when casting pointers into integer objects.

A programming model is a choice made to suit a given compiler, and several can coexist on the same OS. However, the programming model chosen as the primary model for the OS application programming interface (API) typically dominates.

Another consideration is the data model used for device drivers. Drivers make up the majority of the operating system code in most modern operating systems[citation needed] (although many may not be loaded when the operating system is running). Many drivers use pointers heavily to manipulate data, and in some cases have to load pointers of a certain size into the hardware they support for direct memory access (DMA). As an example, a driver for a 32-bit PCI device asking the device to DMA data into upper areas of a 64-bit machine's memory could not satisfy requests from the operating system to load data from the device to memory above the 4 gibibyte barrier, because the pointers for those addresses would not fit into the DMA registers of the device. This problem is solved by having the OS take the memory restrictions of the device into account when generating requests to drivers for DMA, or by using an input–output memory management unit (IOMMU).
Current 64-bit architectures

As of May 2018, 64-bit architectures for which processors are being manufactured include:

    The 64-bit extension created by AMD to Intel's x86 architecture (later licensed by Intel); commonly termed x86-64, AMD64, or x64:
        AMD's AMD64 extensions (used in Athlon 64, Opteron, Sempron, Turion 64, Phenom, Athlon II, Phenom II, FX, Ryzen, and Epyc processors)
        Intel's Intel 64 extensions, used in Intel Core 2-i3-i5-i7-i9, some Atom, and newer Celeron, Pentium, and Xeon processors
            Intel's K1OM architecture, a variant of Intel 64 with no CMOV, MMX, and SSE instructions, used in Xeon Phi coprocessors, binary incompatible with x86-64 programs
        VIA Technologies' 64-bit extensions, used in the VIA Nano processors
    IBM's Power Architecture:
        IBM's POWER4, POWER5, POWER6, POWER7, POWER8, POWER9, and IBM A2 processors
    SPARC V9 architecture:
        Oracle's M8 and S7 processors
        Fujitsu's SPARC64 XII and SPARC64 XIfx processors
    IBM's z/Architecture, a 64-bit version of the ESA/390 architecture, used in IBM's eServer zSeries and System z mainframes:
        IBM z13 and z14
        Hitachi AP8000E
    HP-Intel's IA-64 architecture:
        Intel's Itanium processors
    MIPS Technologies' MIPS64 architecture
    ARM Holdings' AArch64 architecture
    Elbrus architecture:
        Elbrus-8S
    NEC SX architecture
        SX-Aurora TSUBASA
    RISC-V

Most architectures of 64 bits that are derived from the same architecture of 32 bits can execute code written for the 32-bit versions natively, with no performance penalty.[citation needed] This kind of support is commonly called bi-arch support or more generally multi-arch support. 
			print ('' '')
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20016:
			print ('' '')
In computer architecture, 128-bit integers, memory addresses, or other data units are those that are 128 bits (16 octets) wide. Also, 128-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.

While there are currently no mainstream general-purpose processors built to operate on 128-bit integers or addresses, a number of processors do have specialized ways to operate on 128-bit chunks of data. The IBM System/370 could be considered the first simple 128-bit computer, as it used 128-bit floating-point registers. Most modern CPUs feature single-instruction multiple-data (SIMD) instruction sets (Streaming SIMD Extensions, AltiVec etc.) where 128-bit vector registers are used to store several smaller numbers, such as four 32-bit floating-point numbers. A single instruction can then operate on all these values in parallel. However, these processors do not operate on individual numbers that are 128 binary digits in length; only their registers have the size of 128 bits.

The DEC VAX supported operations on 128-bit integer ('O' or octaword) and 128-bit floating-point ('H-float' or HFLOAT) datatypes. Support for such operations was an upgrade option rather than being a standard feature. Since the VAX's registers were 32 bits wide, a 128-bit operation used four consecutive registers or four longwords in memory.

The ICL 2900 Series provided a 128-bit accumulator, and its instruction set included 128-bit floating-point and packed decimal arithmetic.

In the same way that compilers emulate e.g. 64-bit integer arithmetic on architectures with register sizes less than 64 bits, some compilers also support 128-bit integer arithmetic. For example, the GCC C compiler 4.6 and later has a 128-bit integer type __int128 for some architectures.[1] For the C programming language, this is a compiler-specific extension, as C11 itself does not guarantee support for 128-bit integers.

A 128-bit register can store 2128 (over 3.40 × 1038) different values. The range of integer values that can be stored in 128 bits depends on the integer representation used. With the two most common representations, the range is 0 through 340,282,366,920,938,463,463,374,607,431,768,211,455 (2128 − 1) for representation as an (unsigned) binary number, and −170,141,183,460,469,231,731,687,303,715,884,105,728 (−2127) through 170,141,183,460,469,231,731,687,303,715,884,105,727 (2127 − 1) for representation as two's complement.
Uses

    The free software used to implement RISC-V architecture is defined for 32, 64 and 128 bits of integer data width.
    Universally Unique Identifiers (UUID) consist of a 128-bit value.
    IPv6 routes computer network traffic amongst a 128-bit range of addresses.
    ZFS is a 128-bit file system.
    GPU chips commonly move data across a 128-bit bus.[2]
    128 bits is a common key size for symmetric ciphers and a common block size for block ciphers in cryptography.
    128-bit processors could be used for addressing directly up to 2128 (over 3.40 × 1038) bytes, which would greatly exceed the total data stored on Earth as of 2010, which has been estimated to be around 1.2 zettabytes (1.42 × 1021 bytes).[3]
    Quadruple precision (128-bit) floating-point numbers can store 64-bit fixed point numbers or integers accurately without losing precision.
    The AS/400 virtual instruction set defines all pointers as 128-bit. This gets translated to the hardware's real instruction set as required, allowing the underlying hardware to change without needing to recompile the software. Past hardware was 48-bit CISC, while current hardware is 64-bit PowerPC. Because pointers are defined to be 128-bit, future hardware may be 128-bit without software incompatibility.
    Increasing the word size can speed up multiple precision mathematical libraries. Applications include cryptography, and potentially speed up algorithms used in complex mathematical processing (numerical analysis, signal processing, complex photo editing and audio and video processing).

    Apache Avro uses a 128-bit random number as synchronization marker for efficient splitting of data files.[4]

History

A 128-bit multicomparator was described by researchers in 1976.[5]

A CPU with 128-bit multimedia extensions was designed by researchers in 1999.[6] 
			noMore = input(''Press [ENTER] key to exit'')
		if WikIDSelect == 20017:
			print ('' '')
In computer architecture, 256-bit integers, memory addresses, or other data units are those that are 256 bits (32 octets) wide. Also, 256-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.

There are currently no mainstream general-purpose processors built to operate on 256-bit integers or addresses, though a number of processors do operate on 256-bit data. CPUs feature SIMD instruction sets (Advanced Vector Extensions and the FMA instruction set etc.) where 256-bit vector registers are used to store several smaller numbers, such as eight 32-bit floating-point numbers, and a single instruction can operate on all these values in parallel. However, these processors do not operate on individual numbers that are 256 binary digits in length, only their registers have the size of 256-bits. Binary digits are found together in 128-bit collections.
Contents

    1 Uses
    2 History
    3 See also
    4 References

Uses
Laptop computer using an Efficeon processor

    256 bits is a common key size for symmetric ciphers in cryptography, such as Advanced Encryption Standard.
    Modern GPU chips move data across a 256-bit memory bus.
    256-bit processors could be used for addressing directly up to 2256 bytes. Already 2128 (128-bit) would greatly exceed the total data stored on Earth as of 2010, which has been estimated to be around 1.2 zettabytes (over 270 bytes).[1]
    The Efficeon processor was Transmeta's second-generation 256-bit VLIW design which employed a software engine to convert code written for x86 processors to the native instruction set of the chip.[2][3]
    Increasing the word size can accelerate multiple precision mathematical libraries. Applications include cryptography.
    Researchers at the University of Cambridge use a 256-bit capability pointer, which includes capability and addressing information, on their CHERI capability system.[4]

History

			print ("The DARPA funded Data-Intensive Architecture (DIVA) system incorporated processor-in-memory (PIM) 5-stage pipelined 256-bit 
			print ("'datapath, complete with register file and ALU blocks in a ''WideWord'' processor in 2002.[5] 
			noMore = input("Press [ENTER] key to exit")
		if WikIDSelect == 20018:
			print (" ")
			print ("In computer architecture, 512-bit integers, memory addresses, or other data units are those that are 512 bits wide. Also, ")
			print ("512-bit CPU and ALU architectures are those that are based on registers, address buses, or data buses of that size.")
			print (" ")
			print ("There are currently no mainstream general-purpose processors built to operate on 512-bit integers or addresses, though a ")
			print ("number of processors do operate on 512-bit data. As of 2013, the Intel Xeon Phi has a vector processing unit with 512-bit") 
			print ("vector registers, each one holding sixteen 32-bit elements or eight 64-bit elements, and a single instruction can operate on") 
			print ("all these values in parallel. However, the Xeon Phi's vector processing unit does not operate on individual numbers that are ")
			print ("512 bits in length.[1]")
			more1 = input("Uses")
			print ("The AMD Radeon R9 290X (Sapphire OEM version pictured here) uses a 512 bit memory bus")
			print ("PICTURE NOT AVAILABLE IN COMMAND LINE VIEW")
			print ("	Some GPUs such as the Nvidia GTX280,[2] GTX285,[3] Quadro FX 5800[4] and several Tesla products move data across a 512-bit") 
			print ("	memory bus. Then AMD Radeon R9 290, R9 290X and 295X2 followed.")
			print ("	Many hash functions, such as SHA-512, have a 512-bit output.")
			print ("	AVX-512 are 512-bit extensions to the 256-bit Advanced Vector Extensions SIMD instructions for x86 instruction set ")
			print ("	architecture proposed by Intel in July 2013, and released on 2016 with Knights Landing, and in 2018 on the HEDT and ")
			print ("	consumer server platform, with Skylake-X and Skylake-SP respectively.")
			noMore = input("Press [ENTER] key to exit")
		if WikIDSelect == 20019:
			print ("Variables in the UCALC source code")
			print ("\n")
			print ("noMore   - this is an overwrite variable meant to hold back text from just flooding down too fast. It just requires enter to be pressed, and is there to tell you that this is the end of an article, mode, or feature")
			print ("more1    - this is an overwrite variable that divides articles into section, and must be bypassed to continue. Bypass by pressing the [ENTER] key")
			print ("calcIDSes - this is an integer that takes you to different modes on a calculator")
			print ("WikIDSelect - this is an integer that accepts the input to go into different articles")
			print ("konloop - this is a loop function that loops output")
			print ("modID - this is a string that prints out the calculator hardware model")
			print ("conloop - this is another loop function that loops output")
			print (" ")
			noMore = input("Press [ENTER] key to exit")
		if WikIDSelect == 30000:
			print ("This section is not yet available")
			noMore = input("Press [ENTER] key to exit")
			print ("Exiting")
			print ("Please wait...")
		if WikIDSelect == 30001:
			print ("This section is not yet available")
			noMore = input("Press [ENTER] key to exit")
			print ("Exiting")
			print ("Please wait...")
		if WikIDSelect == 30002:
			print ("Names of large numbers")
			print ("When we start working with massive numbers, we should use a variable as the name. It takes A LOT longer to spell each number out.")
			print ("Here is a list of names of large numbers")
			print ("Ones place (1-9)")
			print ("Tens place (10-99)")
			print ("Hundreds place (100-999)")
			print ("Thousands place (1000-9999)")
			print ("Ten Thousands place (10000-99999)")
			print ("Hundred thousands place (100000-999999)")
			print ("Millions place (1000000-9999999)")
			print ("Ten millions place (10000000-99999999)")
			print ("Hundred millions place (100000000-999999999)")
			print ("Billions place (1000000000-9999999999)")
			print ("Ten Billions place (10000000000-99999999999)")
			print ("Hundred billions place (100,000,000,000-9,999,999,999)")
			print ("Trillions place (1,000,000,000,000-9,999,999,999)")
			print ("Ten trillions place (10,000,000,000,000-99,999,999,999,999)")
			print ("Hundred trillions place (100,000,000,000,000-999,999,999,999,999)")
			print ("Quadrillions place (1,000,000,000,000,000-9,999,999,999,999)")
			print ("Ten quadrillions place (10,000,000,000,000,000-99,999,999,999,999,999)")
			print ("Hundred quadrillions place (100,000,000,000,000,000-999,999,999,999,999)")
			print ("Quintillions place (1,000,000,000,000,000,000-9,999,999,999,999,999,999)")
			print ("Ten quintillions place (10,000,000,000,000,000,000-99,999,999,999,999,999,999)")
			print ("Hundred quintillions place (100,000,000,000,000,000,000-999,999,999,999,999,999,999)")
			print ("Sextillions place (1,000,000,000,000,000,000,000-9,999,999,999,999,999,999,999)")
			print ("Ten sextillions place (10,000,000,000,000,000,000,000,000-99,999,999,999,999,999,999,999,999)")
			print ("Hundred sextillions place (100,000,000,000,000,000,000,000,000-999,999,999,999,999,999,999,999,999)")
			print ("Septillions place (1,000,000,000,000,000,000,000,000,000-999,9,999,999,999,999,999,999,999,999,999)")
			print ("Ten septillions place (10,000,000,000,000,000,000,000,000,000-99,999,999,999,999,999,999,999,999,999)")
			print ("Hundred septillions place (100,000,000,000,000,000,000,000,000,000-999,999,999,999,999,999,999,999,999,999)")
			print ("Octillions place (1,000,000,000,000,000,000,000,000,000-9,999,999,999,999,999,999,999,999,999)")
			print ("Ten Octillions place (10,000,000,000,000,000,000,000,000,000-99,999,999,999,999,999,999,999,999,999)")
			print ("Hundred octillions place (100,000")
			print ("Nonillions place (1,000")
			print ("Ten nonillions place (10,000")
			print ("Hundred nonillions place (100,000")
			print ("Decillions place (1,000")
			print ("Ten decillions place (10,000")
			print ("Hundred decillions place (100,000")
			print ("Undecillions place (1,000")
			print ("Ten undecillions place (10,000")
			print ("Hundred undecillions place (100,000")
			print ("Duodecillions place (1,000")
			print ("Ten duodecillions place (10,000")
			print ("Hundred duodecillions place (100,000")
			print ("Tredecillions place (1,000")
			print ("Ten tredecillions place (10,000")
			print ("Hundred tredecillions place (100,000")
			print ("Quattuordecillions place (1,000")
			print ("Ten Quattuordecillions place (10,000")
			print ("Hundreds Quattuordecillions place (100,000")
			print ("Quindecillions place (1,000")
			print ("Ten Quindecillions place (10,000")
			print ("Hundred Quindecillions place (100,000")
			print ("Sexdecillions place (1,000")
			print ("Ten Sexdecillions place (10,000")
			print ("Hundred Sexdecillions place (100,000")
			print ("Septendecillions place (1,000")
			print ("Ten Septendecillions place (10,000")
			print ("Hundreds Septendecillions place (100,000")
			print ("Octodecillions place (1,000")
			print ("Ten Octodecillions place (10,000")
			print ("Hundred Octodecillions place (100,000")
			print ("Novemdecillions place (1,000")
			print ("Ten Novemdecillions place (10,000")
			print ("Hundred Novemdecillions place (100,000")
			print ("Vigintillions place (1,000")
			print ("Ten Vigintillions place (10,000")
			print ("Hundred Vigintillions place (100,000")
			print ("Centillions place (1,000")
			print ("Ten Centillions place (10,000")
			print ("Hundred Centillions place (100,000")
			print ("Googol (10,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000,000")
			print ("Googolplex (too large to write)")
			print ("Those are the names of large numbers. However, this calculator is not able to go past the 100 undecillion mark under 128 bit mode")
		if WikIDSelect == 30003:
			print ("Superstitious numbers")
			print ("\nUnlucky 13")
			print ("Excerpt from https://www.wikipedia.org/13_(number_")
			print ("The number 13 is considered an unlucky number in some countries.[11] The end of the Mayan calendar's 13th Baktun was superstitiously feared as a harbinger of the apocalyptic 2012 phenomenon.[12] Fear of the number 13 has a specifically recognized phobia, Triskaidekaphobia, a word coined in 1911. The superstitious sufferers of triskaidekaphobia try to avoid bad luck by keeping away from anything numbered or labelled thirteen. As a result, companies and manufacturers use another way of numbering or labelling to avoid the number, with hotels and tall buildings being conspicuous examples (thirteenth floor).[13] It is also considered unlucky to have thirteen guests at a table. Friday the 13th has been considered an unlucky day.[11]")
			print ("There are a number of theories as to why the number thirteen became associated with bad luck, but none of them have been accepted as likely.[11]")
			print ("The Last Supper: At Jesus Christ's last supper, there were thirteen people around the table, counting Christ and the twelve apostles. Some believe this is unlucky because one of those thirteen, Judas Iscariot, was the betrayer of Jesus Christ. From the 1890s, a number of English language sources relate the ''unlucky'' thirteen to an idea that at the Last Supper, Judas, the disciple who betrayed Jesus, was the 13th to sit at the table.[14]")
			print ("Knights Templar: On Friday 13 October 1307, King Philip IV of France ordered the arrest of the Knights Templar,[11] and most of the knights were tortured and killed.")
			print ("Full Moons: A year with 13 full moons instead of 12 posed problems for the monks in charge of the calendars. ''This was considered a very unfortunate circumstance, especially by the monks who had charge of the calendar of thirteen months for that year, and it upset the regular arrangement of church festivals. For this reason thirteen came to be considered an unlucky number.''[15] However, a typical century has about 37 years that have 13 full moons, compared to 63 years with 12 full moons, and typically every third or fourth year has 13 full moons.[16]")
			print ("A Repressed Lunar Cult: In ancient cultures, the number 13 represented femininity, because it corresponded to the number of lunar (menstrual) cycles in a year (13 x 28 = 364 days). The theory is that, as the solar calendar triumphed over the lunar, the number thirteen became anathema.[11][17]")
			print ("Hammurabi's Code: There is a myth that the earliest reference to thirteen being unlucky or evil is in the Babylonian Code of Hammurabi (circa 1780 BC), where the thirteenth law is said to be omitted. In fact, the original Code of Hammurabi has no numeration. The translation by L.W. King (1910), edited by Richard Hooker, omitted one article: If the seller have gone to (his) fate (i. e., have died), the purchaser shall recover damages in said case fivefold from the estate of the seller. Other translations of the Code of Hammurabi, for example the translation by Robert Francis Harper, include the 13th article.[18]")
			print ("\nLucky 13")
			print ("Excerpt from https://www.wikipedia.org/13_(number)_")
			print ("In some countries, such as Italy, 13 is considered a lucky number.[19] The expression fare tredici (''to do 13'') means hit the jackpot. 17 is considered an unlucky number instead.[20]")
			print ("\n666")
			print ("Excerpt from https://www.wikipedia.org/666_(number)_")
			print ("Number of the Beast")
			print ("666 is often associated with the devil.")
			print ("Main article: Number of the Beast")
			print ("In the Textus Receptus manuscripts of the New Testament, the Book of Revelation (13:17–18) cryptically asserts 666 to be ''man's number'' or ''the number of a man'' (depending on how the text is translated) associated with the Beast, an antagonistic creature that appears briefly about two-thirds into the apocalyptic vision. Some manuscripts of the original Greek use the symbols χξϛ chi xi stigma (or χξϝ with a digamma), while other manuscripts spell out the number in words.")
			print ("In modern popular culture, 666 has become one of the most widely recognized symbols for the Antichrist or, alternatively, the devil. The number 666 is purportedly used to invoke Satan. Earnest references to the number occur both among apocalypticist Christian groups and in explicitly anti-Christian subcultures. References in contemporary Western art or literature are, more likely than not, intentional references to the Beast symbolism. Such popular references are therefore too numerous to list.")
			print ("It is common to see the symbolic role of the integer 666 transferred to the digit sequence 6-6-6. Some people take the Satanic associations of 666 so seriously that they actively avoid things related to 666 or the digits 6-6-6. This is known as hexakosioihexekontahexaphobia.")
			print ("The number is cited as 616 in some early biblical manuscripts, the earliest known instance being in Papyrus 115.[3][4]")
			print ("Other occurrences")
			print ("In the Bible, 666 is the number of talents of gold Solomon collected each year (see 1 Kings 10:14, 2 Chronicles 9:13 and also in Ezra 2:13).")
			print ("In the Bible, 666 is the number of Adonikam's descendants who return to Jerusalem and Judah from the Babylonian exile (see Ezra 2:13).")
			print ("In the Bible, there may be a latent reference to 666 in the name of the great sixth-century BC king of Babylon. Commonly spelled Nebuchadnezzar, transliterating from the Book of Daniel, the name is Nebuchadrezzar or Nebuchadrezzur in the Book of Jeremiah (see Jeremiah 49:28–30). The number of each name can be calculated, since Hebrew letters double as numbers (see Gematria, Hebrew numerals). Nebuchadrezzar is 663, and Nebuchadrezzur, 669. Midway between the two variants is 666. If the mysteries of Jeremiah are to be related to those of Revelation, Nebuchadrezzar, who came (though bidden by God) to crush God's people, may prefigure the end-times beast.[5]")
			print ("Using gematria, Neron Caesar transliterated from Greek into Hebrew produces the number 666. The Latin spelling of ''Nero Caesar'' transliterated into Hebrew produces the number 616. Thus, in the Bible, 666 may have been a coded reference to Nero, the Roman Emperor from 55 to 68 AD.[6]")
		if WikIDSelect == 30004:
			print ("Slang numbers")
			print ("420 - Also known as ''420 blaze it'' is a number referrring to smoking weed")
			print ("69 - Refers to 69ing, or the 69 sex position")
			print ("3 - The number of the illuminati")
			print ("1738 - The title of the song ''1738'' by fetty wap")
			print ("888 - Alternate to 666")
			print ("8008 - For some calculator UIs this looks like BOOB")
			print ("8008135 - For some calculator UIs this looks like BOOBIES")
		if WikIDSelect == 30005:
			print ("Roman numerals")
			print ("\nNumeral chart")
			print ("__________________________________________________________________________________________________________________")
			print ("| I | II | III | IV | V | VI | VII | VIII | IX | X | XI | XII | XIII | XIV | XV | XVI | XVII | XVIII | XVIX | XX |")
			print ("|---|----|-----|----|---|----|-----|------|----|---|----|-----|------|-----|----|-----|------|-------|------|----|")
			print ("| 1 | 02 | 003 | 04 | 5 | 06 | 007 | 0008 | 09 |10 | 11 | 012 | 0013 | 014 | 15 | 016 | 0017 | 00018 | 0019 | 20 |")
			print ("|---|----|-----|----|---|----|-----|------|----|---|----|-----|------|-----|----|-----|------|-------|------|----|")
			print ("| XXI | XXII | XXIII | XXIV | XXV | XXVI | XXVII | XXVIII | XXVIX | XXX | XXXI | XXXII | XXXIII | XXXIV | XXXV | XXXVI | XXXVII | XXXVIII | XXXVIX | XL |")
			print ("|-----|------|-------|------|-----|------|-------|--------|-------|-----|------|-------|--------|-------|------|-------|--------|---------|--------|----|")
			print ("| 021 | 0022 | 00023 | 0024 | 025 | 0026 | 00027 | 000028 | 00029 | 030 | 0031 | 00032 | 000033 | 00034 | 0035 | 00036 | 000037 | 0000038 | 000039 | 40 |")
			print ("|-----|------|-------|------|-----|------|-------|--------|-------|-----|------|-------|--------|-------|------|-------|--------|---------|--------|----|")
			print ("| XLI | XLII | XLIII | XLIV | XLV | XLVI | XLVII | XLVIII | XLIX | L | LI | LII | LIII | LIV | LV | LVI | LVII | LVIII | LVIX | LX |")
			print ("|-----|------|-------|------|-----|------|-------|--------|------|---|----|-----|------|-----|----|-----|------|-------|------|----|")
			print ("| 041 | 0042 | 00043 | 0044 | 045 | 0046 | 00047 | 000048 | 0049 |50 | 51 | 052 | 0053 | 054 | 55 | 056 | 0057 | 00058 | 0059 | 60 |")
			print ("|-----|------|-------|------|-----|------|-------|--------|------|---|----|-----|------|-----|----|-----|------|-------|------|----|")
			print ("| LXI | LXII | LXIII | LXIV | LXV | LXVI | LXVII | LXVIII | LXIX | LXX | LXXI | LXXII | LXXIII | LXXIV | LXXV | LXXVI | LXXVII | LXXVIII | LXXIX | LXXX |")
			print ("|-----|------|-------|------|-----|------|-------|--------|------|-----|------|-------|--------|-------|------|-------|--------|---------|-------|------|")
			print ("| 061 | 0062 | 00063 | 0064 | 065 | 0066 | 00067 | 000068 | 0069 | 070 | 0071 | 00072 | 000073 | 00074 | 0075 | 00076 | 000077 | 0000078 | 00079 | 0080 |")
			print ("|-----|------|-------|------|-----|------|-------|--------|------|-----|------|-------|--------|-------|------|-------|--------|---------|-------|------|")
			print ("| LXXXI | LXXXII | LXXXIII | LXXXXIV | LXXXXV | LXXXXVI | LXXXVII | LXXXVIII | LXXXVIX | XC | XCI | XCII | XCIII | XCIV | XCV | XCVI | XCVII | XCVIII | XCVIX | C   |") 
			print ("|-------|--------|---------|---------|--------|---------|---------|----------|---------|----|-----|------|-------|------|-----|------|-------|--------|-------|")
			print ("| 00081 | 000082 | 000083  | 0000084 | 000085 | 0000086 | 0000087 | 00000088 | 0000089 | 90 | 091 | 0092 | 00093 | 0094 | 095 | 0096 | 00097 | 000098 | 00099 | 100 |")
			print ("|-------|--------|---------|---------|--------|---------|---------|----------|---------|----|-----|------|-------|------|-----|------|-------|--------|-------|")
		if WikIDSelect == 30006:
			print ("Multiples table")
			print ("\n")
			print ("| 0  |  1  |  2  |")
			print ("| 1  |  1  |  2  |")
			print ("| 2  |  2  |  3  |")
		if WikIDSelect == 30007:
			print ("Intellect Quotient")
			print ("Excerpt from https://www.wikipedia.org/Intelligence_Quotient")
			print ("An intelligence quotient (IQ) is a total score derived from several standardized tests designed to assess human intelligence. ")
			print ("The abbreviation ''IQ'' was coined by the psychologist William Stern for the German term Intelligenzquotient, his term for a ")
			print ("scoring method for intelligence tests at University of Breslau he advocated in a 1912 book.[1] Historically, IQ is a score ")
			print ("obtained by dividing a person's mental age score, obtained by administering an intelligence test, by the person's chronological ")
			print ("age, both expressed in terms of years and months. The resulting fraction is multiplied by 100 to obtain the IQ score.[2] When ")
			print ("current IQ tests were developed, the median raw score of the norming sample is defined as IQ 100 and scores each standard ")
			print ("deviation (SD) up or down are defined as 15 IQ points greater or less,[3] although this was not always so historically. ")
			print ("By this definition, approximately two-thirds of the population scores are between IQ 85 and IQ 115. About 2.5 percent of the ")
			print ("population scores above 130, and 2.5 percent below 70.[4][5]")
			print (" ")
			print ("Scores from intelligence tests are estimates of intelligence. Unlike, for example, distance and mass, a concrete measure of ")
			print ("intelligence cannot be achieved given the abstract nature of the concept of ''intelligence''.[6] IQ scores have been shown to") 
			print ("be associated with such factors as morbidity and mortality,[7][8] parental social status,[9] and, to a substantial degree, ")
			print ("biological parental IQ. While the heritability of IQ has been investigated for nearly a century, there is still debate about") 
			print ("the significance of heritability estimates[10][11] and the mechanisms of inheritance.[12]")
			print (" ")
			print ("IQ scores are used for educational placement, assessment of intellectual disability, and evaluating job applicants. Even when") 
			print ("students improve their scores on standardized tests, they do not always improve their cognitive abilities, such as memory,")
			print ("attention and speed.[13] In research contexts they have been studied as predictors of job performance, and income. They are") 
			print ("also used to study distributions of psychometric intelligence in populations and the correlations between it and other ")
			print ("variables. Raw scores on IQ tests for many populations have been rising at an average rate that scales to three IQ points per ")
			print ("decade since the early 20th century, a phenomenon called the Flynn effect. Investigation of different patterns of increases in ")
			print ("subtest scores can also inform current research on human intelligence.")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Contents")
			print ("1 History")
			print ("1.1 Precursors to IQ testing")
			print ("1.2 General factor (g)")
			print ("1.3 United States military selection in World War I")
			print ("1.4 IQ testing and the Eugenics movement in the United States")
			print ("1.5 Cattell–Horn–Carroll theory")
			print ("1.6 Other theories")
			print ("2 Current tests")
			print ("3 Test bias or differential item functioning")
			print ("4 Reliability and validity")
			print ("5 Flynn effect")
			print ("6 Age")
			print ("7 Genetics and environment")
			print ("7.1 Heritability")
			print ("7.2 Shared family environment")
			print ("7.3 Non-shared family environment and environment outside the family")
			print ("7.4 Individual genes")
			print ("7.5 Gene-environment interaction")
			print (" 8 Interventions")
			print ("9 Music")
			print ("10 Brain anatomy")
			print ("11 Health")
			print ("12 Social correlations")
			print ("12.1 School performance")
			print ("12.2 Job performance")
			print ("12.3 Income")
			print ("12.4 Crime")
			print ("12.5 Health and mortality")
			print ("12.6 Other accomplishments")
			print ("13 Group-IQ or the collective intelligence factor c")
			print ("14 Group differences")
			print ("14.1 Sex")
			print ("14.2 Race and intelligence")
			print ("14.2.1 Race and intelligence in United States of America")
			print ("15 Public policy")
			print ("16 Criticism and views")
			print ("16.1 Relationship to intelligence")
			print ("16.2 Criticism of IQ")
			print ("16.3 Systematic exclusion of threshold effects")
			print ("16.4 Test bias")
			print ("16.5 Intermingling cultures and IQ classification fairness")
			print ("16.6 Outdated methodology")
			print ("16.7 Intelligence: Knowns and Unknowns")
			print ("16.8 Dynamic assessment")
			print ("17 Classification")
			print ("18 High IQ societies")
			print ("19 See also")
			print ("20 References")
			print ("21 Bibliography")
			print ("22 External links")
			print (" ")
			print ("\n\n\n\n\n\n\n")
			more1 = input("History")
			print ("See also: History of the race and intelligence controversy")
			more1 = input("Precursors to IQ testing")
			print ("Historically, even before IQ tests were devised, there were attempts to classify people into intelligence categories by")
			print ("observing their behavior in daily life.[14][15] Those other forms of behavioral observation are still important for ")
			print ("validating classifications based primarily on IQ test scores. Both intelligence classification by observation of behavior") 
			print ("outside the testing room and classification by IQ testing depend on the definition of ''intelligence'' used in a particular")
			print ("case and on the reliability and error of estimation in the classification procedure.")
			print (" ")
			print ("The English statistician Francis Galton made the first attempt at creating a standardized test for rating a person's")
			print ("intelligence. A pioneer of psychometrics and the application of statistical methods to the study of human diversity and the ")
			print ("study of inheritance of human traits, he believed that intelligence was largely a product of heredity (by which he did not ")
			print ("mean genes, although he did develop several pre-Mendelian theories of particulate inheritance).[16][17][18] He hypothesized ")
			print ("that there should exist a correlation between intelligence and other observable traits such as reflexes, muscle grip, and head ")
			print ("size.[19] He set up the first mental testing centre in the world in 1882 and he published ''Inquiries into Human Faculty and ")
			print ("Its Development'' in 1883, in which he set out his theories. After gathering data on a variety of physical variables, he was ")
			print ("unable to show any such correlation, and he eventually abandoned this research.[20][21]")
			print (" ")
			print ("French psychologist Alfred Binet was one of the key developers of what later became known as the Stanford–Binet test.")
			print (" ")
			print ("French psychologist Alfred Binet, together with Victor Henri and Théodore Simon had more success in 1905, when they published ")
			print ("the Binet-Simon test, which focused on verbal abilities. It was intended to identify mental retardation in school children,[22]")
			print ("but in specific contradistinction to claims made by psychiatrists that these children were ''sick'' (not ''slow'') and should ") 
			print ("therefore be removed from school and cared for in asylums.[23] The score on the Binet-Simon scale would reveal the child's ")
			print ("mental age. For example, a six-year-old child who passed all the tasks usually passed by six-year-olds—but nothing beyond—would ")
			print ("have a mental age that matched his chronological age, 6.0. (Fancher, 1985). Binet thought that intelligence was multifaceted, ")
			print ("but came under the control of practical judgment.")
			print (" ")
			print ("In Binet's view, there were limitations with the scale and he stressed what he saw as the remarkable diversity of intelligence ")
			print ("and the subsequent need to study it using qualitative, as opposed to quantitative, measures (White, 2000). American psychologist") 
			print ("Henry H. Goddard published a translation of it in 1910. American psychologist Lewis Terman at Stanford University revised the")
			print ("Binet-Simon scale, which resulted in the Stanford-Binet Intelligence Scales (1916). It became the most popular test in the ")
			print ("United States for decades.[22][24][25][26]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("General factor (g)")
			print ("Main article: g factor")
			print (" ")
			print ("The many different kinds of IQ tests include a wide variety of item content. Some test items are visual, while many are verbal.")
			print ("Test items vary from being based on abstract-reasoning problems to concentrating on arithmetic, vocabulary, or general ")
			print ("knowledge.")
			print (" ")
			print ("The British psychologist Charles Spearman in 1904 made the first formal factor analysis of correlations between the tests. He ")
			print ("observed that children's school grades across seemingly unrelated school subjects were positively correlated, and reasoned that ")
			print ("these correlations reflected the influence of an underlying general mental ability that entered into performance on all kinds of") 
			print ("mental tests. He suggested that all mental performance could be conceptualized in terms of a single general ability factor and") 
			print ("a large number of narrow task-specific ability factors. Spearman named it g for ''general factor'' and labeled the specific ") 
			print ("factors or abilities for specific tasks s. In any collection of test items that make up an IQ test, the score that best ")
			print ("measures g is the composite score that has the highest correlations with all the item scores. Typically, the ''g-loaded'' ")
			print ("composite score of an IQ test battery appears to involve a common strength in abstract reasoning across the test's item ")
			print ("content. Therefore, Spearman and others have regarded g as closely related to the essence of human intelligence.[citation needed]")
			print (" ")
			print ("Spearman's argument proposing a general factor of human intelligence is still accepted in principle by many psychometricians.") 
			print ("Today's factor models of intelligence typically represent cognitive abilities as a three-level hierarchy, where there are a ")
			print ("large number of narrow factors at the bottom of the hierarchy, a handful of broad, more general factors at the intermediate ")
			print ("level, and at the apex a single factor, referred to as the g factor, which represents the variance common to all cognitive ")
			print ("tasks. However, this view is not universally accepted; other factor analyses of the data, with different results, are possible.") 
			print ("Some psychometricians regard g as a statistical artifact.[citation needed]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("United States military selection in World War I")
			print (" ")
			print ("During World War I, a way was needed to evaluate and assign Army recruits to appropriate tasks. This led to the development of")
			print ("several mental tests by Robert Yerkes, who worked with major hereditarians of American psychometrics—including Terman, ")
			print ("Goddard—to write the test.[27] The testing generated controversy and much public debate in the United States. Nonverbal or ")
			print ("''performance'' tests were developed for those who could not speak English or were suspected of malingering.[22] Based on ")
			print ("Goddard's translation of the Binet-Simon test, the tests had an impact in screening men for officer training:")
			print (" ")
			print ("	...the tests did have a strong impact in some areas, particularly in screening men for officer training. At the start of")
			print ("the war, the army and national guard maintained nine thousand officers. By the end, two hundred thousand officers presided, ")
			print ("and two- thirds of them had started their careers in training camps where the tests were applied. In some camps, no man scoring")
			print ("below C could be considered for officer training.[27]")
			print (" ")
			print ("1.75 million men were tested in total, making the results the first mass-produced written tests of intelligence, though ")
			print ("considered dubious and non-usable, for reasons including high variability of test implementation throughout different camps and")
			print ("questions testing for familiarity with American culture rather than intelligence.[27] After the war, positive publicity ")
			print ("promoted by army psychologists helped to make psychology a respected field.[28] Subsequently, there was an increase in jobs and")
			print ("funding in psychology in the United States.[29] Group intelligence tests were developed and became widely used in schools and") 
			print ("industry.[30]")
			print (" ")
			print ("The results of these tests, which at the time reaffirmed contemporary racism and nationalism, are considered controversial and ")
			print ("dubious, having rested on certain contested assumptions: that intelligence was heritable, innate, and could be relegated to a ")
			print ("single number, the tests were enacted systematically, and test questions actually tested for innate intelligence rather than") 
			print ("subsuming environmental factors.[27] The tests also allowed for the bolstering of jingoist narratives in the context of ")
			print ("increased immigration, which may have influenced the passing of the Immigration Restriction Act of 1924.[27]")
			print (" ")
			print ("L.L. Thurstone argued for a model of intelligence that included seven unrelated factors (verbal comprehension, word fluency,")
			print ("number facility, spatial visualization, associative memory, perceptual speed, reasoning, and induction). While not widely used,")
			print ("Thurstone's model influenced later theories.[22]")
			print (" ")
			print ("David Wechsler produced the first version of his test in 1939. It gradually became more popular and overtook the Stanford-Binet ")
			print ("in the 1960s. It has been revised several times, as is common for IQ tests, to incorporate new research. One explanation is that")
			print ("psychologists and educators wanted more information than the single score from the Binet. Wechsler's ten or more subtests ")
			print ("provided this. Another is that the Stanford-Binet test reflected mostly verbal abilities, while the Wechsler test also ")
			print ("reflected nonverbal abilities. The Stanford-Binet has also been revised several times and is now similar to the Wechsler in")
			print ("several aspects, but the Wechsler continues to be the most popular test in the United States.[22]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("IQ testing and the Eugenics movement in the United States")
			print (" ")
			print ("Eugenics refers to the principles of heredity used to improve the human race. Francis Galton first used the term in the late") 
			print ("1800s.[31] The eugenics movement was popularized by Progressivism in the US in the 1920s and 1930s.[32]")
			print (" ")
			print ("Goddard was a eugenicist. In 1908, he published his own version, The Binet and Simon Test of Intellectual Capacity, and ")
			print ("cordially promoted the test. He quickly extended the use of the scale to the public schools (1913), to immigration ")
			print ("(Ellis Island, 1914) and to a court of law (1914).[33]")
			print (" ")
			print ("Different from Galton, who promoted eugenics through selective breeding for positive traits, Goddard went with the US eugenics ")
			print ("movement to eliminate ''undesirable'' traits.[34] Goddard used the term ''feeble-minded'' to refer to people who did not ")
			print ("perform well in the test and thus were intellectually inferior. He argued that ''feeble-mindedness'' is caused by heredity,") 
			print ("thus feeble-minded people should be prevented from giving birth, either by institutional isolation or sterilization surgeries.")
			print ("[33] At first sterilization targeted the disabled and was extended to poor people. Goddard's intelligence test was endorsed by ")
			print ("the eugenicists to push for laws for forced sterilization. Different states adopted the sterilization laws at different pace. ")
			print ("These laws forced over 64,000 people to go through sterilization in the United States.[35]")
			print (" ")
			print ("California's sterilization program was so effective that the Nazis turned to the government for advice on how to prevent the")
			print ("birth of the ''unfit''.[36] The US eugenics movement lost its momentum in 1940s and was halted in view of the horrors of Nazi ")
			print ("Germany.")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Cattell–Horn–Carroll theory")
			print ("Main article: Cattell–Horn–Carroll theory")
			print ("Psychologist Raymond Cattell defined fluid and crystallized intelligence and authored the Cattell Culture Fair III IQ test.")
			print ("Raymond Cattell (1941) proposed two types of cognitive abilities in a revision of Spearman's concept of general intelligence.")
			print ("Fluid intelligence (Gf) was hypothesized as the ability to solve novel problems by using reasoning, and crystallized ")
			print ("intelligence (Gc) was hypothesized as a knowledge-based ability that was very dependent on education and experience. In ")
			print ("addition, fluid intelligence was hypothesized to decline with age, while crystallized intelligence was largely resistant to the") 
			print ("effects of aging. The theory was almost forgotten, but was revived by his student John L. Horn (1966) who later argued Gf and")
			print ("Gc were only two among several factors, and who eventually identified nine or ten broad abilities. The theory continued to be ")
			print ("called Gf-Gc theory.[22]")
			print (" ")
			print ("John B. Carroll (1993), after a comprehensive reanalysis of earlier data, proposed the three stratum theory, which is a ")
			print ("hierarchical model with three levels. The bottom stratum consists of narrow abilities that are highly specialized (e.g., ")
			print ("induction, spelling ability). The second stratum consists of broad abilities. Carroll identified eight second-stratum abilities.") 
			print ("Carroll accepted Spearman's concept of general intelligence, for the most part, as a representation of the uppermost, third") 
			print ("stratum.[37][38]")
			print (" ")
			print ("In 1999, a merging of the Gf-Gc theory of Cattell and Horn with Carroll's Three-Stratum theory has led to the Cattell–Horn–Carroll theory (CHC Theory). It has greatly influenced many of the current broad IQ tests.[22]")
			print (" ")
			print ("In CHC theory, a hierarchy of factors is used; g is at the top. Under it are ten broad abilities that in turn are subdivided into seventy narrow abilities. The broad abilities are:[22]")
			print (" ")
			print ("	Fluid intelligence (Gf) includes the broad ability to reason, form concepts, and solve problems using unfamiliar information or novel procedures.")
			print ("    Crystallized intelligence (Gc) includes the breadth and depth of a person's acquired knowledge, the ability to communicate one's knowledge, and the ability to reason using previously learned experiences or procedures.")
			print ("    Quantitative reasoning (Gq) is the ability to comprehend quantitative concepts and relationships and to manipulate numerical symbols.")
			print ("    Reading and writing ability (Grw) includes basic reading and writing skills.")
			print ("    Short-term memory (Gsm) is the ability to apprehend and hold information in immediate awareness, and then use it within a few seconds.")
			print ("    Long-term storage and retrieval (Glr) is the ability to store information and fluently retrieve it later in the process of thinking.")
			print ("    Visual processing (Gv) is the ability to perceive, analyze, synthesize, and think with visual patterns, including the ability to store and recall visual representations.")
			print ("    Auditory processing (Ga) is the ability to analyze, synthesize, and discriminate auditory stimuli, including the ability to process and discriminate speech sounds that may be presented under distorted conditions.")
			print ("    Processing speed (Gs) is the ability to perform automatic cognitive tasks, particularly when measured under pressure to maintain focused attention.")
			print ("    Decision/reaction time/speed (Gt) reflects the immediacy with which an individual can react to stimuli or a task (typically measured in seconds or fractions of seconds; it is not to be confused with Gs, which typically is measured in intervals of 2–3 minutes). See Mental chronometry.")
			print (" ")
			print ("Modern tests do not necessarily measure all of these broad abilities. For example, Gq and Grw may be seen as measures of school ")
			print ("achievement and not IQ.[22] Gt may be difficult to measure without special equipment. g was earlier often subdivided into only ")
			print ("Gf and Gc, which were thought to correspond to the nonverbal or performance subtests and verbal subtests in earlier versions of") 
			print ("the popular Wechsler IQ test. More recent research has shown the situation to be more complex.[22] Modern comprehensive IQ ")
			print ("tests do not stop at reporting a single IQ score. Although they still give an overall score, they now also give scores for ")
			print ("many of these more restricted abilities, identifying particular strengths and weaknesses of an individual.[22]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Other theories")
			print (" ")
			print ("J.P. Guilford's Structure of Intellect (1967) model used three dimensions which when combined yielded a total of 120 types of") 
			print ("intelligence. It was popular in the 1970s and early 1980s, but faded owing to both practical problems and theoretical")
			print ("criticisms.[22]")
			print (" ")
			print ("Alexander Luria's earlier work on neuropsychological processes led to the PASS theory (1997). It argued that only looking at ")
			print ("one general factor was inadequate for researchers and clinicians who worked with learning disabilities, attention disorders,") 
			print ("intellectual disability, and interventions for such disabilities. The PASS model covers four kinds of processes (planning ")
			print ("process, attention/arousal process, simultaneous processing, and successive processing). The planning processes involve ")
			print ("decision making, problem solving, and performing activities and requires goal setting and self-monitoring.")
			print (" ")
			print ("The attention/arousal process involves selectively attending to a particular stimulus, ignoring distractions, and maintaining") 
			print ("vigilance. Simultaneous processing involves the integration of stimuli into a group and requires the observation of ")
			print ("relationships. Successive processing involves the integration of stimuli into serial order. The planning and attention/arousal") 
			print ("components comes from structures located in the frontal lobe, and the simultaneous and successive processes come from ")
			print ("structures located in the posterior region of the cortex.[39][40][41] It has influenced some recent IQ tests, and been seen as")			
			print ("a complement to the Cattell-Horn-Carroll theory described above.[22]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Current tests")
			print ("Normalized IQ distribution with mean 100 and standard deviation 15.")
			print (" ")
			print ("There are a variety of individually administered IQ tests in use in the English-speaking world.[42][43] The most commonly used") 
			print ("individual IQ test series is the Wechsler Adult Intelligence Scale for adults and the Wechsler Intelligence Scale for Children ")
			print ("for school-age test-takers. Other commonly used individual IQ tests (some of which do not label their standard scores as ''IQ''")
			print ("scores) include the current versions of the Stanford-Binet Intelligence Scales, Woodcock-Johnson Tests of Cognitive Abilities, ")
			print ("the Kaufman Assessment Battery for Children, the Cognitive Assessment System, and the Differential Ability Scales.")
			print (" ")
			print ("IQ tests that measure intelligence also include:")
			print (" ")
			print ("    Raven's Progressive Matrices ")
			print ("    Cattell Culture Fair III ")
			print ("    Reynolds Intellectual Assessment Scales ")
			print ("    Thurstone's Primary Mental Abilities[44][45] ")
			print ("    Kaufman Brief Intelligence Test[46]")
			print ("   Multidimensional Aptitude Battery II")
			print ("   Das–Naglieri cognitive assessment system")
			print (" ")
			print ("IQ scales are ordinally scaled.[47][48][49][50][51] While one standard deviation is 15 points, and two SDs are 30 points, and")
			print ("so on, this does not imply that mental ability is linearly related to IQ, such that IQ 50 means half the cognitive ability of ")
			print ("IQ 100. In particular, IQ points are not percentage points.")
			print (" ")
			print ("On a related note, this fixed standard deviation means that the proportion of the population who have IQs in a particular range") 
			print ("is theoretically fixed, and current Wechsler tests only give Full Scale IQs between 40 and 160. This should be borne in mind ")
			print ("when considering reports of people with much higher IQs.[52][53]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Test bias or differential item functioning")
			print (" ")
			print ("Differential item functioning (DIF), sometimes referred to as measurement bias, is a phenomenon when participants from ")
			print ("different groups (e.g. gender, race, disability) with the same latent abilities give different answers to specific questions on ")
			print ("the same IQ test.[54] DIF analysis measures such specific items on a test alongside measuring participants latent abilities on ")
			print ("other similar questions. A consistent different group response to a specific question among similar type of questions can ")
			print ("indicate an effect of DIF. It does not count as differential item functioning if both groups have equally valid chance of ")
			print ("giving different responses to the same questions. Such bias can be a result of culture, educational level and other factors")
			print ("that are independent of group traits. DIF is only considered if test-takers from different groups with the same underlying ")
			print ("latent ability level have a different chance of giving specific responses.[55] Such questions are usually removed in order to") 
			print ("make the test equally fair for both groups. Common techniques for analyzing DIF are item response theory (IRT) based methods, ")
			print ("Mantel-Haenszel, and logistic regression.[55]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Reliability and validity")
			print (" ")
			print ("Psychometricians generally regard IQ tests as having high statistical reliability.[9][56] A high reliability implies that – ")
			print ("although test-takers may have varying scores when taking the same test on differing occasions, and although they may have ")
			print ("varying scores when taking different IQ tests at the same age – the scores generally agree with one another and across time.")
			print ("Like all statistical quantities, any particular estimate of IQ has an associated standard error that measures uncertainty about ")
			print ("the estimate. For modern tests, the standard error of measurement is about three points[citation needed]. Clinical psychologists")
			print ("generally regard IQ scores as having sufficient statistical validity for many clinical purposes.[22][57][58] In a survey of 661")
			print ("randomly sampled psychologists and educational researchers, published in 1988, Mark Snyderman and Stanley Rothman reported a") 
			print ("general consensus supporting the validity of IQ testing. ''On the whole, scholars with any expertise in the area of ")
			print ("intelligence and intelligence testing (defined very broadly) share a common view of the most important components of ")
			print ("intelligence, and are convinced that it can be measured with some degree of accuracy.'' Almost all respondents picked out ")
			print ("abstract reasoning, ability to solve problems and ability to acquire knowledge as the most important elements.[59]")
			print (" ")
			print ("IQ scores can differ to some degree for the same person on different IQ tests, so a person does not always belong to the same") 
			print ("IQ score range each time the person is tested. (IQ score table data and pupil pseudonyms adapted from description of KABC-II ")
			print ("norming study cited in Kaufman 2009.[60][61]) Pupil 	KABC-II 	WISC-III 	WJ-III")
			print ("Asher 	90 	95 	111")
			print ("Brianna 	125 	110 	105")
			print ("Colin 	100 	93 	101")
			print ("Danica 	116 	127 	118")
			print ("Elpha 	93 	105 	93")
			print ("Fritz 	106 	105 	105")
			print ("Georgi 	95 	100 	90")
			print ("Hector 	112 	113 	103")
			print ("Imelda 	104 	96 	97")
			print ("Jose 	101 	99 	86")
			print ("Keoku 	81 	78 	75")
			print ("Leo 	116 	124 	102")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Flynn effect")
			print ("Main article: Flynn effect")
			print (" ")
			print ("Since the early 20th century, raw scores on IQ tests have increased in most parts of the world.[62][63][64] When a new version ")
			print ("of an IQ test is normed, the standard scoring is set so performance at the population median results in a score of IQ 100. The ")
			print ("phenomenon of rising raw score performance means if test-takers are scored by a constant standard scoring rule, IQ test scores ")
			print ("have been rising at an average rate of around three IQ points per decade. This phenomenon was named the Flynn effect in the") 
			print ("book The Bell Curve after James R. Flynn, the author who did the most to bring this phenomenon to the attention of ")
			print ("psychologists.[65][66]")
			print (" ")
			print ("Researchers have been exploring the issue of whether the Flynn effect is equally strong on performance of all kinds of IQ test") 
			print ("items, whether the effect may have ended in some developed nations, whether there are social subgroup differences in the ")
			print ("effect, and what possible causes of the effect might be.[67] A 2011 textbook, IQ and Human Intelligence, by N. J. Mackintosh, ")
			print ("noted the Flynn effect demolishes the fears that IQ would be decreased. He also asks whether it represents a real increase in ")
			print ("intelligence beyond IQ scores.[68] A 2011 psychology textbook, lead authored by Harvard Psychologist Professor Daniel Schacter, ")
			print ("noted that humans' inherited intelligence could be going down while acquired intelligence goes up.[69]")
			print (" ")
			print ("Research has revealed that the Flynn effect has slowed or reversed course in several Western countries beginning in the late")
			print ("20th century. The phenomenon has been termed the negative Flynn effect.[70][71] A study of Norwegian military conscripts' test ")
			print ("records found that IQ scores have been falling for generations born after the year 1975, and that the underlying nature of both ")
			print ("initial increasing and subsequent falling trends appears to be environmental rather than genetic.[71]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Age")
			print (" ")
			print ("IQ can change to some degree over the course of childhood.[72] However, in one longitudinal study, the mean IQ scores of ")
			print ("tests at ages 17 and 18 were correlated at r=0.86 with the mean scores of tests at ages five, six, and seven and at r=0.96 with")
			print ("the mean scores of tests at ages 11, 12, and 13.[9]")
			print (" ")
			print ("For decades, practitioners' handbooks and textbooks on IQ testing have reported IQ declines with age after the beginning of ")
			print ("adulthood. However, later researchers pointed out this phenomenon is related to the Flynn effect and is in part a cohort effect") 
			print ("rather than a true aging effect. A variety of studies of IQ and aging have been conducted since the norming of the first ")
			print ("Wechsler Intelligence Scale drew attention to IQ differences in different age groups of adults. Current consensus is that fluid")
			print ("intelligence generally declines with age after early adulthood, while crystallized intelligence remains intact. Both cohort")
			print ("effects (the birth year of the test-takers) and practice effects (test-takers taking the same form of IQ test more than once)") 
			print ("must be controlled to gain accurate data. It is unclear whether any lifestyle intervention can preserve fluid intelligence into ")
			print ("older ages.[73]")
			print (" ")
			print ("The exact peak age of fluid intelligence or crystallized intelligence remains elusive. Cross-sectional studies usually show ")
			print ("that especially fluid intelligence peaks at a relatively young age (often in the early adulthood) while longitudinal data ")
			print ("mostly show that intelligence is stable until mid-adulthood or later. Subsequently, intelligence seems to decline slowly.[74]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Genetics and environment")
			print (" ")
			print ("Environmental and genetic factors play a role in determining IQ. Their relative importance has been the subject of much ")
			print ("research and debate.[75]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Heritability")
			print ("See also: Heritability of IQ and Environment and intelligence")
			print (" ")
			print ("Heritability is defined as the proportion of variance in a trait which is attributable to genotype within a defined population ")
			print ("in a specific environment. A number of points must be considered when interpreting heritability.[76] Heritability, as a term, ")
			print ("applies to populations, and in populations there are variations in traits between individuals. Heritability measures how much ")
			print ("of that variation is caused by genetics. The value of heritability can change if the impact of environment (or of genes) in the ")
			print ("population is substantially altered. A high heritability of a trait does not mean environmental effects, such as learning, are") 
			print ("not involved. Since heritability increases during childhood and adolescence, one should be cautious drawing conclusions ")
			print ("regarding the role of genetics and environment from studies where the participants are not followed until they are adults.")
			print ("[citation needed]")
			print (" ")
			print ("The general figure for the heritability of IQ, according to an authoritative American Psychological Association report, is ")
			print ("0.45 for children, and rises to around 0.75 for late adolescents and adults.[77][78] Heritability measures in infancy are as ")
			print ("low as 0.2, around 0.4 in middle childhood, and as high as 0.9 in adulthood.[79][80] One proposed explanation is that people ")
			print ("with different genes tend to reinforce the effects of those genes, for example by seeking out different environments.[9][81]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Shared family environment")
			print (" ")
			print ("Family members have aspects of environments in common (for example, characteristics of the home). This shared family")
			print ("environment accounts for 0.25–0.35 of the variation in IQ in childhood. By late adolescence, it is quite low ")
			print ("(zero in some studies). The effect for several other psychological traits is similar. These studies have not looked at the ")
			print ("effects of such extreme environments, such as in abusive families.[9][82][83][84]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Non-shared family environment and environment outside the family")
			print (" ")
			print ("Although parents treat their children differently, such differential treatment explains only a small amount of ")				
			print ("nonshared environmental influence. One suggestion is that children react differently to the same environment because of ")
			print ("different genes. More likely influences may be the impact of peers and other experiences outside the family.[9][83]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Individual genes")
			print (" ")
			print ("A very large proportion of the over 17,000 human genes are thought to have an effect on the development and functionality of ")
			print ("the brain.[85] While a number of individual genes have been reported to be associated with IQ, none have a strong effect. Deary")
			print ("and colleagues (2009) reported that no finding of a strong single gene effect on IQ has been replicated.[86] Recent findings of ")
			print ("gene associations with normally varying intelligence differences in adults continue to show weak effects for any one gene;[87] ")
			print ("likewise in children,[88] but see.[89]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Gene-environment interaction")
			print (" ")
			print ("David Rowe reported an interaction of genetic effects with socioeconomic status, such that the heritability was high in ")
			print ("high-SES families, but much lower in low-SES families.[90] In the US, this has been replicated in infants,[91] children,[92]") 
			print ("adolescents,[93] and adults.[94] Outside the US, studies show no link between heritability and SES.[95] Some effects may even ")
			print ("reverse sign outside the US.[95][96]")
			print (" ")
			print ("Dickens and Flynn (2001) have argued that genes for high IQ initiate an environment-shaping feedback cycle, with genetic") 
			print ("effects causing bright children to seek out more stimulating environments that then further increase their IQ. In Dickens") 
			print ("model, environment effects are modeled as decaying over time. In this model, the Flynn effect can be explained by an increase") 
			print ("in environmental stimulation independent of it being sought out by individuals. The authors suggest that programs aiming to ")
			print ("increase IQ would be most likely to produce long-term IQ gains if they enduringly raised children's drive to seek out ")
			print ("cognitively demanding experiences.[97][98]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Interventions")
			print (" ")
			print ("In general, educational interventions, as those described below, have shown short-term effects on IQ, but long-term follow-up ")
			print ("is often missing. For example, in the US very large intervention programs such as the Head Start Program have not produced ")
			print ("lasting gains in IQ scores. More intensive, but much smaller projects such as the Abecedarian Project have reported lasting ")
			print ("effects, often on socioeconomic status variables, rather than IQ.[9]")
			print (" ")
			print ("Recent studies have shown that training in using one's working memory may increase IQ. A study on young adults published in") 
			print ("April 2008 by a team from the Universities of Michigan and Bern supports the possibility of the transfer of fluid intelligence") 
			print ("from specifically designed working memory training.[99] Further research will be needed to determine nature, extent and ")
			print ("duration of the proposed transfer. Among other questions, it remains to be seen whether the results extend to other kinds of") 
			print ("fluid intelligence tests than the matrix test used in the study, and if so, whether, after training, fluid intelligence ")
			print ("measures retain their correlation with educational and occupational achievement or if the value of fluid intelligence for ")
			print ("predicting performance on other tasks changes. It is also unclear whether the training is durable of extended periods of time.")
			print ("[100]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Music")
			print (" ")
			print ("Musical training in childhood has been found to correlate with higher than average IQ.[101][102] It is popularly thought that ")
			print ("listening to classical music raises IQ. However, multiple attempted replications (e.g.[103]) have shown that this is at best a ")
			print ("short-term effect (lasting no longer than 10 to 15 minutes), and is not related to IQ-increase.[104]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Brain anatomy")
			print ("Main article: Neuroscience and intelligence")
			print (" ")
			print ("Several neurophysiological factors have been correlated with intelligence in humans, including the ratio of brain weight to ")
			print ("body weight and the size, shape, and activity level of different parts of the brain. Specific features that may affect IQ ")
			print ("include the size and shape of the frontal lobes, the amount of blood and chemical activity in the frontal lobes, the total") 
			print ("amount of gray matter in the brain, the overall thickness of the cortex, and the glucose metabolic rate.[105]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Health")
			print ("Main articles: Impact of health on intelligence and Cognitive epidemiology")
			print (" ")
			print ("Health is important in understanding differences in IQ test scores and other measures of cognitive ability. Several factors ")
			print ("can lead to significant cognitive impairment, particularly if they occur during pregnancy and childhood when the brain is ")
			print ("growing and the blood–brain barrier is less effective. Such impairment may sometimes be permanent, sometimes be partially or") 
			print ("wholly compensated for by later growth.[citation needed]")
			print (" ")
			print ("Since about 2010, researchers such as Eppig, Hassel, and MacKenzie have found a very close and consistent link between IQ ")
			print ("scores and infectious diseases, especially in the infant and preschool populations and the mothers of these children.[106] ")
			print ("They have postulated that fighting infectious diseases strains the child's metabolism and prevents full brain development. ")
			print ("Hassel postulated that it is by far the most important factor in determining population IQ. However, they also found that ")
			print ("subsequent factors such as good nutrition and regular quality schooling can offset early negative effects to some extent.")
			print (" ")
			print ("Developed nations have implemented several health policies regarding nutrients and toxins known to influence cognitive function.")
			print ("These include laws requiring fortification of certain food products and laws establishing safe levels of pollutants (e.g. lead,")
			print ("mercury, and organochlorides). Improvements in nutrition, and in public policy in general, have been implicated in worldwide ")
			print ("IQ increases.[citation needed]")
			print (" ")
			print ("Cognitive epidemiology is a field of research that examines the associations between intelligence test scores and health. ")
			print ("Researchers in the field argue that intelligence measured at an early age is an important predictor of later health and ")
			print ("mortality differences.")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Social correlations")
			more1 = input("School performance")
			print (" ")
			print ("The American Psychological Association's report Intelligence: Knowns and Unknowns states that wherever it has been studied, ")
			print ("children with high scores on tests of intelligence tend to learn more of what is taught in school than their lower-scoring ")
			print ("peers. The correlation between IQ scores and grades is about .50. This means that the explained variance is 25%. Achieving good ")
			print ("grades depends on many factors other than IQ, such as ''persistence, interest in school, and willingness to study'' (p. 81).[9]")
			print (" ")
			print ("It has been found that the correlation of IQ scores with school performance depends on the IQ measurement used. For ")
			print ("undergraduate students, the Verbal IQ as measured by WAIS-R has been found to correlate significantly (0.53) with the grade")
			print ("point average (GPA) of the last 60 hours. In contrast, Performance IQ correlation with the same GPA was only 0.22 in the same") 
			print ("study.[107]")
			print (" ")
			print ("Some measures of educational aptitude correlate highly with IQ tests – for instance, Frey and Detterman (2004) reported a ")
			print ("correlation of 0.82 between g (general intelligence factor) and SAT scores;[108] another research found a correlation of 0.81")
			print ("between g and GCSE scores, with the explained variance ranging ''from 58.6% in Mathematics and 48% in English to 18.1% in Art ")
			print ("and Design''.[109]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Job performance")
			print (" ")
			print ("According to Schmidt and Hunter, ''for hiring employees without previous experience in the job the most valid predictor of ")
			print ("future performance is general mental ability.''[110] The validity of IQ as a predictor of job performance is above zero for ")
			print ("all work studied to date, but varies with the type of job and across different studies, ranging from 0.2 to 0.6.[111] The ")
			print ("correlations were higher when the unreliability of measurement methods was controlled for.[9] While IQ is more strongly ")
			print ("correlated with reasoning and less so with motor function,[112] IQ-test scores predict performance ratings in all occupations.")
			print ("[110] That said, for highly qualified activities (research, management) low IQ scores are more likely to be a barrier to ")
			print ("adequate performance, whereas for minimally-skilled activities, athletic strength (manual strength, speed, stamina, and ")
			print ("coordination) are more likely to influence performance.[110] The prevailing view among academics is that it is largely ")
			print ("through the quicker acquisition of job-relevant knowledge that higher IQ mediates job performance. This view has been ")
			print ("challenged by Byington & Felps (2010), who argued that ''the current applications of IQ-reflective tests allow individuals ")
			print ("with high IQ scores to receive greater access to developmental resources, enabling them to acquire additional capabilities") 
			print ("over time, and ultimately perform their jobs better.''[113]")
			print (" ")
			print ("In establishing a causal direction to the link between IQ and work performance, longitudinal studies by Watkins and others ")
			print ("suggest that IQ exerts a causal influence on future academic achievement, whereas academic achievement does not substantially") 
			print ("influence future IQ scores.[114] Treena Eileen Rohde and Lee Anne Thompson write that general cognitive ability, but not")
			print ("specific ability scores, predict academic achievement, with the exception that processing speed and spatial ability predict")
			print ("performance on the SAT math beyond the effect of general cognitive ability.[115]")
			print (" ")
			print ("The US military has minimum enlistment standards at about the IQ 85 level. There have been two experiments with lowering this")
			print ("to 80 but in both cases these men could not master soldiering well enough to justify their costs.[116]")
			more1 = input("Income")
			print (" ")
			print ("While it has been suggested that ''in economic terms it appears that the IQ score measures something with decreasing ")
			print ("marginal value. It is important to have enough of it, but having lots and lots does not buy you that much'',[117][118] ")
			print ("large-scale longitudinal studies indicate an increase in IQ translates into an increase in performance at all levels of IQ:") 
			print ("i.e. ability and job performance are monotonically linked at all IQ levels.[119][120] Charles Murray, coauthor of The Bell ")
			print ("Curve, found that IQ has a substantial effect on income independent of family background.[121]")
			print (" ")
			print ("The link from IQ to wealth is much less strong than that from IQ to job performance. Some studies indicate that IQ is unrelated")
			print ("to net worth.[122][123]")
			print (" ")
			print ("The American Psychological Association's 1995 report Intelligence: Knowns and Unknowns stated that IQ scores accounted for ")
			print ("(explained variance) about a quarter of the social status variance and one-sixth of the income variance. Statistical controls") 
			print ("for parental SES eliminate about a quarter of this predictive power. Psychometric intelligence appears as only one of a great")
			print ("many factors that influence social outcomes.[9]")
			print (" ")
			print ("In a meta-analysis, Strenze (2006) reviewed much of the literature and estimated the correlation between IQ and income to be ")
			print ("about 0.23.[124]")
			print (" ")
			print ("Some studies claim that IQ only accounts for (explains) a sixth of the variation in income because many studies are based on") 
			print ("young adults, many of whom have not yet reached their peak earning capacity, or even their education. On pg 568 of The g ")
			print ("Factor, Arthur Jensen claims that although the correlation between IQ and income averages a moderate 0.4 (one sixth or 16% ")
			print ("of the variance), the relationship increases with age, and peaks at middle age when people have reached their maximum career")
			print ("potential. In the book, A Question of Intelligence, Daniel Seligman cites an IQ income correlation of 0.5 (25% of the variance).")
			print (" ")
			print ("A 2002 study[125] further examined the impact of non-IQ factors on income and concluded that an individual's location, ")
			print ("inherited wealth, race, and schooling are more important as factors in determining income than IQ.")
			more1 = input("Crime")
			print (" ")
			print ("The American Psychological Association's 1995 report Intelligence: Knowns and Unknowns stated that the correlation between ")
			print ("IQ and crime was −0.2. It was −0.19 between IQ scores and number of juvenile offenses in a large Danish sample; with social")
			print ("class controlled, the correlation dropped to −0.17. A correlation of 0.20 means that the explained variance is 4%. The causal")
			print ("links between psychometric ability and social outcomes may be indirect. Children with poor scholastic performance may feel")
			print ("alienated. Consequently, they may be more likely to engage in delinquent behavior, compared to other children who do well.[9]")
			print (" ")
			print ("In his book The g Factor (1998), Arthur Jensen cited data which showed that, regardless of race, people with IQs between 70 ")
			print ("and 90 have higher crime rates than people with IQs below or above this range, with the peak range being between 80 and 90.")
			print (" ")
			print ("The 2009 Handbook of Crime Correlates stated that reviews have found that around eight IQ points, or 0.5 SD, separate criminals")
			print ("from the general population, especially for persistent serious offenders. It has been suggested that this simply reflects that ")
			print ("''only dumb ones get caught'' but there is similarly a negative relation between IQ and self-reported offending. That children")
			print ("with conduct disorder have lower IQ than their peers ''strongly argues'' for the theory.[126]")
			print (" ")
			print ("A study of the relationship between US county-level IQ and US county-level crime rates found that higher average IQs were ")
			print ("associated with lower levels of property crime, burglary, larceny rate, motor vehicle theft, violent crime, robbery, and ")
			print ("aggravated assault. These results were not ''confounded by a measure of concentrated disadvantage that captures the effects")
			print ("of race, poverty, and other social disadvantages of the county.''[127][128]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Health and mortality")
			print (" ")
			print ("Multiple studies conducted in Scotland have found that higher IQs in early life are associated with lower mortality and")
			print ("morbidity rates later in life.[129][130]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Other accomplishments")
			print ("Average adult combined IQs associated with real-life accomplishments by various tests[131][132] Accomplishment 	IQ 	Test/study ")
			print ("Year")
			print ("MDs, JDs, and PhDs 	125 	WAIS-R 	1987")
			print ("College graduates 	112 	KAIT 	2000")
			print ("K-BIT 	1992")
			print ("115 	WAIS-R") 	
			print ("1–3 years of college 	104 	KAIT ")	
			print ("K-BIT 	")
			print ("105–110 	WAIS-R 	")
			print ("Clerical and sales workers 	100–105 		")
			print ("High school graduates, skilled workers (e.g., electricians, cabinetmakers) 	100 	KAIT ")	
			print ("WAIS-R 	")
			print ("97 	K-BIT 	")
			print ("1–3 years of high school (completed 9–11 years of school) 	94 	KAIT 	")
			print ("90 	K-BIT 	")
			print ("95 	WAIS-R 	")
			print ("Semi-skilled workers (e.g. truck drivers, factory workers) 	90–95 ")		
			print ("Elementary school graduates (completed eighth grade) 	90 		")
			print ("Elementary school dropouts (completed 0–7 years of school) 	80–85 		")
			print ("Have 50/50 chance of reaching high school 	75 		")
			print ("Average IQ of various occupational groups:[133] Accomplishment 	IQ 	Test/study 	Year")
			print ("Professional and technical 	112 		")
			print ("Managers and administrators 	104 		")
			print ("Clerical workers, sales workers, skilled workers, craftsmen, and foremen 	101 		")
			print ("Semi-skilled workers (operatives, service workers, including private household) 	92") 		
			print ("Unskilled workers 	87 		")
			print ("Type of work that can be accomplished:[131] Accomplishment 	IQ 	Test/study 	Year")
			print ("Adults can harvest vegetables, repair furniture 	60 ")		
			print ("Adults can do domestic work 	50 	")	
			print (" ")
			print ("There is considerable variation within and overlap among these categories. People with high IQs are found at all levels of ")
			print ("education and occupational categories. The biggest difference occurs for low IQs with only an occasional college graduate or")
			print ("professional scoring below 90.[22]")
			more1 = input("Group-IQ or the collective intelligence factor c")
			print ("\n\n\n\n\n\n\n")
			print ("Main article: Collective intelligence")
			print (" ")
			print ("With operationalization and methodology derived from the general intelligence factor g, a new scientific understanding of ")
			print ("collective intelligence, defined as a group’s general ability to perform a wide range of tasks,[134] aims to explain ")
			print ("intelligent behavior of groups. Goal is to detect and explain a general intelligence factor c for groups, parallel to the g ")
			print ("factor for individuals. As g is highly interrelated with the concept of IQ,[135][136] this measurement of collective ")
			print ("intelligence can be interpreted as intelligence quotient for groups (Group-IQ) even though the score is not a quotient per se")
			print ("Current evidence suggests that this Group-IQ is only moderately correlated with group members' IQs but with other correlates")
			print ("such as group members' Theory of Mind.[134]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Group differences")
			print (" ")
			print ("Among the most controversial issues related to the study of intelligence is the observation that intelligence measures such as ")
			print ("IQ scores vary between ethnic and racial groups and sexes. While there is little scholarly debate about the existence of some ")
			print ("of these differences, their causes remain highly controversial both within academia and in the public sphere.[137]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Sex")
			print ("Main article: Sex differences in intelligence")
			print (" ")
			print ("Most IQ tests are constructed so that there are no overall score differences between females and males.[9][138] Popular IQ ")
			print ("batteries such as the WAIS and the WISC-R are also constructed in order to eliminate sex differences.[139] In a paper")
			print ("presented at the International Society for Intelligence Research in 2002, it was pointed out that because test constructors")
			print ("and the United States' Educational Testing Service (which developed the US SAT test) often eliminate items showing marked ")
			print ("sex differences in order to reduce the perception of bias, the ''true sex'' difference is masked. Items like the Mental ")
			print ("Rotations Test and reaction time tests, which show a male advantage in IQ, are often removed.[140] Meta-analysis focusing on") 
			print ("gender differences in math performance found nearly identical performance for boys and girls,[141] and the subject of ")
			print ("mathematical intelligence and gender has been controversial.[142]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("IQ by country")
			more1 = input("Race and intelligence")
			print ("Main articles: Race and intelligence and Nations and intelligence")
			print ("Race and intelligence in United States of America")
			print (" ")
			print ("The 1996 Task Force investigation on Intelligence sponsored by the American Psychological Association concluded that there")
			print ("are significant variations in IQ across races.[9] The problem of determining the causes underlying this variation relates ")
			print ("to the question of the contributions of ''nature and nurture'' to IQ. Psychologists such as Alan S. Kaufman[143] and Nathan")
			print ("Brody[144] and statisticians such as Bernie Devlin[145] argue that there are insufficient data to conclude that this is ")
			print ("because of genetic influences. A review article published in 2012 by leading scholars on human intelligence concluded, ")
			print ("after reviewing the prior research literature, that group differences in IQ are best understood as environmental in origin.")
			print ("[146]")
			print (" ")
			print ("In considering disparities between test results of different ethnic groups, one might investigate the effects of stereotype ")
			print ("threat (a situational predicament in which a person feels at risk of confirming negative stereotypes about the group(s) he ")
			print ("identifies with),[147] as well as culture and acculturation.[148] This phenomenon has been criticized as a fiction of ")
			print ("publication bias.[149]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Public policy")
			print ("Main article: Intelligence and public policy")
			print (" ")
			print ("In the United States, certain public policies and laws regarding military service,[150][151] education, public benefits,")
			print ("[152] capital punishment,[153] and employment incorporate an individual's IQ into their decisions. However, in the case of") 
			print ("Griggs v. Duke Power Co. in 1971, for the purpose of minimizing employment practices that disparately impacted racial")
			print ("minorities, the U.S. Supreme Court banned the use of IQ tests in employment, except when linked to job performance via a job") 
			print ("analysis. Internationally, certain public policies, such as improving nutrition and prohibiting neurotoxins, have as one of ")
			print ("their goals raising, or preventing a decline in, intelligence.")
			print (" ")
			print ("A diagnosis of intellectual disability is in part based on the results of IQ testing. Borderline intellectual functioning is a") 
			print ("categorization where a person has below average cognitive ability (an IQ of 71–85), but the deficit is not as severe as ")
			print ("intellectual disability (70 or below).")
			print (" ")
			print ("In the United Kingdom, the eleven plus exam which incorporated an intelligence test has been used from 1945 to decide, at")
			print ("eleven years of age, which type of school a child should go to. They have been much less used since the widespread ")
			print ("introduction of comprehensive schools.")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Criticism and views")
			more1 = input("Relationship to intelligence")
			print ("See also: Intelligence")
			print (" ")
			print ("IQ is the most thoroughly researched means of measuring intelligence, and by far the most widely used in practical settings. ")
			print ("However, while IQ strives to measure some concepts of intelligence, it may fail to serve as an accurate measure of broader ")
			print ("definitions of intelligence. IQ tests examine some areas of intelligence, while neglecting to account for other areas, such as")
			print ("creativity and social intelligence.")
			print (" ")
			print ("Critics such as Keith Stanovich do not dispute the reliability of IQ test scores or their capacity to predict some kinds of")
			print ("achievement, but argue that basing a concept of intelligence on IQ test scores alone neglects other important aspects of") 
			print ("mental ability.[9][154]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Criticism of IQ")
			print (" ")
			print ("Some scientists dispute the worthiness of IQ entirely. In The Mismeasure of Man (1996), paleontologist Stephen Jay Gould")
			print ("criticized IQ tests and argued that they were used for scientific racism. He argued that g was a mathematical artifact and") 
			print ("criticized:")
			print (" ")
			print ("	...the abstraction of intelligence as a single entity, its location within the brain, its quantification as one number ")
			print ("for each individual, and the use of these numbers to rank people in a single series of worthiness, invariably to find that ")
			print ("oppressed and disadvantaged groups—races, classes, or sexes—are innately inferior and deserve their status.[155] ")
			print (" ")
			print ("Arthur Jensen responded:")
			print (" ")
			print ("    ...what Gould has mistaken for ''reification'' is neither more nor less than the common practice in every science of") 
			print ("hypothesizing explanatory models to account for the observed relationships within a given domain. Well known examples ")
			print ("include the heliocentric theory of planetary motion, the Bohr atom, the electromagnetic field, the kinetic theory of gases,") 
			print ("gravitation, quarks, Mendelian genes, mass, velocity, etc. None of these constructs exists as a palpable entity occupying")
			print ("physical space.[156] ")
			print (" ")
			print ("Jensen also argued that even if g were replaced by a model with several intelligences this would change the situation less ")
			print ("than expected. He argues that all tests of cognitive ability would continue to be highly correlated with one another and there")
			print ("would still be a black-white gap on cognitive tests.[157] Hans Eysenck responded to Gould by stating that no psychologist had")
			print ("said that intelligence was an area located in the brain.[158] Eysenck also argued IQ tests were not racist, pointing out that")
			print ("Northeast Asians and Jews both scored higher than non-Jewish Europeans on IQ tests, and this would not please European racists.")
			print ("[159]")
			print (" ")
			print ("Psychologist Peter Schönemann persistently criticized IQ, calling it ''the IQ myth''. He argued that g is a flawed theory")
			print ("and that the high heritability estimates of IQ are based on false assumptions.[160][161] Robert Sternberg, another significant")
			print ("critic of g as the main measure of human cognitive abilities, argued that reducing the concept of intelligence to the")
			print ("measure of g does not fully account for the different skills and knowledge types that produce success in human society.[162]")
			more1 = input("Systematic exclusion of threshold effects")
			print ("\n\n\n\n\n\n\n")
			print (" ")
			print ("Cecil Reynolds and Paul Kline argue that the construction of IQ tests around the rule that they should show a bell curve")
			print ("distribution in the population leads to systematic exclusion of cognitive tests that display threshold effects and are not")
			print ("gradually variable, as well as biasing IQ tests towards questions that can be made to fit a bell curve model and against")
			print ("questions that show any non-bell distributions. They argue that just as swarms change their collective behavior at certain")
			print ("thresholds of animals in the swarm, it is possible that brains change their abilities at thresholds of number of connected ")
			print ("neurons and/or level of connectivity. Cecil Reynolds and Paul Kline argue that such a bias may be the reason why IQ tests")
			print ("yield paradoxes such as the heredity paradox between high heredity showed by twin studies and the high environmental")
			print ("effect shown by the Flynn effect and suggest that other cognitive tests that do not conform to bell curve distributions")
			print ("should be tried with the possibility that some of them may produce falsifiable predictions of key abilities requiring a ")
			print ("critical level of underlying quantitative brain access and simpler proxies of such in every case, unlike IQ tests which")
			print ("are argued to fail the falsifiability criterion by defining away problems by systematically demanding bell curves and ")
			print ("failing to make any absolute system requirement predictions of what brain capacity is required to make a certain ")
			print ("performance. It is argued that probabilistic predictions with loopholes for ''exceptions'' are not scientifically ")
			print ("appliceable to capacity theories, as capacities follow minimum system requirements for performing tasks.[163][164]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Test bias")
			print ("See also: Stereotype threat")
			print (" ")
			print ("The American Psychological Association's report Intelligence: Knowns and Unknowns stated that in the United States IQ tests") 
			print ("as predictors of social achievement are not biased against African Americans since they predict future performance, ")
			print ("such as school achievement, similarly to the way they predict future performance for Caucasians.[9] While agreeing that ")
			print ("IQ tests predict performance equally well for all racial groups, Nicholas Mackintosh also points out that there may still") 
			print ("be a bias inherent in IQ testing if the education system is also systematically biased against African Americans, in")
			print ("which case educational performance may in fact also be an underestimation of African American children's cognitive")
			print ("abilities.[165] Earl Hunt points out that while this may be the case that would not be a bias of the test, but of society.[166]")
			print (" ")
			print ("However, IQ tests may well be biased when used in other situations. A 2005 study stated that ''differential validity in ")
			print ("prediction suggests that the WAIS-R test may contain cultural influences that reduce the validity of the WAIS-R as a measure") 
			print ("of cognitive ability for Mexican American students,''[167] indicating a weaker positive correlation relative to sampled ")
			print ("white students. Other recent studies have questioned the culture-fairness of IQ tests when used in South Africa.[168][169]") 
			print ("Standard intelligence tests, such as the Stanford-Binet, are often inappropriate for autistic children; the alternative of ")
			print ("using developmental or adaptive skills measures are relatively poor measures of intelligence in autistic children, and may ")
			print ("have resulted in incorrect claims that a majority of autistic children are mentally retarded.[170]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Intermingling cultures and IQ classification fairness")
			print (" ")
			print ("Barbara P. Uzzell and Harvey N. Switzky argue that defining IQ from an average at a period of time and putting different")
			print ("thresholds of what is considered retarded based on average IQ test performance in a culture faces issues of defining who ")
			print ("belongs to what culture. They argue that since people are not actually in boxes of isolated cultures, essentialistic ")
			print ("classification of culture that is said to make IQ tests ''culturally fair'' will show false ''evidence'' of underlying ")
			print ("cognitive differences between individuals who are formally classified in the same culture but have faced different cultural") 
			print ("non-shared environments due to the fluid intermingling of cultures in real life, making IQ tests a false measure of mental ")
			print ("retardation. It is argued by Barbara P. Uzzell and Harvey N. Switzky that different social treatment depending on hereditary ")
			print ("factors in appearance that may not necessarily be classified as ''racial'' but can often be considered individual leads to an")
			print ("appearance of genes for such appearances being linked to learned behaviors and false evidence of the genes affecting the ")
			print ("brain's response to the environment, and that environmental differences in whether other people with whom a person speaks are") 
			print ("willing to counter misunderstandings with factual arguments or dismisses the person as ''incapable of reasoning if he or she ")
			print ("does not already know it'' creates differences in the opportunities to learn rules that can be used for solving problems in ")
			print ("IQ tests and that widespread persistence of such cultural treatment gives a false appearance of IQ tests being reliable ")
			print ("and valid measures of underlying cognitive abilities. It is argued that such effects of different opportunities to ")
			print ("sharpen arguments through debate in all walks of life, including prejudice towards choice of words shaped by earlier ")
			print ("differences in debate opportunities, make different predictions than lab setting only stereotype threat theory and ")
			print ("must therefore be tested by different evidence than that theory, and that discrimination in society based on choice of") 
			print ("words is a possible explanation of apparent links between IQ test performance and success in society.[171][172]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Outdated methodology")
			print ("See also: Psychometrics")
			print (" ")
			print ("According to a 2006 article, contemporary psychological research often did not reflect substantial recent developments in ")
			print ("psychometrics and ''bears an uncanny resemblance to the psychometric state of the art as it existed in the 1950s.''[173]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Intelligence: Knowns and Unknowns")
			print (" ")
			print ("In response to the controversy surrounding The Bell Curve, the American Psychological Association's Board of Scientific ")
			print ("Affairs established a task force in 1995 to write a report on the state of intelligence research which could be used by all") 
			print ("sides as a basis for discussion, Intelligence: Knowns and Unknowns. The full text of the report is available through several ")
			print ("websites.[9]")
			print (" ")
			print ("In this paper, the representatives of the association regret that IQ-related works are frequently written with a view to ")
			print ("their political consequences: ''research findings were often assessed not so much on their merits or their scientific ")
			print ("standing as on their supposed political implications''.")
			print (" ")
			print ("The task force concluded that IQ scores do have high predictive validity for individual differences in school ")
			print ("achievement. They confirm the predictive validity of IQ for adult occupational status, even when variables such as ")
			print ("education and family background have been statistically controlled. They stated that individual differences in ")
			print ("intelligence are substantially influenced by both genetics and environment.")
			print (" ")
			print ("The report stated that a number of biological factors, including malnutrition, exposure to toxic substances, and various ")
			print ("prenatal and perinatal stressors, result in lowered psychometric intelligence under at least some conditions. The task ")
			print ("force agrees that large differences do exist between the average IQ scores of blacks and whites, saying")
			print (" ")
			print ("	The cause of that differential is not known; it is apparently not due to any simple form of bias in the content or ")
			print ("	administration of the tests themselves. The Flynn effect shows that environmental factors can produce differences of at") 
			print ("	least this magnitude, but that effect is mysterious in its own right. Several culturally based explanations of the ")
			print ("	Black/ White IQ differential have been proposed; some are plausible, but so far none has been conclusively supported.") 
			print ("	There is even less empirical support for a genetic interpretation. In short, no adequate explanation of the ")
			print ("	differential between the IQ means of Blacks and Whites is presently available. ")
			print (" ")
			print ("The APA journal that published the statement, American Psychologist, subsequently published eleven critical responses in ")
			print ("January 1997, several of them arguing that the report failed to examine adequately the evidence for partly genetic ")
			print ("explanations.")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Dynamic assessment")
			print (" ")
			print ("An alternative to standard IQ tests originated in the writings of psychologist Lev Vygotsky (1896–1934) from his ")
			print ("last two years of work.[174][175] The notion of the zone of proximal development that he introduced in 1933, ")
			print ("roughly a year before his death, served as the banner for his proposal to diagnose development as the level of actual") 
			print ("development that can be measured by the child's independent problem solving and, at the same time, the level of proximal,") 
			print ("or potential development that is measured in the situation of moderately assisted problem solving by the child.[176] The ")
			print ("maximum level of complexity and difficulty of the problem that the child is capable to solve under some guidance indicates ")
			print ("the level of potential development. Then, the difference between the higher level of potential and the lower level of ")
			print ("actual development indicates the zone of proximal development. Combination of the two indexes—the level of actual and the") 
			print ("zone of the proximal development—according to Vygotsky, provides a significantly more informative indicator of psychological") 
			print ("development than the assessment of the level of actual development alone.[177][178]")
			print (" ")
			print ("The ideas on the zone of development were later developed in a number of psychological and educational theories and ")
			print ("practices. Most notably, they were developed under the banner of dynamic assessment that focuses on the testing of ")
			print ("learning and developmental potential[179][180][181] (for instance, in the work of Reuven Feuerstein and his associates,[182]") 
			print ("who has criticized standard IQ testing for its putative assumption or acceptance of ''fixed and immutable'' characteristics ")
			print ("of intelligence or cognitive functioning). Grounded in developmental theories of Vygotsky and Feuerstein, who maintained ")
			print ("that human beings are not static entities but are always in states of transition and transactional relationships with the ")
			print ("world, dynamic assessment received also considerable support in the recent revisions of cognitive developmental theory by ")
			print ("Joseph Campione, Ann Brown, and John D. Bransford and in theories of multiple intelligences by Howard Gardner and Robert ")
			print ("Sternberg.[183] Still, dynamic assessment has not been implemented in education on a large scale as is up to now, by ")
			print ("admission of one of its notable proponents, ''in search of its identity''.[184]")
			print ("\n\n\n\n\n\n\n")
			more1 = input("Classification")
			print ("Main article: IQ classification")
			print (" ")
			print ("IQ classification is the practice used by IQ test publishers for designating IQ score ranges into various categories with ")
			print ("labels such as ''superior'' or ''average.''[185] IQ classification was preceded historically by attempts to classify human ")
			print ("beings by general ability based on other forms of behavioral observation. Those other forms of behavioral observation are ")
			print ("still important for validating classifications based on IQ tests.")
			print ("\n\n\n\n\n\n\n")
			more1 = input("High IQ societies")
			print ("Main article: High IQ society")
			print (" ")
			print ("There are social organizations, some international, which limit membership to people who have scores as high as or ")
			print ("higher than the 98th percentile (2 standard deviations above the mean) on some IQ test or equivalent. Mensa International") 
			print ("is perhaps the best known of these. The largest 99.9th percentile (3 standard deviations above the mean) society is the")
			print ("Triple Nine Society. ")
			print ("\n\n\n\n\n\n\n")
			noMore = input("Press [ENTER] key to quit")
		if WikIDSelect == 30008:
			print ("Bit slicing is a technique for constructing a processor from modules of processors of smaller bit width, for the purpose of ")
			print ("increasing the word length; in theory to make an arbitrary n-bit CPU. Each of these component modules processes one bit ")
			print ("field or 'slice' of an operand. The grouped processing components would then have the capability to process the chosen full ")
			print ("word-length of a particular software design.")
			print (" ")
			print ("Bit slicing more or less died out due to the advent of the microprocessor. Recently it's been used in ALUs for quantum ")
			print ("computers, and has been used as a software technique (e.g. in x86 CPUs, for cryptography.[1])")
			more1 = input("Contents")
			print (" ")
			print ("1 Operational details")
			print ("2 Historical necessity")
			print ("3 Modern use")
			print ("3.1 Software use on non-bit-slice hardware")
			print ("3.2 Bit-sliced quantum computers")
			print ("4 See also")
			print ("5 References")
			print ("6 External links")
			print (" ")
			more1 = input("Operational details")
			print (" ")
			print ("Bit slice processors usually include an arithmetic logic unit (ALU) of 1, 2, 4, 8 or 16 bits and control lines ")
			print ("(including carry or overflow signals that are internal to the processor in non-bitsliced CPU designs).")
			print (" ")
			print ("For example, two 4-bit ALU chips could be arranged side by side, with control lines between them, to form an 8-bit ALU")
			print ("(result need not be power of two, e.g. three 1-bit can make a 3-bit ALU,[2] thus 3-bit (or n-bit) CPU, while 3-bit, or any") 
			print ("CPU with higher odd-number of bits, hasn't been manufactured and sold in volume). Four 4-bit ALU chips could be used to") 
			print ("build a 16-bit ALU. It would take eight chips to build a 32-bit word ALU. The designer could add as many slices as ")
			print ("required to manipulate increasingly longer word lengths.")
			print (" ")
			print ("A microsequencer or control ROM would be used to execute logic to provide data and control signals to regulate function of ")
			print ("the component ALUs.")
			print (" ")
			print ("Known bit-slice microprocessor modules:")
			print (" ")
			print ("1-bit slice:")
			print ("...")
			print (" ")
			print ("2-bit slice:")
			print ("Intel 3000 family (1974), e.g. Intel 3002 with Intel 3001, second-sourced by Signetics and Intersil[3]")
			print ("Signetics 8X02 family (1977)[4]")
			print (" ")
			print ("4-bit slice:")
			print ("National GPC/P / IMP-4 (1973),[5] second-sourced by Rockwell")
			print ("National IMP-16 family (1973), e.g. IMP-00A/520D (RALU) with IMP16A/521D and IMP16A/522D, cascadable up to 16 bit")
			print ("AMD Am2900 family (1975), e.g. AM2901, AM2903")
			print ("Monolithic Memories 5700/6700 family (1974)[6][7][8][9] e.g. MMI 5701 / MMI 6701, second-sourced by ITT Semiconductors")
			print ("Texas Instruments SBP0400 (1975), cascadable up to 16 bit")
			print ("Texas Instruments SN74181 (1970)")
			print ("Texas Instruments SN74S281 with SN74S282")
			print ("Texas Instruments SN74S481 with SN74S482 (1976)[10]")
			print ("Fairchild 9400 (MACROLOGIC), 4700")
			print ("Motorola M10800 family (1979),[11] e.g. MC10800")
			print (" ")
			print ("8-bit slice:")
			print ("National IMP-8 family (1974), cascadable up to 32-bit")
			print ("Texas Instruments SN54AS888 / SN74AS888")
			print ("Fairchild 100K")
			print ("ZMD U830C [de] (1978/1981), cascadable up to 32 bit")
			print ("16-bit slice:")
			print ("AMD Am29100 family")
			print ("Synopsys 49C402")
			print (" ")
			more1 = input("Historical necessity")
			print (" ")
			print ("Bit slicing, although not called that at the time, was also used in computers before large scale integrated circuits ")
			print ("(LSI, the predecessor to today's VLSI, or very-large-scale integration circuits). The first bit-sliced machine was ")
			print ("EDSAC 2, built at the University of Cambridge Mathematical Laboratory in 1956–1958.[citation needed]")
			print (" ")
			print ("Prior to the mid-1970s and late 1980s there was some debate over how much bus width was necessary in a given computer system ")
			print ("to make it function. Silicon chip technology and parts were much more expensive than today. Using multiple, simpler, and ")
			print ("thus less expensive ALUs was seen[by whom?] as a way to increase computing power in a cost effective manner. ")
			print ("While 32-bit architecture microprocessors were being discussed at the time,[by whom?] few were in production.[citation needed]")
			print (" ")
			print ("The UNIVAC 1100 series mainframes (one of the oldest series, originating in the 1950s) has a 36-bit architecture and the ")
			print ("1100/60 introduced in 1979 used nine Motorola MC10800 4-bit ALU[11] chips to implement the needed word width while using ")
			print ("modern integrated circuits.[12]")
			print (" ")
			print ("At the time 16-bit processors were common but expensive, and 8-bit processors, such as the Z80, were widely used in the ")
			print ("nascent home computer market.")
			print (" ")
			print ("Combining components to produce bit slice products allowed engineers and students to create more powerful and complex ")
			print ("computers at a more reasonable cost, using off-the-shelf components that could be custom-configured. The complexities ")
			print ("of creating a new computer architecture were greatly reduced when the details of the ALU were already specified (and debugged).")
			print (" ")
			print ("The main advantage was that bit slicing made it economically possible in smaller processors to use bipolar transistors,")
			print ("[citation needed] which switch much faster than NMOS or CMOS transistors.[citation needed] This allowed for much higher ")
			print ("clock rates, where speed was needed; for example DSP functions or matrix transformation, or as in the Xerox Alto, the ")
			print ("combination of flexibility and speed, before discrete CPUs were able to deliver that.")
			more1 = input("Modern use")
			print ("Software use on non-bit-slice hardware")
			print ("")
			print ("In more recent times, the term bit-slicing was re-coined by Matthew Kwan[13] to refer to the technique of using a") 
			print ("general purpose CPU to implement multiple parallel simple virtual machines using general logic instructions to ")
			print ("perform Single Instruction Multiple Data (SIMD) operations. This technique is also known as SIMD Within A Register (SWAR).")
			print (" ")
			print ("This was initially in reference to Eli Biham's 1997 paper A Fast New DES Implementation in Software,[14] which achieved ")
			print ("significant gains in performance of DES by using this method.")
			more1 = input("Bit-sliced quantum computers")
			print (" ")
			print ("To simplify the circuit structure and reduces the hardware cost of quantum computers (proposed to run the MIPS32 ")
			print ("instruction set) a 50 GHz superconducting ''4-bit bit-slice arithmetic logic unit (ALU) for 32-bit rapid single-flux-quantum") 
			print ("microprocessors was demonstrated.''[15] ")
			noMore = input("Press [ENTER] to quit")
if uCMainConsole == 5:
	konloop == 0
	conloop = int(1)
	while conloop == 1:
		print ("Public calculator")
		print ("The unlocked speed-dial calculator")
		print ("Type: 64 bit")
		print ("Language: English")
		ent1 = input("Access public calculator by pressing enter once (DO NOT TYPE ANYTHING)")
		if ent1 == (""):
			print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\nCalculator ultimate")
			print ("|==================================================================|==================================================================|")
			print ("| Select a mode                                                    | Choose for me                                            [ID: 0] |")
			print ("|                                                                  |                                                                  |")
			print ("| Currency                              [ID: 10] .                 | Modular division                      [ID: 11]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Addition                              [ID: 12]                   | Subtraction                           [ID: 13]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Multiplication                        [ID: 14]                   | Division                              [ID: 15]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Distributive                          [ID: 16]                   | Temperature                           [ID: 17]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Weight                                [ID: 18]                   | Distance                              [ID: 19]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Number graph                          [ID: 20]                   | Square root                           [ID: 21]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| RGB Colors                            [ID: 22]                   | Speed                                 [ID: 23]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Energy                                [ID: 24]                   | Days since                            [ID: 25]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Years since                           [ID: 26]                   | Days between                          [ID: 27]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Years between                         [ID: 28]                   | Percentage                            [ID: 29]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Addition with decimals                [ID: 30]                   | Subtraction with decimals             [ID: 31]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Multiplication with decimals          [ID: 32]                   | Division with decimals                [ID: 33]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Modular division with decimals        [ID: 34]                   | First 100,000 digits of PI            [ID: 35]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Greater than                          [ID: 36]                   | Less than                             [ID: 37]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Greater than or equal to              [ID: 38]                   | Less than or equal to                 [ID: 39]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Not equal to                          [ID: 40]                   | Equal to                              [ID: 41]                   |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Greater than (with decimals)          [ID: 42]                   | Less than or equal (with decimals)                     [ID: 43]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Greater than or equal to (with decimals)               [ID: 44]  | Less than or equal to (with decimals)                  [ID: 46]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Greater than (with decimals)                           [ID: 47]  | Not equal to (with decimals)                           [ID: 48]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Equal to (with decimals)                               [ID: 49]  | Generate a random number                               [ID: 50]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Generate a random number (with decimals)               [ID: 51]  | Min and Max                                            [ID: 52]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Memory calculator                                      [ID: 53]  | Vote counter                                           [ID: 54]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| Roman numeral calculator                               [ID: 55]  | Grade calculator                                       [ID: 56]  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("| IQ Calculator                                          [ID: 57]  |                                                                  |")
			print ("|------------------------------------------------------------------|------------------------------------------------------------------|")
			print ("|                                                                  |                                                                  |")
			print ("=======================================================================================================================================")
			print ("\n\n")
			# randomiz = int(input("For randomizer users, press 0 to continue"))
			print ("This feature is not yet functional, sorry :/")
			calcIDSes = int(input("Enter an ID to continue: "))
			# if calcIDSes == 0:
			#	calcIDSes == (random.randint (10, 52)
			if calcIDSes == 10:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Currency calculator")
				print ("Select a currency to get started")
				print ("$ - ID: 1")
				print ("¢ - ID: 2")
				print ("¥ - ID: 3")
				print ("£ - ID: 4")
				currencyID = int(input("Enter an ID (1-4): "))
				if (currencyID == 1 or 2 or 3 or 4):
					print ("Currency verified")
					currencystr = str
					if (currencyID == 1):
						currencystr == ("$")
						print ("Currency selected: $")
					if (currencyID == 2):
						currencystr == ("¢")
						print ("Currency selected: ¢")
					if (currencyID == 3):
						currencystr == ("¥")
						print ("Currency selected: ¥")
					if (currencyID == 4):
						currencystr == ("£")
						print ("Currency selected: £")
					print ("\n\n")
					currencycalc1 = float(input("Enter an amount: "))
					currencycalc2 = int(input("Select a calculation type:\n| + | ID = 1 | - | ID = 2 | * | ID = 3 | / | ID = 4 | % | ID = 5 | "))
					currencycalc3 = float(input("Enter second amount: "))
					if (currencycalc2 == 1 and currencyID == 1):
						currencytotal = float(currencycalc1 + currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "$")
					if (currencycalc2 == 1 and currencyID == 2):
						currencytotal = float(currencycalc1 + currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¢")
					if (currencycalc2 == 1 and currencyID == 3):
						currencytotal = float(currencycalc1 + currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¥")
					if (currencycalc2 == 1 and currencyID == 4):
						currencytotal = float(currencycalc1 + currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "£")
					if (currencycalc2 == 2 and currencyID == 1):
						currencytotal = float(currencycalc1 - currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "$")
					if (currencycalc2 == 2 and currencyID == 2):
						currencytotal = float(currencycalc1 - currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¢")
					if (currencycalc2 == 2 and currencyID == 3):
						currencytotal = float(currencycalc1 - currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¥")
					if (currencycalc2 == 2 and currencyID == 4):
						currencytotal = float(currencycalc1 - currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "£")
					if (currencycalc2 == 3 and currencyID == 1):
						currencytotal = float(currencycalc1 * currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "$")
					if (currencycalc2 == 3 and currencyID == 2):
						currencytotal = float(currencycalc1 * currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¢")
					if (currencycalc2 == 3 and currencyID == 3):
						currencytotal = float(currencycalc1 * currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¥")
					if (currencycalc2 == 3 and currencyID == 4):
						currencytotal = float(currencycalc1 * currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "£")
					if (currencycalc2 == 4 and currencyID == 1):
						currencytotal = float(currencycalc1 / currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "$")
					if (currencycalc2 == 4 and currencyID == 2):
						currencytotal = float(currencycalc1 / currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¢")
					if (currencycalc2 == 4 and currencyID == 3):
						currencytotal = float(currencycalc1 / currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¥")
					if (currencycalc2 == 4 and currencyID == 4):
						currencytotal = float(currencycalc1 / currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "£")
					if (currencycalc2 == 5 and currencyID == 1):
						currencytotal = float(currencycalc1 % currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "$")
					if (currencycalc2 == 5 and currencyID == 2):
						currencytotal = float(currencycalc1 % currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¢")
					if (currencycalc2 == 5 and currencyID == 3):
						currencytotal = float(currencycalc1 % currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "¥")
					if (currencycalc2 == 5 and currencyID == 4):
						currencytotal = float(currencycalc1 % currencycalc3)
						print ("The current amount is: " + str(currencytotal) + "£")
					bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 11:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Modular division")
				modivision1 = int(input("Enter first number to mod: "))
				modivision2 = int(input("Enter second number to mod: "))
				curanswer = (modivision1 % modivision2)
				print ("The remainder of " + str(modivision1) + " and " + str(modivision2) + " is " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 12:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Addition")
				add1 = int(input("Enter first number to add: "))
				add2 = int(input("\nEnter second number to add: "))
				add3 = int(input("\nEnter third number to add (if you only want to use 2 numbers, type 0): "))
				add4 = int(input("\nEnter fourth number to add (if you only want to use 2 numbers, type 0): "))
				add5 = int(input("\nEnter fifth number to add (if you only want to use 2 numbers, type 0): "))
				curanswer = (add1 + add2 + add3 + add4 + add5)
				print ("\n\nThe answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 13:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Subtract")
				minus1 = int(input("Enter first number to subtract: "))
				minus2 = int(input("\nEnter second number to subtract: "))
				minus3 = int(input("\nEnter third number to subtract (if you only want to use 2 numbers, type 0): "))
				minus4 = int(input("\nEnter fourth number to subtract (if you only want to use 2 numbers, type 0): "))
				minus5 = int(input("\nEnter fifth number to subtract (if you only want to use 2 numbers, type 0): "))
				curanswer = (minus1 - minus2 - minus3 - minus4 - minus5)
				print ("\n\nThe answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 14:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Multiply")
				multiply1 = int(input("Enter first number to multiply: "))
				multiply2 = int(input("Enter second number to multiply: "))
				curanswer = (multiply1 * multiply2)
				print ("\n\nThe answer is: " + str(curanswer)) 
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 15:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Divide")
				divided1 = int(input("Enter first number to divide: "))
				divided2 = int(input("Enter second number to divide: "))
				curanswer = (divided1 / divided2)
				print ("\n\nThe answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 16:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Distributive")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate distributive properties")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 17:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Temperature")
				fahOrCel = int(input("What do you want to start with? Fahrenheit (1) Celsius (2) "))
				if fahOrCel == 1:
					fahent = float(input("Enter the temperature in Fahrenheit: "))
				if fahOrCel == 2:
					celent = float(input("Enter the temperature in Celsius: "))
					fahent = (celent * 1.8 + 32)
					print ("The temperature in Fahrenheit is " + str(fahent))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 18:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Weight")
				print ("\nChart")
				print ("Gram      ID = 1")
				print ("Kilogram  ID = 2")
				print ("Pound     ID = 3")
				print ("Ton - 2000 pounds   ID = 4")
				weiunit = int(input("Enter a weight ID to start | ID: ")) 
				if weiunit == 1:
					print ("You selected [GRAM]")
				if weiunit == 2:
					print ("You selected [KILOGRAM]")
				if weiunit == 3:
					print ("You selected [POUND]")
				if weiunit == 4:
					print ("You selected [TON]")
				maunit = int(input("What type of calculation are you doing? \nAddition [ID = 1] Subtraction [ID = 2] Multiplication [ID = 3] division [ID = 4] Modular division [ID = 5] "))
				dropwei1 = float(input("Enter first number: "))
				dropwei2 = float(input("Enter second number: "))
				if weiunit == 1:
					if maunit == 1:
						ans = float(dropwei1 + dropwei2)
						uni = str
						if weiunit == 1:
							uni = ("Gram(s)")
						if weiunit == 2:
							uni = ("Kilogram(s)")
						if weiunit == 3:
							uni = ("Pound(s)")
						if weiunit == 4:
							uni = ("Ton(s)")
						print ("The answer is " + str(ans) + " " + str(uni))
				if weiunit == 1:
					if maunit == 2:
						ans = float(dropwei1 - dropwei2)
						uni = str
						if weiunit == 1:
							uni = ("Gram(s)")
						if weiunit == 2:
							uni = ("Kilogram(s)")
						if weiunit == 3:
							uni = ("Pound(s)")
						if weiunit == 4:
							uni = ("Ton(s)")
						print ("The answer is " + str(ans) + " " + str(uni))
				if weiunit == 1:
					if maunit == 3:
						ans = float(dropwei1 * dropwei2)
						uni = str
						if weiunit == 1:
							uni = ("Gram(s)")
						if weiunit == 2:
							uni = ("Kilogram(s)")
						if weiunit == 3:
							uni = ("Pound(s)")
						if weiunit == 4:
							uni = ("Ton(s)")
						print ("The answer is " + str(ans) + " " + str(uni))
				if weiunit == 1:
					if maunit == 4:
						ans = float(dropwei1 / dropwei2)
						uni = str
						if weiunit == 1:
							uni = ("Gram(s)")
						if weiunit == 2:
							uni = ("Kilogram(s)")
						if weiunit == 3:
							uni = ("Pound(s)")
						if weiunit == 4:
							uni = ("Ton(s)")
						print ("The answer is " + str(ans) + " " + str(uni))
				if weiunit == 1:
					if maunit == 5:
						ans = float(dropwei1 % dropwei2)
						uni = str
						if weiunit == 1:
							uni = ("Gram(s)")
						if weiunit == 2:
							uni = ("Kilogram(s)")
						if weiunit == 3:
							uni = ("Pound(s)")
						if weiunit == 4:
							uni = ("Ton(s)")
						print ("The answer is " + str(ans) + " " + str(uni))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 19:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Distance")
				sortoptTXT = input("New sorting options are available! ")
				sortoption = int(input("Enter an ID to change sorting view (A-Z = 0) (Z-A = 1) (smallest to largest = 2) (largest to smallest = 3)"))
				if sortoption == 0:
					print ("\nAngstrom")
					print ("Astronomical unit")
					print ("Centimeter")
					print ("Chains")
					print ("Decameter")
					print ("Decimeter")
					print ("Feet")
					print ("Hectometer")
					print ("Inch")
					print ("Kilometer")
					print ("Light year")
					print ("Link")
					print ("Meter")
					print ("Micrometer")
					print ("Mil")
					print ("Mile")
					print ("Millimeter")
					print ("Nanometer")
					print ("Nautical mile")
					print ("Parsec")
					print ("Picometer")
					print ("Rod")
					print ("Yard")
					print ("| Sorting from A-Z | Other sorting methods currently now unavailable |")
				if sortoption == 1:
					print ("\nYard")
					print ("Rod")
					print ("Picometer")
					print ("Parsec")
					print ("Nautical mile")
					print ("Nanometer")
					print ("Millimeter")
					print ("Mile")
					print ("Mil")
					print ("Micrometer")
					print ("Meter")
					print ("Link")
					print ("Light year")
					print ("Kilometer")
					print ("Inch")
					print ("Hectometer")
					print ("Feet")
					print ("Decimeter")
					print ("Decameter")
					print ("Chains")
					print ("Centimeter")
					print ("Astronomical unit")
					print ("Angstrom")
					print ("| Sorting from Z-A | Other sorting methods currently now unavailable |")
				mode1 = input("Type your preferred form of measurement from the list above: ")
				if mode1 == ("Angstrom"):
					angstrocalc = int(input("Enter an amount of angstroms (NO DECIMALS): "))
				if mode1 == ("Astronomical unit"):	
					astrocalc = int(input("Enter an amount in astronomical units (NO DECIMALS): "))
				if mode1 == ("Centimeters"):
					centimecalc = int(input("Enter an amount in centimeters (NO DECIMALS): "))
				if mode1 == ("Chains"):
					chaincalc = int(input("Enter an amount in chains (NO DECIMALS): "))
				if mode1 == ("Decameters"):
					decamecalc = int(input("Enter an amount in decameters (NO DECIMALS): "))
				if mode1 == ("Decimeters"):
					decamicalc = int(input("Enter an amount in decimeters (NO DECIMALS): "))
				if mode1 == ("Feet"):
					feetcalc = int(input("Enter an amount in feet (NO DECIMALS): "))
				if mode1 == ("Hectometer"):
					hectomecalc = int(input("Enter an amount in hectometers (NO DECIMALS): "))
				if mode1 == ("Inch"):
					inchcalc = int(input("Enter an amount in inches (NO DECIMALS): "))
				if mode1 == ("Kilometer"):
					kilomecalc = int(input("Enter an amount in kilometers (NO DECIMALS): "))
				if mode1 == ("Light year"): # to infinity... and beyond 
					lightyrcalc = int(input("Enter an amount in light years (NO DECIMALS): ")) # That's one small step for man... one giant leap... for mankind
				if mode1 == ("Link"): # Not to be confused with: The Legend Of Zelda (video game series by Nintendo) [1985-2018]
					linkcalc = int(input("Enter an amount in links (NO DECIMALS): "))
				if mode1 == ("Meter"):
					metercalc = int(input("Enter an amount in meters (NO DECIMALS): "))
				if mode1 == ("Micrometer"):
					micrometercalc = int(input("Enter an amount in micrometers (NO DECIMALS): "))
				if mode1 == ("Mil"): # not to be confused with miles
					milcalc = int(input("Enter an amount in mil's (NO DECIMALS): "))
				if mode1 == ("Mile"): # not to be confused with mils
					milecalc = int(input("Enter an amount in miles (NO DECIMALS): "))
				if mode1 == ("Millimeter"):
					millimetercalc = int(input("Enter an amount in millimeters (NO DECIMALS): "))
				if mode1 == ("Nanometer"):
					nanometercalc = int(input("Enter an amount in nanometers (NO DECIMALS): "))
				if mode1 == ("Nautical mile"): # Naughty nautical miles
					nautimilecalc = int(input("Enter an amount in nautical miles (NO DECIMALS): "))
				if mode1 == ("Parsec"):
					parseccalc = int(input("Enter an amount in parsec's (NO DECIMALS): "))
				if mode1 == ("Picometer"):
					picometercalc = int(input("Enter an amount in picometers (NO DECIMALS): "))
				if mode1 == ("Rod"):
					rodcalc = int(input("Enter an amount in rods (NO DECIMALS): "))
				if mode1 == ("Yard"):
					yardcalc = int(input("Enter an amount in yards (NO DECIMALS): "))
				# You get ALL the options! :) 
				print ("Addition +    [ID: 1]")
				print ("Subtraction - [ID: 2]")
				print ("Multiply *    [ID: 3]")
				print ("Divide /      [ID: 4]")
				print ("Mod %         [ID: 5]")
				unit2 = int(input("Enter an ID for the calculation"))
				mode2 = int(input("Enter an amount: "))
				if unit2 == 1:
					if mode1 == ("Angstrom"):
						curanswer = int(angstrocalc + mode2)
						print ("The answer is: " + str(curanswer) + " Angstroms")
						print ("This also translates to:")
						astrounits = int(curanswer / 1000000000)
						centimeters = int(curanswer / 10000000)
						chains = int(curanswer / 10000000)
						decameters = int(curanswer / 100000000000)
						decimeters = int(curanswer / 1000000000)
						feet = int(curanswer / 1000000000)
						hectometers = int(curanswer / 1000000000000)
						inches = int(curanswer / 100000000)
						kilometers = int(curanswer / 1000000000000000)
						lightyears = str("Cannot calculate due to a theoretical limit")
						links = int(curanswer / 1000000000)
						meters = int(curanswer / 10000000000)
						micrometers = int(curanswer / 10000)
						mils = int(curanswer / 100000000)
						miles = int(curanswer / 1000000000)
						millimeters = int(curanswer / 10000000)
						nanometers = int(curanswer / 10)
						nauticalMiles = str("Cannot calculate due to a theoretical limit")
						parsecs = int(curanswer / 10000000)
						picometers = int(curanswer * 100)
						rods = int(curanswer / 1000000000)
						yards = int(curanswer / 1000000000)
						print ("Astronomical units: " + str(astrounits) + " Note: this answer may not be accurate")
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains) + " Note: this answer may not be accurate")
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet) + " Note: this answer may not be accurate")
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches) + " Note: this answer may not be accurate")
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links) + " Note: this answer may not be accurate")
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils) + " Note: this answer may not be accurate")
						print ("Miles: " + str(miles) + " Note: this answer may not be accurate")
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs) + " Note: this answer may not be accurate")
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods) + " Note: this answer may not be accurate")
						print ("Yards: " + str(yards) + "Note: this answer may not be accurate")
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Astronomical unit"):
						curanswer = (astrocalc + mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = str("Cannot calculate due to a theoretical limit")
						centimeters = int(curanswer * 14959790000000)
						chains = int(curanswer * 74364650000)
						decameters = int(curanswer * 14959790000)
						decimeters = int(curanswer * 1495979000000)
						feet = int(curanswer * 490806700000)
						hectometers = int(curanswer * 1495979000)
						inches = int(curanswer * 588980000000)
						kilometers = int(curanswer * 149597900)
						lightyears = int(curanswer * 0.000015812)
						links = int(curanswer * 7436465000)
						meters = int(curanswer * 149597900000)
						micrometers = int(curanswer * 149597900000000000)
						mils = int(curanswer * 5889680000000000)
						miles = int(curanswer * 92955810)
						millimeters = int(curanswer * 149597900000000)
						nanometers = int(curanswer * 149597900000000016384)
						nauticalMiles = int(curanswer * 80776350)
						parsecs = int(curanswer * 0.000004848137)
						picometers = str("Cannot calculate due to a theoretical limit")
						rods = int(curanswer * 29745800000)
						yards = int(curanswer * 163602200000)
						print ("Astronomical units: " + str(astrocalc))
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Centimeters"):
						curanswer = (centimecalc + mode2)
						print ("The answer is: " + str(curanswer) + " Centimeters")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 100000000)
						astrocalc = int(curanswer * 0.00000000000006684587)
						chains = int(curanswer * 0.000497097)
						decameters = int(curanswer * 1000)
						decimeters = int(curanswer * 10)
						feet = int(curanswer * 0.0328084)
						hectometers = int(curanswer * 10000)
						inches = int(curanswer * 0.3937008)
						kilometers = int(curanswer * 100000)
						lightyears = int(curanswer * 0.000000000000000001057001)
						links = int(curanswer * 0.0497097)
						meters = int(curanswer * 0.01)
						micrometers = int(curanswer * 10000)
						mils = int(curanswer * 393.7008)
						miles = int(curanswer * 0.000006213712)
						millimeters = int(curanswer * 10)
						nanometers = int(curanswer * 10000000)
						nauticalMiles = int(curanswer * 0.000005399565)
						parsecs = int(curanswer * 0.0000000000000000003240779)
						picometers = int(curanswer * 1000000000)
						rods = int(curanswer * 0.001988384)
						yards = int(curanswer * 0.01093613)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Chains"):
						curanswer = (chaincalc + mode2)
						print ("The answer is: " + str(curanswer) + " Chains")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 201168000000)
						astrocalc = int(curanswer * 0.0000000001344725)
						centimeters = int(curanswer * 2011.68)
						decameters = int(curanswer * 2.01168)
						decimeters = int(curanswer * 201.168)
						feet = int(curanswer * 66)
						hectometers = int(curanswer * 0.201168)
						inches = int(curanswer * 792)
						kilometers = int(curanswer * 0.0201168)
						lightyears = int(curanswer * 0.000000000000002126347)
						links = int(curanswer * 100)
						meters = int(curanswer * 20.1168)
						micrometers = int(curanswer * 20116800)
						mils = int(curanswer * 792000)
						miles = int(curanswer * 0.0125)
						millimeters = int(curanswer * 20116.8)
						nanometers = int(curanswer * 20116800000)
						nauticalMiles = int(curanswer * 0.0108622)
						parsecs = int(curanswer * 0.0000000000000006519411)
						picometers = int(curanswer * 20116800000000)
						rods = int(curanswer * 3.999992)
						yards = int(curanswer * 22)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Centimers: " + str(centimeters))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
				if unit2 == 2:
					if mode1 == ("Angstrom"):
						curanswer = int(angstrocalc - mode2)
						print ("The answer is: " + str(curanswer) + " Angstroms")
						print ("This also translates to:")
						astrounits = int(curanswer / 1000000000)
						centimeters = int(curanswer / 10000000)
						chains = int(curanswer / 10000000)
						decameters = int(curanswer / 100000000000)
						decimeters = int(curanswer / 1000000000)
						feet = int(curanswer / 1000000000)
						hectometers = int(curanswer / 1000000000000)
						inches = int(curanswer / 100000000)
						kilometers = int(curanswer / 1000000000000000)
						lightyears = str("Cannot calculate due to a theoretical limit")
						links = int(curanswer / 1000000000)
						meters = int(curanswer / 10000000000)
						micrometers = int(curanswer / 10000)
						mils = int(curanswer / 100000000)
						miles = int(curanswer / 1000000000)
						millimeters = int(curanswer / 10000000)
						nanometers = int(curanswer / 10)
						nauticalMiles = str("Cannot calculate due to a theoretical limit")
						parsecs = int(curanswer / 10000000)
						picometers = int(curanswer * 100)
						rods = int(curanswer / 1000000000)
						yards = int(curanswer / 1000000000)
						print ("Astronomical units: " + str(astrounits) + " Note: this answer may not be accurate")
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains) + " Note: this answer may not be accurate")
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet) + " Note: this answer may not be accurate")
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches) + " Note: this answer may not be accurate")
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links) + " Note: this answer may not be accurate")
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils) + " Note: this answer may not be accurate")
						print ("Miles: " + str(miles) + " Note: this answer may not be accurate")
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs) + " Note: this answer may not be accurate")
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods) + " Note: this answer may not be accurate")
						print ("Yards: " + str(yards) + "Note: this answer may not be accurate")
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Astronomical unit"):
						curanswer = (astrocalc - mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = str("Cannot calculate due to a theoretical limit")
						centimeters = int(curanswer * 14959790000000)
						chains = int(curanswer * 74364650000)
						decameters = int(curanswer * 14959790000)
						decimeters = int(curanswer * 1495979000000)
						feet = int(curanswer * 490806700000)
						hectometers = int(curanswer * 1495979000)
						inches = int(curanswer * 588980000000)
						kilometers = int(curanswer * 149597900)
						lightyears = int(curanswer * 0.000015812)
						links = int(curanswer * 7436465000)
						meters = int(curanswer * 149597900000)
						micrometers = int(curanswer * 149597900000000000)
						mils = int(curanswer * 5889680000000000)
						miles = int(curanswer * 92955810)
						millimeters = int(curanswer * 149597900000000)
						nanometers = int(curanswer * 149597900000000016384)
						nauticalMiles = int(curanswer * 80776350)
						parsecs = int(curanswer * 0.000004848137)
						picometers = str("Cannot calculate due to a theoretical limit")
						rods = int(curanswer * 29745800000)
						yards = int(curanswer * 163602200000)
						print ("Astronomical units: " + str(astrocalc))
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Centimeters"):
						curanswer = (centimecalc - mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 100000000)
						astrocalc = int(curanswer * 0.00000000000006684587)
						chains = int(curanswer * 0.000497097)
						decameters = int(curanswer * 1000)
						decimeters = int(curanswer * 10)
						feet = int(curanswer * 0.0328084)
						hectometers = int(curanswer * 10000)
						inches = int(curanswer * 0.3937008)
						kilometers = int(curanswer * 100000)
						lightyears = int(curanswer * 0.000000000000000001057001)
						links = int(curanswer * 0.0497097)
						meters = int(curanswer * 0.01)
						micrometers = int(curanswer * 10000)
						mils = int(curanswer * 393.7008)
						miles = int(curanswer * 0.000006213712)
						millimeters = int(curanswer * 10)
						nanometers = int(curanswer * 10000000)
						nauticalMiles = int(curanswer * 0.000005399565)
						parsecs = int(curanswer * 0.0000000000000000003240779)
						picometers = int(curanswer * 1000000000)
						rods = int(curanswer * 0.001988384)
						yards = int(curanswer * 0.01093613)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Chains"):
						curanswer = (chaincalc - mode2)
						print ("The answer is: " + str(curanswer) + " Chains")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 201168000000)
						astrocalc = int(curanswer * 0.0000000001344725)
						centimeters = int(curanswer * 2011.68)
						decameters = int(curanswer * 2.01168)
						decimeters = int(curanswer * 201.168)
						feet = int(curanswer * 66)
						hectometers = int(curanswer * 0.201168)
						inches = int(curanswer * 792)
						kilometers = int(curanswer * 0.0201168)
						lightyears = int(curanswer * 0.000000000000002126347)
						links = int(curanswer * 100)
						meters = int(curanswer * 20.1168)
						micrometers = int(curanswer * 20116800)
						mils = int(curanswer * 792000)
						miles = int(curanswer * 0.0125)
						millimeters = int(curanswer * 20116.8)
						nanometers = int(curanswer * 20116800000)
						nauticalMiles = int(curanswer * 0.0108622)
						parsecs = int(curanswer * 0.0000000000000006519411)
						picometers = int(curanswer * 20116800000000)
						rods = int(curanswer * 3.999992)
						yards = int(curanswer * 22)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Centimeters: " + str(centimeters))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
				if unit2 == 3:
					if mode1 == ("Angstrom"):
						curanswer = int(angstrocalc	* mode2)
						print ("The answer is: " + str(curanswer) + " Angstroms")
						print ("This also translates to:")
						astrounits = int(curanswer / 1000000000)
						centimeters = int(curanswer / 10000000)
						chains = int(curanswer / 10000000)
						decameters = int(curanswer / 100000000000)
						decimeters = int(curanswer / 1000000000)
						feet = int(curanswer / 1000000000)
						hectometers = int(curanswer / 1000000000000)
						inches = int(curanswer / 100000000)
						kilometers = int(curanswer / 1000000000000000)
						lightyears = str("Cannot calculate due to a theoretical limit")
						links = int(curanswer / 1000000000)
						meters = int(curanswer / 10000000000)
						micrometers = int(curanswer / 10000)
						mils = int(curanswer / 100000000)
						miles = int(curanswer / 1000000000)
						millimeters = int(curanswer / 10000000)
						nanometers = int(curanswer / 10)
						nauticalMiles = str("Cannot calculate due to a theoretical limit")
						parsecs = int(curanswer / 10000000)
						picometers = int(curanswer * 100)
						rods = int(curanswer / 1000000000)
						yards = int(curanswer / 1000000000)
						print ("Astronomical units: " + str(astrounits) + " Note: this answer may not be accurate")
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains) + " Note: this answer may not be accurate")
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet) + " Note: this answer may not be accurate")
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches) + " Note: this answer may not be accurate")
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links) + " Note: this answer may not be accurate")
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils) + " Note: this answer may not be accurate")
						print ("Miles: " + str(miles) + " Note: this answer may not be accurate")
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs) + " Note: this answer may not be accurate")
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods) + " Note: this answer may not be accurate")
						print ("Yards: " + str(yards) + "Note: this answer may not be accurate")
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Astronomical unit"):
						curanswer = (astrocalc * mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = str("Cannot calculate due to a theoretical limit")
						centimeters = int(curanswer * 14959790000000)
						chains = int(curanswer * 74364650000)
						decameters = int(curanswer * 14959790000)
						decimeters = int(curanswer * 1495979000000)
						feet = int(curanswer * 490806700000)
						hectometers = int(curanswer * 1495979000)
						inches = int(curanswer * 588980000000)
						kilometers = int(curanswer * 149597900)
						lightyears = int(curanswer * 0.000015812)
						links = int(curanswer * 7436465000)
						meters = int(curanswer * 149597900000)
						micrometers = int(curanswer * 149597900000000000)
						mils = int(curanswer * 5889680000000000)
						miles = int(curanswer * 92955810)
						millimeters = int(curanswer * 149597900000000)
						nanometers = int(curanswer * 149597900000000016384)
						nauticalMiles = int(curanswer * 80776350)
						parsecs = int(curanswer * 0.000004848137)
						picometers = str("Cannot calculate due to a theoretical limit")
						rods = int(curanswer * 29745800000)
						yards = int(curanswer * 163602200000)
						print ("Astronomical units: " + str(astrocalc))
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Centimeters"):
						curanswer = (centimecalc * mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 100000000)
						astrocalc = int(curanswer * 0.00000000000006684587)
						chains = int(curanswer * 0.000497097)
						decameters = int(curanswer * 1000)
						decimeters = int(curanswer * 10)
						feet = int(curanswer * 0.0328084)
						hectometers = int(curanswer * 10000)
						inches = int(curanswer * 0.3937008)
						kilometers = int(curanswer * 100000)
						lightyears = int(curanswer * 0.000000000000000001057001)
						links = int(curanswer * 0.0497097)
						meters = int(curanswer * 0.01)
						micrometers = int(curanswer * 10000)
						mils = int(curanswer * 393.7008)
						miles = int(curanswer * 0.000006213712)
						millimeters = int(curanswer * 10)
						nanometers = int(curanswer * 10000000)
						nauticalMiles = int(curanswer * 0.000005399565)
						parsecs = int(curanswer * 0.0000000000000000003240779)
						picometers = int(curanswer * 1000000000)
						rods = int(curanswer * 0.001988384)
						yards = int(curanswer * 0.01093613)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Chains"):
						curanswer = (chaincalc * mode2)
						print ("The answer is: " + str(curanswer) + " Chains")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 201168000000)
						astrocalc = int(curanswer * 0.0000000001344725)
						centimeters = int(curanswer * 2011.68)
						decameters = int(curanswer * 2.01168)
						decimeters = int(curanswer * 201.168)
						feet = int(curanswer * 66)
						hectometers = int(curanswer * 0.201168)
						inches = int(curanswer * 792)
						kilometers = int(curanswer * 0.0201168)
						lightyears = int(curanswer * 0.000000000000002126347)
						links = int(curanswer * 100)
						meters = int(curanswer * 20.1168)
						micrometers = int(curanswer * 20116800)
						mils = int(curanswer * 792000)
						miles = int(curanswer * 0.0125)
						millimeters = int(curanswer * 20116.8)
						nanometers = int(curanswer * 20116800000)
						nauticalMiles = int(curanswer * 0.0108622)
						parsecs = int(curanswer * 0.0000000000000006519411)
						picometers = int(curanswer * 20116800000000)
						rods = int(curanswer * 3.999992)
						yards = int(curanswer * 22)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Centimers: " + str(centimeters))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
				if unit2 == 4:
					if mode1 == ("Angstrom"):
						curanswer = int(angstrocalc / mode2)
						print ("The answer is: " + str(curanswer) + " Angstroms")
						print ("This also translates to:")
						astrounits = int(curanswer / 1000000000)
						centimeters = int(curanswer / 10000000)
						chains = int(curanswer / 10000000)
						decameters = int(curanswer / 100000000000)
						decimeters = int(curanswer / 1000000000)
						feet = int(curanswer / 1000000000)
						hectometers = int(curanswer / 1000000000000)
						inches = int(curanswer / 100000000)
						kilometers = int(curanswer / 1000000000000000)
						lightyears = str("Cannot calculate due to a theoretical limit")
						links = int(curanswer / 1000000000)
						meters = int(curanswer / 10000000000)
						micrometers = int(curanswer / 10000)
						mils = int(curanswer / 100000000)
						miles = int(curanswer / 1000000000)
						millimeters = int(curanswer / 10000000)
						nanometers = int(curanswer / 10)
						nauticalMiles = str("Cannot calculate due to a theoretical limit")
						parsecs = int(curanswer / 10000000)
						picometers = int(curanswer * 100)
						rods = int(curanswer / 1000000000)
						yards = int(curanswer / 1000000000)
						print ("Astronomical units: " + str(astrounits) + " Note: this answer may not be accurate")
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains) + " Note: this answer may not be accurate")
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet) + " Note: this answer may not be accurate")
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches) + " Note: this answer may not be accurate")
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links) + " Note: this answer may not be accurate")
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils) + " Note: this answer may not be accurate")
						print ("Miles: " + str(miles) + " Note: this answer may not be accurate")
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs) + " Note: this answer may not be accurate")
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods) + " Note: this answer may not be accurate")
						print ("Yards: " + str(yards) + "Note: this answer may not be accurate")
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Astronomical unit"):
						curanswer = (astrocalc / mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = str("Cannot calculate due to a theoretical limit")
						centimeters = int(curanswer * 14959790000000)
						chains = int(curanswer * 74364650000)
						decameters = int(curanswer * 14959790000)
						decimeters = int(curanswer * 1495979000000)
						feet = int(curanswer * 490806700000)
						hectometers = int(curanswer * 1495979000)
						inches = int(curanswer * 588980000000)
						kilometers = int(curanswer * 149597900)
						lightyears = int(curanswer * 0.000015812)
						links = int(curanswer * 7436465000)
						meters = int(curanswer * 149597900000)
						micrometers = int(curanswer * 149597900000000000)
						mils = int(curanswer * 5889680000000000)
						miles = int(curanswer * 92955810)
						millimeters = int(curanswer * 149597900000000)
						nanometers = int(curanswer * 149597900000000016384)
						nauticalMiles = int(curanswer * 80776350)
						parsecs = int(curanswer * 0.000004848137)
						picometers = str("Cannot calculate due to a theoretical limit")
						rods = int(curanswer * 29745800000)
						yards = int(curanswer * 163602200000)
						print ("Astronomical units: " + str(astrocalc))
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Centimeters"):
						curanswer = (centimecalc / mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 100000000)
						astrocalc = int(curanswer * 0.00000000000006684587)
						chains = int(curanswer * 0.000497097)
						decameters = int(curanswer * 1000)
						decimeters = int(curanswer * 10)
						feet = int(curanswer * 0.0328084)
						hectometers = int(curanswer * 10000)
						inches = int(curanswer * 0.3937008)
						kilometers = int(curanswer * 100000)
						lightyears = int(curanswer * 0.000000000000000001057001)
						links = int(curanswer * 0.0497097)
						meters = int(curanswer * 0.01)
						micrometers = int(curanswer * 10000)
						mils = int(curanswer * 393.7008)
						miles = int(curanswer * 0.000006213712)
						millimeters = int(curanswer * 10)
						nanometers = int(curanswer * 10000000)
						nauticalMiles = int(curanswer * 0.000005399565)
						parsecs = int(curanswer * 0.0000000000000000003240779)
						picometers = int(curanswer * 1000000000)
						rods = int(curanswer * 0.001988384)
						yards = int(curanswer * 0.01093613)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Chains"):
						curanswer = (chaincalc / mode2)
						print ("The answer is: " + str(curanswer) + " Chains")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 201168000000)
						astrocalc = int(curanswer * 0.0000000001344725)
						centimeters = int(curanswer * 2011.68)
						decameters = int(curanswer * 2.01168)
						decimeters = int(curanswer * 201.168)
						feet = int(curanswer * 66)
						hectometers = int(curanswer * 0.201168)
						inches = int(curanswer * 792)
						kilometers = int(curanswer * 0.0201168)
						lightyears = int(curanswer * 0.000000000000002126347)
						links = int(curanswer * 100)
						meters = int(curanswer * 20.1168)
						micrometers = int(curanswer * 20116800)
						mils = int(curanswer * 792000)
						miles = int(curanswer * 0.0125)
						millimeters = int(curanswer * 20116.8)
						nanometers = int(curanswer * 20116800000)
						nauticalMiles = int(curanswer * 0.0108622)
						parsecs = int(curanswer * 0.0000000000000006519411)
						picometers = int(curanswer * 20116800000000)
						rods = int(curanswer * 3.999992)
						yards = int(curanswer * 22)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Centimers: " + str(centimeters))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
				if unit2 == 5:
					if mode1 == ("Angstrom"):
						curanswer = int(angstrocalc % mode2)
						print ("The answer is: " + str(curanswer) + " Angstroms")
						print ("This also translates to:")
						astrounits = int(curanswer / 1000000000)
						centimeters = int(curanswer / 10000000)
						chains = int(curanswer / 10000000)
						decameters = int(curanswer / 100000000000)
						decimeters = int(curanswer / 1000000000)
						feet = int(curanswer / 1000000000)
						hectometers = int(curanswer / 1000000000000)
						inches = int(curanswer / 100000000)
						kilometers = int(curanswer / 1000000000000000)
						lightyears = str("Cannot calculate due to a theoretical limit")
						links = int(curanswer / 1000000000)
						meters = int(curanswer / 10000000000)
						micrometers = int(curanswer / 10000)
						mils = int(curanswer / 100000000)
						miles = int(curanswer / 1000000000)
						millimeters = int(curanswer / 10000000)
						nanometers = int(curanswer / 10)
						nauticalMiles = str("Cannot calculate due to a theoretical limit")
						parsecs = int(curanswer / 10000000)
						picometers = int(curanswer * 100)
						rods = int(curanswer / 1000000000)
						yards = int(curanswer / 1000000000)
						print ("Astronomical units: " + str(astrounits) + " Note: this answer may not be accurate")
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains) + " Note: this answer may not be accurate")
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet) + " Note: this answer may not be accurate")
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches) + " Note: this answer may not be accurate")
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links) + " Note: this answer may not be accurate")
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils) + " Note: this answer may not be accurate")
						print ("Miles: " + str(miles) + " Note: this answer may not be accurate")
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs) + " Note: this answer may not be accurate")
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods) + " Note: this answer may not be accurate")
						print ("Yards: " + str(yards) + "Note: this answer may not be accurate")
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Astronomical unit"):
						curanswer = (astrocalc % mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = str("Cannot calculate due to a theoretical limit")
						centimeters = int(curanswer * 14959790000000)
						chains = int(curanswer * 74364650000)
						decameters = int(curanswer * 14959790000)
						decimeters = int(curanswer * 1495979000000)
						feet = int(curanswer * 490806700000)
						hectometers = int(curanswer * 1495979000)
						inches = int(curanswer * 588980000000)
						kilometers = int(curanswer * 149597900)
						lightyears = int(curanswer * 0.000015812)
						links = int(curanswer * 7436465000)
						meters = int(curanswer * 149597900000)
						micrometers = int(curanswer * 149597900000000000)
						mils = int(curanswer * 5889680000000000)
						miles = int(curanswer * 92955810)
						millimeters = int(curanswer * 149597900000000)
						nanometers = int(curanswer * 149597900000000016384)
						nauticalMiles = int(curanswer * 80776350)
						parsecs = int(curanswer * 0.000004848137)
						picometers = str("Cannot calculate due to a theoretical limit")
						rods = int(curanswer * 29745800000)
						yards = int(curanswer * 163602200000)
						print ("Astronomical units: " + str(astrocalc))
						print ("Centimeters: " + str(centimeters))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Centimeters"):
						curanswer = (centimecalc % mode2)
						print ("The answer is: " + str(curanswer) + " Astronomical units")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 100000000)
						astrocalc = int(curanswer * 0.00000000000006684587)
						chains = int(curanswer * 0.000497097)
						decameters = int(curanswer * 1000)
						decimeters = int(curanswer * 10)
						feet = int(curanswer * 0.0328084)
						hectometers = int(curanswer * 10000)
						inches = int(curanswer * 0.3937008)
						kilometers = int(curanswer * 100000)
						lightyears = int(curanswer * 0.000000000000000001057001)
						links = int(curanswer * 0.0497097)
						meters = int(curanswer * 0.01)
						micrometers = int(curanswer * 10000)
						mils = int(curanswer * 393.7008)
						miles = int(curanswer * 0.000006213712)
						millimeters = int(curanswer * 10)
						nanometers = int(curanswer * 10000000)
						nauticalMiles = int(curanswer * 0.000005399565)
						parsecs = int(curanswer * 0.0000000000000000003240779)
						picometers = int(curanswer * 1000000000)
						rods = int(curanswer * 0.001988384)
						yards = int(curanswer * 0.01093613)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Chains: " + str(chains))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
					if mode1 == ("Chains"):
						curanswer = (chaincalc % mode2)
						print ("The answer is: " + str(curanswer) + " Chains")
						print ("This also translates to:")
						angstrocalc = int(curanswer * 201168000000)
						astrocalc = int(curanswer * 0.0000000001344725)
						centimeters = int(curanswer * 2011.68)
						decameters = int(curanswer * 2.01168)
						decimeters = int(curanswer * 201.168)
						feet = int(curanswer * 66)
						hectometers = int(curanswer * 0.201168)
						inches = int(curanswer * 792)
						kilometers = int(curanswer * 0.0201168)
						lightyears = int(curanswer * 0.000000000000002126347)
						links = int(curanswer * 100)
						meters = int(curanswer * 20.1168)
						micrometers = int(curanswer * 20116800)
						mils = int(curanswer * 792000)
						miles = int(curanswer * 0.0125)
						millimeters = int(curanswer * 20116.8)
						nanometers = int(curanswer * 20116800000)
						nauticalMiles = int(curanswer * 0.0108622)
						parsecs = int(curanswer * 0.0000000000000006519411)
						picometers = int(curanswer * 20116800000000)
						rods = int(curanswer * 3.999992)
						yards = int(curanswer * 22)
						print ("Astronomical units: " + str(astrocalc))
						print ("Angstroms: " + str(angstrocalc))
						print ("Centimers: " + str(centimeters))
						print ("Decameters: " + str(decameters))
						print ("Decimeters: " + str(decimeters))
						print ("Feet: " + str(feet))
						print ("Hectometers: " + str(hectometers))
						print ("Inches: " + str(inches))
						print ("Kilometers: " + str(kilometers))
						print ("Light years: " + str(lightyears))
						print ("Links: " + str(links))
						print ("Meters: " + str(meters))
						print ("Micrometers: " + str(micrometers))
						print ("Mils: " + str(mils))
						print ("Miles: " + str(miles))
						print ("Millimeters: " + str(millimeters))
						print ("Nanometers: " + str(nanometers))
						print ("Nautical miles: " + str(nauticalMiles))
						print ("Parsecs: " + str(parsecs))
						print ("Picometers: " + str(picometers))
						print ("Rods: " + str(rods))
						print ("Yards: " + str(yards))
						exit1 = input("Press [ENTER] key to continue")
				'''
				Angstrom = 0.1 nanometers 
				Angstrom = 0.00000001 centimeters 
				Angstrom = 0.00001 micrometers
				Angstrom = 0.000003937008 mil 
				Angstrom = 100 picometers 
				Angstrom = 0.00000000000497097 chains
				Angstrom = 0.00000000001 decameters 
				Angstrom = 0.000000001 decimeters 
				Angstrom = 0.000000000328084 feet 
				Angstrom = 0.000000000001 hectometers 
				Angstrom = 0.0000000000001 kilometers 
				Angstrom = 0.00000000000000000000000001057001 lighyears
				Angstrom = 0.000000000497097 links 
				Angstrom = 0.0000000001 meters 
				But is an Angstrom the smallest form of measurement? 
				'''
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 20:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Graph")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to use graphing")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 21:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Square root")
				sqrtmain1 = int(input("Enter a number to find its square root: "))
				curanswer = (sqrtmain1 * sqrtmain1) 
				print ("The square root of " + str(sqrtmain1) + " is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 22:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("RGB Calculator")
				red1 = int(input("[RED] Enter a number 0-255 "))
				green1 = int(input("[GREEN] Enter a number 0-255 "))
				blue1 = int(input("[BLUE] Enter a number 0-255 "))
				print ("r: " + str(red1) + " g: " + str(green1) + " b: " + str(blue1))
				if (red1 == 0) and (green1 == 0) and (blue1 == 0):
					print ("The current color is [BLACK]")
				if (red1 == 255) and (green1 == 255) and (blue1 == 255):
					print ("The current color is [WHITE]")
				if (red1 == 255) and (green1 == 0) and (blue1 == 0):
					print ("The current color is [RED]")
				if (red1 == 0) and (green1 == 255) and (blue1 == 0):
					print ("The current color is [GREEN]")
				if (red1 == 0) and (green1 == 0) and (blue1 == 255):
					print ("The current color is [BLUE]")
				if (red1 == 255) and (green1 == 255) and (blue1 == 0):
					print ("The current color is [YELLOW]")
				if (red1 == 255) and (green1 == 0) and (blue1 == 255):
					print ("The current color is [MAGENTA]")
				if (red1 == 0) and (green1 == 255) and (blue1 == 255):
					print ("The current color is [CYAN]")
				print ("Thank you for using the RGB calculator!")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 23:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Speed calculator")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the speed")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 24:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Energy calculator")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the energy")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 25:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Days since")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the days since a date")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 26:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Years since")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the years since a year")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 27:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Days between")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the days between a date")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 28:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Years between")
				print ("This mode is currently unavailable. Sorry for the inconvenience ")
				print ("We are still working on adding in new features and stabilizing the program. Please install a newer version to calculate the years between a date")
				print ("No error, just not here yet")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 29:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Percentage")
				percent1 = float(input("Enter a number to find its percentage"))
				curanswer = (percent1 / 1)
				print (str(percent1) + " is " + str(curanswer) + " percent of 100")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 30:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Addition (with decimals)")
				add1dec1 = float(input("Enter number 1: "))
				add2dec2 = float(input("Enter number 2: "))
				curanswer = (add1dec1 + add2dec2)
				print ("The current answer is: " + str(curanswer))
				add3dec3 = float(input("Enter number 3: "))
				curanswer = (add1dec1 + add2dec2 + add3dec3)
				print ("The current answer is: " + str(curanswer)) 
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 31:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Subtraction (with decimals)")
				subtract1dec1 = float(input("Enter number 1: "))
				subtract2dec2 = float(input("Enter number 2: "))
				curanswer = (subtract1dec1 - subtract2dec2)
				print ("The current answer is: " + str(curanswer))
				subtract3dec3 = float(input("Enter numer 3: "))
				curanswer = (subtract1dec1 - subtract2dec2 - subtract3dec3)
				print ("The current answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 32:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Multiplication (with decimals)")
				multiply1dec1 = float(input("Enter number 1: "))
				multiply2dec2 = float(input("Enter number 2: "))
				curanswer = (multiply1dec1 * multiply2dec2)
				print ("The current answer is: " + str(curanswer))
				multiply3dec3 = float(input("Enter number 3: "))
				curanswer = (multiply1dec1 * multiply2dec2 * multiply3dec3)
				print ("The current answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 33:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Division (with decimals)")
				div1dec1 = float(input("Enter number 1: "))
				div2dec2 = float(input("Enter number 2: "))
				curanswer = (div1dec1 / div2dec2)
				print ("The current answer is: " + str(curanswer))
				div3dec3 = float(input("Enter number 3: "))
				curanswer = (div1dec1 / div2dec2 / div3dec3)
				print ("The current answer is: " + str(curanswer))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 34:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 35:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("First 100K digits of Pi")
				print ("3.141592653589793238462643383279502884197169399375105820974944592307816406286 208998628034825342117067982148086513282306647093844609550582231725359408128481 117450284102701938521105559644622948954930381964428810975665933446128475648233 786783165271201909145648566923460348610454326648213393607260249141273724587006 606315588174881520920962829254091715364367892590360011330530548820466521384146 951941511609433057270365759591953092186117381932611793105118548074462379962749 567351885752724891227938183011949129833673362440656643086021394946395224737190 702179860943702770539217176293176752384674818467669405132000568127145263560827 785771342757789609173637178721468440901224953430146549585371050792279689258923 542019956112129021960864034418159813629774771309960518707211349999998372978049 951059731732816096318595024459455346908302642522308253344685035261931188171010 003137838752886587533208381420617177669147303598253490428755468731159562863882 353787593751957781857780532171226806613001927876611195909216420198938095257201 065485863278865936153381827968230301952035301852968995773622599413891249721775 283479131515574857242454150695950829533116861727855889075098381754637464939319 255060400927701671139009848824012858361603563707660104710181942955596198946767 837449448255379774726847104047534646208046684259069491293313677028989152104752 162056966024058038150193511253382430035587640247496473263914199272604269922796 782354781636009341721641219924586315030286182974555706749838505494588586926995 690927210797509302955321165344987202755960236480665499119881834797753566369807 426542527862551818417574672890977772793800081647060016145249192173217214772350 141441973568548161361157352552133475741849468438523323907394143334547762416862 518983569485562099219222184272550254256887671790494601653466804988627232791786 085784383827967976681454100953883786360950680064225125205117392984896084128488 626945604241965285022210661186306744278622039194945047123713786960956364371917 287467764657573962413890865832645995813390478027590099465764078951269468398352 595709825822620522489407726719478268482601476990902640136394437455305068203496 252451749399651431429809190659250937221696461515709858387410597885959772975498 930161753928468138268683868942774155991855925245953959431049972524680845987273 644695848653836736222626099124608051243884390451244136549762780797715691435997 700129616089441694868555848406353422072225828488648158456028506016842739452267 467678895252138522549954666727823986456596116354886230577456498035593634568174 324112515076069479451096596094025228879710893145669136867228748940560101503308 617928680920874760917824938589009714909675985261365549781893129784821682998948 722658804857564014270477555132379641451523746234364542858444795265867821051141 354735739523113427166102135969536231442952484937187110145765403590279934403742 007310578539062198387447808478489683321445713868751943506430218453191048481005 370614680674919278191197939952061419663428754440643745123718192179998391015919 561814675142691239748940907186494231961567945208095146550225231603881930142093 762137855956638937787083039069792077346722182562599661501421503068038447734549 202605414665925201497442850732518666002132434088190710486331734649651453905796 268561005508106658796998163574736384052571459102897064140110971206280439039759 515677157700420337869936007230558763176359421873125147120532928191826186125867 321579198414848829164470609575270695722091756711672291098169091528017350671274 858322287183520935396572512108357915136988209144421006751033467110314126711136 990865851639831501970165151168517143765761835155650884909989859982387345528331 635507647918535893226185489632132933089857064204675259070915481416549859461637 180270981994309924488957571282890592323326097299712084433573265489382391193259 746366730583604142813883032038249037589852437441702913276561809377344403070746 921120191302033038019762110110044929321516084244485963766983895228684783123552 658213144957685726243344189303968642624341077322697802807318915441101044682325 271620105265227211166039666557309254711055785376346682065310989652691862056476 931257058635662018558100729360659876486117910453348850346113657686753249441668 039626579787718556084552965412665408530614344431858676975145661406800700237877 659134401712749470420562230538994561314071127000407854733269939081454664645880 797270826683063432858785698305235808933065757406795457163775254202114955761581 400250126228594130216471550979259230990796547376125517656751357517829666454779 174501129961489030463994713296210734043751895735961458901938971311179042978285 647503203198691514028708085990480109412147221317947647772622414254854540332157 185306142288137585043063321751829798662237172159160771669254748738986654949450 114654062843366393790039769265672146385306736096571209180763832716641627488880 078692560290228472104031721186082041900042296617119637792133757511495950156604 963186294726547364252308177036751590673502350728354056704038674351362222477158 915049530984448933309634087807693259939780541934144737744184263129860809988868 741326047215695162396586457302163159819319516735381297416772947867242292465436 680098067692823828068996400482435403701416314965897940924323789690706977942236 250822168895738379862300159377647165122893578601588161755782973523344604281512 627203734314653197777416031990665541876397929334419521541341899485444734567383 162499341913181480927777103863877343177207545654532207770921201905166096280490 926360197598828161332316663652861932668633606273567630354477628035045077723554 710585954870279081435624014517180624643626794561275318134078330336254232783944 975382437205835311477119926063813346776879695970309833913077109870408591337464 144282277263465947047458784778720192771528073176790770715721344473060570073349 243693113835049316312840425121925651798069411352801314701304781643788518529092 854520116583934196562134914341595625865865570552690496520985803385072242648293 972858478316305777756068887644624824685792603953527734803048029005876075825104 747091643961362676044925627420420832085661190625454337213153595845068772460290 161876679524061634252257719542916299193064553779914037340432875262888963995879 475729174642635745525407909145135711136941091193932519107602082520261879853188 770584297259167781314969900901921169717372784768472686084900337702424291651300 500516832336435038951702989392233451722013812806965011784408745196012122859937 162313017114448464090389064495444006198690754851602632750529834918740786680881 833851022833450850486082503930213321971551843063545500766828294930413776552793 975175461395398468339363830474611996653858153842056853386218672523340283087112 328278921250771262946322956398989893582116745627010218356462201349671518819097 303811980049734072396103685406643193950979019069963955245300545058068550195673 022921913933918568034490398205955100226353536192041994745538593810234395544959 778377902374216172711172364343543947822181852862408514006660443325888569867054 315470696574745855033232334210730154594051655379068662733379958511562578432298 827372319898757141595781119635833005940873068121602876496286744604774649159950 549737425626901049037781986835938146574126804925648798556145372347867330390468 838343634655379498641927056387293174872332083760112302991136793862708943879936 201629515413371424892830722012690147546684765357616477379467520049075715552781 965362132392640616013635815590742202020318727760527721900556148425551879253034 351398442532234157623361064250639049750086562710953591946589751413103482276930 624743536325691607815478181152843667957061108615331504452127473924544945423682 886061340841486377670096120715124914043027253860764823634143346235189757664521 641376796903149501910857598442391986291642193994907236234646844117394032659184 044378051333894525742399508296591228508555821572503107125701266830240292952522 011872676756220415420516184163484756516999811614101002996078386909291603028840 026910414079288621507842451670908700069928212066041837180653556725253256753286 129104248776182582976515795984703562226293486003415872298053498965022629174878 820273420922224533985626476691490556284250391275771028402799806636582548892648 802545661017296702664076559042909945681506526530537182941270336931378517860904 070866711496558343434769338578171138645587367812301458768712660348913909562009 939361031029161615288138437909904231747336394804575931493140529763475748119356 709110137751721008031559024853090669203767192203322909433467685142214477379393 751703443661991040337511173547191855046449026365512816228824462575916333039107 225383742182140883508657391771509682887478265699599574490661758344137522397096 834080053559849175417381883999446974867626551658276584835884531427756879002909 517028352971634456212964043523117600665101241200659755851276178583829204197484 423608007193045761893234922927965019875187212726750798125547095890455635792122 103334669749923563025494780249011419521238281530911407907386025152274299581807 247162591668545133312394804947079119153267343028244186041426363954800044800267 049624820179289647669758318327131425170296923488962766844032326092752496035799 646925650493681836090032380929345958897069536534940603402166544375589004563288 225054525564056448246515187547119621844396582533754388569094113031509526179378 002974120766514793942590298969594699556576121865619673378623625612521632086286 922210327488921865436480229678070576561514463204692790682120738837781423356282 360896320806822246801224826117718589638140918390367367222088832151375560037279 839400415297002878307667094447456013455641725437090697939612257142989467154357 846878861444581231459357198492252847160504922124247014121478057345510500801908 699603302763478708108175450119307141223390866393833952942578690507643100638351 983438934159613185434754649556978103829309716465143840700707360411237359984345 225161050702705623526601276484830840761183013052793205427462865403603674532865 105706587488225698157936789766974220575059683440869735020141020672358502007245 225632651341055924019027421624843914035998953539459094407046912091409387001264 560016237428802109276457931065792295524988727584610126483699989225695968815920 560010165525637567856672279661988578279484885583439751874454551296563443480396 642055798293680435220277098429423253302257634180703947699415979159453006975214 829336655566156787364005366656416547321704390352132954352916941459904160875320 186837937023488868947915107163785290234529244077365949563051007421087142613497 459561513849871375704710178795731042296906667021449863746459528082436944578977 233004876476524133907592043401963403911473202338071509522201068256342747164602 433544005152126693249341967397704159568375355516673027390074972973635496453328 886984406119649616277344951827369558822075735517665158985519098666539354948106 887320685990754079234240230092590070173196036225475647894064754834664776041146 323390565134330684495397907090302346046147096169688688501408347040546074295869 913829668246818571031887906528703665083243197440477185567893482308943106828702 722809736248093996270607472645539925399442808113736943388729406307926159599546 262462970706259484556903471197299640908941805953439325123623550813494900436427 852713831591256898929519642728757394691427253436694153236100453730488198551706 594121735246258954873016760029886592578662856124966552353382942878542534048308 330701653722856355915253478445981831341129001999205981352205117336585640782648 494276441137639386692480311836445369858917544264739988228462184490087776977631 279572267265556259628254276531830013407092233436577916012809317940171859859993 384923549564005709955856113498025249906698423301735035804408116855265311709957 089942732870925848789443646005041089226691783525870785951298344172953519537885 534573742608590290817651557803905946408735061232261120093731080485485263572282 576820341605048466277504500312620080079980492548534694146977516493270950493463 938243222718851597405470214828971117779237612257887347718819682546298126868581 705074027255026332904497627789442362167411918626943965067151577958675648239939 176042601763387045499017614364120469218237076488783419689686118155815873606293 860381017121585527266830082383404656475880405138080163363887421637140643549556 186896411228214075330265510042410489678352858829024367090488711819090949453314 421828766181031007354770549815968077200947469613436092861484941785017180779306 810854690009445899527942439813921350558642219648349151263901280383200109773868 066287792397180146134324457264009737425700735921003154150893679300816998053652 027600727749674584002836240534603726341655425902760183484030681138185510597970 566400750942608788573579603732451414678670368809880609716425849759513806930944 940151542222194329130217391253835591503100333032511174915696917450271494331515 588540392216409722910112903552181576282328318234254832611191280092825256190205 263016391147724733148573910777587442538761174657867116941477642144111126358355 387136101102326798775641024682403226483464176636980663785768134920453022408197 278564719839630878154322116691224641591177673225326433568614618654522268126887 268445968442416107854016768142080885028005414361314623082102594173756238994207 571362751674573189189456283525704413354375857534269869947254703165661399199968 262824727064133622217892390317608542894373393561889165125042440400895271983787 386480584726895462438823437517885201439560057104811949884239060613695734231559 079670346149143447886360410318235073650277859089757827273130504889398900992391 350337325085598265586708924261242947367019390772713070686917092646254842324074 855036608013604668951184009366860954632500214585293095000090715105823626729326 453738210493872499669933942468551648326113414611068026744663733437534076429402 668297386522093570162638464852851490362932019919968828517183953669134522244470 804592396602817156551565666111359823112250628905854914509715755390024393153519 090210711945730024388017661503527086260253788179751947806101371500448991721002 220133501310601639154158957803711779277522597874289191791552241718958536168059 474123419339842021874564925644346239253195313510331147639491199507285843065836 193536932969928983791494193940608572486396883690326556436421664425760791471086 998431573374964883529276932822076294728238153740996154559879825989109371712621 828302584811238901196822142945766758071865380650648702613389282299497257453033 283896381843944770779402284359883410035838542389735424395647555684095224844554 139239410001620769363684677641301781965937997155746854194633489374843912974239 143365936041003523437770658886778113949861647874714079326385873862473288964564 359877466763847946650407411182565837887845485814896296127399841344272608606187 245545236064315371011274680977870446409475828034876975894832824123929296058294 861919667091895808983320121031843034012849511620353428014412761728583024355983 003204202451207287253558119584014918096925339507577840006746552603144616705082 768277222353419110263416315714740612385042584598841990761128725805911393568960 143166828317632356732541707342081733223046298799280490851409479036887868789493 054695570307261900950207643349335910602454508645362893545686295853131533718386 826561786227363716975774183023986006591481616404944965011732131389574706208847 480236537103115089842799275442685327797431139514357417221975979935968525228574 526379628961269157235798662057340837576687388426640599099350500081337543245463 596750484423528487470144354541957625847356421619813407346854111766883118654489 377697956651727966232671481033864391375186594673002443450054499539974237232871 249483470604406347160632583064982979551010954183623503030945309733583446283947 630477564501500850757894954893139394489921612552559770143685894358587752637962 559708167764380012543650237141278346792610199558522471722017772370041780841942 394872540680155603599839054898572354674564239058585021671903139526294455439131 663134530893906204678438778505423939052473136201294769187497519101147231528932 677253391814660730008902776896311481090220972452075916729700785058071718638105 496797310016787085069420709223290807038326345345203802786099055690013413718236 837099194951648960075504934126787643674638490206396401976668559233565463913836 318574569814719621084108096188460545603903845534372914144651347494078488442377 217515433426030669883176833100113310869042193903108014378433415137092435301367 763108491351615642269847507430329716746964066653152703532546711266752246055119 958183196376370761799191920357958200759560530234626775794393630746305690108011 494271410093913691381072581378135789400559950018354251184172136055727522103526 803735726527922417373605751127887218190844900617801388971077082293100279766593 583875890939568814856026322439372656247277603789081445883785501970284377936240 782505270487581647032458129087839523245323789602984166922548964971560698119218 658492677040395648127810217991321741630581055459880130048456299765112124153637 451500563507012781592671424134210330156616535602473380784302865525722275304999 883701534879300806260180962381516136690334111138653851091936739383522934588832 255088706450753947395204396807906708680644509698654880168287434378612645381583 428075306184548590379821799459968115441974253634439960290251001588827216474500 682070419376158454712318346007262933955054823955713725684023226821301247679452 264482091023564775272308208106351889915269288910845557112660396503439789627825 001611015323516051965590421184494990778999200732947690586857787872098290135295 661397888486050978608595701773129815531495168146717695976099421003618355913877 781769845875810446628399880600616229848616935337386578773598336161338413385368 421197893890018529569196780455448285848370117096721253533875862158231013310387 766827211572694951817958975469399264219791552338576623167627547570354699414892 904130186386119439196283887054367774322427680913236544948536676800000106526248 547305586159899914017076983854831887501429389089950685453076511680333732226517 566220752695179144225280816517166776672793035485154204023817460892328391703275 425750867655117859395002793389592057668278967764453184040418554010435134838953 120132637836928358082719378312654961745997056745071833206503455664403449045362 756001125018433560736122276594927839370647842645676338818807565612168960504161 139039063960162022153684941092605387688714837989559999112099164646441191856827 700457424343402167227644558933012778158686952506949936461017568506016714535431 581480105458860564550133203758645485840324029871709348091055621167154684847780 394475697980426318099175642280987399876697323769573701580806822904599212366168 902596273043067931653114940176473769387351409336183321614280214976339918983548 487562529875242387307755955595546519639440182184099841248982623673771467226061 633643296406335728107078875816404381485018841143188598827694490119321296827158 884133869434682859006664080631407775772570563072940049294030242049841656547973 670548558044586572022763784046682337985282710578431975354179501134727362577408 021347682604502285157979579764746702284099956160156910890384582450267926594205 550395879229818526480070683765041836562094555434613513415257006597488191634135 955671964965403218727160264859304903978748958906612725079482827693895352175362 185079629778514618843271922322381015874445052866523802253284389137527384589238 442253547265309817157844783421582232702069028723233005386216347988509469547200 479523112015043293226628272763217790884008786148022147537657810581970222630971 749507212724847947816957296142365859578209083073323356034846531873029302665964 501371837542889755797144992465403868179921389346924474198509733462679332107268 687076806263991936196504409954216762784091466985692571507431574079380532392523 947755744159184582156251819215523370960748332923492103451462643744980559610330 799414534778457469999212859999939961228161521931488876938802228108300198601654 941654261696858678837260958774567618250727599295089318052187292461086763995891 614585505839727420980909781729323930106766386824040111304024700735085782872462 713494636853181546969046696869392547251941399291465242385776255004748529547681 479546700705034799958886769501612497228204030399546327883069597624936151010243 655535223069061294938859901573466102371223547891129254769617600504797492806072 126803922691102777226102544149221576504508120677173571202718024296810620377657 883716690910941807448781404907551782038565390991047759414132154328440625030180 275716965082096427348414695726397884256008453121406593580904127113592004197598 513625479616063228873618136737324450607924411763997597461938358457491598809766 744709300654634242346063423747466608043170126005205592849369594143408146852981 505394717890045183575515412522359059068726487863575254191128887737176637486027 660634960353679470269232297186832771739323619200777452212624751869833495151019 864269887847171939664976907082521742336566272592844062043021411371992278526998 469884770232382384005565551788908766136013047709843861168705231055314916251728 373272867600724817298763756981633541507460883866364069347043720668865127568826 614973078865701568501691864748854167915459650723428773069985371390430026653078 398776385032381821553559732353068604301067576083890862704984188859513809103042 359578249514398859011318583584066747237029714978508414585308578133915627076035 639076394731145549583226694570249413983163433237897595568085683629725386791327 505554252449194358912840504522695381217913191451350099384631177401797151228378 546011603595540286440590249646693070776905548102885020808580087811577381719174 177601733073855475800605601433774329901272867725304318251975791679296996504146 070664571258883469797964293162296552016879730003564630457930884032748077181155 533090988702550520768046303460865816539487695196004408482065967379473168086415 645650530049881616490578831154345485052660069823093157776500378070466126470602 145750579327096204782561524714591896522360839664562410519551052235723973951288 181640597859142791481654263289200428160913693777372229998332708208296995573772 737566761552711392258805520189887620114168005468736558063347160373429170390798 639652296131280178267971728982293607028806908776866059325274637840539769184808 204102194471971386925608416245112398062011318454124478205011079876071715568315 407886543904121087303240201068534194723047666672174986986854707678120512473679 247919315085644477537985379973223445612278584329684664751333657369238720146472 367942787004250325558992688434959287612400755875694641370562514001179713316620 715371543600687647731867558714878398908107429530941060596944315847753970094398 839491443235366853920994687964506653398573888786614762944341401049888993160051 207678103588611660202961193639682134960750111649832785635316145168457695687109 002999769841263266502347716728657378579085746646077228341540311441529418804782 543876177079043000156698677679576090996693607559496515273634981189641304331166 277471233881740603731743970540670310967676574869535878967003192586625941051053 358438465602339179674926784476370847497833365557900738419147319886271352595462 518160434225372996286326749682405806029642114638643686422472488728343417044157 348248183330164056695966886676956349141632842641497453334999948000266998758881 593507357815195889900539512085351035726137364034367534714104836017546488300407 846416745216737190483109676711344349481926268111073994825060739495073503169019 731852119552635632584339099822498624067031076831844660729124874754031617969941 139738776589986855417031884778867592902607004321266617919223520938227878880988 633599116081923535557046463491132085918979613279131975649097600013996234445535 014346426860464495862476909434704829329414041114654092398834443515913320107739 441118407410768498106634724104823935827401944935665161088463125678529776973468 430306146241803585293315973458303845541033701091676776374276210213701354854450 926307190114731848574923318167207213727935567952844392548156091372812840633303 937356242001604566455741458816605216660873874804724339121295587776390696903707 882852775389405246075849623157436917113176134783882719416860662572103685132156 647800147675231039357860689611125996028183930954870905907386135191459181951029 732787557104972901148717189718004696169777001791391961379141716270701895846921 434369676292745910994006008498356842520191559370370101104974733949387788598941 743303178534870760322198297057975119144051099423588303454635349234982688362404 332726741554030161950568065418093940998202060999414021689090070821330723089662 119775530665918814119157783627292746156185710372172471009521423696483086410259 288745799932237495519122195190342445230753513380685680735446499512720317448719 540397610730806026990625807602029273145525207807991418429063884437349968145827 337207266391767020118300464819000241308350884658415214899127610651374153943565 721139032857491876909441370209051703148777346165287984823533829726013611098451 484182380812054099612527458088109948697221612852489742555551607637167505489617 301680961380381191436114399210638005083214098760459930932485102516829446726066 613815174571255975495358023998314698220361338082849935670557552471290274539776 214049318201465800802156653606776550878380430413431059180460680083459113664083 488740800574127258670479225831912741573908091438313845642415094084913391809684 025116399193685322555733896695374902662092326131885589158083245557194845387562 878612885900410600607374650140262782402734696252821717494158233174923968353013 617865367376064216677813773995100658952887742766263684183068019080460984980946 976366733566228291513235278880615776827815958866918023894033307644191240341202 231636857786035727694154177882643523813190502808701857504704631293335375728538 660588890458311145077394293520199432197117164223500564404297989208159430716701 985746927384865383343614579463417592257389858800169801475742054299580124295810 545651083104629728293758416116253256251657249807849209989799062003593650993472 158296517413579849104711166079158743698654122234834188772292944633517865385673 196255985202607294767407261676714557364981210567771689348491766077170527718760 119990814411305864557791052568430481144026193840232247093924980293355073184589 035539713308844617410795916251171486487446861124760542867343670904667846867027 409188101424971114965781772427934707021668829561087779440504843752844337510882 826477197854000650970403302186255614733211777117441335028160884035178145254196 432030957601869464908868154528562134698835544456024955666843660292219512483091 060537720198021831010327041783866544718126039719068846237085751808003532704718 565949947612424811099928867915896904956394762460842406593094862150769031498702 067353384834955083636601784877106080980426924713241000946401437360326564518456 679245666955100150229833079849607994988249706172367449361226222961790814311414 660941234159359309585407913908720832273354957208075716517187659944985693795623 875551617575438091780528029464200447215396280746360211329425591600257073562812 638733106005891065245708024474937543184149401482119996276453106800663118382376 163966318093144467129861552759820145141027560068929750246304017351489194576360 789352855505317331416457050499644389093630843874484783961684051845273288403234 520247056851646571647713932377551729479512613239822960239454857975458651745878 771331813875295980941217422730035229650808917770506825924882232215493804837145 478164721397682096332050830564792048208592047549985732038887639160199524091893 894557676874973085695595801065952650303626615975066222508406742889826590751063 756356996821151094966974458054728869363102036782325018232370845979011154847208 761821247781326633041207621658731297081123075815982124863980721240786887811450 165582513617890307086087019897588980745664395515741536319319198107057533663373 803827215279884935039748001589051942087971130805123393322190346624991716915094 854140187106035460379464337900589095772118080446574396280618671786101715674096 766208029576657705129120990794430463289294730615951043090222143937184956063405 618934251305726829146578329334052463502892917547087256484260034962961165413823 007731332729830500160256724014185152041890701154288579920812198449315699905918 201181973350012618772803681248199587707020753240636125931343859554254778196114 293516356122349666152261473539967405158499860355295332924575238881013620234762 466905581643896786309762736550472434864307121849437348530060638764456627218666 170123812771562137974614986132874411771455244470899714452288566294244023018479 120547849857452163469644897389206240194351831008828348024924908540307786387516 591130287395878709810077271827187452901397283661484214287170553179654307650453 432460053636147261818096997693348626407743519992868632383508875668359509726557 481543194019557685043724800102041374983187225967738715495839971844490727914196 584593008394263702087563539821696205532480321226749891140267852859967340524203 109179789990571882194939132075343170798002373659098537552023891164346718558290 685371189795262623449248339249634244971465684659124891855662958932990903523923 333364743520370770101084388003290759834217018554228386161721041760301164591878 053936744747205998502358289183369292233732399948043710841965947316265482574809 948250999183300697656936715968936449334886474421350084070066088359723503953234 017958255703601693699098867113210979889707051728075585519126993067309925070407 024556850778679069476612629808225163313639952117098452809263037592242674257559 989289278370474445218936320348941552104459726188380030067761793138139916205806 270165102445886924764924689192461212531027573139084047000714356136231699237169 484813255420091453041037135453296620639210547982439212517254013231490274058589 206321758949434548906846399313757091034633271415316223280552297297953801880162 859073572955416278867649827418616421878988574107164906919185116281528548679417 363890665388576422915834250067361245384916067413734017357277995634104332688356 950781493137800736235418007061918026732855119194267609122103598746924117283749 312616339500123959924050845437569850795704622266461900010350049018303415354584 283376437811198855631877779253720116671853954183598443830520376281944076159410 682071697030228515225057312609304689842343315273213136121658280807521263154773 060442377475350595228717440266638914881717308643611138906942027908814311944879 941715404210341219084709408025402393294294549387864023051292711909751353600092 197110541209668311151632870542302847007312065803262641711616595761327235156666 253667271899853419989523688483099930275741991646384142707798870887422927705389 122717248632202889842512528721782603050099451082478357290569198855546788607946 280537122704246654319214528176074148240382783582971930101788834567416781139895 475044833931468963076339665722672704339321674542182455706252479721997866854279 897799233957905758189062252547358220523642485078340711014498047872669199018643 882293230538231855973286978092225352959101734140733488476100556401824239219269 506208318381454698392366461363989101210217709597670490830508185470419466437131 229969235889538493013635657618610606222870559942337163102127845744646398973818 856674626087948201864748767272722206267646533809980196688368099415907577685263 986514625333631245053640261056960551318381317426118442018908885319635698696279 503673842431301133175330532980201668881748134298868158557781034323175306478498 321062971842518438553442762012823457071698853051832617964117857960888815032960 229070561447622091509473903594664691623539680920139457817589108893199211226007 392814916948161527384273626429809823406320024402449589445612916704950823581248 739179964864113348032475777521970893277226234948601504665268143987705161531702 669692970492831628550421289814670619533197026950721437823047687528028735412616 639170824592517001071418085480063692325946201900227808740985977192180515853214 739265325155903541020928466592529991435379182531454529059841581763705892790690 989691116438118780943537152133226144362531449012745477269573939348154691631162 492887357471882407150399500944673195431619385548520766573882513963916357672315 100555603726339486720820780865373494244011579966750736071115935133195919712094 896471755302453136477094209463569698222667377520994516845064362382421185353488 798939567318780660610788544000550827657030558744854180577889171920788142335113 866292966717964346876007704799953788338787034871802184243734211227394025571769 081960309201824018842705704609262256417837526526335832424066125331152942345796 556950250681001831090041124537901533296615697052237921032570693705109083078947 999900499939532215362274847660361367769797856738658467093667958858378879562594 646489137665219958828693380183601193236857855855819555604215625088365020332202 451376215820461810670519533065306060650105488716724537794283133887163139559690 583208341689847606560711834713621812324622725884199028614208728495687963932546 428534307530110528571382964370999035694888528519040295604734613113826387889755 178856042499874831638280404684861893818959054203988987265069762020199554841265 000539442820393012748163815853039643992547020167275932857436666164411096256633 730540921951967514832873480895747777527834422109107311135182804603634719818565 557295714474768255285786334934285842311874944000322969069775831590385803935352 135886007960034209754739229673331064939560181223781285458431760556173386112673 478074585067606304822940965304111830667108189303110887172816751957967534718853 722930961614320400638132246584111115775835858113501856904781536893813771847281 475199835050478129771859908470762197460588742325699582889253504193795826061621 184236876851141831606831586799460165205774052942305360178031335726326705479033 840125730591233960188013782542192709476733719198728738524805742124892118347087 662966720727232565056512933312605950577772754247124164831283298207236175057467 387012820957554430596839555568686118839713552208445285264008125202766555767749 596962661260456524568408613923826576858338469849977872670655519185446869846947 849573462260629421962455708537127277652309895545019303773216664918257815467729 200521266714346320963789185232321501897612603437368406719419303774688099929687 758244104787812326625318184596045385354383911449677531286426092521153767325886 672260404252349108702695809964759580579466397341906401003636190404203311357933 654242630356145700901124480089002080147805660371015412232889146572239314507607 167064355682743774396578906797268743847307634645167756210309860409271709095128 086309029738504452718289274968921210667008164858339553773591913695015316201890 888748421079870689911480466927065094076204650277252865072890532854856143316081 269300569378541786109696920253886503457718317668688592368148847527649846882194 973972970773718718840041432312763650481453112285099002074240925585925292610302 106736815434701525234878635164397623586041919412969769040526483234700991115424 260127343802208933109668636789869497799400126016422760926082349304118064382913 834735467972539926233879158299848645927173405922562074910530853153718291168163 721939518870095778818158685046450769934394098743351443162633031724774748689791 820923948083314397084067308407958935810896656477585990556376952523265361442478 023082681183103773588708924061303133647737101162821461466167940409051861526036 009252194721889091810733587196414214447865489952858234394705007983038853886083 103571930600277119455802191194289992272235345870756624692617766317885514435021 828702668561066500353105021631820601760921798468493686316129372795187307897263 735371715025637873357977180818487845886650433582437700414771041493492743845758 710715973155943942641257027096512510811554824793940359768118811728247215825010 949609662539339538092219559191818855267806214992317276316321833989693807561685 591175299845013206712939240414459386239880938124045219148483164621014738918251 010909677386906640415897361047643650006807710565671848628149637111883219244566 394581449148616550049567698269030891118568798692947051352481609174324301538368 470729289898284602223730145265567989862776796809146979837826876431159883210904 371561129976652153963546442086919756737000573876497843768628768179249746943842 746525631632300555130417422734164645512781278457777245752038654375428282567141 288583454443513256205446424101103795546419058116862305964476958705407214198521 210673433241075676757581845699069304604752277016700568454396923404171108988899 341635058515788735343081552081177207188037910404698306957868547393765643363197 978680367187307969392423632144845035477631567025539006542311792015346497792906 624150832885839529054263768766896880503331722780018588506973623240389470047189 761934734430843744375992503417880797223585913424581314404984770173236169471976 571535319775499716278566311904691260918259124989036765417697990362375528652637 573376352696934435440047306719886890196814742876779086697968852250163694985673 021752313252926537589641517147955953878427849986645630287883196209983049451987 439636907068276265748581043911223261879405994155406327013198989570376110532360 629867480377915376751158304320849872092028092975264981256916342500052290887264 692528466610466539217148208013050229805263783642695973370705392278915351056888 393811324975707133102950443034671598944878684711643832805069250776627450012200 352620370946602341464899839025258883014867816219677519458316771876275720050543 979441245990077115205154619930509838698254284640725554092740313257163264079293 418334214709041254253352324802193227707535554679587163835875018159338717423606 155117101312352563348582036514614187004920570437201826173319471570086757853933 607862273955818579758725874410254207710547536129404746010009409544495966288148 691590389907186598056361713769222729076419775517772010427649694961105622059250 242021770426962215495872645398922769766031052498085575947163107587013320886146 326641259114863388122028444069416948826152957762532501987035987067438046982194 205638125583343642194923227593722128905642094308235254408411086454536940496927 149400331978286131818618881111840825786592875742638445005994422956858646048103 301538891149948693543603022181094346676400002236255057363129462629609619876056 425996394613869233083719626595473923462413459779574852464783798079569319865081 597767535055391899115133525229873611277918274854200868953965835942196333150286 956119201229888988700607999279541118826902307891310760361763477948943203210277 335941690865007193280401716384064498787175375678118532132840821657110754952829 497493621460821558320568723218557406516109627487437509809223021160998263303391 546949464449100451528092508974507489676032409076898365294065792019831526541065 813682379198409064571246894847020935776119313998024681340520039478194986620262 400890215016616381353838151503773502296607462795291038406868556907015751662419 298724448271942933100485482445458071889763300323252582158128032746796200281476 243182862217105435289834820827345168018613171959332471107466222850871066611770 346535283957762599774467218571581612641114327179434788599089280848669491413909 771673690027775850268664654056595039486784111079011610400857274456293842549416 759460548711723594642910585090995021495879311219613590831588262068233215615308 683373083817327932819698387508708348388046388478441884003184712697454370937329 836240287519792080232187874488287284372737801782700805878241074935751488997891 173974612932035108143270325140903048746226294234432757126008664250833318768865 075642927160552528954492153765175149219636718104943531785838345386525565664065 725136357506435323650893679043170259787817719031486796384082881020946149007971 513771709906195496964007086766710233004867263147551053723175711432231741141168 062286420638890621019235522354671166213749969326932173704310598722503945657492 461697826097025335947502091383667377289443869640002811034402608471289900074680 776484408871134135250336787731679770937277868216611786534423173226463784769787 514433209534000165069213054647689098505020301504488083426184520873053097318949 291642532293361243151430657826407028389840984160295030924189712097160164926561 341343342229882790992178604267981245728534580133826099587717811310216734025656 274400729683406619848067661580502169183372368039902793160642043681207990031626 444914619021945822969099212278855394878353830564686488165556229431567312827439 082645061162894280350166133669782405177015521962652272545585073864058529983037 918035043287670380925216790757120406123759632768567484507915114731344000183257 034492090971243580944790046249431345502890068064870429353403743603262582053579 011839564908935434510134296961754524957396062149028872893279252069653538639644 322538832752249960598697475988232991626354597332444516375533437749292899058117 578635555562693742691094711700216541171821975051983178713710605106379555858890 556885288798908475091576463907469361988150781468526213325247383765119299015610 918977792200870579339646382749068069876916819749236562422608715417610043060890 437797667851966189140414492527048088197149880154205778700652159400928977760133 075684796699295543365613984773806039436889588764605498387147896848280538470173 087111776115966350503997934386933911978988710915654170913308260764740630571141 109883938809548143782847452883836807941888434266622207043872288741394780101772 139228191199236540551639589347426395382482960903690028835932774585506080131798 840716244656399794827578365019551422155133928197822698427863839167971509126241 054872570092407004548848569295044811073808799654748156891393538094347455697212 891982717702076661360248958146811913361412125878389557735719498631721084439890 142394849665925173138817160266326193106536653504147307080441493916936326237376 777709585031325599009576273195730864804246770121232702053374266705314244820816 813030639737873664248367253983748769098060218278578621651273856351329014890350 988327061725893257536399397905572917516009761545904477169226580631511102803843 601737474215247608515209901615858231257159073342173657626714239047827958728150 509563309280266845893764964977023297364131906098274063353108979246424213458374 090116939196425045912881340349881063540088759682005440836438651661788055760895 689672753153808194207733259791727843762566118431989102500749182908647514979400 316070384554946538594602745244746681231468794344161099333890899263841184742525 704457251745932573898956518571657596148126602031079762825416559050604247911401 695790033835657486925280074302562341949828646791447632277400552946090394017753 633565547193100017543004750471914489984104001586794617924161001645471655133707 407395026044276953855383439755054887109978520540117516974758134492607943368954 378322117245068734423198987884412854206474280973562580706698310697993526069339 213568588139121480735472846322778490808700246777630360555123238665629517885371 967303463470122293958160679250915321748903084088651606111901149844341235012464 692802880599613428351188471544977127847336176628506216977871774382436256571177 945006447771837022199910669502165675764404499794076503799995484500271066598781 360380231412683690578319046079276529727769404361302305178708054651154246939526 512710105292707030667302444712597393995051462840476743136373997825918454117641 332790646063658415292701903027601733947486696034869497654175242930604072700505 903950314852292139257559484507886797792525393176515641619716844352436979444735 596426063339105512682606159572621703669850647328126672452198906054988028078288 142979633669674412480598219214633956574572210229867759974673812606936706913408 155941201611596019023775352555630060624798326124988128819293734347686268921923 977783391073310658825681377717232831532908252509273304785072497713944833389255 208117560845296659055394096556854170600117985729381399825831929367910039184409 928657560599359891000296986446097471471847010153128376263114677420914557404181 590880006494323785583930853082830547607679952435739163122188605754967383224319 565065546085288120190236364471270374863442172725787950342848631294491631847534 753143504139209610879605773098720135248407505763719925365047090858251393686346 386336804289176710760211115982887553994012007601394703366179371539630613986365 549221374159790511908358829009765664730073387931467891318146510931676157582135 142486044229244530411316065270097433008849903467540551864067734260358340960860 553374736276093565885310976099423834738222208729246449768456057956251676557408 841032173134562773585605235823638953203853402484227337163912397321599544082842 166663602329654569470357718487344203422770665383738750616921276801576618109542 009770836360436111059240911788954033802142652394892968643980892611463541457153 519434285072135345301831587562827573389826889852355779929572764522939156747756 667605108788764845349363606827805056462281359888587925994094644604170520447004 631513797543173718775603981596264750141090665886616218003826698996196558058720 863972117699521946678985701179833244060181157565807428418291061519391763005919 431443460515404771057005433900018245311773371895585760360718286050635647997900 413976180895536366960316219311325022385179167205518065926351803625121457592623 836934822266589557699466049193811248660909979812857182349400661555219611220720 309227764620099931524427358948871057662389469388944649509396033045434084210246 240104872332875008174917987554387938738143989423801176270083719605309438394006 375611645856094312951759771393539607432279248922126704580818331376416581826956 210587289244774003594700926866265965142205063007859200248829186083974373235384 908396432614700053242354064704208949921025040472678105908364400746638002087012 666420945718170294675227854007450855237772089058168391844659282941701828823301 497155423523591177481862859296760504820386434310877956289292540563894662194826 871104282816389397571175778691543016505860296521745958198887868040811032843273 986719862130620555985526603640504628215230615459447448990883908199973874745296 981077620148713400012253552224669540931521311533791579802697955571050850747387 475075806876537644578252443263804614304288923593485296105826938210349800040524 840708440356116781717051281337880570564345061611933042444079826037795119854869 455915205196009304127100727784930155503889536033826192934379708187432094991415 959339636811062755729527800425486306005452383915106899891357882001941178653568 214911852820785213012551851849371150342215954224451190020739353962740020811046 553020793286725474054365271759589350071633607632161472581540764205302004534018 357233829266191530835409512022632916505442612361919705161383935732669376015691 442994494374485680977569630312958871916112929468188493633864739274760122696415 884890096571708616059814720446742866420876533479985822209061980217321161423041 947775499073873856794118982466091309169177227420723336763503267834058630193019 324299639720444517928812285447821195353089891012534297552472763573022628138209 180743974867145359077863353016082155991131414420509144729353502223081719366350 934686585865631485557586244781862010871188976065296989926932817870557643514338 206014107732926106343152533718224338526352021773544071528189813769875515757454 693972715048846979361950047772097056179391382898984532742622728864710888327017 372325881824465843624958059256033810521560620615571329915608489206434030339526 226345145428367869828807425142256745180618414956468611163540497189768215422772 247947403357152743681940989205011365340012384671429655186734415374161504256325 671343024765512521921803578016924032669954174608759240920700466934039651017813 485783569444076047023254075555776472845075182689041829396611331016013111907739 863246277821902365066037404160672496249013743321724645409741299557052914243820 807609836482346597388669134991978401310801558134397919485283043673901248208244 481412809544377389832005986490915950532285791457688496257866588599917986752055 455809900455646117875524937012455321717019428288461740273664997847550829422802 023290122163010230977215156944642790980219082668986883426307160920791408519769 523555348865774342527753119724743087304361951139611908003025587838764420608504 473063129927788894272918972716989057592524467966018970748296094919064876469370 275077386643239191904225429023531892337729316673608699622803255718530891928440 380507103006477684786324319100022392978525537237556621364474009676053943983823 576460699246526008909062410590421545392790441152958034533450025624410100635953 003959886446616959562635187806068851372346270799732723313469397145628554261546 765063246567662027924520858134771760852169134094652030767339184114750414016892 412131982688156866456148538028753933116023229255561894104299533564009578649534 093511526645402441877594931693056044868642086275720117231952640502309977456764 783848897346431721598062678767183800524769688408498918508614900343240347674268 624595239589035858213500645099817824463608731775437885967767291952611121385919 472545140030118050343787527766440276261894101757687268042817662386068047788524 288743025914524707395054652513533945959878961977891104189029294381856720507096 460626354173294464957661265195349570186001541262396228641389779673332907056737 696215649818450684226369036784955597002607986799626101903933126376855696876702 929537116252800554310078640872893922571451248113577862766490242516199027747109 033593330930494838059785662884478744146984149906712376478958226329490467981208 998485716357108783119184863025450162092980582920833481363840542172005612198935 366937133673339246441612522319694347120641737549121635700857369439730597970971 972666664226743111776217640306868131035189911227133972403688700099686292254646 500638528862039380050477827691283560337254825579391298525150682996910775425764 748832534141213280062671709400909822352965795799780301828242849022147074811112 401860761341515038756983091865278065889668236252393784527263453042041880250844 236319038331838455052236799235775292910692504326144695010986108889991465855188 187358252816430252093928525807796973762084563748211443398816271003170315133440 230952635192958868069082135585368016100021374085115448491268584126869589917414 913382057849280069825519574020181810564129725083607035685105533178784082900004 155251186577945396331753853209214972052660783126028196116485809868458752512999 740409279768317663991465538610893758795221497173172813151793290443112181587102 351874075722210012376872194474720934931232410706508061856237252673254073332487 575448296757345001932190219911996079798937338367324257610393898534927877747398 050808001554476406105352220232540944356771879456543040673589649101761077594836 454082348613025471847648518957583667439979150851285802060782055446299172320202 822291488695939972997429747115537185892423849385585859540743810488262464878805 330427146301194158989632879267832732245610385219701113046658710050008328517731 177648973523092666123458887310288351562644602367199664455472760831011878838915 114934093934475007302585581475619088139875235781233134227986650352272536717123 075686104500454897036007956982762639234410714658489578024140815840522953693749 971066559489445924628661996355635065262340533943914211127181069105229002465742 360413009369188925586578466846121567955425660541600507127664176605687427420032 957716064344860620123982169827172319782681662824993871499544913730205184366907 672357740005393266262276032365975171892590180110429038427418550789488743883270 306328327996300720069801224436511639408692222074532024462412115580435454206421 512158505689615735641431306888344318528085397592773443365538418834030351782294 625370201578215737326552318576355409895403323638231921989217117744946940367829 618592080340386757583411151882417743914507736638407188048935825686854201164503 135763335550944031923672034865101056104987272647213198654343545040913185951314 518127643731043897250700498198705217627249406521461995923214231443977654670835 171474936798618655279171582408065106379950018429593879915835017158075988378496 225739851212981032637937621832245659423668537679911314010804313973233544909082 491049914332584329882103398469814171575601082970658306521134707680368069532297 199059990445120908727577622535104090239288877942463048328031913271049547859918 019696783532146444118926063152661816744319355081708187547705080265402529410921 826485821385752668815558411319856002213515888721036569608751506318753300294211 868222189377554602722729129050429225978771066787384000061677215463844129237119 352182849982435092089180168557279815642185819119749098573057033266764646072875 743056537260276898237325974508447964954564803077159815395582777913937360171742 299602735310276871944944491793978514463159731443535185049141394155732938204854 212350817391254974981930871439661513294204591938010623142177419918406018034794 988769105155790555480695387854006645337598186284641990522045280330626369562649 091082762711590385699505124652999606285544383833032763859980079292284665950355 121124528408751622906026201185777531374794936205549640107300134885315073548735 390560290893352640071327473262196031177343394367338575912450814933573691166454 128178817145402305475066713651825828489809951213919399563324133655677709800308 191027204099714868741813466700609405102146269028044915964654533010775469541308 871416531254481306119240782118869005602778182423502269618934435254763357353648 561936325441775661398170393063287216690572225974520919291726219984440964615826 945638023950283712168644656178523556516412771282691868861557271620147493405227 694659571219831494338162211400693630743044417328478610177774383797703723179525 543410722344551255558999864618387676490397246116795901810003509892864120419516 355110876320426761297982652942588295114127584126273279079880755975185157684126 474220947972184330935297266521001566251455299474512763155091763673025946213293 019040283795424632325855030109670692272022707486341900543830265068121414213505 715417505750863990767394633514620908288893493837643939925690060406731142209331 219593620298297235116325938677224147791162957278075239505625158160313335938231 150051862689053065836812998810866326327198061127154885879809348791291370749823 057592909186293919501472119758606727009254771802575033773079939713453953264619 526999659638565491759045833358579910201271320458390320085387888163363768518208 372788513117522776960978796214237216254521459128183179821604411131167140691482 717098101545778193920231156387195080502467972579249760577262591332855972637121 120190572077140914864507409492671803581515757151405039761096384675556929897038 354731410022380258346876735012977541327953206097115450648421218593649099791776 687477448188287063231551586503289816422828823274686610659273219790716238464215 348985247621678905026099804526648392954235728734397768049577409144953839157556 548545905897649519851380100795801078375994577529919670054760225255203445398871 253878017196071816407812484784725791240782454436168234523957068951427226975043 187363326301110305342333582160933319121880660826834142891041517324721605335584 999322454873077882290525232423486153152097693846104258284971496347534183756200 301491570327968530186863157248840152663983568956363465743532178349319982554211 730846774529708583950761645822963032442432823773745051702856069806788952176819 815671078163340526675953942492628075696832610749532339053622309080708145591983 735537774874202903901814293731152933464446815121294509759653430628421531944572 711861490001765055817709530246887526325011970520947615941676872778447200019278 913725184162285778379228443908430118112149636642465903363419454065718354477191 244662125939265662030688852005559912123536371822692253178145879259375044144893 398160865790087616502463519704582889548179375668104647461410514249887025213993 687050937230544773411264135489280684105910771667782123833281026218558775131272 117934444820144042574508306394473836379390628300897330624138061458941422769474 793166571762318247216835067807648757342049155762821758397297513447899069658953 254894033561561316740327647246921250575911625152965456854463349811431767025729 566184477548746937846423373723898192066204851189437886822480727935202250179654 534375727416391079197295295081294292220534771730418447791567399173841831171036 252439571615271466900581470000263301045264354786590329073320546833887207873544 476264792529769017091200787418373673508771337697768349634425241994995138831507 487753743384945825976556099655595431804092017849718468549737069621208852437701 385375768141663272241263442398215294164537800049250726276515078908507126599703 670872669276430837722968598516912230503746274431085293430527307886528397733524 601746352770320593817912539691562106363762588293757137384075440646896478310070 458061344673127159119460843593582598778283526653115106504162329532904777217408 355934972375855213804830509000964667608830154061282430874064559443185341375522 016630581211103345312074508682433943215904359443031243122747138584203039010607 094031523555617276799416002039397509989762933532585557562480899669182986422267 750236019325797472674257821111973470940235745722227121252685238429587427350156 366009318804549333898974157149054418255973808087156528143010267046028431681923 039253529779576586241439270154974087927313105163611913757700892956482332364829 826302460797587576774537716010249080462430185652416175665560016085912153455626 760219268998285537787258314514408265458348440947846317877737479465358016996077 940556870119232860804113090462935087182712593466871276669487389982459852778649 956916546402945893506496433580982476596516514209098675520380830920323048734270 346828875160407154665383461961122301375945157925269674364253192739003603860823 645076269882749761872357547676288995075211480485252795084503395857083813047693 788132112367428131948795022806632017002246033198967197064916374117585485187848 401205484467258885140156272501982171906696081262778548596481836962141072171421 498636191877475450965030895709947093433785698167446582826791194061195603784539 785583924076127634410576675102430755981455278616781594965706255975507430652108 530159790807334373607943286675789053348366955548680391343372015649883422089339 997164147974693869690548008919306713805717150585730714881564992071408675825960 287605645978242377024246980532805663278704192676846711626687946348695046450742 021937394525926266861355294062478136120620263649819999949840514386828525895634 226432870766329930489172340072547176418868535137233266787792173834754148002280 339299735793615241275582956927683723123479898944627433045456679006203242051639 628258844308543830720149567210646053323853720314324211260742448584509458049408 182092763914000854042202355626021856434899414543995041098059181794888262805206 644108631900168856815516922948620301073889718100770929059048074909242714101893 354281842999598816966099383696164438152887721408526808875748829325873580990567 075581701794916190611400190855374488272620093668560447559655747648567400817738 170330738030547697360978654385938218722058390234444350886749986650604064587434 600533182743629617786251808189314436325120510709469081358644051922951293245007 883339878842933934243512634336520438581291283434529730865290978330067126179813 031679438553572629699874035957045845223085639009891317947594875212639707837594 486113945196028675121056163897600888009274611586080020780334159145179707303683 519697776607637378533301202412011204698860920933908536577322239241244905153278 095095586645947763448226998607481329730263097502881210351772312446509534965369 309001863776409409434983731325132186208021480992268550294845466181471555744470 966953017769043427203189277060471778452793916047228153437980353967986142437095 668322149146543801459382927739339603275404800955223181666738035718393275707714 204672383862461780397629237713120958078936384144792980258806552212926209362393 063731349664018661951081158347117331202580586672763999276357907806381881306915 636627412543125958993611964762610140556350339952314032311381965623632719896183 725484533370206256346422395276694356837676136871196292181875457608161705303159 072882870071231366630872275491866139577373054606599743781098764980241401124214 277366808275139095931340415582626678951084677611866595766016599817808941498575 497628438785610026379654317831363402513581416115190209649913354873313111502270 068193013592959597164019719605362503355847998096348871803911161281359596856547 886832585643789617315976200241962155289629790481982219946226948713746244472909 345647002853769495885959160678928249105441251599630078136836749020937491573289 627002865682934443134234735123929825916673950342599586897069726733258273590312 128874666045146148785034614282776599160809039865257571726308183349444182019353 338507129234577437557934406217871133006310600332405399169368260374617663856575 887758020122936635327026710068126182517291460820254189288593524449107013820621 155382779356529691457650204864328286555793470720963480737269214118689546732276 775133569019015372366903686538916129168888787640752549349424973342718117889275 993159671935475898809792452526236365903632007085444078454479734829180208204492 667063442043755532505052752283377888704080403353192340768563010934777212563908 864041310107381785333831603813528082811904083256440184205374679299262203769871 801806112262449090924264198582086175117711378905160914038157500336642415609521 632819712233502316742260056794128140621721964184270578432895980288233505982820 819666624903585778994033315227481777695284368163008853176969478369058067106482 808359804669884109813515865490693331952239436328792399053481098783027450017206 543369906611778455436468772363184446476806914282800455107468664539280539940910 875493916609573161971503316696830992946634914279878084225722069714887558063748 030886299511847318712477729191007022758889348693945628951580296537215040960310 776128983126358996489341024703603664505868728758905140684123812424738638542790 828273382797332688550493587430316027474906312957234974261122151741715313361862 241091386950068883589896234927631731647834007746088665559873338211382992877691 149549218419208777160606847287467368188616750722101726110383067178785669481294 878504894306308616994879870316051588410828235127415353851336589533294862949449 506186851477910580469603906937266267038651290520113781085861618888694795760741 358553458515176805197333443349523012039577073962377131603024288720053732099825 300897761897312981788194467173116064723147624845755192873278282512718244680782 421521646956781929409823892628494376024885227900362021938669648221562809360537 317804086372726842669642192994681921490870170753336109479138180406328738759384 826953558307739576144799727000347288018278528138950321798634521611106660883931 405322694490545552786789441757920244002145078019209980446138254780585804844241 640477503153605490659143007815837243012313751156228401583864427089071828481675 752712384678245953433444962201009607105137060846180118754312072549133499424761 711563332140893460915656155060031738421870157022610310191660388706466143889773 631878094071152752817468957640158104701696524755774089164456867771715850058326 994340167720215676772406812836656526412298243946513319735919970940327593850266 955747023181320324371642058614103360652453693916005064495306016126782264894243 739716671766123104897503188573216555498834212180284691252908610148552781527762 562375045637576949773433684601560772703550962904939248708840628106794362241870 474700836884267102255830240359984164595112248527263363264511401739524808619463 584078375355688562231711552094722306543709260679735100056554938122457548372854 571179739361575616764169289580525729752233855861138832217110736226581621884244 317885748879810902665379342666421699091405653643224930133486798815488662866505 234699723557473842483059042367714327879231642240387776433019260019228477831383 763253612102533693581262408686669973827597736568222790721583247888864236934639 616436330873013981421143030600873066616480367898409133592629340230432497492688 783164360268101130957071614191283068657732353263965367739031766136131596555358 499939860056515592193675997771793301974468814837110320650369319289452140265091 546518430993655349333718342529843367991593941746622390038952767381333061774762 957494386871697845376721949350659087571191772087547710718993796089477451265475 750187119487073873678589020061737332107569330221632062843206567119209695058576 117396163232621770894542621460985841023781321581772760222273813349541048100307 327510779994899197796388353073444345753297591426376840544226478421606312276964 696715647399904371590332390656072664411643860540483884716191210900870101913072 607104411414324197679682854788552477947648180295973604943970047959604029274629 920357209976195014034831538094771460105633344699882082212058728151072918297121 191787642488035467231691654185225672923442918712816323259696541354858957713320 833991128877591722611527337901034136208561457799239877832508355073019981845902 595835598926055329967377049172245493532968330000223018151722657578752405883224 908582128008974790932610076257877042865600699617621217684547899644070506624171 021332748679623743022915535820078014116534806564748823061500339206898379476625 503654982280532966286211793062843017049240230198571997894883689718304380518217 441914766042975243725168343541121703863137941142209529588579806015293875275379 903093887168357209576071522190027937929278630363726876582268124199338480816602 160372215471014300737753779269906958712128928801905203160128586182549441335382 078488346531163265040764242839087012101519423196165226842200371123046430067344 206474771802135307012409886035339915266792387110170622186588357378121093517977 560442563469499978725112544085452227481091487430725986960204027594117894258128 188215995235965897918114407765335432175759525553615812800116384672031934650729 680799079396371496177431211940202129757312516525376801735910155733815377200195 244454362007184847566341540744232862106099761324348754884743453966598133871746 609302053507027195298394327142537115576660002578442303107342955153394506048622 276496668762407932435319299263925373107689213535257232108088981933916866827894 828117047262450194840970097576092098372409007471797334078814182519584259809624 174761013825264395513525931188504563626418830033853965243599741693132289471987 830842760040136807470390409723847394583489618653979059411859931035616843686921 948538205578039577388136067954990008512325944252972448666676683464140218991594 456530942344065066785194841776677947047204195882204329538032631053749488312218 039127967844610013972675389219511911783658766252808369005324900459741094706877 291232821430463533728351995364827432583311914445901780960778288358373011185754 365995898272453192531058811502630754257149394302445393187017992360816661130542 625399583389794297160207033876781503301028012009599725222228080142357109476035 192554443492998676781789104555906301595380976187592035893734197896235893112598 390259831026719330418921510968915622506965911982832345550305908173073519550372 166587028805399213857603703537710517802128012956684198414036287272562321442875 430221090947272107347413497551419073704331827662617727599688882602722524713368 335345281669277959132886138176634985772893690096574956228710302436259077241221 909430087175569262575806570991201665962243608024287002454736203639484125595488 172727247365346778364720191830399871762703751572464992228946793232269361917764 161461879561395669956778306829031658969943076733350823499079062410020250613405 734430069574547468217569044165154063658468046369262127421107539904218871612761 778701425886482577522388918459952337629237791558574454947736129552595222657863 646211837759847370034797140820699414558071908021359073226923310083175951065901 912129479540860364075735875020589020870457967000705526250581142066390745921527 330940682364944159089100922029668052332526619891131184201629163107689408472356 436680818216865721968826835840278550078280404345371018365109695178233574303050 485265373807353107418591770561039739506264035544227515610110726177937063472380 499066692216197119425912044508464174638358993823994651739550900085947999013602 667426149429006646711506717542217703877450767356374215478290591101261915755587 023895700140511782264698994491790830179547587676016809410013583761357859135692 445564776446417866711539195135769610486492249008344671548638305447791433009768 048687834818467273375843689272431044740680768527862558516509208826381323362314 873333671476452045087662761495038994950480956046098960432912335834885999029452 640028499428087862403981181488476730121675416110662999555366819312328742570206 373835202008686369131173346973174121915363324674532563087134730279217495622701 468732586789173455837996435135880095935087755635624881049385299900767513551352 779241242927748856588856651324730251471021057535251651181485090275047684551825 209633189906852761443513821366215236889057878669943228881602837748203550601602 989400911971385017987168363374413927597364401700701476370665570350433812111357 641501845182141361982349515960106475271257593518530433287553778305750956742544 268471221961870917856078393614451138333564910325640573389866717812397223751931 643061701385953947436784339267098671245221118969084023632741149660124348309892 994173803058841716661307304006758838043211155537944060549772170594282151488616 567277124090338772774562909711013488518437411869565544974573684521806698291104 505800429988795389902780438359628240942186055628778842880212755388480372864001 944161425749990427200959520465417059810498996750451193647117277222043610261407 975080968697517660023718774834801612031023468056711264476612374762785219024120 256994353471622666089367521983311181351114650385489502512065577263614547360442 685949807439693233129712737715734709971395229118265348515558713733662912024271 430250376326950135091161295299378586468130722648600827088133353819370368259886 789332123832705329762585738279009782646054559855513183668884462826513379849166 783940976135376625179825824966345877195012438404035914084920973375464247448817 618407002356958017741017769692507781489338667255789856458985105689196092439884 156928069698335224022563457049731224526935419383700484318335719651662672157552 419340193309901831930919658292096965624766768365964701959575473934551433741370 876151732367720422738567427917069820454995309591887243493952409444167899884631 984550485239366297207977745281439941825678945779571255242682608994086331737153 889626288962940211210888442737656862452761213037101730078513571540453304150795 944777614359743780374243664697324713841049212431413890357909241603640631403814 983148190525172093710396402680899483257229795456404270175772290417323479607361 878788991331830584306939482596131871381642346721873084513387721908697510494284 376932502498165667381626061594176825250999374167288395174406693254965340310145 222531618900923537648637848288134420987004809622717122640748957193900291857330 746010436072919094576799461492929042798168772942648772995285843464777538690695 014898413392454039414468026362540211861431703125111757764282991464453340892097 696169909837265236176874560589470496817013697490952307208268288789073019001825 342580534342170592871393173799314241085264739094828459641809361413847583113613 057610846236683723769591349261582451622155213487924414504175684806412063652017 038633012953277769902311864802006755690568229501635493199230591424639621702532 974757311409422018019936803502649563695586642590676268568737211033915679383989 576556519317788300024161353956243777784080174881937309502069990089089932808839 743036773659552489130015663329407790713961546453408879151030065132193448667324 827590794680787981942501958262232039513125201410996053126069655540424867054998 678692302174698900954785072567297879476988883109348746442640071818316033165551 153427615562240547447337804924621495213325852769884733626918264917433898782478 927846891882805466998230368993978341374758702580571634941356843392939606819206 177333179173820856243643363535986349449689078106401967407443658366707158692452 118299789380407713750129085864657890577142683358276897855471768718442772612050 926648610205153564284063236848180728794071712796682006072755955590404023317874 944734645476062818954151213916291844429765106694796935401686601005519607768733 539651161493093757096855455938151378956903925101495326562814701199832699220006 639287537471313523642158926512620407288771657835840521964605410543544364216656 224456504299901025658692727914275293117208279393775132610605288123537345106837 293989358087124386938593438917571337630072031976081660446468393772580690923729 752348670291691042636926209019960520412102407764819031601408586355842760953708 655816427399534934654631450404019952853725200495780525465625115410925243799132 626271360909940290226206283675213230506518393405745011209934146491843332364656 937172591448932415900624202061288573292613359680872650004562828455757459659212 053034131011182750130696150983551563200431078460190656549380654252522916199181 995960275232770224985573882489988270746593635576858256051806896428537685077201 222034792099393617926820659014216561592530673794456894907085326356819683186177 226824991147261573203580764629811624401331673789278868922903259334986179702199 498192573961767307583441709855922217017182571277753449150820527843090461946083 521740200583867284970941102326695392144546106621500641067474020700918991195137 646690448126725369153716229079138540393756007783515337416774794210038400230895 185099454877903934612222086506016050035177626483161115332558770507354127924990 985937347378708119425305512143697974991495186053592040383023571635272763087469 321962219006426088618367610334600225547747781364101269190656968649501268837629 690723396127628722304114181361006026404403003599698891994582739762411461374480 405969706257676472376606554161857469052722923822827518679915698339074767114610 302277660602006124687647772881909679161335401988140275799217416767879923160396 356949285151363364721954061117176738737255572852294005436178517650230754469386 930787349911035218253292972604455321079788771144989887091151123725060423875373 484125708606406905205845212275453384800820530245045651766951857691320004281675 805492481178051983264603244579282973012910531838563682120621553128866856495651 261389226136706409395333457052698695969235035309422454386527867767302754040270 224638448355323991475136344104405009233036127149608135549053153902100229959575 658370538126196568314428605795669662215472169562087001372776853696084070483332 513279311223250714863020695124539500373572334680709465648308920980153487870563 349109236605755405086411152144148143463043727327104502776866195310785832333485 784029716092521532609255893265560067212435946425506599677177038844539618163287 961446081778927217183690888012677820743010642252463480745430047649288555340906 218515365435547412547615276977266776977277705831580141218568801170502836527554 321480348800444297999806215790456416195721278450892848980642649742709057912906 921780729876947797511244730599140605062994689428093103421641662993561482813099 887074529271604843363081840412646963792584309418544221635908457614607855856247 381493142707826621518554160387020687698046174740080832434366538235455510944949 843109349475994467267366535251766270677219418319197719637801570216993367508376 005716345464367177672338758864340564487156696432104128259564534984138841289042 068204700761559691684303899934836679354254921032811336318472259230555438305820 694167562999201337317548912203723034907268106853445403599356182357631283776764 063101312533521214199461186935083317658785204711236433122676512996417132521751 355326186768194233879036546890800182713528358488844411176123410117991870923650 718485785622102110400977699445312179502247957806950653296594038398736990724079 767904082679400761872954783596349279390457697366164340535979221928587057495748 169669406233427261973351813662606373598257555249650980726012366828360592834185 584802695841377255897088378994291054980033111388460340193916612218669605849157 148573356828614950001909759112521880039641976216355937574371801148055944229873 041819680808564726571354761283162920044988031540210553059707666636274932830891 688093235929008178741198573831719261672883491840242972129043496552694272640255 964146352591434840067586769035038232057293413298159353304444649682944136732344 215838076169483121933311981906109614295220153617029857510559432646146850545268 497576480780800922133581137819774927176854507553832876887447459159373116247060 109124460982942484128752022446259447763874949199784044682925736096853454984326 653686284448936570411181779380644161653122360021491876876946739840751717630751 684985635920148689294310594020245796962292456664488196757629434953532638217161 339575779076637076456957025973880043841580589433613710655185998760075492418721 171488929522173772114608115434498266547987258005667472405112200738345927157572 771521858994694811794064446639943237004429114074721818022482583773601734668530 074498556471542003612359339731291445859152288740871950870863221883728826282288 463184371726190330577714765156414382230679184738603914768310814135827575585364 359772165002827780371342286968878734979509603110889919614338666406845069742078 770028050936720338723262963785603865321643234881555755701846908907464787912243 637555666867806761054495501726079114293083128576125448194444947324481909379536 900820638463167822506480953181040657025432760438570350592281891987806586541218 429921727372095510324225107971807783304260908679427342895573555925272380551144 043800123904168771644518022649168164192740110645162243110170005669112173318942 340054795968466980429801736257040673328212996215368488140410219446342464622074 557564396045298531307140908460849965376780379320189914086581466217531933766597 011433060862500982956691763884605676297293146491149370462446935198403953444913 514119366793330193661766365255514917498230798707228086085962611266050428929696 653565251668888557211227680277274370891738963977225756489053340103885593112567 999151658902501648696142720700591605616615970245198905183296927893555030393468 121976158218398048396056252309146263844738629603984892438618729850777592879272 206855480721049781765328621018747676689724884113956034948037672703631692100735 083407386526168450748249644859742813493648037242611670426687083192504099761531 907685577032742178501000644198412420739640013960360158381056592841368457411910 273642027416372348821452410134771652960312840865841978795111651152982781462037 913985500639996032659124852530849369031313010079997719136223086601109992914287 124938854161203802041134018888721969347790449752745428807280350930582875442075 513481666092787935356652125562013998824962847872621443236285367650259145046837 763528258765213915648097214192967554938437558260025316853635673137926247587804 944594418342917275698837622626184636545274349766241113845130548144983631178978 448973207671950878415861887969295581973325069995140260151167552975057543781024 223895792578656212843273120220071673057406928686936393018676595825132649914595 026091706934751940897535746401683081179884645247361895605647942635807056256328 118926966302647953595109712765913623318086692153578860781275991053717140220450 618607537486630635059148391646765672320571451688617079098469593223672494673758 309960704258922048155079913275208858378111768521426933478692189524062265792104 362034885292626798401395321645879115157905046057971083898337186403802441751134 722647254701079479399695355466961972676325522991465493349966323418595145036098 034409221220671256769872342794070885707047429317332918852389672197135392449242 617864118863779096281448691786946817759171715066911148002075943201206196963779 510322708902956608556222545260261046073613136886900928172106819861855378098201 847115416363032626569928342415502360097804641710852553761272890533504550613568 414377585442967797701466029438768722511536380119175815402812081825560648541078 793359892106442724489861896162941341800129513068363860929410008313667337215300 835269623573717533073865333820484219030818644918409372394403340524490955455801 640646076158101030176748847501766190869294609876920169120218168829104087070956 095147041692114702741339005225334083481287035303102391969997859741390859360543 359969707560446013424245368249609877258131102473279856207212657249900346829388 687230489556225320446360263985422525841646432427161141981780248259556354490721 922658386366266375083594431487763515614571074552801615967704844271419443518327 569840755267792641126176525061596523545718795667317091331935876162825592078308 018520689015150471334038610031005591481785211038475454293338918844412051794396 997019411269511952656491959418997541839323464742429070271887522353439367363366 320030723274703740712398256202466265197409019976245205619855762576000870817308 328834438183107005451449354588542267857855191537229237955549433341017442016960 009069641561273229777022121795186837635908225512881647002199234886404395915301 846400471432118636062252701154112228380277853891109849020134274101412155976996 543887719748537643115822983853312307175113296190455900793806427669581901484262 799122179294798734890186847167650382732855205908298452980625925035212845192592 798659350613296194679625237397256558415785374456755899803240549218696288849033 256085145534439166022625777551291620077279685262938793753045418108072928589198 971538179734349618723292761474785019261145041327487324297058340847111233374627 461727462658241532427105932250625530231473875925172478732288149145591560503633 457542423377916037495250249302235148196138116256391141561032684495807250827343 176594405409826976526934457986347970974312449827193311386387315963636121862349 726140955607992062831699942007205481152535339394607685001990988655386143349578 165008996164907967814290114838764568217491407562376761845377514403147541120676 016072646055685925779932207033733339891636950434669069482843662998003741452762 771654762382554617088318981086880684785370553648046935095881802536052974079353 867651119507937328208314626896007107517552061443378411454995013643244632819334 638905093654571450690086448344018042836339051357815727397333453728426337217406 577577107983051755572103679597690188995849413019599957301790124019390868135658 553966194137179448763207986880037160730322054742357226689680188212342439188598 416897227765219403249322731479366923400484897605903795809469604175427961378255 378122394764614783292697654516229028170110043784603875654415173943396004891531 881757665050095169740241564477129365661425394936888423051740012992055685428985 389794266995677702708914651373689220610441548166215680421983847673087178759027 920917590069527345668202651337311151800018143412096260165862982107666352336177 400783778342370915264406305407180784335806107296110555002041513169637304684921 335683726540030750982908936461204789111475303704989395283345782408281738644132 271000296831194020332345642082647327623383029463937899837583655455991934086623 509096796113400486702712317652666371077872511186035403755448741869351973365662 177235922939677646325156202348757011379571209623772343137021203100496515211197 601317641940820343734851285260291333491512508311980285017785571072537314913921 570910513096505988599993156086365547740355189816673353588004821466509974143376 118277772335191074121757284159258087259131507460602563490377726337391446137703 802131834744730111303267029691733504770163210661622783002726928336558401179141 944780874825336071440329625228577500980859960904093631263562132816207145340610 422411208301000858726425211226248014264751942618432585338675387405474349107271 004975428115946601713612259044015899160022982780179603519408004651353475269877 760952783998436808690898919783969353217998013913544255271791022539701081063214 304851137829149851138196914304349750018998068164441212327332830719282436240673 319655469267785119315277511344646890550424811336143498460484905125834568326644 152848971397237604032821266025351669391408204994732048602162775979177123475109 750240307893575993771509502175169355582707253391189233407022383207758580213717 477837877839101523413209848942345961369234049799827930414446316270721479611745 697571968123929191374098292580556195520743424329598289898052923336641541925636 738068949420147124134052507220406179435525255522500874879008656831454283516775 054229480327478304405643858159195266675828292970522612762871104013480178722480 178968405240792436058274246744307672164527031345135416764966890127478680101029 513386269864974821211862904033769156857624069929637249309720162870720018983542 369036414927023696193854737248032985504511208919287982987446786412915941753167 560253343531062674525450711418148323988060729714023472552071349079839898235526 872395090936566787899238371257897624875599044322889538837731734894112275707141 095979004791930104674075041143538178246463079598955563899188477378134134707024 674736211204898622699188851745625173251934135203811586335012391305444191007362 844756751416105041097350585276204448919097890198431548528053398577784431393388 399431044446566924455088594631408175122033139068159659251054685801313383815217 641821043342978882611963044311138879625874609022613090084997543039577124323061 690626291940392143974027089477766370248815549932245882597902063125743691094639 325280624164247686849545532493801763937161563684785982371590238542126584061536 722860713170267474013114526106376538339031592194346981760535838031061288785205 154693363924108846763200956708971836749057816308515813816196688222204757043759 061433804072585386208356517699842677452319582418268369827016023741493836349662 935157685406139734274647089968561817016055110488097155485911861718966802597354 170542398513556001872033507906094642127114399319604652742405088222535977348151 913543857125325854049394601086579379805862014336607882521971780902581737087091 646045272797715350991034073642502038638671822052287969445838765294795104866071 739022932745542678566977686593992341683412227466301506215532050265534146099524 935605085492175654913483095890653617569381763747364418337897422970070354520666 317092960759198962773242309025239744386101426309868773391388251868431650102796 491149773758288891345034114886594867021549210108432808078342808941729800898329 753694064496990312539986391958160146899522088066228540841486427478628197554662 927881462160717138188018084057208471586890683691939338186427845453795671927239 797236465166759201105799566396259853551276355876814021340982901629687342985079 247184605687482833138125916196247615690287590107273310329914062386460833337863 825792630239159000355760903247728133888733917809696660146961503175422675112599 331552967421333630022296490648093458200818106180210022766458040027821333675857 301901137175467276305904435313131903609248909724642792845554991349000518029570 708291905255678188991389962513866231938005361134622429461024895407240485712325 662888893172211643294781619055486805494344103409068071608802822795968695013364 381426825217047287086301013730115523686141690837567574763723976318575703810944 339056456446852418302814810799837691851212720193504404180460472162693944578837 709010597469321972055811407877598977207200968938224930323683051586265728111463 799698313751793762321511125234973430524062210524423435373290565516340666950616 589287821870775679417608071297378133518711793165003315552382248773065344417945 341539520242444970341012087407218810938826816751204229940494817944947273289477 011157413944122845552182842492224065875268917227278060711675404697300803703961 878779669488255561467438439257011582954666135867867189766129731126720007297155 361302750355616781776544228744211472988161480270524380681765357327557860250584 708401320883793281600876908130049249147368251703538221961903901499952349538710 599735114347829233949918793660869230137559636853237380670359114424326856151210 940425958263930167801712866923928323105765885171402021119695706479981403150563 304514156441462316376380990440281625691757648914256971416359843931743327023781 233693804301289262637538266779503416933432360750024817574180875038847509493945 489620974048544263563716499594992098088429479036366629752600324385635294584472 894454716620929749549661687741412088213047702281611645604400723635158114972973 921896673738264720472264222124201656015028497130633279581430251601369482556701 478093579088965713492615816134690180696508955631012121849180584792272069187169 631633004485802010286065785859126997463766174146393415956953955420331462802651 895116793807457331575984608617370268786760294367778050024467339133243166988035 407323238828184750105164133118953703648842269027047805274249060349208295475505 400345716018407257453693814553117535421072655783561549987444748042732345788006 187314934156604635297977945507535930479568720931672453654720838168585560604380 197703076424608348987610134570939487700294617579206195254925575710903852517148 852526567104534981341980339064152987634369542025608027761442191431892139390883 454313176968510184010384447234894886952098194353190650655535461733581404554483 788475252625394966586999205841765278012534103389646981864243003414679138061902 805960785488801078970551694621522877309010446746249797999262712095168477956848 258334140226647721084336243759374161053673404195473896419789542533503630186140 095153476696147625565187382329246854735693580289601153679178730355315937836308 224861517777054157757656175935851201669294311113886358215966761883032610416465 171484697938542262168716140012237821377977413126897726671299202592201740877007 695628347393220108815935628628192856357189338495885060385315817976067947984087 836097596014973342057270460352179060564760328556927627349518220323614411258418 242624771201203577638889597431823282787131460805353357449429762179678903456816 988955351850447832561638070947695169908624710001974880920500952194363237871976 487033922381154036347548862684595615975519376541011501406700122692747439388858 994385973024541480106123590803627458528849356325158538438324249325266608758890 831870070910023737710657698505643392885433765834259675065371500533351448990829 388773735205145933304962653141514138612443793588507094468804548697535817021290 849078734780681436632332281941582734567135644317153796781805819585246484008403 290998194378171817730231700398973305049538735611626102399943325978012689343260 558471027876490107092344388463401173555686590358524491937018104162620850429925 869743581709813389404593447193749387762423240985283276226660494238512970945324 558625210360082928664972417491914198896612955807677097959479530601311915901177 394310420904907942444886851308684449370590902600612064942574471035354765785924 270813041061854621988183009063458818703875585627491158737542106466795134648758 677154383801852134828191581246259933516019893559516796893285220582479942103451 271587716334522299541883968044883552975336128683722593539007920166694133909116 875880398882886921600237325736158820716351627133281051818760210485218067552664 867390890090719513805862673512431221569163790227732870541084203784152568328871 804698795251307326634027851905941733892035854039567703561132935448258562828761 061069822972142096199350933131217118789107876687204454887608941017479864713788 246215395593333327556200943958043453791978228059039595992743691379377866494096 404877784174833643268402628293240626008190808180439091455635193685606304508914 228964521998779884934747772913279726602765840166789013649050874114212686196986 204412696528298108704547986155954533802120115564697997678573892018624359932677 768945406050821883822790983362716712449002676117849826437703300208184459000971 723520433199470824209877151444975101705564302954282181967000920251561584417420 593365814813490269311151709387226002645863056132560579256092733226557934628080 568344392137368840565043430739657406101777937014142461549307074136080544210029 560009566358897789926763051771878194370676149821756418659011616086540863539151 303920131680576903417259645369235080641744656235152392905040947995318407486215 121056183385456617665260639371365880252166622357613220194170137266496607325201 077194793126528276330241380516490717456596485374835466919452358031530196916048 099460681490403781982973236093008713576079862142542209641900436790547904993007 837242158195453541837112936865843055384271762803527912882112930835157565659994 474178843838156514843422985870424559243469329523282180350833372628379183021659 183618155421715744846577842013432998259456688455826617197901218084948033244878 725818377480552226815101137174536841787028027445244290547451823467491956418855 124442133778352142386597992598820328708510933838682990657199461490629025742768 603885051103263854454041918495886653854504057132362968106914681484786965916686 184275679846004186876229805556296304595322792305161672159196867584952363529893 578850774608153732145464298479231051167635774949462295256949766035947396243099 534331040499420967788382700271447849406903707324910644415169605325656058677875 741747211082743577431519406075798356362914332639781221894628744779811980722564 671466405485013100965678631488009030374933887536418316513498254669467331611812 336485439764932502617954935720430540218297487125110740401161140589991109306249 231281311634054926257135672181862893278613883371802853505650359195274140086951 092616754147679266803210923746708721360627833292238641361959412133927803611827 632410600474097111104814000362334271451448333464167546635469973149475664342365 949349684588455152415075637660508663282742479413606287604129064491382851945640 264315322585862404314183866959063324506300039221319264762596269151090445769530 144405461803785750303668621246227863975274666787012100339298487337501447560032 210062235802934377495503203701273846816306102657030087227546296679688089058712 767636106622572235222973920644309352432722810085997309513252863060110549791564 479184500461804676240892892568091293059296064235702106152464620502324896659398 732493396737695202399176089847457184353193664652912584806448019652016283879518 949933675924148562613699594530728725453246329152911012876377060557060953137752 775186792329213495524513308986796916512907384130216757323863757582008036357572 800275449032795307990079944254110872569318801466793559583467643286887696661009 739574996783659339784634695994895061049038364740950469522606385804675807306991 229047408987916687211714752764471160440195271816950828973353714853092893704638 442089329977112585684084660833993404568902678751600877546126798801546585652206 121095349079670736553970257619943137663996060606110640695933082817187642604357 342536175694378484849525010826648839515970049059838081210522111109194332395113 605144645983421079905808209371646452312770402316007213854372346126726099787038 565709199850759563461324846018840985019428768790226873455650051912154654406382 925385127631766392205093834520430077301702994036261543400132276391091298832786 392041230044555168405488980908077917463609243933491264116424009388074635660726 233669584276458369826873481588196105857183576746200965052606592926354829149904 576830721089324585707370166071739819448502884260396366074603118478622583105658 087087030556759586134170074540296568763477417643105175103673286924555858208237 203860178173940517513043799486882232004437804310317092103426167499800007301609 481458637448877852227307633049538394434538277060876076354209844500830624763025 357278103278346176697054428715531534001649707665719598504174819908720149087568 603778359199471934335277294728553792578768483230110185936580071729118696761765 505377503029303383070644891281141202550615089641100762382457448865518258105814 034532012475472326908754750707857765973254284445935304499207001453874894822655 644222369636554419422544133821222547749753549462482768053333698328415613869236 344335855386847111143049824839899180316545863828935379913053522283343013795337 295401625762322808113849949187614414132293376710656349252881452823950620902235 787668465011666009738275366040544694165342223905210831458584703552935221992827 276057482126606529138553034554974455147034493948686342945965843102419078592368 022456076393678416627051855517870290407355730462063969245330779578224594971042 018804300018388142900817303945050734278701312446686009277858181104091151172937 487362788787490746528556543474888683106411005102302087510776891878152562273525 155037953244485778727761700196485370355516765520911933934376286628461984402629 525218367852236747510880978150709897841308624588152266096355140187449583692691 779904712072649490573726428600521140358123107600669951853612486274675637589622 529911649606687650826173417848478933729505673900787861792535144062104536625064 046372881569823231750059626108092195521115085930295565496753886261297233991462 835847604862762702730973920200143224870758233735491524608560821032888297418390 647886992327369136004883743661522351705843770554521081551336126214291181561530 175888257359489250710887926212864139244330938379733386780613179523731526677382 085802470143352700924380326695174211950767088432634644274912755890774686358216 216604274131517021245858605623363149316464691394656249747174195835421860774871 105733845843368993964591374060338215935224359475162623918868530782282176398323 730618020424656047752794310479618972429953302979249748168405289379104494700459 086499187272734541350810198388186467360939257193051196864560185578245021823106 588943798652243205067737996619695547244058592241795300682045179537004347245176 289356677050849021310773662575169733552746230294303120359626095342357439724965 921101065781782610874531887480318743082357369919515634095716270099244492974910 548985151965866474014822510633536794973714251022934188258511737199449911509758 374613010550506419772153192935487537119163026203032858865852848019350922587577 559742527658401172134232364808402714335636754204637518255252494432965704386138 786590196573880286840189408767281671413703366173265012057865391578070308871426 151907500149257611292767519309672845397116021360630309054224396632067432358279 788933232440577919927848463333977773765590187057480682867834796562414610289950 848739969297075043275302997287229732793444298864641272534816060377970729829917 302929630869580199631241330493935049332541235507105446118259114111645453471032 988104784406778013807713146540009938630648126661433085820681139583831916954555 825942689576984142889374346708410794631893253910696395578070602124597489829356 461356078898347241997947856436204209461341238761319886535235831299686226894860 840845665560687695450127448663140505473535174687300980632278046891224682146080 672762770840240226615548502400895289165711761743902033758487784291128962324705 919187469104200584832614067733375102719565399469716251724831223063391932870798 380074848572651612343493327335666447335855643023528088392434827876088616494328 939916639921048830784777704804572849145630335326507002958890626591549850940797 276756712979501009822947622896189159144152003228387877348513097908101912926722 710377889805396415636236416915498576840839846886168437540706512103906250612810 766379904790887967477806973847317047525344215639038720123880632368803701794930 895490077633152306354837425681665336160664198003018828712376748189833024683637 148830925928337590227894258806008728603885916884973069394802051122176635913825 152427867009440694235512020156837777885182467002565170850924962374772681369428 435006293881442998790530105621737545918267997321773502936892806521002539626880 749809264345801165571588670044350397650532347828732736884086354000274067678382 196352222653929093980736739136408289872201777674716811819585613372158311905468 293608323697611345028175783020293484598292500089568263027126329586629214765314 223335179309338795135709534637718368409244442209631933129562030557551734006797 374061416210792363342380564685009203716715264255637185388957141641977238742261 059666739699717316816941543509528319355641770566862221521799115135563970714331 289365755384464832620120642433801695586269856102246064606933079384785881436740 700059976970364901927332882613532936311240365069865216063898725026723808740339 674439783025829689425689674186433613497947524552629142652284241924308338810358 005378702399954217211368655027534136221169314069466951318692810257479598560514 500502171591331775160995786555198188619321128211070944228724044248115340605589 595835581523201218460582056359269930347885113206862662758877144603599665610843 072569650056306448918759946659677284717153957361210818084154727314266174893313 417463266235422207260014601270120693463952056444554329166298666078308906811879 009081529506362678207561438881578135113469536630387841209234694286873083932043 233387277549680521030282154432472338884521534372725012858974769146080831440412 586818154004918777228786980185345453700652665564917091542952275670922221747411 206272065662298980603289167206874365494824610869736722554740481288924247185432 360575341167285075755205713115669795458488739874222813588798584078313506054829 055148278529489112190538319562422871948475940785939804790109419407067176443903 273071213588738504999363883820550168340277749607027684488028191222063688863681 104356952930065219552826152699127163727738841899328713056346468822739828876319 864570983630891778648708667618548568004767255267541474285102814580740315299219 781455775684368111018531749816701642664788409026268282444825802753209454991510 451851771654631180490456798571325752811791365627815811128881656228587603087597 496384943527567661216895926148503078536204527450775295063101248034180458405943 292607985443562009370809182152392037179067812199228049606973823874331262673030 679594396095495718957721791559730058869364684557667609245090608820221223571925 453671519183487258742391941089044411595993276004450655620646116465566548759424 736925233695599303035509581762617623184956190649483967300203776387436934399982 943020914707361894793269276244518656023955905370512897816345542332011497599489 627842432748378803270141867695262118097500640514975588965029300486760520801049 153788541390942453169171998762894127722112946456829486028149318156024967788794 981377721622935943781100444806079767242927624951078415344642915084276452000204 276947069804177583220909702029165734725158290463091035903784297757265172087724 474095226716630600546971638794317119687348468873818665675127929857501636341131 462753049901913564682380432997069577015078933772865803571279091376742080565549 362541")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 36:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Greater than calculator")
				isItGreater1 = int(input("Enter the first number: "))
				isItGreater2 = int(input("Enter the second number: "))
				if (isItGreater1 > isItGreater2):
					curanswer = isItGreater1
					lessThan = isItGreater2
				if (isItGreater1 < isItGreater2):
					curanswer = isItGreater2
					lessThan = isItGreater1
				print (str(curanswer) + " is greater than " + str(lessThan))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 37:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 38:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 39:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 40:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 41:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 42:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 43:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 44:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 45:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 46:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 47:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 48:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 49:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("")
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 50:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Random Number Generator")
				ranrange = int(input("How many random numbers do you want to generate (1-100 MAX recommended): "))
				rand1 = int(input("Enter the start number of the random range: "))
				rand2 = int(input("Enter the end number of the random range: "))
				staran = int
				staran = 0
				while not (staran == ranrange):
					ranrange - 1
					print (random.randint(rand1, rand2))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad) ")					
			if calcIDSes == 51:
				print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
				print ("Random Number Generator (with decimals)")
				ranrange = float(input("How many random numbers do you want to generate (1-100 MAX recommended): "))
				rand1 = float(input("Enter the start number of the random range: "))
				rand2 = float(input("Enter the end number of the random range: "))
				staran = float
				staran == 0.0
				while not (staran == ranrange):
					ranrange - 1.0
					print (random.randint(rand1, rand2))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 52:
				print ("Min and Max")
				mimax = int(input("Minimum (0) Maximum (1) "))
				mimaxf = int(input("No decimals (0) Decimals (1) "))
				if (mimax == 1):
					if (mimaxf == 0):
						int1 = int(input("Enter a number: "))
						print ("Largest: " + str(int1))
						int2 = int(input("Enter a number: "))
						larg = int(max(int1, int2))
						print ("Largest: " + str(larg))
						int3 = int(input("Enter a number: "))
						larg = int(max(int1, int2, int3))
						print ("Largest: " + str(larg))
						int4 = int(input("Enter a number: "))
						larg = int(max(int1, int2, int3, int4))
						print ("Largest: " + str(larg))
						int5 = int(input("Enter a number: "))
						larg = int(max(int1, int2, int3, int4, 	int5))
						print ("Largest: " + str(larg))
						int6 = int(input("Enter a number: "))
						larg = int(max(int1, int2, int3, int4, int5, int6))
						print ("Largest: " + str(larg))
				if (mimax == 1):
					if (mimaxf == 1):
						int1 = float(input("Enter a number: "))
						print ("Largest: " + str(int1))
						int2 = float(input("Enter a number: "))
						larg = float(max(int1, int2))
						print ("Largest: " + str(larg))
						int3 = float(input("Enter a number: "))
						larg = float(max(int1, int2, int3))
						print ("Largest: " + str(larg))
						int4 = float(input("Enter a number: "))
						larg = float(max(int1, int2, int3, int4))
						print ("Largest: " + str(larg))
						int5 = float(input("Enter a number: "))
						larg = float(max(int1, int2, int3, int4, 	int5))
						print ("Largest: " + str(larg))
						int6 = float(input("Enter a number: "))
						larg = float(max(int1, int2, int3, int4, int5, int6))
						print ("Largest: " + str(larg))
				if (mimax == 0):
					if (mimaxf == 0):
						int1 = int(input("Enter a number: "))
						print ("Smallest: " + str(int1))
						int2 = int(input("Enter a number: "))
						larg = int(min(int1, int2))
						print ("Smallest: " + str(larg))
						int3 = int(input("Enter a number: "))
						larg = int(min(int1, int2, int3))
						print ("Smallest: " + str(larg))
						int4 = int(input("Enter a number: "))
						larg = int(min(int1, int2, int3, int4))
						print ("Smallest: " + str(larg))
						int5 = int(input("Enter a number: "))
						larg = int(min(int1, int2, int3, int4, 	int5))
						print ("Smallest: " + str(larg))
						int6 = int(input("Enter a number: "))
						larg = int(min(int1, int2, int3, int4, int5, int6))
						print ("Smallest: " + str(larg))
				if (mimax == 0):
					if (mimaxf == 1):
						int1 = float(input("Enter a number: "))
						print ("Smallest: " + str(int1))
						int2 = float(input("Enter a number: "))
						larg = float(min(int1, int2))
						print ("Smallest: " + str(larg))
						int3 = float(input("Enter a number: "))
						larg = float(min(int1, int2, int3))
						print ("Smallest: " + str(larg))
						int4 = float(input("Enter a number: "))
						larg = float(min(int1, int2, int3, int4))
						print ("Smallest: " + str(larg))
						int5 = float(input("Enter a number: "))
						larg = float(min(int1, int2, int3, int4, int5))
						print ("Smallest: " + str(larg))
						int6 = float(input("Enter a number: "))
						larg = float(min(int1, int2, int3, int4, int5, int6))
						print ("Smallest: " + str(larg))
				bloat1 = input("| FAIL! SETUP RESTARTING (we can't fix the bug right now, we are porting features in. Stabilizing later, my bad)")
			if calcIDSes == 53:
				print ("Memory calculator")
				basenum = int(input("Base 2 binary (0) Base 10 binary (1) "))
				print ("Byte (0) Kilobyte (1) Megabyte (2) Gigabyte (3) Terabyte (4) Petabyte (5) Exabyte (6) Zettabyte (7) Yottabyte (8)")
				byteID = int(input("Enter an ID (0-8) "))
				if byteID == 0:
					print ("Byte calculator")
					bytecount = int(input("Enter an amount: "))
					bitcount = int(bytecount * 8)
					print ("Total bits: " + str(bitcount))
				if byteID == 1:
					print ("Kilobyte calculator")
					kbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 2:
					print ("Megabyte calculator")
					mbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 3:
					print ("Gigabyte calculator")
					gbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						mbytecount = int(gbytecount * 1024)
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						mbytecount = int(gbytecount * 1000)
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)
					print ("Total Megabytes: " + str(mbytecount))
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 4:
					print ("Terabyte calculator")
					tbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						gbytecount = int(tbytecount * 1024)
						mbytecount = int(gbytecount * 1024)
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 1024)
					if basenum == 1:
						gbytecount = int(tbytecount * 1000)
						mbytecount = int(gbytecount * 1000)
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 1000)
					print ("Total Gigabytes: " + str(gbytecount))
					print ("Total Megabytes: " + str(mbytecount))
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 5:
					print ("Petabyte calculator")
					pbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						tbytecount = int(pbytecount * 1024)
						gbytecount = int(tbytecount * 1024)
						mbytecount = int(gbytecount * 1024)
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						tbytecount = int(pbytecount * 1000)
						gbytecount = int(tbytecount * 1000)
						mbytecount = int(gbytecount * 1000)
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)
					print ("Total Terabytes: " + str(tbytecount))
					print ("Total Gigabytes: " + str(gbytecount))
					print ("Total Megabytes: " + str(mbytecount))
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total Bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 6:
					print ("Exabyte calculator")
					exbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						pbytecount = int(exbytecount * 1024)
						tbytecount = int(pbytecount * 1024)
						gbytecount = int(tbytecount * 1024)
						mbytecount = int(gbytecount * 1024)
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						pbytecount = int(exbytecount * 1000)
						tbytecount = int(pbytecount * 1000)
						gbytecount = int(tbytecount * 1000)
						mbytecount = int(gbytecount * 1000)
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)
					print ("Total Petabytes: " + str(pbytecount))
					print ("Total Terabytes: " + str(tbytecount))
					print ("Total Gigabytes: " + str(gbytecount))
					print ("Total Megabytes: " + str(mbytecount))
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 7:
					print ("Zettabyte calculator")
					zbytecount = int(input("Enter an amount: "))
					if basenum == 0:
						exbytecount = int(zbytecount * 1024)
						pbytecount = int(exbytecount * 1024)
						tbytecount = int(pbytecount * 1024)
						gbytecount = int(tbytecount * 1024)
						mbytecount = int(gbytecount * 1024)
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						exbytecount = int(zbytecount * 1000)
						pbytecount = int(exbytecount * 1000)
						tbytecount = int(pbytecount * 1000)
						gbytecount = int(tbytecount * 1000)
						mbytecount = int(gbytecount * 1000)
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)
					print ("Total Exabytes: " + str(exbytecount))
					print ("Total Petabytes: " + str(pbytecount))
					print ("Total Terabytes: " + str(tbytecount))
					print ("Total Gigabytes: " + str(gbytecount))
					print ("Total Megabytes: " + str(mbytecount))
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
				if byteID == 8:
					print ("Yottabyte calculator")
					ybytecount = int(input("Enter an amount: "))
					if basenum == 0:
						zbytecount = int(ybytecount * 1024)
						exbytecount = int(zbytecount * 1024)
						pbytecount = int(exbytecount * 1024)
						tbytecount = int(pbytecount * 1024)
						gbytecount = int(tbytecount * 1024)
						mbytecount = int(gbytecount * 1024)
						kbytecount = int(mbytecount * 1024)
						bytecount = int(kbytecount * 1024)
						bitcount = int(bytecount * 8)
					if basenum == 1:
						zbytecount = int(ybytecount * 1000)
						exbytecount = int(zbytecount * 1000)
						pbytecount = int(exbytecount * 1000)
						tbytecount = int(pbytecount * 1000)
						gbytecount = int(tbytecount * 1000)
						mbytecount = int(gbytecount * 1000)
						kbytecount = int(mbytecount * 1000)
						bytecount = int(kbytecount * 1000)
						bitcount = int(bytecount * 8)	
					print ("Total Zettabytes: " + str(zbytecount))
					print ("Total Exabytes: " + str(exbytecount))
					print ("Total Petabytes: " + str(pbytecount))
					print ("Total Terabytes: " + str(tbytecount))
					print ("Total Gigabytes: " + str(gbytecount))
					print ("Total Megabytes: " + str(mbytecount))
					print ("Total Kilobytes: " + str(kbytecount))
					print ("Total bytes: " + str(bytecount))
					print ("Total bits: " + str(bitcount))
			if calcIDSes == 54:
				print ("Vote calculator")
				print ("\nSetting up")
				print ("Please set up the candidates")
				print ("Candidate One")
				cand1nam = str(input("Enter Candidate 1's name"))
				cand1pos = str(input("Enter Candidate 1's position (Ex: Governer, President, Mayor, etc"))
				cand1par = str(input("Enter Candidate 1's party"))
				print ("Candidate Two")
				cand2nam = str(input("Enter Candidate 2's name"))
				cand2pos = str(input("Enter Candidate 2's position (Ex: Governer, President, Mayor, etc"))
				cand2par = str(input("Enter Candidate 2's party"))
				votingSes = int(0)
				c1vote = int(0)
				c2vote = int(0)
				while votingSes == 0:
					print ("Candidate positions")
					print (str(cand1nam) + " | " + str(cand1pos) + " | " + str(cand1par) + " | Current vote count: " + str(c1vote))
					print (str(cand2nam) + " | " + str(cand2pos) + " | " + str(cand2par) + " | Current vote count: " + str(c2vote))
					voteTime = int(input("Who do you want to vote for? " + str(cand1nam) + " (0) " + str(cand2nam) + " (1) "))
					if voteTime == 0:
						# (c1vote == c1vote ++ 1)
						c1vote += 1
						print ("You voted for " + str(cand1nam))
					if voteTime == 1:
						# (c2vote == c2vote ++ 1)
						c2vote += 1
						print ("You voted for " + str(cand2nam))
			if calcIDSes == 55:
				print ("Roman numeral calculator")
				print ("Note: this calculator is locked in 8 BIT MODE")
				print ("The maximum value that can be translated however is only 100")
				getInputForRome1 = int(input("Enter a number to calculate: "))
				print ("Addition            [ID: 1]")
				print ("Subtraction         [ID: 2]")
				print ("Multiplication      [ID: 3]")
				print ("Division            [ID: 4]")
				print ("Modular division    [ID: 5]")
				getInputForRome2 = int(input("What type of calculation do you want to do out of the given options? Enter ID here: "))
				getInputForRome3 = int(input("Enter the second number to calculate"))
				if getInputForRome2 == 1:
					preRome = int(getInputForRome1 + getInputForRome3)
				if getInputForRome2 == 2:
					preRome = int(getInputForRome1 - getInputForRome3)
				if getInputForRome2 == 3:
					preRome = int(getInputForRome1 * getInputForRome3)	
				if getInputForRome2 == 4:
					preRome = int(getInputForRome1 / getInputForRome3)	
				if getInputForRome2 == 5:
					preRome = int(getInputForRome1 % getInputForRome3)	
				if preRome < 1:
					print ("Syntax error! The number you entered is too small to be transferred as a roman numeral")
				if preRome == 1:
					print ("The answer is I")
				if preRome == 2:
					print ("The answer is II")
				if preRome == 3:
					print ("The answer is III")
				if preRome == 4:
					print ("The answer is IV")
				if preRome == 5:
					print ("The answer is V")
				if preRome == 6:
					print ("The answer is VI")
				if preRome == 7:
					print ("The answer is VII")
				if preRome == 8:
					print ("The answer is VIII")
				if preRome == 9:
					print ("The answer is IX")
				if preRome == 10:
					print ("The answer is X")
				if preRome == 11:
					print ("The answer is XI")
				if preRome == 12:
					print ("The answer is XII")
				if preRome == 13:
					print ("The answer is XIII")
				if preRome == 14:
					print ("The answer is XIV")
				if preRome == 15:
					print ("The answer is XV")
				if preRome == 16:
					print ("The answer is XVI")
				if preRome == 17:
					print ("The answer is XVII")
				if preRome == 18:
					print ("The answer is XVIII")
				if preRome == 19:
					print ("The answer is XIX")
				if preRome == 20:
					print ("The answer is XX")
				if preRome == 21:
					print ("The answer is XXI")
				if preRome == 22:
					print ("The answer is XXII")
				if preRome == 23:
					print ("The answer is XXIII")
				if preRome == 24:
					print ("The answer is XXIV")
				if preRome == 25:
					print ("The answer is XXV")
				if preRome == 26:
					print ("The answer is XXVI")
				if preRome == 27:
					print ("The answer is XXVII")
				if preRome == 28:
					print ("The answer is XXVIII")
				if preRome == 29:
					print ("The answer is XXIX")
				if preRome == 30:
					print ("The answer is XXX")
				if preRome == 31:
					print ("The answer is XXXI")
				if preRome == 32:
					print ("The answer is XXXII")
				if preRome == 33:
					print ("The answer is XXXIII")
				if preRome == 34:
					print ("The answer is XXXIV")
				if preRome == 35:
					print ("The answer is XXXV")
				if preRome == 36:
					print ("The answer is XXXVI")
				if preRome == 37:
					print ("The answer is XXXVII")
				if preRome == 38:
					print ("The answer is XXXVIII")
				if preRome == 39:
					print ("The answer is XXXVIX")
				if preRome == 40:
					print ("The answer is XL")
				if preRome == 41:
					print ("The answer is XLI")
				if preRome == 42:
					print ("The answer is XLII")
				if preRome == 43:
					print ("The answer is XLIII")
				if preRome == 44:
					print ("The answer is XLIV")
				if preRome == 45:
					print ("The answer is XLV")
				if preRome == 46:
					print ("The answer is XLVI")
				if preRome == 47:
					print ("The answer is XLVII")
				if preRome == 48:
					print ("The answer is XLVIII")
				if preRome == 49:
					print ("The answer is XLVIX")
				if preRome == 50:
					print ("The answer is L")
				if preRome == 51:
					print ("The answer is LI")
				if preRome == 52:
					print ("The answer is LII")
				if preRome == 53:
					print ("The answer is LIII")
				if preRome == 54:
					print ("The answer is LIV")
				if preRome == 55:
					print ("The answer is LV")
				if preRome == 56:
					print ("The answer is LVI")
				if preRome == 57:
					print ("The answer is LVII")
				if preRome == 58:
					print ("The answer is LVIII")
				if preRome == 59:
					print ("The answer is LVIX")
				if preRome == 60:
					print ("The answer is LX")
				if preRome == 61:
					print ("The answer is LXI")
				if preRome == 62:
					print ("The answer is LXII")
				if preRome == 63:
					print ("The answer is LXIII")
				if preRome == 64:
					print ("The answer is LXIV")
				if preRome == 65:
					print ("The answer is LXV")
				if preRome == 66:
					print ("The answer is LXVI")
				if preRome == 67:
					print ("The answer is LXVII")
				if preRome == 68:
					print ("The answer is LXVIII")
				if preRome == 69:
					print ("The answer is LXVIX")
				if preRome == 70:
					print ("The answer is LXX")
				if preRome == 71:
					print ("The answer is LXXI")
				if preRome == 72:
					print ("The answer is LXXII")
				if preRome == 73:
					print ("The answer is LXXIII")
				if preRome == 74:
					print ("The answer is LXXIV")
				if preRome == 75:
					print ("The answer is LXXV")
				if preRome == 76:
					print ("The answer is LXXVI")
				if preRome == 77:
					print ("The answer is LXXVII")
				if preRome == 78:
					print ("The answer is LXXVIII")
				if preRome == 79:
					print ("The answer is LXXVIX")
				if preRome == 80:
					print ("The answer is LXXX")
				if preRome == 81:
					print ("The answer is LXXXI")
				if preRome == 82:
					print ("The answer is LXXXII")
				if preRome == 83:
					print ("The answer is LXXXIII")
				if preRome == 84:
					print ("The answer is LXXXIV")
				if preRome == 85:
					print ("The answer is LXXXV")
				if preRome == 86:
					print ("The answer is LXXXVI")
				if preRome == 87:
					print ("The answer is LXXXVII")
				if preRome == 88:
					print ("The answer is LXXXVIII")
				if preRome == 89:
					print ("The answer is LXXXVIX")
				if preRome == 90:
					print ("The answer is XC")
				if preRome == 91:
					print ("The answer is XCI")
				if preRome == 92:
					print ("The answer is XCII")
				if preRome == 93:
					print ("The answer is XCIII")
				if preRome == 94:
					print ("The answer is XCIV")
				if preRome == 95:
					print ("The answer is XCV")
				if preRome == 96:
					print ("The answer is XCVI")
				if preRome == 97:
					print ("The answer is XCVII")
				if preRome == 98:
					print ("The answer is XCVIII")
				if preRome == 99:
					print ("The answer is XCVIX")
				if preRome == 100:
					print ("The answer is C")
				if preRome == 101:
					print ("The answer is CI") # continue here
				if preRome == 102:
					print ("The answer is CII") 
				if preRome == 103:
					print ("The answer is CIII")
				if preRome == 104:
					print ("The answer is CIV")
				if preRome == 105:
					print ("The answer is CV")
				if preRome == 106:
					print ("The answer is CVI")
				if preRome == 107:
					print ("The answer is CVII")
				if preRome == 108:
					print ("The answer is CVIII")
				if preRome == 109:
					print ("The answer is CVIX")
				if preRome == 110:
					print ("The answer is CX")
				if preRome == 111:
					print ("The answer is CXI")
				if preRome == 112:
					print ("The answer is CXII")
				if preRome == 113:
					print ("The answer is CXIII")
				if preRome == 114:
					print ("The answer is CXIV")
				if preRome == 115:
					print ("The answer is CXV")
				if preRome == 116:
					print ("The answer is CXVI")
				if preRome == 117:
					print ("The answer is CXVII")
				if preRome == 118:
					print ("The answer is CXVIII")
				if preRome == 119:
					print ("The answer is CXIX")
				if preRome == 120:
					print ("The answer is CXX")
				if preRome == 121:
					print ("The answer is CXXI")
				if preRome == 122:
					print ("The answer is CXXII")
				if preRome == 123:
					print ("The answer is CXXIII")
				if preRome == 124:
					print ("The answer is CXXIV")
				if preRome == 125:
					print ("The answer is CXXV")
				if preRome == 126:
					print ("The answer is CXXVI")
				if preRome == 127:
					print ("The answer is CXXVII")
				if preRome == 128:
					print ("The answer is CXXVIII")
				if preRome == 129:
					print ("The answer is CXXIX")
				if preRome == 130:
					print ("The answer is CXXX")
				if preRome == 131:
					print ("The answer is CXXXI")
				if preRome == 132:
					print ("The answer is CXXXII")
				if preRome == 133:
					print ("The answer is CXXXIII")
				if preRome == 134:
					print ("The answer is CXXXIV")
				if preRome == 135:
					print ("The answer is CXXXV")
				if preRome == 136:
					print ("The answer is CXXXVI")
				if preRome == 137:
					print ("The answer is CXXXVII")
				if preRome == 138:
					print ("The answer is CXXXVIII")
				if preRome == 139:
					print ("The answer is CXXXIX")
				if preRome == 140:
					print ("The answer is CXL")
				if preRome == 141:
					print ("The answer is CXLI")
				if preRome == 142:
					print ("The answer is CXLII")
				if preRome == 143:
					print ("The answer is CXLIII")
				if preRome == 144:
					print ("The answer is CXLIV")
				if preRome == 145:
					print ("The answer is CXLV")
				if preRome == 146:
					print ("The answer is CXLVI")
				if preRome == 147:
					print ("The answer is CXLVII")
				if preRome == 148:
					print ("The answer is CXLVIII")
				if preRome == 149:
					print ("The answer is CXLVIX")
				if preRome == 150:
					print ("The answer is CL")
				if preRome == 151:
					print ("The answer is CLI")
				if preRome == 152:
					print ("The answer is CLII")
				if preRome == 153:
					print ("The answer is CLIII")
				if preRome == 154:
					print ("The answer is CLIV")
				if preRome == 155:
					print ("The answer is CLV")
				if preRome == 156:
					print ("The answer is CLVI")
				if preRome == 157:
					print ("The answer is CLVII")
				if preRome == 158:
					print ("The answer is CLVIII")
				if preRome == 159:
					print ("The answer is CLVIX")
				if preRome == 160:
					print ("The answer is CLX")
				if preRome == 161:
					print ("The answer is CLXI")
				if preRome == 162:
					print ("The answer is CLXII")
				if preRome == 163:
					print ("The answer is CLXIII")
				if preRome == 164:
					print ("The answer is CLXIV")
				if preRome == 165:
					print ("The answer is CLXV")
				if preRome == 166:
					print ("The answer is CLXVI")
				if preRome == 167:
					print ("The answer is CLXVII")
				if preRome == 168:
					print ("The answer is CLXVIII")
				if preRome == 169:
					print ("The answer is CLXIX")
				if preRome == 170:
					print ("The answer is CLXX")
				if preRome == 171:
					print ("The answer is CLXXI")
				if preRome == 172:
					print ("The answer is CLXXII")
				if preRome == 173:
					print ("The answer is CLXXIII")
				if preRome == 174:
					print ("The answer is CLXXIV")
				if preRome == 175:
					print ("The answer is CLXXV")
				if preRome == 176:
					print ("The answer is CLXXVI")
				if preRome == 177:
					print ("The answer is CLXXVII")
				if preRome == 178:
					print ("The answer is CLXXVIII")
				if preRome == 179:
					print ("The answer is CLXXIX")
				if preRome == 180:
					print ("The answer is CLXXX")
				if preRome == 181:
					print ("The answer is CLXXXI")
				if preRome == 182:
					print ("The answer is CLXXXII")
				if preRome == 183:
					print ("The answer is CLXXXIII")
				if preRome == 184:
					print ("The answer is CLXXXIV")
				if preRome == 185:
					print ("The answer is CLXXXV")
				if preRome == 186:
					print ("The answer is CLXXXVI")
				if preRome == 187:
					print ("The answer is CLXXXVII")
				if preRome == 188:
					print ("The answer is CLXXXVIII")
				if preRome == 189:
					print ("The answer is CLXXXVIX")
				if preRome == 190:
					print ("The answer is CXC")
				if preRome == 191:
					print ("The answer is CXCI")
				if preRome == 192:
					print ("The answer is CXCII")
				if preRome == 193:
					print ("The answer is CXCIII")
				if preRome == 194:
					print ("The answer is CXCIV")
				if preRome == 195:
					print ("The answer is CXCV")
				if preRome == 196:
					print ("The answer is CXCVI")
				if preRome == 197:
					print ("The answer is CXCVII")
				if preRome == 198:
					print ("The answer is CXCVIII")
				if preRome == 199:
					print ("The answer is CXCVIX")
				if preRome == 200:
					print ("The answer is CC")
				if preRome == 201:
					print ("The answer is CCI")
				if preRome == 202:
					print ("The answer is CCII")
				if preRome == 203:
					print ("The answer is CCIII")
				if preRome == 204:
					print ("The answer is CCIV")
				if preRome == 205:
					print ("The answer is CCV")
				if preRome == 206:
					print ("The answer is CCVI")
				if preRome == 207:
					print ("The answer is CCVII")
				if preRome == 208:
					print ("The answer is CCVIII")
				if preRome == 209:
					print ("The answer is CCVIX")
				if preRome == 210:
					print ("The answer is CCX")
				if preRome == 211:
					print ("The answer is CCXI")
				if preRome == 212:
					print ("The answer is CCXII")
				if preRome == 213:
					print ("The answer is CCXIII")
				if preRome == 214:
					print ("The answer is CCXIV")
				if preRome == 215:
					print ("The answer is CCXV")
				if preRome == 216:
					print ("The answer is CCXVI")
				if preRome == 217:
					print ("The answer is CCXVII")
				if preRome == 218:
					print ("The answer is CCXVIII")
				if preRome == 219:
					print ("The answer is CCXVIX")
				if preRome == 220:
					print ("The answer is CCXX")
				if preRome == 221:
					print ("The answer is CCXXI")
				if preRome == 222:
					print ("The answer is CCXXII")
				if preRome == 223:
					print ("The answer is CCXXIII")
				if preRome == 224:
					print ("The answer is CCXXIV")
				if preRome == 225:
					print ("The answer is CCXXV")
				if preRome == 226:
					print ("The answer is CCXXVI")
				if preRome == 227:
					print ("The answer is CCXXVII")
				if preRome == 228:
					print ("The answer is CCXXVIII")
				if preRome == 229:
					print ("The answer is CCXXVIX")
				if preRome == 230:
					print ("The answer is CCXXX")
				if preRome == 231:
					print ("The answer is CCXXXI")
				if preRome == 232:
					print ("The answer is CCXXXII")
				if preRome == 233:
					print ("The answer is CCXXXIII")
				if preRome == 234:
					print ("The answer is CCXXXIV")
				if preRome == 235:
					print ("The answer is CCXXXV")
				if preRome == 236:
					print ("The answer is CCXXXVI")
				if preRome == 237:
					print ("The answer is CCXXXVII")
				if preRome == 238:
					print ("The answer is CCXXXVIII")
				if preRome == 239:
					print ("The answer is CCXXXVIX")
				if preRome == 240:
					print ("The answer is CCXL")
				if preRome == 241:
					print ("The answer is CCXLI")
				if preRome == 242:
					print ("The answer is CCXLII")
				if preRome == 243:
					print ("The answer is CCXLIII")
				if preRome == 244:
					print ("The answer is CCXLIV")
				if preRome == 245:
					print ("The answer is CCXLV")
				if preRome == 246:
					print ("The answer is CCXLVI")
				if preRome == 247:
					print ("The answer is CCXLVII")
				if preRome == 248:
					print ("The answer is CCXLVIII")
				if preRome == 249:
					print ("The answer is CCXLVIX")
				if preRome == 250:
					print ("The answer is CCL")
				if preRome == 251:
					print ("The answer is CCLI")
				if preRome == 252:
					print ("The answer is CCLII")
				if preRome == 253:
					print ("The answer is CCLIII")
				if preRome == 254:
					print ("The answer is CCLIV")
				if preRome == 255:
					print ("The answer is CCLV")
				if preRome > 255:
					print ("Syntax error! The number you entered is too large for an 8 bit value")
				fallOfTheRomanNumeral = input("Press [ENTER] key to exit")
			if calcIDSes == 56:
				print ("UCALC Grading Manager")
				print ("\nSelect a grading format:")
				print ("Pass/fail    | Possible grades: P/F                                   | ID: 1")
				print ("Numerals     | Possible grades: 1 2 3 4                               | ID: 2")
				print ("Standard     | Possible grades: A+ A A- B+ B B- C+ C C- D+ D D- F     | ID: 3")
				print ("================================================================================")
				print ("Grading rules ")
				print ("Pass/fail ")
				print ("0-50% = fail | 51%-100% = pass")
				print ("Numerals")
				print ("0-25% = 1 | 26-50% = 2 | 51-75% = 3 | 76-100% = 4 |")
				print ("Standard")
				print ("100% = A+ | 95-99% = A | 90-94% = A- | 85-89% = B+ | 80-84% = B | 77-79% = B- |")
				print ("70-76% = C+ | 65-69% = C | 62-64% = C- | 58-61% = D+ | 55-57% = D | 50-54 = D- | 0-49% = F")
				print ("=================================================================================================")
				gradTypeSe1 = int(input("Enter a grade format ID from above: "))
				if gradTypeSe1 == 1:
					className = str(input("Enter your class's name: "))
					Student1name = str(input("Enter the name of the student: "))
					assign1name = str(input("Enter the name of the assignment: "))
					student1assign1grade = float(input("How many points did the student score? "))
					maxassign1grade = float(input("Enter the maximum score for the assignment"))
					totalScore1 = float(student1assign1grade / maxassign1grade * 100)
					print (str(className) + "\n" + str(Student1name) + "\nAssignent: " + str(assign1name) + "\nScore: " + str(student1assign1grade) + " out of " + str(maxassign1grade))
					if totalScore1 > 50:
						gradeSymb1 = str("P")
					if totalScore1 < 50:
						gradeSymb1 = str("F")
					print ("Score: " + str(totalScore1) + " (" + str(gradeSymb1) + ")")
				if gradTypeSe1 == 2:
					className = str(input("Enter your class's name: "))
					Student1name = str(input("Enter the name of the student: "))
					assign1name = str(input("Enter the name of the assignment: "))
					student1assign1grade = float(input("How many points did the student score? "))
					maxassign1grade = float(input("Enter the maximum score for the assignment: "))
					totalScore1 = float(student1assign1grade / maxassign1grade * 100)
					print (str(className) + "\n" + str(Student1name) + "\nAssignent: " + str(assign1name) + "\nScore: " + str(student1assign1grade) + " out of " + str(maxassign1grade))
					if totalScore1 > 75:
						gradeSymb1 = str("4")
					if (totalScore1 < 75):
						if (totalScore1 > 50):
							gradeSymb1 = str("3")
					if (totalScore1 < 50):
						if (totalScore1 > 25):
							gradeSymb1 = str("2")
					if (totalScore1 < 25):
						if (totalScore1 > -1):
							gradeSymb1 = str("1")
				if gradTypeSe1 == 3:
					className = str(input("Enter your class's name: "))
					Student1name = str(input("Enter the name of the student: "))
					assign1name = str(input("Enter the name of the assignment: "))
					student1assign1grade = float(input("How many points did the student score? "))
					maxassign1grade = float(input("Enter the maximum score for the assignment: "))
					totalScore1 = float(student1assign1grade / maxassign1grade * 100)
					print (str(className) + "\n" + str(Student1name) + "\nAssignent: " + str(assign1name) + "\nScore: " + str(student1assign1grade) + " out of " + str(maxassign1grade))
					if totalScore1 == 100:
						gradeSymb1 = str("A+")
					if (totalScore1 < 95):
						if (totalScore1 > 100):
							gradeSymb1 = str("A")
					if (totalScore1 < 90):
						if (totalScore1 > 95):
							gradeSymb1 = str("A-")
					if (totalScore1 < 85):
						if (totalScore1 > 90):
							gradeSymb1 = str("B+")
					if (totalScore1 < 80):
						if (totalScore1 > 85):
							gradeSymb1 = str("B")
					if (totalScore1 < 77):
						if (totalScore1 > 80):
							gradeSymb1 = str("B-")
					if (totalScore1 < 70):
						if (totalScore1 > 77):
							gradeSymb1 = str("C+")
					if (totalScore1 < 65):
						if (totalScore1 > 70):
							gradeSymb = str("C")
					if (totalScore1 < 62):
						if (totalScore1 > 65):
							gradeSymb1 = str("C-")
					if (totalScore1 < 58):
						if (totalScore1 > 62):
							gradeSymb1 = str("D+")
					if (totalScore1 < 55):
						if (totalScore1 > 58):
							gradeSymb1 = str("D")
					if (totalScore1 < 50):
						if (totalScore1 > 55):
							gradeSymb1 = str("D-")
					if (totalScore1 < 49):
						gradeSymb1 = str("F")
					print ("Score: " + str(totalScore1) + " (" + str(gradeSymb1) + ")")
			if calcIDSes == 57:
				print ("IQ Calculator")
				print ("For more information, please read about IQ under the UCALC documentation")
				noMore = input("Press [ENTER] key to exit")
if uCMainConsole == 6:
		print ("Games")
		print ("\n\nThis area requires administrator access to prevent distraction")
		entadminam = str(input("Enter an administrative username: "))
		if (entadminam == adminusr):
			print ("Admin name entered successfully!")
			entadminpas = str(input("Enter the administrators password: "))
			if (entadminpas == adminpas):
				print ("Password entry confirmed!")
				print ("Logging in...\nPlease wait")
				gameLoop = int(1)
				while gameLoop == 1:
					print ("===================================================")
					print ("Game catalog")
					print ("2048  | ID: 10")
					print ("Launch the X  | ID: 11")
					print ("Rock! Paper! Scissors!  | ID: 12")
					print ("Tic-Tac-Toe | ID: 13")
					print ("Pig [ID: 14]")
					print ("Pimun [ID: 15]")
					print ("X cups [ID: 16] ")
					print ("Yahtzee! [ID: 17]")
					print ("Solitaire [ID: 18]")
					print ("Bingo! [ID: 19]")
					print ("Minesweeper [ID: 20]")
					print ("===================================================")
					gameselectID = int(input("Enter an ID to start: "))
					if gameselectID == 10:
						print ("\n\n\n\n\n\n\n\n")
						print ("Welcome to 2048!")
						print ("Multiples of 2:")
						print ("2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 9192, 16384, 32768, x+")
						print ("ERROR! This game is not available in the Command Line version. Please use the Graphical mode to play this game")
						print ("ERROR! (2) This game is not yet developed. Please use a newer version to continue")
						endgame1 = input("Exiting game, press [ENTER] key to continue")
					if gameselectID == 11:
						print ("Launch the X")
						print ("\n\n")
						launchx1 = input("Press [ENTER] key to start")
						megalaunch = (1)
						while megalaunch == (1):
							print ("   x   ")
							launchx2 = input("Press [ENTER] to launch the X")
							print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
						print ("All Xcrafts have been launched")
						exit = input("Press [ENTER] key to quit")
					if gameselectID == 12:
						print ("Rock Paper Scissors")
						startGameIn = input("Press [ENTER] key to start")
						print ("You are playing against your calculator. Good luck!")
						calcrand = int(random.randint(1, 3))
						playerpos = int
						print ("Select your position:")
						rocpapsci = int(input("Rock (0) Paper (1) Scissors (2) "))
						calcwins = int(0)
						userwins = int(0)
						game1 = int(1)
						print ("Rock!")
						print ("Paper!")
						print ("Scissors!")
						while game1 == 1:
							if rocpapsci == 0:
								playerpos = str("Rock")
							if rocpapsci == 1:
								playerpos = str("Paper")
							if rocpapsci == 2:
								playerpos = str("Scissors")
							if calcrand == 1:
								if playerpos == ("Rock"):
									print ("It's a tie!")
									print ("Rock vs. Rock")
								if playerpos == ("Paper"):
									print ("Player loses!\nCalculator wins!")
									print ("Rock vs. paper = rock")
									calcwins += 1
								if playerpos == ("Scissors"):
									print ("Player wins!\nCalculator loses!")
									print ("Rock vs. scissors = scissors")
									userwins += 1
							if calcrand == 2:
								if playerpos == ("Rock"):
									print ("Player loses!\nCalculator wins!")
									print ("Rock vs. Paper = Paper")
									calcwins += 1
								if playerpos == ("Paper"):
									print ("It's a tie!")
									print ("Paper vs. paper")
								if playerpos == ("Scissors"):
									print ("Player wins!\nCalculator loses!")
									print ("Paper vs. scissors = scissors")
									userwins += 1
							if calcrand == 3:
								if playerpos == ("Rock"):
									print ("User wins!\bCalculator loses!")
									print ("Rock vs. Scissors = rock")
									userwins  += 1
								if playerpos == ("Paper"):	
									print ("User loses!\nCalculator wins!")
									print ("Paper vs. scissors = scissors")
									calcwins += 1
								if playerpos == ("Scissors"):
									print ("It's a tie!")
									print ("Scissors vs. Scissors")
							print ("Game results:")
							print ("User: " + str(userwins))
							print ("Calc: " + str(calcwins))
							calcrand = int(random.randint(1, 3))
							nexgame = input("Press [ENTER] key to start a new game")
							print ("Select your position:")
							rocpapsci = int(input("Rock (0) Paper (1) Scissors (2) "))
					if gameselectID == 13:
						print ("Tic-Tac-Toe")
						print (" * | * | * ")
						print (" - | - | - ")
						print (" * | * | * ")
						print (" - | - | - ")
						print (" * | * | * ")
						ticgrid = int(input("Enter a position to start (1-9)"))
						ticgridR = int(random.randint(1, 8))
						print ("This game is unavailable")
						exit = input("Press [ENTER] key to quit")
					if gameselectID == 14:
						print ("Pig")
						print ("\nHow to play")
						print ("Roll random numbers. Get to 500 before your computer")
						print ("This game is unavailable")
						exit = input("Press [ENTER] key to quit")
					if gameselectID == 15:
						print ("P I - M U N")
						print ("Introductory Edition")
						pimunstart = input("\n\n\n\n\nPress [ENTER] key to start")
						print ("\n\n\n")
						introTXT1 = input("Welcome to the world of PIMUN")
						introTXT2 = input("This is a world full of creatures called 'appits'")
						introTXT3 = input("An appit is found out in the wild world of PIMUN. Each appit has it's own abilities")
						introTXT4 = input("However, appits have a common enemy known as malware!")
						introTXT5 = input("You MUST protect and collect appits and kill out the malware that plagues the land")
						introTXT6 = input("Work your way up and take out the evil teams that work in the malware labs")
						introTXT7 = input("[Stuxe] my name is Stuxe and I am going to help you start your journey")
						# LOOONG list of game definitions. Should load within milliseconds 
						appitcount = int(0)
						score = int(0)
						highScore = int(0)
						appit1 = str("<Empty>")
						appit2 = str("<Empty>")
						appit3 = str("<Empty>")
						appit4 = str("<Empty>")
						appit5 = str("<Empty>")
						appit1pos = str("Basic script")
						appit2pos = str("Basic script")
						appit3pos = str("Basic script")
						appit4pos = str("Basic script")
						appit5pos = str("Basic script")
						appit1LVL = int(0)
						appit2LVL = int(0)
						appit3LVL = int(0)
						appit4LVL = int(0)
						appit5LVL = int(0)
						appit1XP = int(0)
						appit2XP = int(0)
						appit3XP = int(0)
						appit4XP = int(0)
						appit5XP = int(0)
						print ("==================================================================")
						print ("| [-_-]                                                          |")
						print ("| [=====================] ( [] ) ( [] ) ( [] )                   |")
						print ("|                                                                |")
						print ("|                                                                |")
						print ("|   (-.-)                                                        |")
						print ("|    |[|                                                         |")
						print ("|    /  \\                                                        |")
						print ("|                                                                |")
						print ("|__________   ___________________________________________________|")
						introTXT8 = input("[STUXE] Now you get to choose your starter appit")
						starteroptions = input("| HTMO lvl 1 | Pithon lvl 1 | scratcher lvl 1")
						starterchoice = input("Choose a starter appit (0-2) ")
						if starterchoice == ("0"):
							introTXT9 = input("You chose HTMO lvl 1")
							appit1 = str("HTMO")
							appit1LVL = int(1)
						if starterchoice == 1:
							introTXT9 = input("You chose Pithon lvl 1")
							appit1 = str("Pithon")
							appit1LVL = int(1)
						if starterchoice == 2:
							introTXT9 = input("You chose Scratcher lvl 1")
							appit1 = str("Scratcher")
							appit1LVL = int(1)
						introTXT10 = input("[STUXE] Now how about you go outside")
						introTXT11 = input("[STUXE] I have a trainer ready for you")
						print ("==================================================================                    ")
						print ("| (-.-)                                                           ")
						print ("|  |[|                                                            ")
						print ("|                                                                 ")
						print ("|           | \ _ / |                                             ")
						print ("|                                                                 ")
						introTXT12 = input("[WHITMAN] Hey there")
						introTXT13 = input("[WHITMAN] The names whitman")
						introTXT14 = input("[WHITMAN] I heard you were into this 'appit' stuff")
						introTXT15 = input("[WHITMAN] show me what you got!")
						if starterchoice == ("0"):
							introTXT16 = input("[WHITMAN] ...\n[WHITMAN] Woah there, that seems like some unfair competition")
							introTXT17 = input("[WHITMAN] an HTMO is no match for ANY appit")
							introTXT18 = input("[WHITMAN] Here, have some XP and we'll try again")
							appit1LVL += 1
							appit1XP += 20
							introTXT19 = input("Your HTMO has leveled up!")
							introTXT20 = input("Level 2")
							appit1LVL += 1
							appit1XP += 30
							introTXT21 = input("Your HTMO has leveled up!")
							introTXT22 = input("Level 3")
							appit1LVL += 1
							appit1XP += 100
							introTXT23 = input("Your HTMO has leveled up!")
							introTXT24 = input("Level 4")
							appit1LVL += 1
							appit1XP += 300
							introTXT25 = input("Your HTMO has leveled up!")
							introTXT26 = input("Level 5")
							introTXT27 = input("What's this? Your HTMO is evolving...")
							appit1pos = str("Simple structure")
							introTXT28 = input("Your HTMO has evolved from a simple script to a simple structure")
							introTXT29 = input("[WHITMAN] OK, let's get this going! Welcome to your first battle")
						if starterchoice == ("1"):
							introTXT30 = input("[WHITMAN] A Pithon? No way!")
							introTXT31 = input("[WHITMAN] Why did that pimp give that to you?")
							introTXT32 = input("[WHITMAN] upupup, no time for answers, let's give that python some exercise!")
						if starterchoice == ("2"):
							introTXT33 = input("[WHITMAN] A scratcher?")
							introTXT34 = input("[WHITMAN] You are one SIIIIIIIIMPLE man")
							introTXT35 = input("[WHITMAN] let's get that scratcher started, fight me!")
						introTXT36 = input("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
						introTXT37 = input("A wild email worm appeared")
						emwormlvl = int(2)
						emwormhealth = int(50)
						emwormdamage = int(12)
						emwormname = str("I-LOVE-YOU.vbs")
						if starterchoice == ("0"):
							print ("| HTML5_webstructure.htm | " + str(appit1LVL))
							print ("|")
							print ("|")
							print ("|")
							print ("|")
							print ("|" + str(emwormname) + " " + " LVL: " + str(emwormlvl))
							print ("| Block | Delete | Flee")
							battleloop = int(1)
							while battleloop == 1:
								introTXT38 = input("What will you do? ")
								if introTXT38 == ("Block"):
									introTXT39 = input("You used block")
									introTXT40 = input("It wasn't very effective")
								if introTXT38 == ("Delete"):
									introTXT41 = input("You used DELETE")
									introTXT42 = input("It was very effective")
									emwormhealth = int(0)
									introTXT43 = input(str(emwormname) + " fainted")
									introTXT44 = input("You earned 6 xp")
									appit1XP += 6
									battleloop -= 1
								if introTXT38 == ("Flee"):
									introTXT45 = input("[WHITMAN] You cannot flee your first fight. Com'on!")
						if starterchoice == ("1"):
							print ("| Hello_World.py | " + str(appit1LVL))
							print ("|")
							print ("|")
							print ("|")
							print ("|")
							print ("|" + str(emwormname) + " " + " LVL: " + str(emwormlvl))
							print ("| Buffer | Delete | Flee")
							battleloop = int(1)
							while battleloop == 1:
								introTXT38 = input("What will you do? ")
								if introTXT38 == ("Buffer"):
									introTXT39 = input("You used buffer")
									introTXT40 = input("It wasn't very effective")
								if introTXT38 == ("Delete"):
									introTXT41 = input("You used DELETE")
									introTXT42 = input("It was very effective")
									emwormhealth = int(0)
									introTXT43 = input(str(emwormname) + " fainted")
									introTXT44 = input("You earned 6 xp")
									appit1XP += 6
									battleloop -= 1
								if introTXT38 == ("Flee"):
									introTXT45 = input("[WHITMAN] You cannot flee your first fight. Com'on!")
						if starterchoice == ("2"):
							print ("| Untitled.sb | " + str(appit1LVL))
							print ("|")
							print ("|")
							print ("|")
							print ("|")
							print ("|" + str(emwormname) + " " + " LVL: " + str(emwormlvl))
							print ("| Run project | Delete | Flee")
							battleloop = int(1)
							while battleloop == 1:
								introTXT38 = input("What will you do? ")
								if introTXT38 == ("Block"):
									introTXT39 = input("You used run project")
									introTXT40 = input("It wasn't very effective")
								if introTXT38 == ("Delete"):
									introTXT41 = input("You used DELETE")
									introTXT42 = input("It was very effective")
									emwormhealth = int(0)
									introTXT43 = input(str(emwormname) + " fainted")
									introTXT44 = input("You earned 6 xp")
									appit1XP += 6
									battleloop -= 1
								if introTXT38 == ("Flee"):
									introTXT45 = input("[WHITMAN] You cannot flee your first fight. Com'on!")
						introTXT46 = input("[WHITMAN] Good job on destroying my worm")
						introTXT47 = input("[WHITMAN] ...")
						introTXT48 = input("[STUXE] Whitman, what are you still doing here?")
						introTXT49 = input("[WHITMAN] oh, ha, just finishing up")
						introTXT50 = input("[WHITMAN] got to go kid, see ya later")
						introTXT51 = input("You are now on your own")
						introTXT52 = input("Consider looking at your appdex")
						introTXT53 = input("| Appdex | continue | ")
						if introTXT53 == ("Appdex"):
							print ("The Pimun appdex")
							print ("Appits")
							print ("HTMO - starter")
							print ("Evolutions")
							print ("Level 1 - Basic script")
							print ("Level 5 - Structured web page")
							print ("Level 10 - Strong web frame")
							print ("Level 20 - Java belly")
							print ("Level 40 - Source code megablock")
							print ("Level 60 - Client")
							print ("Level 80 - website meta HQ")
							print ("Level requirements")
							print ("Level 2 - 20 xp | Level 3 - 50 xp | level 4 - 150 xp | level 5 - 400 xp | level 6 - 700 xp | level 7 - 1000 xp")
							print ("Level 8 - 2000 xp | level 9 - 2500 xp | level 10 - 3200 xp | level 11 - 4000 xp | level 12 - 6000 xp | level 13 - 8000 xp")
							next = input("Press [ENTER] key for more")
							print ("Pithon - Starter")
							print ("Level 1 - Basic script")
							print ("Level 20 - Basic command-line")
							print ("Level 50 - Full command line")
							print ("Level 120 - Workstation")
							print ("Level 140 - Toolkit")
							print ("Level requirements")
							print ("Level 2 - 20 xp | Level 3 - 50 xp | level 4 - 150 xp | level 5 - 400 xp | level 6 - 700 xp | level 7 - 1000 xp")
							print ("Level 8 - 2000 xp | level 9 - 2500 xp | level 10 - 3200 xp | level 11 - 4000 xp | level 12 - 6000 xp | level 13 - 8000 xp")
							next = input("Press [ENTER] key for more")
							print ("Scratcher - Starter")
							print ("Level 1 - Basic script")
							print ("Level 5 - New project")
							print ("Level 10 - Advanced project")
							print ("Level 20 - SB2 project")
							print ("Level requirements")
							print ("Level 2 - 20 xp | Level 3 - 50 xp | level 4 - 150 xp | level 5 - 400 xp | level 6 - 700 xp | level 7 - 1000 xp")
							print ("Level 8 - 2000 xp | level 9 - 2500 xp | level 10 - 3200 xp | level 11 - 4000 xp | level 12 - 6000 xp | level 13 - 8000 xp")
							next = input("Press [ENTER] key for more")
							print ("JavJar Jinx - Common")
							print ("Level 1 - Mini archive")
							print ("Level 20 - Mega archive")
							next = input("Press [ENTER] key for more")
							print ("Javajuice - Common")
							print ("Level 1 - basic script")
							print ("Level 5 - Basic java application")
							print ("Level 25 - Advanced Java application")
							next = input("Press [ENTER] key for more")
							print ("Yammy - Rare")
							print ("Level 1 - Basic script")
							print ("Level 8 - YAML database")
							next = input("Press [ENTER] key for more")
							print ("Bash - Rare")
							print ("Level 1 - Basic script")
							print ("Level 12 - SUDObatch")
							next = input("Press [ENTER] key for more")
							print ("Adobo - Rare")
							print ("Level 1 - CS1")
							print ("Level 10 - CS2")
							print ("Level 20 - CS3")
							print ("Level 30 - CS4")
							print ("Level 50 - CS5")
							print ("Level 60 - CS6")
							print ("Level 90 - CC")
							next = input("Press [ENTER] key for more")
							print ("Malware")
							print ("Email worm - Common")
							print ("Level 1 - I-LOVE-YOU worm")
							next = input("Press [ENTER] key for more")
							print ("Macro - Common")
							print ("Level 1 - Office macro")
							print ("Level 5 - Copy macro")
							print ("Level 20 - Massive macro")
							print ("\tCopies all your moves and uses them against you with 2x the effect")
							next = input("Press [ENTER] key for more")
							print ("Trojan - Common")
							print ("Level 1 - Mini fleet")
							print ("Level 5 - Mini army")
							print ("Level 20 - Army cloner")
							print ("\tDoes the first attack, 80% endurance to all attacks")
							next = input("Press [ENTER] key for more")
							print ("Zip bomb - Rare")
							print ("Level 1 - Tarpit")
							print ("Level 5 - Package")
							print ("Level 20 - Magic package")
							print ("\tUses heavy blocks and sends them to you. Cannot be attacked until all files are extracted. Can only be weakened when corrupted")
							next = input("Press [ENTER] key for more")
							print ("Memz - Rare")
							print ("Level 1 - Version 1.0")
							print ("Level 5 - Version 2.0")
							print ("Level 10 - Version 3.0")
							print ("Level 20 - Version 4.0")
							print ("Level 40 - Version 5.0")
							print ("Level 75 - Vinememz")
							next = input("Press [ENTER] key for more")
							print ("Bonzi buddy - Common")
							print ("Level 1 - New 'friend'")
							print ("Level 5 - Annoyance")
							print ("Level 20 - Team Bonzi")
							print ("\tDistracts you and stalks your moves. Do not show an obvious pattern, or he will be able to defend against it")
							next = input("Press [ENTER] key for more")
							print ("That is the whole index!")
						gamefinished = input("Congratulations!\nYou beat the game")
if uCMainConsole == 7: # File explorer
	print ("UCALC Explorer") # layer 0
	print ("\n")
	exploreLayer1 = int(1)
	while exploreLayer1 == 1:
		print ("Contents of PY://Main") # layer 1
		print ("[-PA-] {DIR} Modes")
		print ("[-PB-] {DIR} Metadata")
		print ("[-PC-] {DIR} Games")
		print ("[-PD-] {DIR} System")
		explorer = input("PY://")
		if explorer == ("PA"):
			explorerLayer1 = int(0)
			explorerLayer2 = int(1)
			while explorerLayer2 == 1:
				print ("Contents of PY://Modes") # layer 2
				print (" ")
				explorer = input("PY://Modes//")
				if explorer == ("PA1"):
					explorerLayer2 == 0
					explorerLayer1 == 1
		if explorer == ("PB"): # layer 1
			explorerLayer1 = int(0)
			explorerLayer2 = int(1)
			while explorerLayer2 == 1:
				print ("Contents of PY://Metadata") # layer 2
				print (" ")
				explorer = input("PY://Metadata//")
				if explorer == ("PB1"):
					explorerLayer2 == 0
					explorerLayer1 == 1
		if explorer == ("PC"): # layer 1
			explorerLayer1 = int(0)
			explorerLayer2 = int(1)
			while explorerLayer2 == 1:
				print ("Contents of PY://Games") # layer 2
				print ("{PROG} 2048.py                |")
				print ("{PROG} Launch_The_X.py        |")
				print ("{PROG} Rock_Paper_Scissors.py | 2369 Bytes")
				print ("{PROG} Tic-Tac-Toe.y          |")
				print ("{PROG} Pig.py                 |")
				print ("{PROG} PiMun.py               |")
				print ("{PROG} X_cups.py              |")
				print ("{PROG} Yahtzee.py             |")
				print ("{PROG} Solitaire.py           |")
				print ("{PROG} Bingo.py               |")
				print ("{PROG} Minesweeper.py         |")				
				explorer = input("PY://Games//")
				if explorer == ("PC1"):
					explorerLayer2 == 0
					explorerLayer1 == 1
		if explorer == ("PD"):
			explorerLayer1 = int(0)
			explorerLayer2 = int(1)
			while explorerLayer2 == 1:
				print ("Contents of PY://System")
				print ("{PROG} Client.py | +394 KB")
				explorer = input("PY://System//")
				if explorer == ("PD1"):
					explorerLayer2 == 0
					explorerLayer1 == 1
if uCMainConsole == 8:
	print ("UCalc Accessories Manager")
	print ("\n")
	print ("Screensavers   [ID: 1]")
	print ("Chatrooms      [ID: 2]")
	selectACessory = str(input("Enter an ID to begin"))
	if selectACessory == ("1"):
		print ("UCalc screensavers")
		print ("\n")
		print ("Number blocks      [ID: 1]")
		print ("Rocket shuttle     [ID: 2]")
		print ("Matrix             [ID: 3]")
		print ("DNA farm           [ID: 4]")
		print ("Binary bay         [ID: 5]")
		screensaverSelect = str(input("Enter an ID to begin"))
		if screensaverSelect == ("1"):
			scron = int(1)
			scrcount = int(0)
			while scron == 1:
				print ("Unavailable")
		if screensaverSelect == ("2"):
			scron = int(1)
			scrcount = int(0)
			while scron == 1:
				print ("Unavailable")
		if screensaverSelect == ("3"):
			scron = int(1)
			scrcount = int(0)
			while scron == 1:
				print ("Unavailable")
		if screensaverSelect == ("4"):
			scron = int(1)
			scrcount = int(0)
			while scron == 1:
				print ("X      X    Y      Y")
				print ("X      X    Y      Y")
				print ("XXXXXXXX    YYYYYYYY")
				print (" X    X      Y    Y ")
				print (" X    X      Y    Y ")
				print (" XXXXXX      YYYYYY ")
				print ("  X  X        Y  Y  ")
				print ("  X  X        Y  Y  ")
				print ("  XXXX        YYYY  ")
				print ("   XX          YY   ")
				print ("   XX          YY   ")
				print ("   XX          YY   ")
				print ("  XXXX        YYYY  ")
				print ("  X  X        Y  Y  ")
				print ("  X  X        Y  Y  ")
				print (" XXXXXX      YYYYYY ")
				print (" X    X      Y    Y ")
				print (" X    X      Y    Y ")
				print ("XXXXXXXX    YYYYYYYY")
				print ("X      X    Y      Y")
				print ("X      X    Y      Y")
				scrcount += 21
		if screensaverSelect == ("5"):
			scron = int(1)
			scrcount = int(0)
			while scron == 1:
				print ("Unavailable")
	if selectACessory == ("2"):
		print ("Chatrooms")
		print ("\n")
		print ("|=====================|")
		print ("| Join a room [ID: 1] |")
		print ("|=====================|")
		print ("\n")
		print ("|===========================|")
		print ("| Create a new room [ID: 2] |")
		print ("|===========================|")
		print ("\n\n\n\n\n\n")
		roomJoiner = str(input("Enter the ID to join or create a room: "))
		if roomJoiner == ("1"):
			print ("No rooms found!")
		if roomJoiner == ("2"):
			print ("New room")
exit1 = input("Press [ENTER] key to exit")
if uCMainConsole == 9:	
	print ("UCalc settings")
	print ("\nFont: [Calibri]")
	print ("[Courier] [Comic Sans] [Times new roman] [Scratch]")
	print ("\nResolution: [EXPANDABLE: (1360x730) ]")
	print ("[1280x720] [1920x1080] [2560x1440] [3840x2160]")
	print ("\nColor type: [MONOCHROME (2 color) ]")
	print ("[16 color] [8 bit] [16 bit] [24 bit] [32 bit]")
	print ("Language: [Python 3.6]")
	print ("[Python 2.7] [Python 3.0] [Python 3.1] [Python 3.2] [Python 3.3] [Python 3.4] [Python 3.5] [Python 3.7] [Python 3.8]")
	print ("Text color")
	print ("Background: [Black]")
	print ("[White] [Grey] [Red] [Blue] [Green] [Orange] [Pink] [Brown] [Purple]")
	print ("Main text: [White]")
	print ("[Black] [Grey] [Red] [Blue] [Green] [Orange] [Pink] [Brown] [Purple]")
	print ("Answer text: [White]")
	print ("[Black] [Grey] [Red] [Blue] [Green] [Orange] [Pink] [Brown] [Purple]")
	print ("Encoding [UTF-8]")
	print ("[No other options available]")
	print (" ")
	IDSelect = int(input("Enter an ID to change a setting: "))
if not uCMainConsole == (1 or 2 or 3 or 4 or 5 or 6 or 7 or 8 or 9):
	print ("System error")
	print ("Shutting down")
endSession2 = str(input("Are you sure you want to end your calculating session? (Y/N)"))
print ("Ending session")