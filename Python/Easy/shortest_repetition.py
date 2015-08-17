def repeat_checker(test_string):
    first_char = test[0]
    print test_string[1:]
    for counter, char in enumerate(test_string[1:]):
        if char == first_char:
            return (counter + 1)
    return len(test)

test = "adcdefg"
print repeat_checker(test)
