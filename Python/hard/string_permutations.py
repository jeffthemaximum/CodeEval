import random

test = 'hat'
my_array = test.split()
new_array = []
for i in range(0, (len(test) ** 3)):
    scrambled = ''.join(random.sample(test, len(test)))
    if 'n' in scrambled:
        print 'yes'
    if (scrambled in new_array):
        pass
    else:
        new_array.append(scrambled)
print ','.join(new_array)
