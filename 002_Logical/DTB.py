# number = 155
# result = ""
# while number !=0:
#     rem = number%2
#     result = str(rem)+result
#     number = number//2
# print(result)
    


number = 1356
result = 0 
mul = 1
while number !=0:
    rem = number%2
    result = rem*mul+result 
    number = number//2
    mul*=10 

print(result)




