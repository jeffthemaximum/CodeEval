import sys

def fourDigit(decimal):
	decimal = decimal * 100
	rounded = format(decimal, '.2f')
	return rounded


def calcPercentage(smallCount, bigCount):
	percentage = (float(smallCount) / float(bigCount))
	percentage = fourDigit(percentage)
	return percentage

total = len(test)
lowerCount= 0
upperCount = 0

for letter in test:
	if letter.islower():
		lowerCount = lowerCount + 1
	else:
		upperCount = upperCount + 1



sys.stdout.write("lowercase: " + str(calcPercentage(lowerCount, total)) + " ")
print "uppercase: " + str(calcPercentage(upperCount, total))
