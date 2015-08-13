def first_max_word(split_line, max_word):
	for index, item in enumerate(split_line):
	    if len(item) == 100:
	        return index

line = "some line with text"
split_line = line.split(" ")
length = [len(word) for word in split_line]
max_word = max(length)
index = first_max_word(split_line, max_word)
print split_line[index]