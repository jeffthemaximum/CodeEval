import sys

def stringarray_to_numarray(string_array):
	num_line = []

	for num in string_array:
		num = int(num)
		num_line.append(num)

	return num_line

test = "2,3,-2,-1,10"
split_line = test.split(",")
num_line = stringarray_to_numarray(split_line)

if len(test) == 1:
	sys.stdout.write(str(test[0] + test[0]) + '\n')
else:
	max1 = max(num_line)
	num_line.remove(max1)
	max2 = max(num_line)

	highest_sum = max1 + max2
	sys.stdout.write(str(highest_sum) + '\n')