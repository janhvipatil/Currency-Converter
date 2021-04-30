# read test.txt
file = open('test.txt', "r")
for lines in file.readlines():
    print(lines[0])
file.close()
