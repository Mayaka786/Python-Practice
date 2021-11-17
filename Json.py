import json
data='''{
    "name":"Ian"
    "phone":{
        "type:"Vivo", 
        "number":"+2 521985674"
        },
        "email":{
            "hide":"yes"
        }
    }'''
    info=json.loads(data)
    print('Name:',info["name"])
    print('Hide:',info["email"]["hide"])