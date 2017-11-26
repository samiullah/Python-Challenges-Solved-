# Write a Python program to accept a filename
# from the user and print the extension of that. 

filename = input("Enter filename with extension")

splitted_filename = filename.split('.')
print('Extension file is ' + splitted_filename[1])
