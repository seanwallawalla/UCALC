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