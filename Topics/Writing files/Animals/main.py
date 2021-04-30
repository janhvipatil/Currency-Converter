# read animals.txt
# and write animals_new.txt

old_file = open('animals.txt', 'r', encoding='utf-8')

animals = []

for animal in old_file.readlines():
    animals.append(animal.replace('\n', ' '))

new_file = open('animals_new.txt', 'w', encoding='utf-8')

new_file.writelines("".join(animals))

new_file.close()
old_file.close()
