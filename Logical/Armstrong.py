for i in range(100,1000):
    number = i
    temp = number
    sum = 0
    while number !=0:
        rem = number%10
        sum+=(rem*rem*rem)
        number = number//10

    if temp==sum:
        print(f"{temp} is Armstrong")
    else:
        pass
        # print(f"{temp} is Not armstrong")
    
