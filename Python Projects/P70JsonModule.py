import json

# this module is very essential from the point of view of web development

data = '{"var1":"vaibhav", "var2":7}'
parsed = json.loads(data)          #this is a dictionary

print(parsed)
print(parsed["var1"])

data2 = {
    "channel_name":"CodeWithHarry",
    "cars":["Tata", "Jaguar"]
}
jscomp = json.dumps(data2)    #now the code in data2 is compatible in javascript
print(jscomp)