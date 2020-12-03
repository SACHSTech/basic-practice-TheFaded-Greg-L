'''
-------------------------------------------------------------------------------
Name:		cake_jog.py

Purpose: Calculates the distance that users would need to exercise after eating a number of cakes.

Author:	Lui.G

Created:	02/12/2020
------------------------------------------------------------------------------
'''

# Predetermined variables
cake_calories = 225

# User inputed variables
cakes_eaten = int(input("How many cakes did you eat? "))

# Compute how many calories and distance to work off calories
calories_eaten = cake_calories * cakes_eaten

distance_to_burn = calories_eaten / 100

# Print calories from cakes and distance to burn off calories
print("")

if cakes_eaten == 1:
  print(cakes_eaten, "cake was eaten,", "which is", calories_eaten)
  print("You would need to jog", str(distance_to_burn) + "km to burn off those calories")
  
else:
  print(cakes_eaten, "cakes was eaten,", "which is", calories_eaten)
  print("You would need to jog", str(distance_to_burn) + "km to burn off those calories")