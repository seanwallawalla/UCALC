print (" ")
print (" ")
print (" ___  ____  ____  ____  ____                                      ")
print ("/ __)(  _ \\( ___)( ___)(  _ \\                                     ")
print ("\\__ \\ )___/ )__)  )__)  )(_) )                                    ")
print ("(___/(__)  (____)(____)(____/                                     ")
print ("  ___    __    __    ___  __  __  __      __   ____  _____  ____  ")
print (" / __)  /__\\  (  )  / __)(  )(  )(  )    /__\\ (_  _)(  _  )(  _ \\ ")
print ("( (__  /(__)\\  )(__( (__  )(__)(  )(__  /(__)\\  )(   )(_)(  )   / ")
print (" \\___)(__)(__)(____)\\___)(______)(____)(__)(__)(__) (_____)(_)\\_) ")
print (" ")
enterToEnter = input("Press [ENTER] key to start! ")
calcIDSes = int(23)
if calcIDSes == 23:
	if calcIDSes == 23:
		if calcIDSes == 23:
			if calcIDSes == 23:
				if calcIDSes == 23:
					print ("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
					print ("Speed calculator")
					more1 = input("New sorting options are available: ")
					print ("| A-Z (0) | Z-A (1) | Slowest to Fastest (2) | Fastest to Slowest (3) |")
					sortOpt = int(input("Enter a sorting ID from above: "))
					if sortOpt == 0:
						print ("Sorting from A-Z")
						print ("Feet per second")
						print ("Kilometres per hour")
						print ("Knots")
						print ("Metres per second")
						print ("Miles per hour")
					if sortOpt == 1:
						print ("Sorting from Z-A")
						print ("Miles per hour")
						print ("Metres per second")
						print ("Knots")
						print ("Kilometres per hour")
						print ("Feet per second")
					if sortOpt == 2:
						print ("Sorting from slowest to fastest")
						print ("/!\\ Warning! this is NOT organized but it still functions correctly")
						print ("Miles per hour")
						print ("Metres per second")
						print ("Knots")
						print ("Kilometres per hour")
						print ("Feet per second")
					if sortOpt == 3:
						print ("Sorting from fastest to slowest")
						print ("/!\\ Warning! this is NOT organized but it still functions correctly")
						print ("Miles per hour")
						print ("Metres per second")
						print ("Knots")
						print ("Kilometres per hour")
						print ("Feet per second")
					unit1 = str(input("Enter a unit name to start: "))
					if (unit1 == "Feet per second" or unit1 == "feet per second" or unit1 == "FEET PER SECOND"):
						feet1 = float(input("Enter an amount in feet: "))
						print ("Select an exponent")
						print ("| Addition (+)         | 0 |")
						print ("| Subtraction (-)      | 1 |")
						print ("| Multiplication (*)   | 2 |")
						print ("| Division (/)         | 3 |")
						print ("| Modular division (%) | 4 |")
						unit2 = int(input("Enter an ID to continue: "))
						if unit2 == 0:
							feet2 = float(input("Enter an amount to add: "))
							curanswer = float(feet1 + feet2)
							print ("The answer is: " + str(curanswer) + " Feet per second")
							kiloCalc = float(curanswer * 1.09728)
							knotCalc = float(curanswer * 0.5924835)
							metreCalc = float(curanswer * 0.3048)
							mileCalc = float(curanswer * 0.6818182)
							print ("This is also equal to: ")
							print ("Kilometres per hour: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 1:
							feet2 = float(input("Enter an amount to subtract by: "))
							curanswer = float(feet1 - feet2)
							print ("The answer is: " + str(curanswer) + " Feet per second")
							kiloCalc = float(curanswer * 1.09728)
							knotCalc = float(curanswer * 0.5924835)
							metreCalc = float(curanswer * 0.3048)
							mileCalc = float(curanswer * 0.6818182)
							print ("This is also equal to: ")
							print ("Kilometres per hour: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 2:
							feet2 = float(input("Enter an amount to multiply by: "))
							curanswer = float(feet1 * feet2)
							print ("The answer is: " + str(curanswer) + " Feet per second")
							kiloCalc = float(curanswer * 1.09728)
							knotCalc = float(curanswer * 0.5924835)
							metreCalc = float(curanswer * 0.3048)
							mileCalc = float(curanswer * 0.6818182)
							print ("This is also equal to: ")
							print ("Kilometres per hour: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 3:
							feet2 = float(input("Enter an amount to divide by: "))
							curanswer = float(feet1 / feet2)
							print ("The answer is: " + str(curanswer) + " Feet per second")
							kiloCalc = float(curanswer * 1.09728)
							knotCalc = float(curanswer * 0.5924835)
							metreCalc = float(curanswer * 0.3048)
							mileCalc = float(curanswer * 0.6818182)
							print ("This is also equal to: ")
							print ("Kilometres per hour: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 4:
							feet2 = float(input("Enter an amount to mod: "))
							curanswer = float(feet1 % feet2)
							print ("The answer is: " + str(curanswer) + " Feet per second")
							kiloCalc = float(curanswer * 1.09728)
							knotCalc = float(curanswer * 0.5924835)
							metreCalc = float(curanswer * 0.3048)
							mileCalc = float(curanswer * 0.6818182)
							print ("This is also equal to: ")
							print ("Kilometres per hour: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
					if (unit1 == "Kilometres per second" or unit1 == "Kilometres" or unit1 == "KILOMETRES"):
						kilo1 = float(input("Enter an amount in kilometres: "))
						print ("Select an exponent")
						print ("| Addition (+)         | 0 |")
						print ("| Subtraction (-)      | 1 |")
						print ("| Multiplication (*)   | 2 |")
						print ("| Division (/)         | 3 |")
						print ("| Modular division (%) | 4 |")
						unit2 = int(input("Enter an ID to continue: "))
						if unit2 == 0:
							kilo2 = float(input("Enter an amount to add: "))
							curanswer = float(kilo1 + kilo2)
							print ("The answer is: " + str(curanswer) + " Kilometres per second")
							feetCalc = float(curanswer * 0.9113444)
							knotCalc = float(curanswer * 0.5399565)
							metreCalc = float(curanswer * 0.2777778)
							mileCalc = float(curanswer * 0.6213712)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 1:
							kilo2 = float(input("Enter an amount to subtract: "))
							curanswer = float(kilo1 - kilo2)
							print ("The answer is: " + str(curanswer) + " Kilometres per second")
							feetCalc = float(curanswer * 0.9113444)
							knotCalc = float(curanswer * 0.5399565)
							metreCalc = float(curanswer * 0.2777778)
							mileCalc = float(curanswer * 0.6213712)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 2:
							kilo2 = float(input("Enter an amount to multiply by: "))
							curanswer = float(kilo1 * kilo2)
							print ("The answer is: " + str(curanswer) + " Kilometres per second")
							feetCalc = float(curanswer * 0.9113444)
							knotCalc = float(curanswer * 0.5399565)
							metreCalc = float(curanswer * 0.2777778)
							mileCalc = float(curanswer * 0.6213712)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 3:
							kilo2 = float(input("Enter an amount to divide by: "))
							curanswer = float(kilo1 / kilo2)
							print ("The answer is: " + str(curanswer) + " Kilometres per second")
							feetCalc = float(curanswer * 0.9113444)
							knotCalc = float(curanswer * 0.5399565)
							metreCalc = float(curanswer * 0.2777778)
							mileCalc = float(curanswer * 0.6213712)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 4:
							kilo2 = float(input("Enter an amount to mod: "))
							curanswer = float(kilo1 % kilo2)
							print ("The answer is: " + str(curanswer) + " Kilometres per second")
							feetCalc = float(curanswer * 0.9113444)
							knotCalc = float(curanswer * 0.5399565)
							metreCalc = float(curanswer * 0.2777778)
							mileCalc = float(curanswer * 0.6213712)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
					if (unit1 == "Knots" or unit1 == "Knot" or unit1 == "KNOTS"):
						knot1 = float(input("Enter an amount in knots: "))
						print ("Select an exponent")
						print ("| Addition (+)         | 0 |")
						print ("| Subtraction (-)      | 1 |")
						print ("| Multiplication (*)   | 2 |")
						print ("| Division (/)         | 3 |")
						print ("| Modular division (%) | 4 |")
						unit2 = int(input("Enter an ID to continue: "))
						if unit2 == 0:
							knot2 = float(input("Enter an amount to add: "))
							curanswer = float(knot1 + knot2)
							print ("The answer is: " + str(curanswer) + " Knots")
							feetCalc = float(curanswer * 1.687811)
							kiloCalc = float(curanswer * 1.852001)
							metreCalc = float(curanswer * 0.5144447)
							mileCalc = float(curanswer * 1.15078)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 1:
							knot2 = float(input("Enter an amount to subtract: "))
							curanswer = float(knot1 - knot2)
							print ("The answer is: " + str(curanswer) + " Knots")
							feetCalc = float(curanswer * 1.687811)
							kiloCalc = float(curanswer * 1.852001)
							metreCalc = float(curanswer * 0.5144447)
							mileCalc = float(curanswer * 1.15078)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 2:
							knot2 = float(input("Enter an amount to multiply by: "))
							curanswer = float(knot1 * knot2)
							print ("The answer is: " + str(curanswer) + " Knots")
							feetCalc = float(curanswer * 1.687811)
							kiloCalc = float(curanswer * 1.852001)
							metreCalc = float(curanswer * 0.5144447)
							mileCalc = float(curanswer * 1.15078)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 3:
							knot2 = float(input("Enter an amount to divide by: "))
							curanswer = float(knot1 % knot2)
							print ("The answer is: " + str(curanswer) + " Knots")
							feetCalc = float(curanswer * 1.687811)
							kiloCalc = float(curanswer * 1.852001)
							metreCalc = float(curanswer * 0.5144447)
							mileCalc = float(curanswer * 1.15078)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 4:
							knot2 = float(input("Enter an amount to mod: "))
							curanswer = float(knot1 % knot2)
							print ("The answer is: " + str(curanswer) + " Knots")
							feetCalc = float(curanswer * 1.687811)
							kiloCalc = float(curanswer * 1.852001)
							metreCalc = float(curanswer * 0.5144447)
							mileCalc = float(curanswer * 1.15078)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Metres per second: " + str(metreCalc))
							print ("Miles per hour: " + str(mileCalc))
					if (unit1 == "Metre" or unit1 == "metre" or unit1 == "METRES"):
						metre1 = float(input("Enter an amount in metres: "))
						print ("Select an exponent")
						print ("| Addition (+)         | 0 |")
						print ("| Subtraction (-)      | 1 |")
						print ("| Multiplication (*)   | 2 |")
						print ("| Division (/)         | 3 |")
						print ("| Modular division (%) | 4 |")
						unit2 = int(input("Enter an ID to continue: "))
						if unit2 == 0:
							metre2 = float(input("Enter an amount to add: "))
							curanswer = float(metre1 + metre2)
							print ("The answer is: " + str(curanswer) + " Metres per second")
							feetCalc = float(curanswer * 3.28084)
							kiloCalc = float(curanswer * 3.6)
							knotCalc = float(curanswer * 1.943844)
							mileCalc = float(curanswer * 2.236936)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 1:
							metre2 = float(input("Enter an amount to subtract by: "))
							curanswer = float(metre1 - metre2)
							print ("The answer is: " + str(curanswer) + " Metres per second")
							feetCalc = float(curanswer * 3.28084)
							kiloCalc = float(curanswer * 3.6)
							knotCalc = float(curanswer * 1.943844)
							mileCalc = float(curanswer * 2.236936)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 2:
							metre2 = float(input("Enter an amount to multiply by: "))
							curanswer = float(metre1 * metre2)
							print ("The answer is: " + str(curanswer) + " Metres per second")
							feetCalc = float(curanswer * 3.28084)
							kiloCalc = float(curanswer * 3.6)
							knotCalc = float(curanswer * 1.943844)
							mileCalc = float(curanswer * 2.236936)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 3:
							metre2 = float(input("Enter an amount to divide by: "))
							curanswer = float(metre1 / metre2)
							print ("The answer is: " + str(curanswer) + " Metres per second")
							feetCalc = float(curanswer * 3.28084)
							kiloCalc = float(curanswer * 3.6)
							knotCalc = float(curanswer * 1.943844)
							mileCalc = float(curanswer * 2.236936)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Miles per hour: " + str(mileCalc))
						if unit2 == 4:
							metre2 = float(input("Enter an amount to mod: "))
							curanswer = float(metre1 % metre2)
							print ("The answer is: " + str(curanswer) + " Metres per second")
							feetCalc = float(curanswer * 3.28084)
							kiloCalc = float(curanswer * 3.6)
							knotCalc = float(curanswer * 1.943844)
							mileCalc = float(curanswer * 2.236936)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Miles per hour: " + str(mileCalc))
				if (unit1 == "Mile" or unit1 == "mile" or unit1 == "MILE"):
						mile1 = float(input("Enter an amount in miles: "))
						print ("Select an exponent")
						print ("| Addition (+)         | 0 |")
						print ("| Subtraction (-)      | 1 |")
						print ("| Multiplication (*)   | 2 |")
						print ("| Division (/)         | 3 |")
						print ("| Modular division (%) | 4 |")
						unit2 = int(input("Enter an ID to continue: "))
						if unit2 == 0:
							mile2 = float(input("Enter an amount to add: "))
							curanswer = float(mile1 + mile2)
							print ("The answer is: " + str(curanswer) + " Miles per hour")
							feetCalc = float(curanswer * 1.466667)
							kiloCalc = float(curanswer * 1.609344)
							knotCalc = float(curanswer * 0.8689758)
							metreCalc = float(curanswer * 0.44704)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per hour: " + str(metreCalc))
						if unit2 == 1:
							mile2 = float(input("Enter an amount to subtract: "))
							curanswer = float(mile1 - mile2)
							print ("The answer is: " + str(curanswer) + " Miles per hour")
							feetCalc = float(curanswer * 1.466667)
							kiloCalc = float(curanswer * 1.609344)
							knotCalc = float(curanswer * 0.8689758)
							metreCalc = float(curanswer * 0.44704)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per hour: " + str(metreCalc))
						if unit2 == 2:
							mile2 = float(input("Enter an amount to multiply by: "))
							curanswer = float(mile1 * mile2)
							print ("The answer is: " + str(curanswer) + " Miles per hour")
							feetCalc = float(curanswer * 1.466667)
							kiloCalc = float(curanswer * 1.609344)
							knotCalc = float(curanswer * 0.8689758)
							metreCalc = float(curanswer * 0.44704)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per hour: " + str(metreCalc))
						if unit2 == 3:
							mile2 = float(input("Enter an amount to divide by: "))
							curanswer = float(mile1 / mile2)
							print ("The answer is: " + str(curanswer) + " Miles per hour")
							feetCalc = float(curanswer * 1.466667)
							kiloCalc = float(curanswer * 1.609344)
							knotCalc = float(curanswer * 0.8689758)
							metreCalc = float(curanswer * 0.44704)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per hour: " + str(metreCalc))
						if unit2 == 4:
							mile2 = float(input("Enter an amount to mod: "))
							curanswer = float(mile1 % mile2)
							print ("The answer is: " + str(curanswer) + " Miles per hour")
							feetCalc = float(curanswer * 1.466667)
							kiloCalc = float(curanswer * 1.609344)
							knotCalc = float(curanswer * 0.8689758)
							metreCalc = float(curanswer * 0.44704)
							print ("This is also equal to: ")
							print ("Feet per second: " + str(feetCalc))
							print ("Kilometres per second: " + str(kiloCalc))
							print ("Knots: " + str(knotCalc))
							print ("Metres per hour: " + str(metreCalc))
noMore = input("Press [ENTER] key to quit")