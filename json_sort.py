import json

with open('./static/events.json') as json_file:
    eve_data = json.load(json_file) 

temp =[]
for i in eve_data:
    temp.append(i['name'])

temp.sort()
print(temp)

dataj = {}

count=0
lists = []

f = open("sorted.json", "a")

f.write("[ \n")

for i in temp:
    count=0
    for j in eve_data:
        if j['name'] == i:
            f.write(json.dumps(j)+",\n")
            lists.append(j)
        else:
            count +=1
f.write("\n]")

f.close()
print("\n\n\n",lists)