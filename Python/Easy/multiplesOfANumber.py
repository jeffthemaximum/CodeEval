import sys

with open(sys.argv[1], 'r') as input:
    test_cases = input.read().strip().splitlines()

for test in test_cases:
	x = test.split(',') #an array
	i = 1
	flag = True

	while flag:
		if (int(x[1]) * i) > int(x[0]):
			print int(x[1]) * i
			flag = False
		else:
			i = i + 1
			continue
		break