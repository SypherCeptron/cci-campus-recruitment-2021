import json
def analyzeJson(stri):
    #cleaing the string
    stri = stri.replace("{","",5)
    stri = stri.replace("}","",5)
    l = len(stri)
    stri = stri.replace("'","",l)
    #determing the string using colon
    for i in stri.split():
        value = i.find(':')
        if value>0:
            New_i = i.replace(":","")
            print(New_i)
      
    
    

with open('task_1.json') as x:
     data = json.load(x)

analyzeJson(str(data)+"")   