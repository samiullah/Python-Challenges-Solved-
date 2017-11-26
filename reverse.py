# Write a Python program which accepts
# the user's first and last name
# and print them in reverse order
# with a space between them.

fname = input("What is your first name")
lname = input("what is your last name")

print('Hello'+' ' +fname+'' +lname)
rev_fname=fname[::-1]
rev_lname = lname[::-1]
print('Your Reversed full name is '+''+rev_fname+' '+rev_lname)



