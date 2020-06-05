# Dictionary
user = {
    'basket': '[1,2,3]',
    'greet': 'hello',
    'age': 20
}
print(user['age']) #Get error if key not exit in user
print(user.get('age'))
print(user.get('agee',55)) # Get default value if key not exit in dictionary

for u in user:
    print(user[u])

# The dict() constructor builds dictionaries directly from sequences of key-value pairs:
user2 = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print(user2)

user3 = {x: x**2 for x in (2,4,6)}
print(user3)

print('basket' in user)
print('size' in user)
print('hello' in user.values())
print('hello' in user.items())
print('greet' in user.items())
print(user.items())
print(user.items())
print(user.values())