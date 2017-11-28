# Write a Python program to print the calendar of a given month and year.
# Note : Use 'calendar' module. 
import calendar
month = input("Enter the month")
year = input("Enter the year")
month=int(month)
year= int(year)

cal = calendar.month(year,month)
print(cal)
