    
test = "5,6,7,8,9,10,10,10,11,11,12,12,12,13"
line = sorted(set([int(i) for i in test.split(',')]))
print line
print ','.join((str(j) for j in line))