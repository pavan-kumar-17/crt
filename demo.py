#Exanple for numeric type
# num=10
# print("num = ",num)
# print(type(num))
num=1.7
print(f"num={num}")
print(type(num))
num=10+15
print("num = ",num)
print(type(num))
# sequemce type - string ,list,tuple,range
Lang=['java', 'python', 'C','C++']
print(Lang)
print(type(Lang))
Lang={'java', 'python', 'C','C++'}
print(Lang)
print(type(Lang))
Lang=('java', 'python', 'C','C++')
print(Lang)
print(type(Lang))
# string
Str1='Good Afternoon'
print(Str1)
print(type(Str1))
Str2=" I'm Learning Python "
print(Str2)
print(type(Str2))
Str3='''HIi
budda Good afternoon,evereyone we started with data type
'''
print(Str3)
print(type(Str3))
# dictionary 
Lang={101:"python",102:"Java"}
print(Lang)
print(type(Lang))
# boolean
a=True
print(a)
print(type(a))
print(True+False)
# range
# range1=range(1,20)
# print(range1)
# print(type(range1))
# for i in range1:
#     print(i)
# step size
range1=range(1,20)
print(range1)
print(type(range1))
for i in range1:
    print(i)

def greet():
    print("Hello, welcome to the demo!")
greet()
greet()
greet()
greet()



def add(a,b):
    print(f"Addition of {a} and {b} is {a+b}")
add(5,3)
add(10,20)


def add(a,b):
    return a+b
print(add(5,3))
print(add(10,20))


