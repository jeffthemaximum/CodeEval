test = int(test)

if 0 <= test and test <= 2:
	print 'Still in Mama\'s arms'
elif test == 3 or test == 4:
	print 'Preschool Maniac'
elif 12 < test and test <= 14:
	print 'Middle school'
elif 15 <= test and test <= 18:
	print 'High School'
elif 19 <= test and test <= 22:
	print 'College'
elif 23 <= test and test <= 65:
	print 'Working for the man'
elif 66 <= test and test <= 100:
	print 'The Golden Years'
else:
	print 'This program is for humans'

