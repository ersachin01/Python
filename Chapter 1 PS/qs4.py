#Write a python program to print the contents of a directory using the os module. 
#Search online for the function which does that.

import os

# Specify the directory path you want to list
# Use "." for the current directory
path = "."

# Get the contents of the directory
contents = os.listdir(path)

# Print each item
print("Directory contents:")
for item in contents:
    print(item)
