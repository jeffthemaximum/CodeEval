test = '1,2,3,4,6;5'
my_array = test.split(';')
nums = my_array[0].split(',')
total = int(my_array[1])
output = ''
for i in range(0, len(nums) - 1):
    nums[i] = int(nums[i])
    diff = total - nums[i]
    if str(diff) in nums:
        output += str(nums[i]) + ',' + str(diff) + ';'
if output is not '':
    print output[:-1]
else:
    print 'NULL'
