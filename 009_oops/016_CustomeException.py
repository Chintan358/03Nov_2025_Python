class AgeInvalidException(Exception):

    def __init__(self, msg):
        super().__init__(msg)

def checkage(age):
    if age>=18:
        print("elegeble")
    else:
        raise AgeInvalidException("Invalid age")

try :
    a = 10/0
    checkage(18)
except Exception as e:
    print(e)
print("hello python")