# Name: Dusty Stepak
# Date: 03.26.2021
# Program: BF.py
# Purpose: Brute forcefully cracks a password of length < 5



# --------------------------------------------------------------------------
# Import Statements
# --------------------------------------------------------------------------
import sys #Allows access to variables from a Terminal call

'''

https://courses.maine.edu/d2l/le/content/150627/viewContent/5025388/Views

Instructions

For this assignment, you have a choice of implementing one of two Python programs. 

1. Create a brute force password cracking program in Python. 
This program should ask the user to enter a password, and 
the program should try to crack it by checking all possible passwords
with the characters a-zA-Z0-9. 
You may limit the search to passwords of length 4 or less - 
brute forcing long passwords can take a very long time. 
There are several ways to go about this, and feel free to find inspiration on 
the interwebs. However, the work should be yours - 
you should understand and be able to explain what your code is doing.

2. Create a socket program in Python where a client can:

    Connect to the server
    Type input, using a special character to indicate the user is done 
    (for example, 'q').

The server should:

    Echo the data received to the screen.
    Write the same data to a file called pythonserverlog.txt
     (or some other similarly bad log file name)

This program (or combination of client and server programs) 
can be based off the code we looked at in class.
'''