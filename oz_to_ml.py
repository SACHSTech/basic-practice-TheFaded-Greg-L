'''
-------------------------------------------------------------------------------
Name:		oz_to_ml.py

Purpose: Calculates the amount of ml required to feed a group of people

Author:	Lui.G

Created:	02/12/2020
------------------------------------------------------------------------------
'''

oz = float(input("Enter amount of ounces: "))
serving_size = int(input("Enter amount of people: "))

ml = oz * 29.5735

required_ml = round(ml, 0) * serving_size

print("You will need", required_ml)