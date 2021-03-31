import json

data = '''{
    "name" : "Chuck",
    "phone" : {
        "type" : "intl",
        "number" : "+1 734 303 4456"
    },
    "email" : {
        "hide" : "yes"
    }
}'''

info = json.loads(data)  # loads => load String, 형태 확인후 알아서 파싱 => dict
# print(type(info)) # dict
print('Name:', info['name'])  # Chuck
print('Hide:', info['email']['hide'])  # yes

# json 형식에서는 큰따옴표 사용!
input = '''[
    {
        "id":"001",
        "x":"2",
        "name":"chuck"
    },
    {
        "id":"009",
        "x":"7",
        "name":"chuck"
    }
]'''

info = json.loads(input)
# print(type(info)) # list
print(info)
print('User count:', len(info))
for item in info:
    print('Name:', item['name'])
    print('Id:', item['id'])
    print('Attribute x:', item['x'])
