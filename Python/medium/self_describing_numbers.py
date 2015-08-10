import pudb

test = 1210

def count_of_elements_in_array(element, num_array):
	count = 0
	for num in num_array:
		if num == element:
			count = count + 1

	return count

def self_describing_check(num_array):
	#pu.db
	l = len(num_array)
	flag = True

	while flag == True:
		for i in range(0, l):
			if num_array[i] != count_of_elements_in_array(i, num_array):
				return 0
		return 1

split_test = list(test)
print self_describing_check(split_test)

