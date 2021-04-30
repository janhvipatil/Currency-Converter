# write your code here
for i in range(1, 11):
    new_file = "file{i}.txt".format(i=str(i))
    with open(new_file, 'at') as f:
        f.write(str(i))
