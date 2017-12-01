# Write a Python program to
# get a new string from a
# given string where "Is"
# has been added to the front. If the given string
# already begins with "Is" then return the string unchanged


def st(given):
  newstr = "Is "+given
  if given[0]+given[1] == "Is":
    return given
  else:
    return newstr


print(st(input("Enter the string:")))
