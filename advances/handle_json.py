import json
import urllib.request

res = urllib.request.urlopen("https://api.github.com/users/tienduy-nguyen/repos")
data = json.load(res)

# write file
# json.dumps() method can convert a Python object into a JSON string.
fName = "data.txt"
jsonFile = "data.json"
try:
    with open(fName, "w") as f:
        json.dump(data, f)
    with open(jsonFile, "w") as f:
        json.dump(data, f)
    print("Done!")
except IOError:
    print("Could not read file: ", fName)


# Data to be written
da = [
    {"id": "04", "number": "2.565686232", "name": "sunil", "department": "HR"},
    {"profile": {"name": "dhfqsdf", "email": "dfqsdfsdqf"}},
]
dictionary = {"id": "04", "number": "2.565686232", "name": "sunil", "department": "HR"}

# Serializing json
json_object = json.dumps(
    dictionary,
    indent=0,
)
print(json_object)
print("sdfdsf", "dfqsdf", json_object)


# Ecoding JSON Data
mydata = {"name": "John", "age": "10"}
jsonStr = json.dumps(mydata)
print(jsonStr)