"""
Binary Conversions
--Logical Operators--

Author: Gavin Mallott
Created: November 12, 2016
Lasted Edited: October 24, 2017
Last Edit: Adding docstrings/annotations
"""


def NOT(bin):
	"""Takes a given binary number and returns the logical NOT of the binary number"""

	bin_int = []

	for letter in bin:
		bin_int.append(int(letter))

	notd_values = []

	for value in range(0,8):
		if bin_int[value] == 1:
			notd_values.append(str(0))
		else:
			notd_values.append(str(1))

	return ''.join(notd_values)


def XOR(bin_one, bin_two):
	"""Takes a given binary number and returns the logical XOR of the binary number"""

	bin_one = str(bin_one)
	bin_two = str(bin_two)
	bin_one_int = [int(letter) for letter in bin_one]
	bin_two_int = [int(letter) for letter in bin_two]

	xord_values = []

	
	for value in range(0,8):
		if bin_one_int[value] == bin_two_int[value]:
			xord_values.append(str(0))
		else:
			xord_values.append(str(1))

	return ''.join(xord_values)


def AND(bin_one, bin_two):
	"""Takes a given binary number and returns the logical AND of the binary number"""

	bin_one_int = []
	bin_two_int = []

	for letter in bin_one:
		bin_one_int.append(int(letter))

	for letter in bin_two:
		bin_two_int.append(int(letter))

	andd_values = []

	for value in range(0,8):
		if bin_one_int[value] == 1 and bin_two_int[value] == 1:
			andd_values.append(str(1))
		else:
			andd_values.append(str(0))


def OR(bin_one, bin_two):
	"""Takes a given binary number and returns the logical OR of the binary number"""

	bin_one_int = []
	bin_two_int = []

	for letter in bin_one:
		bin_one_int.append(int(letter))

	for letter in bin_two:
		bin_two_int.append(int(letter))

	ord_values = []

	for value in range(0,8):
		if bin_one_int[value] == 1 or bin_two_int[value] == 1:
			ord_values.append(str(1))
		else:
			ord_values.append(str(0))
