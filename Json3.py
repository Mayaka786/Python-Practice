import json
input='''[
    {"id:"001"
    "x":"2"
    "name":"Ian""
    },
    {"id="008",
    "x"="7",
    "name:"Vee"
    }
]'''
info=json.loads(input)
print('User count:',len(info))
for item in info:
    print('Name',item['name'])
    print('id',item['id']),
    print('Attributes',item['x'])