
# f = open("text.txt",'w')
# f.write("Everything")
# f.close()

# f = open("text.txt",'w')
# l = ["Python\n","Java\n","PHP\n","Android\n"]
# f.writelines(l)
# f.close()

# f = open("text.txt",'a')
# f.write("Something..")
# f.close()


# f = open("text.txt",'r')
# data = f.read()
# print(data)
# f.close()

# f = open("text.txt",'r')
# while True:
#     data = f.readline()
#     print(data)
#     if not data : 
#         break
# f.close()


# f = open("text.txt",'r')
# data = f.readlines()
# print(data)
# f.close()


# f = open("text.txt",'r')
# data = f.read()
# if not data:
#     print("file empty")
# f.close()


# f = open("text.txt",'r')
# while True:
#     data = f.readline()
#     if 'a' in data.lower() :
#         print(data)
#     if not data : 
#         break
# f.close()


# with open("text.txt",'r') as f:
#     f.seek(10)
#     print(f.tell())
#     data = f.read()
    
#     print(f.tell())
#     print(data) 


# with open("home.txt",'w+') as f:
#     f.write("hello python")
#     f.seek(0)
#     data = f.read()
#     print(data)

# with open("download.png",'rb') as f:
#     data = f.read()
#     print(data)

# import json

# d = {
#     "name":"dev",
#     "email":"ratnani@gmail.com",
#     "phone":"7485968574"
# }

# with open("data.json",'w') as f:
#     json.dump(d,f)


with open("text.txt",'r') as f:
    data = f.readlines()
    for i in data:
        if 'a' in i.lower():
            print(i)