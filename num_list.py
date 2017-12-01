# Write a Python program to check whether a specified value is contained in a group of values. Go to the editor
# Test Data :
# 3 -> [1, 5, 8, 3] : True
# -1 -> [1, 5, 8, 3] : False

def num_checker(li,n):
  if n in li:
    print( "True")
  else:
    print("False")

num_checker([1, 5, 8, 3],2)
num_checker([1, 5, 8, 3],8)
