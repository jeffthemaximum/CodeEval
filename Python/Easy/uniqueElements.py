test = "5,6,7,8,9,10,10,10,11,11,12,12,12,13"
jeff = test.split(",")
nums = []

for string in jeff:
	nums.append(int(string))

setOfNums = sorted(set(nums))

print(",".join( str(j) for j in setOfNums ))
