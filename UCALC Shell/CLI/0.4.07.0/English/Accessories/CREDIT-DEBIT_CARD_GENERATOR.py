import random
calcIDSes = int(60)
if calcIDSes == 60:
	if calcIDSes == 60:
		if calcIDSes == 60:
			if calcIDSes == 60:	
				if calcIDSes == 60:
					print ("Credit/Debit card generator")
					print ("\nMake fake credit cards/debit cards here")
					crebitStart = input("Press [ENTER] key to start")
					print ("Please accept the agreement before you start")
					CRDETOU1 = input("\nCredit card and debit card generator")
					print ("\nThe UCalc credit card / debit card generator is for PERSONAL USE ONLY")
					print ("You cannot use this fake card for scams, fraud, or other deceptive acts")
					print ("This feature was made just for fun. You will not be able to use these as actual cards")
					print ("For legal reasons, card numbers cannot contain more than 15 zeroes, and don't contain any letters")
					print ("Pin numbers work though, be careful")
					CRDETOUAccept = input("\nPress [ENTER] to accept the agreement")
					print ("UCalc credit card generator")
					CRDEBankStr = str(input("Enter the name of your bank: "))
					CRDEUsername = str(input("Enter your name: "))
					GenStart = input("Press [ENTER] key to generate your card")
					pinCard = int(random.randint(1000, 9999))
					carddig1 = int(random.randint(10000, 99999))
					carddig2 = int(random.randint(10000, 99999))
					carddig3 = int(random.randint(10000, 99999))
					carddig4 = int(random.randint(10000, 99999))
					print ("=========================================================\n\n")
					print ("[$] " + str(CRDEBankStr) + "\t\t\t " + str(CRDEUsername))
					print ("\n\nPin: " + str(pinCard))
					print ("\n\n\n")
					print ("| " + str(carddig1) + " - " + str(carddig2) + " - " + str(carddig3) + " - " + str(carddig4)+ " | ")
					print ("\n\n\n\n==========================================================")
					noMore = input("Press [ENTER] key to exit")