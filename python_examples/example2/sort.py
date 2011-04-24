#!/usr/bin/env python
""" This program sorts an array of numbers. Note that the numbers can be
integers, longs, doubles, what have you, because python isn't very picky
about variable types. 

This example will give a general introduction to scripting with input
parameters, importing modules, lists, and some looping.

Input and output formats are as follows:

number of items to sort
item 1
item 2
item 3
etc.

"""

# First, we need to import the modules that we need.
# This is similar to the #include statments in C, but there
# are other ways to do this, which we'll see in another example.
import sys 
import fileinput

# Here, we check to be sure we get the inputs we need.
if (len(sys.argv) != 3):
	print "Usage: " + sys.argv[0] + " inputFile outputFile"
	exit(1)

#Notice that in the 'if' statment, we use a colon instead of braces. Python
#uses whitespace for conditionals and loops and the like instead of braces
#like most languages. This speeds up programming (and makes it easier on your
#fingers), but the expense is getting used to it if you're used to other
#languages.

A = [] #Here we're defining a(n empty) list. Typically, variables in python
#don't need defined first, but because of how we're going to use it later,
# we need to define it here.

for line in fileinput.input([sys.argv[1]]):
	A.append(long(line.strip()))

#Our first loop! For loops in python work like foreach loops in most other languages,
#because lists are a major construct in python. Basically, it's simply "For item in list".
#Also notice that we're opening the file and reading it line by line all in a single line
#of code. We're using the fileinput module we imported earlier to do that.

#You can also see why we needed to define the list above first. For each line, we have to
#append to the list, but we can't append to a non-existant list.

num = A.pop(0) #Here you can see we're using a variable without first defining it.
#We're also using the list like a stack, but we could use it like a queue or what ever
#relevant data structure we wanted.

A.sort() #Finally, instead of any loop or anything, we'll just use a method of lists: sort().

#To finish up, we need to output to a file. Unfortunately, this isn't as nice and neat
#as bringing the file in, but it's not hard. We just need to open the file for writing:
outFile = open(sys.argv[2], 'w')

#and write what we need to:
outFile.write(str(num) + "\n")
for item in A: #Notice that for loop construct, again.
	outFile.write(str(item) + "\n")

#For good programming practice, let's go ahead and close the file.
outFile.close()

#And just in case we're sorting a few million numbers, which could take a few mintues (and was
#the original purpose of this script), we'll let the user know when we're done:
print "Complete."
