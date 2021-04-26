import json

# Loads: convert json file to python format
py_obj = json.loads('{"name": "GN", "active" : false, "value" : null}')
print(py_obj)


# Load
with open('p_to_j.json', 'r') as file:
    data = json.load(file)
    data = json.loads(data)
print(data)