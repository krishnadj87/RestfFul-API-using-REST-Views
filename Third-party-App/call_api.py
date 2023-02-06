import requests
import json

# end-point or url 
URL = 'http://127.0.0.1:8000/api/student-api/'

# data = json.dumps({"id": 1}) # json data
# headers = ({'content-type': 'application/json'})

# res = requests.get(url=URL,  headers=headers, data = data,)


# res = res.json()
# print(res)

def make_get(id=None):
    data = {}
    if id is not None:
        data['id'] = id
    
    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}

    req  = requests.get(url=URL, data=json_data, headers=headers)
    res   = req.json() # json extractio here
    print(res)
    return res

# make_get(22)

def insert_data():

    data = {
        'id': 11,
        'name': 'Ishna'
        
       
    }

    json_data = json.dumps(data)
    headers = {'content-type': 'application/json'}
    req     = requests.patch(url=URL, data=json_data, headers = headers)
    res     = req.json()
    print(res)
    return res
       

insert_data()
    