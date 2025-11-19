number = 1556
result = "" 

l = [0,1,2,3,4,5,6,7,8,9,'A','B','C','D','E','F']

while number !=0:
    rem = number%16
    result=str(l[rem])+result
    number = number//16
   

print(result)




