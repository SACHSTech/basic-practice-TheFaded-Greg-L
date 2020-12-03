'''
-------------------------------------------------------------------------------
Name:		avg_marks.py

Purpose: Prints report card that includes the four course marks as well as the average.

Author:	Lui.G

Created:	02/12/2020
------------------------------------------------------------------------------
'''

# Asks the user for their marks from the four courses.
course_one = float(input("Enter Course One Mark: "))
course_two = float(input("Enter Course Two Mark: "))
course_three = float(input("Enter Course Three Mark: "))
course_four = float(input("Enter Course Four Mark: "))

# Calculate average from four compile
average = (course_one + course_two + course_three + course_four) / 4

# Print the Report Card
print("")
print("Your Report Card:")
print("Course One Mark:", course_one)
print("Course Two Mark:", course_two)
print("Course Three Mark:", course_three)
print("Course Four Mark:", course_four)
print("Term Average:", round(average, 0))
print("")