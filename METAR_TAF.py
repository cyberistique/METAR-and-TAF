import requests
import json
class ids:
    def __init__(self,name,metars,tafs):
        self.name = name
        self.metars = metars
        self.tafs = tafs

id_list = {}
prompt = ""
with open('ids.txt','r') as f:
    for i in f:
        a = i.replace("\n",'')
        b = a+"%2C"
        id_list[a.upper()] = ids(i,[],[])
        prompt += b
prompt = prompt[:-3]

l = requests.session()
o = requests.get(f"https://aviationweather.gov/api/data/metar?ids={prompt}&format=json&taf=true&hours=24")
o = o.json()

for i in range(0,len(o)):
    p = o[i]
    q = p['rawOb']
    r = q[:4]
    s = p['rawTaf']
    id_list[r].metars.append(q+'\n')
    id_list[r].tafs.append(s+'\n')

with open('metars.txt','w') as f:
    for i in id_list.keys():
        f.writelines(id_list[i].metars)
    print("metars done..")

with open('tafs.txt','w') as f:
    for i in id_list.keys():
        f.writelines(id_list[i].tafs)
    print("tafs done..")

