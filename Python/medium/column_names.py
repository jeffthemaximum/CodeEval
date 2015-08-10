import string
import pudb

#get test string to num
test = "705"
test = int(test)

#populate letters and numbers list
letters = list(string.ascii_lowercase)
nums = range(1, 27)

#create dictionary mapping letters and numbers
dictionary = dict(zip(nums, letters))


#initialize variable
alph_len = 26
column_names = []

pu.db
if test > 702:
	leftover = test % 702
	biggest = test / 702
	test = leftover

'''
if (test <= alph_len):
	leftover = test
	column_names.append(dictionary[leftover])
elif (test > alph_len and test < alph_len * (alph_len+1)):
	leftover = test % alph_len
	if leftover == 0:
		leftover = 26
		middle = (test / alph_len) - 1
	else:
		middle = test / alph_len

	column_names.append(dictionary[middle])
	column_names.append(dictionary[leftover])

print(column_names)
'''