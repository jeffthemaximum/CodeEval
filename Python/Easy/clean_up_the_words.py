def alpha_test(c):
    return c if c.isalpha() else " "

test = "13What213are;11you-123+138doing7"
spacey_array = map(alpha_test, test)
clean_string = " ".join(''.join(spacey_array).split()).lower()
print clean_string
