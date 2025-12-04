student = {
    "name" : "Test",
    "email":"test@gmail.com",
    "age":25,
    "lang":["Gujarati","Hindi","English"],
    
}

# print(student)
# print(student['name'])  
# print(student.get('name1'))
# print(student['lang'][0])
# print(type(student))
# print(type(student['lang']))

# print(student.keys())
# print(student.values())
# print(student.items())
# print(student)

# student['age'] = 56

# student.update({"Gender":"Male"})
# student['lang'].insert(1,"Marathi")

# student.pop("name")
# student.popitem()
# del student['name']
# student.clear()
# del student


# for i in student.keys():
#     print(i)

# for i in student.values():
    # print(i)

# for i,j in student.items():
#     print(i,j)


    

# print(student)


# t = {
#     "name":"test",
#     25 : "abc",
#     True:25,
#     25.36:"xyz",
#     ("a","b") : "xyz"
# }
# print(t)


# students = {
#     "st1" : {
#         "name":"test",
#         "email":"test@gmail.com"
#     },
#     "st2" : {
#         "name":"tech",
#         "email":"tech@gmail.com"
#     },
#     "st3" : {
#         "name":"abc",
#         "email":"abc@gmail.com"
#     },
# }

# for i,j in students.items():
#     print(i)
#     for a,b in j.items():
#         print(a,b)



# t = dict.fromkeys("a","b")
# print(t)

# x = student.setdefault("name","abc")
# print(x)
# print(student)

a = {"python":30,"java":50}
b = {"India":"IN","Canada":"CN"}
a.update(b)
print(a)