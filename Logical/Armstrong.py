number = 161
temp = number
sum = 0
while number !=0:
    rem = number%10
    sum+=(rem*rem*rem)
    number = number//10

if temp==sum:
    print("Armstrong")
else:
    print("Not armstrong")
    