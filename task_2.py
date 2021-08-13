import operator
class testdictionary(dict):
  
    
        def __init__(self):
            self = dict()
          
    
        def add(self, key, value):
            self[key] = value
            
def AnalzeString(stri):
    stri = stri.lower()
    ori = stri
    z= ""
    for i in range(len(stri)):
        
        for j in range(len(stri)):
            if stri[i].lower()==stri[j].lower() and i!=j:
                z = z+stri[i]

    
        
    Newobj = testdictionary()
    duplicate = set(z)

    duplicate = str(duplicate)
     
    
    
    duplicate = duplicate.replace("{","",5)
    duplicate = duplicate.replace("}","",5)
    duplicate = duplicate.replace("'","",len(duplicate))
    duplicate = duplicate.replace(",","",len(duplicate))
    duplicate = duplicate.replace(" ","",len(duplicate))

    for i in range(len(duplicate)):
        Newobj.add(duplicate[i],count(ori,duplicate[i]))
    Newobj = sorted(Newobj.items(), key=operator.itemgetter(1))
    
    New_dup = ""
    for i in range(len(Newobj)):
        New_dup = New_dup+ Newobj[len(duplicate)-i-1][0]
    
    duplicate = New_dup
    New_stri = ''.join(i for i in stri if i.isalnum())
    distinct = set(New_stri)
    
    distinct = str(distinct)
    distinct = distinct.replace("{","",5)
    distinct = distinct.replace("}","",5)
    distinct = distinct.replace("'","",len(distinct))
    distinct = distinct.replace(",","",len(distinct))
    distinct = distinct.replace(" ","",len(distinct))
    
    New_distinct = distinct
    for i in range(len(distinct)):
        for j in range(len(duplicate)):
            if distinct[i]==duplicate[j]:
                New_distinct=New_distinct.replace(distinct[i],"")
                
    Dict = {"uniqueCharacters": New_distinct,
            "uniqueCharacterCount":len(New_distinct),
            "duplicateCharacters":duplicate,
            "duplicateCharacterCount":len(duplicate)
            }
    print(Dict)
def count(str,ch):
    x=0
    for i in range(len(str)):
        if(str[i] == ch):
            x = x+1
    return x        
        
stri = "It is not enough for code to work."
AnalzeString(stri)            