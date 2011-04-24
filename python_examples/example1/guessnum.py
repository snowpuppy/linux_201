#!/usr/bin/env python

#Here we import the modules we need.
import random

random.seed() #We need to seed the randomizer

number = random.randint(0,100) #and pull a number from it.
trys = 10 #We're only giving them 10 tries.
guess = -1 #And we need a base guess.

while guess != number and trys != 0: #So, we need to let them guess if they haven't guessed and if they have tries left
	guess = int(raw_input("Guess a number from 0 to 100: ")) #Get the input from them.

	if guess < number: #Yell at them that they're wrong.
		print "Guess Higher!"
	elif guess > number:
		print "Guess Lower!"
	
	trys = trys - 1 #Decrease the number of tries.

if guess == number: #Once we break out of the while, if they were right, tell them so, otherwise tell them they were wrong.
	print "Congratulations! You guessed correcty!"
else:
	print "The answer was " + number
