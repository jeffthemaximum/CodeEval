test = "5;7 -3 -10 4 2 8 -2 4 -5 -2"

split = test.split(";")
n = int(split[0])
nums = split[1].split(" ")
biggest = -101

numnums = []
for i in range(0, len(nums)):
	numnums.append(int(nums[i]))

for i in range(0, len(numnums)):
	count = 0
	if (i <= len(numnums) - n):
		for j in range(i,(i+n)):
			count += numnums[j]
		if (count > biggest):
			biggest = count

print biggest