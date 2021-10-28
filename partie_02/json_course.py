import json


chemin = r"C:\Users\kenzi\Documents\FORMATION_PYTHON\partie_02\json.json"
with open(chemin,"w") as f:
    json.dump("bbbb",f) #erase and write inside json file

with open(chemin,"w") as f:
    json.dump(list(range(10)),f,indent=4) #write a list of numbers with indent 4 char

with open(chemin,"r") as f:# read a json file
    contenu = json.load(f)
    print(contenu)

# add data to a json file
with open(chemin,"r") as f:
    data = json.load(f)
data.append(list(range(4))) 
with open(chemin,"w") as f:
    json.dump(data,f,indent=4) #add the new data
