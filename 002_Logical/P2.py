# *
# **
# ***
# ****
# *****

# len=5
# stars = 1
# for i in range(1,len+1):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1


# len=5
# stars = len
# for i in range(1,len+1):
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1


# len=5
# stars = 1
# spaces = len-1
# for i in range(1,len+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=1
#     spaces-=1


# len=5
# stars = len
# spaces = 0
# for i in range(1,len+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars-=1
#     spaces+=1


# len=5
# stars = 1
# spaces = len-1
# for i in range(1,len+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end=" ")
#     print()
#     stars+=1
#     spaces-=1


# len=5
# stars = 1
# spaces = len-1
# for i in range(1,len+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     stars+=2
#     spaces-=1


# len=9
# mid = (len//2)+1
# stars = 1
# spaces = len-1
# for i in range(1,len+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         print("*",end="")
#     print()
#     if i<mid:
#         stars+=2
#         spaces-=1
#     else:
#         stars-=2
#         spaces+=1



# len=9
# mid = (len//2)+1
# stars = 1
# spaces = len-1
# for i in range(1,len+1):
#     for k in range(spaces):
#         print(" ",end="")
#     for j in range(stars):
#         if j==0 or j==stars-1:
#             print("*",end="")
#         else:
#             print(" ",end="")
#     print()
#     if i<mid:
#         stars+=2
#         spaces-=1
#     else:
#         stars-=2
#         spaces+=1