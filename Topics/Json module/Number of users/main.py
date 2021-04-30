# write your code here
with open('users.json', 'r') as users_json:
    users_json = json.load(users_json)
    print(len(users_json.get('users')))
