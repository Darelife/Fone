import json
from urllib.request import urlopen

def jsonsave(url, file):
    with urlopen(url) as cn:
        data = json.load(cn)
    with open (file, "w") as f:
        json.dump(data, f, indent=2)

def jsondata(data, file):
    data1 = json.load(data)
    with open(file, "w") as f:
       json.dump(data1, f, indent = 2)
