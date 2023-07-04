import json
input='''
[
{
"id":"001",
"x":"2",
"name":"Chuck"
},
{
"id":"009",
"x":"7",
"name":"Chuck"
}
]'''
info=json.loads(input)
print('count',len(info))

for item in info:
    print("name",item['name'])