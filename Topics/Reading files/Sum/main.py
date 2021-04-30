# read test.txt
file = open('sums.txt', "r")
for lines in file.readlines():
    num1 = int(lines.split()[0])
    num2 = int(lines.split()[1])
    print(num1 + num2)
file.close()
