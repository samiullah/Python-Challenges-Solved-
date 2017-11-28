# Write a Python program to get  the difference between a given  number and 17, if the number is greater than  17 return double the absolute difference

number = input("Enter the number")

num = int(number)

diff = num - 17

if num > 17:
  print(2*diff)
else:
  print("sorry dude number was less than 17")
