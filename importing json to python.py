import json
data= '''{
    "name": "Ian",
    "phone":{
        "type:Vivo",
        "numeber":"071245987"
    },
    "email":{
        "hide":"yes"
    }
}

info=json.loads(data)
print('Name:',info["name"])
print('Hide:',info["email"]["Hide"])