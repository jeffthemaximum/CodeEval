test = "zero;two;five;seven;eight;four"
my_dict = {
    'zero': '0',
    'one': '1',
    'two': '2',
    'three': '3',
    'four': '4',
    'five': '5',
    'six': '6',
    'seven': '7',
    'eight': '8',
    'nine': '9'
}
my_array = test.split(';')
output = ''
for num in my_array:
    output += my_dict[num.rstrip()]
print output
