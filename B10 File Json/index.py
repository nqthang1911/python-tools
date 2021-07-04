import json

# đọc file json
'''
data = ""
with open('data.json') as file_name:
    data = json.load(file_name)
'''

#ghi file json
data = {}
data['users'] = []
data['users'].append({"id":0, "name":"Nguyen", "age":20})
data['users'].append({"id":1, "name":"Quyet", "age":21})
data['users'].append({"id":2, "name":"Thang", "age":22})

with open('data.json','w') as file_json:
    json.dump(data, file_json)