# Write a Python program to find whether a
# given number (accept from the user)
# is even or odd, print out an appropriate message to the user.

num = input("Enter number ")
n = int(num)
if n%2 == 0:
  print(num+" is even")
else:
  print(num +" is odd")
