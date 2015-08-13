import pudb


def intersection(line):
    split_line = line.split(";")
    array1 = split_line[0].split(",")
    array2 = split_line[1].split(",")
    intersection = list(set(array1) & set(array2))
    intersection.sort()
    if len(intersection) is 0:
        print ""
    else:
        printline(intersection)


def printline(intersection):
    output = ""
    for i in range(0, len(intersection)):
        if (i != len(intersection) - 1):
            output += intersection[i]
            output += ","
        else:
            output += intersection[i]
    print output

line = "78,79,80,81,82,83,84,85,86,87,88;83,84,85,86,87,88,89,90"
intersection(line)
