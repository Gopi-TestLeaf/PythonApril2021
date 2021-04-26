# Python th json

data = {
    'name' : 'Gopinath Jayakumar',
    'exp'  : 10,
    'value': None,
    'is_nothing': True,
    'hobbies': ('always sleeping....', 'always eats')
}


import json

# dumps: convert python to json
print(type(data))
data = json.dumps(data, indent=4)
print(data)

# dump: write the json file
with open('p_to_j.json', 'w') as file:
    json.dump(data, file)