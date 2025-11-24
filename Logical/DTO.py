
number = 106
result = 0 
mul = 1
while number !=0:
    rem = number%8
    result = rem*mul+result 
    number = number//8
    mul*=10 

print(result)




