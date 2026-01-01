import re

# st = "Sun rises in in east"

# k = re.match("S",st)
# k = re.search("in",st)
# k = re.findall("in",st)
# k = re.finditer("in",st)
# k = re.sub("s","T",st)
# k = re.split(" ",st)
# print(k)

# st = "tocps tech"
# k = re.match('t.c',st)
# k = re.search('t.c',st)
# k = re.findall('t.c',st)
# k = re.finditer('t.c',st)
# print(next(k))
# print(next(k))


# st = "toops tech"
# k = re.search("^tech",st)
# k = re.search("ch$",st)
# k = re.search("to*p",st)
# k = re.search("to+p",st)
# k = re.search("to?p",st)
# print(k)



# st = "topss"
# k = re.search("^[a-z0-9]{5,10}$",st)
# print(k)

# st = re.findall(r"\Babc\B","dfdfabcfddfd dsdabc abcdsd")
# print(st)

# st = re.findall("[a-z0-9]*","hel2lo tops hello python 12212")
# print(st)

#alphabates only
# username = input("enter username :")
# k = re.match("^[a-zA-Z]+$",username)
# if k is None:
#     print("Invalid format")
# else:
#     print(username)

#Number only
# phone = input("enter phone :")
# k = re.match("^[0-9]{10}$",phone)
# if k is None:
#     print("Invalid format")
# else:
#     print(phone)


#email : abc@gmail.com
# email = input("enter email :")
# k = re.match("^[a-zA-Z0-9_-]+@[a-zA-Z]+\\.[a-zA-Z]{2,4}$",email)
# if k is None:
#     print("Invalid format")
# else:
#     print(email)



# data formate : dd-mm-yyyy
date = input("enter Date :")
# k = re.match("\\d{2}-\\d{2}-\\d{4}",date)
k = re.match(r"\d{2}-(0[0-9]|1[0-2])-\d{4}", date)

if k is None:
    print("Invalid format")
else:
    print(date)
