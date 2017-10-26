"""
Binary Conversions
--Decimal, Binary, Hexadecimal, Ascii Conversions--

Author: Gavin Mallott
Created: November 12, 2016
Lasted Edited: October 24, 2017
Last Edit: Adding docstrings/annotations
"""


from ascii_lib import interpret_hex_to_acii, interpret_ascii_to_hex


def decimal_to_binary(dec):
	"""Takes a given decimal number and converts it into a binary number"""

	dec = int(dec)
	binary_number = []
	value = 128
	for x in range(0,8):
		if dec >= value:
			binary_number.append("1")
			dec -= value
			value /= 2		
		else:
			binary_number.append("0")
			value /= 2

	return ''.join(binary_number)


def decimal_to_hex(dec):
	"""Takes a given decimal number and converts it into a hexadecimal number"""

	dec = int(dec)
	first = int(dec / 16)
	second = 0
	if first > 0:
		second = dec - (16*first)
	else:
		second = dec

	if first > 9:
		if first == 10: first = "A"
		if first == 11: first = "B"
		if first == 12: first = "C"
		if first == 13: first = "D"
		if first == 14: first = "E"
		if first == 15: first = "F"

	if second > 9:
		if second == 10: second = "A"
		if second == 11: second = "B"
		if second == 12: second = "C"
		if second == 13: second = "D"
		if second == 14: second = "E"
		if second == 15: second = "F"

	return str(first) + str(second)


def binary_to_hex(bin):
	"""Takes a given binary number and converts in into a hexadecimal number"""

	return decimal_to_hex(binary_to_decimal(bin))


def binary_to_decimal(bin):
	"""Takes a given binary number and converts it into a decimal number"""

	value = 128
	number_list = []
	for bit in str(bin):
		bit = int(bit)
		number_list.append(int(bit*value))
		value /= 2
	return str(sum(number_list))
	

def hex_to_decimal(hex):
	"""Takes a given hexadecimal number and converts it into a decimal number"""

	number = []
	value = 16
	for item in hex:

		if item == "A": item = 10
		if item == "B": item = 11
		if item == "C": item = 12
		if item == "D": item = 13
		if item == "E": item = 14
		if item == "F": item = 15
		number.append(int(int(item)*value))
		value /= 16
	return str(sum(number))


def hex_to_binary(hex):
	"""Takes a given hexadecimal number and converts it into a binary number"""

	return decimal_to_binary(hex_to_decimal(hex))


# Text and number conversion
def ascii_to_hex(ascii):
	"""Takes a given ascii value and converts it into a hexadecimal number"""

	return interpret_ascii_to_hex(ascii)

def hex_to_ascii(hex):
	"""Takes a given hexadecimal number and converts it into an ascii value"""

	return interpret_hex_to_acii(hex)

def ascii_to_binary(ascii):
	"""Takes a given ascii value and converts it into a binary number"""

	return hex_to_binary(ascii_to_hex(ascii))

def binary_to_ascii(bin):
	"""Takes a given binary number and converts it into an ascii value"""

	return hex_to_ascii(binary_to_hex(bin))

def ascii_to_decimal(ascii):
	"""Takes a given ascii value and converts it into a decimal number"""

	return hex_to_decimal(ascii_to_hex(ascii))

def decimal_to_ascii(dec):
	"""Takes a given decimal number and converts it into an ascii value"""

	return hex_to_ascii(decimal_to_hex(dec))