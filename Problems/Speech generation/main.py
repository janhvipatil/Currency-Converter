digits = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine']

phone_number = list(input())

for i in range(len(phone_number)):
    val = int(phone_number[i])
    print(digits[val])
