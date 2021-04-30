# write the code here

str_ = input()

file = open('input.txt', 'w', encoding='utf-8')

file.writelines("".join(str_))

file.close()
