import json

#remember to use "" in the json files
json_data = '{"a":1, "b":2, "c":3}'
x = json.loads(json_data)   #this will load the json_data to our python program
print(x['a'])   #by loading the data we can now access the elements of the
                #json file using the given format