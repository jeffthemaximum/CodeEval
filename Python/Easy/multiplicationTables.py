import sys

def whitespace(length):
	if length == 1:
		sys.stdout.write("   ")
	elif length == 2:
		sys.stdout.write("  ")
	else:
		sys.stdout.write(" ")

for j in range(1, 13):
	for i in range(1,13):
		k = str(j * i)
		if (i != 1):
			whitespace(len(k))
		sys.stdout.write(k)
	print("")