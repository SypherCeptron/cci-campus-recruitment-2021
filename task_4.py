array_one = [1,5,8,9,10]
array_two = [5, 8, 9, 10, 12, 20, 40, 60, 70]
input_number = 10
x = array_one
y = array_two
w=0
z=0

for i in range(len(x)):
    if x[i]==input_number:w=1
   
        

for i in range(len(y)):
     if y[i] ==input_number:z=1
if w==0 and z==0:print("number "+str(input_number)+" is not found in both arrays")   
if w==0 and z==1:print("number "+str(input_number)+" is found in second arrays") 
if w==1 and z==0:print("number "+str(input_number)+" is found in first arrays") 
if w==1 and z==1:print("number "+str(input_number)+" is found in both arrays")   