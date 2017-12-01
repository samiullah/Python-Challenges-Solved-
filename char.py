# # Write a Python program to get the n
# # (non-negative integer) copies of the
# first 2 characters of a given string. Return the
# # n copies of the whole string if the length is less than 2.

def dude(str,n):
  if len(str)>2:
    print( n*(str[0]+str[1]))
  elif len(str)==2:
    print(n*(str))

dude("sami",3)
dude("sa",99)
