import pudb
import sys

def stringarray_to_numarray(string_array):
	num_line = []

	for num in string_array:
		num = int(num)
		num_line.append(num)

	return num_line


#pu.db
test = "-10,2,3,-2,0,5,-15"
split_line = test.split(",")
num_line = stringarray_to_numarray(split_line)
l = len(num_line)
highest_sum = 0

for i in range(0, l):
	for j in range(i+1, l):
		sum_elements = num_line[i] + num_line[j]
		if sum_elements > highest_sum:
			highest_sum = sum_elements

sys.stdout.write(str(highest_sum) + '\n')
