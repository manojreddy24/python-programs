print("hello")
# it is comment in python
name=input("who are you?")
print("iam",name)
# convert elevator floor
inp=input("elevetor floor?")
usf=int(inp)+1
print("floor num",usf)
#important fundamentals
print('manoj "laptop"')
print('manoj\'s "laptop"')# will alow this
print("\n for new line")
print(r'c:\docs\new')# r means raw string
len(name)
cla=[1,'second','third']
details=[24,'manoj',25]
cla[1]
concat=[cla,details]
details.insert(1,'iam')
details.pop(2)
del details[1]
details.extend([2,5,4])
a=5
id(a) #id gives addresss
b=a
id(b)# address of a and b is same
a=4
id(a)# address of a changes but bis remains past one#
#data types
type(a)
i=2
j=3
c=complex(i,j)# result as a+bj
m=4
n=7
m<n
int(True)#1
int(False)#0
range(10)#range(0,10)
list(range(2,10,2))
#dic keys
d={'manoj':'note3','vishnu':'note4','raj':'none'}
d.keys()
d.values()
d['manoj']# or d.get['manoj']
bin(25)# binary num of 25
0b0101#5
oct(25)
hex(25)
0xf
# user input
x=int(input("enter first number"))
y=int(input("enter second number"))
z=x+y
z
#
ch=input('enter a char')[0]
ch
