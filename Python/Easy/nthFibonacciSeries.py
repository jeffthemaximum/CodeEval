test = "12"
test = int(test)
dict = {}
dict[0] = 0
dict[1] = 1

for i in xrange(2,test+1):
	dict[i] = (dict[i-1] + dict[i-2])

print dict[test]
