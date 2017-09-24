#Bitwise Operands
def NOT(bin):
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
	bin_one = str(bin_one)
	bin_two = str(bin_two)
	bin_one_int = []
	bin_two_int = []

	for letter in bin_one:
		bin_one_int.append(int(letter))

	for letter in bin_two:
		bin_two_int.append(int(letter))

	xord_values = []

	
	for value in range(0,8):
		if bin_one_int[value] == bin_two_int[value]:
			xord_values.append(str(0))
		else:
			xord_values.append(str(1))

	return ''.join(xord_values)
			

def AND(bin_one, bin_two):
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
