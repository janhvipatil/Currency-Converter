camel_case = input()
snake_case = ""

for i in range(len(camel_case)):
    if camel_case[i].isupper() and i > 0:
        snake_case += '_'
        snake_case += str(camel_case[i]).lower()
    else:
        snake_case += str(camel_case[i]).lower()

print(snake_case)
