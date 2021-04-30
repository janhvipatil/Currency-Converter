# read test_file.txt
file = open('test_file.txt', "r", encoding='UTF-16')
print(file.readline())
file.close()
