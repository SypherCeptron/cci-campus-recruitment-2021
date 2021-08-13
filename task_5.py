string = input()
stringx = string.lower()
difva = 86 
sum = 0
for i in range(len(stringx)):
    sum  = sum + (ord(stringx[i])-86)
   
print("value of " +string+ " is "+str(sum) )  