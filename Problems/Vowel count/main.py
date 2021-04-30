string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

count = 0

for i in range(len(string)):
    if string[i] in vowels:
        count += 1

print(count)
