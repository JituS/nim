#! /usr/local/bin/python
from random import randint
number = randint(30, 50)
while number > 0:
	number -= int(raw_input("current number is {}, Play : ".format(number)))
	number -= number if number <= 1 else (number - 1) if number < 5 else (number - 5) % 3 or 3
	

