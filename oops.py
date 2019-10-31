# class and object
class comp:
    def config():
        print("it will be print")
## execution
c1=comp()# obj=class()
c1.config()#obj.method(function)
#-------------------------------------------------------------------------------

# passing arguments
class comp:
    def __int__(self,cpu,ram):
        self.cpu=cpu
        self.ram=ram
        def config(self):
          print("configis=",self.cpu,self.ram)
## execution
p1=comp("i5",8)
p2=comp("manoj",20)
p1.config()
p2.config()
      # or
      class Person:
...   def __init__(self, name, age):
...     self.name = name
...     self.age = age
p1=Person("i5",8)
p1.name()
p1.age()
#------------------------------------------------------------------------------

# types of variables
class car:
  wheels=4 # class variable
  def __init__(self):
    self.mail=10#   instance variable
    self.com="bmw"#    ,,
##execution
c1=car()
>>> c2=car()
>>> car.wheels=6
c1.mail=55
>>> print(c1.com,c1.mail,c1.wheels)
print(c2.com,c2.mail,c2.wheels)
#-------------------------------------------------------------------------------

# types of methods
class student:
    name="manoj"
    def __init__(self,m1,m2,m3,iam):
        self.m1=m1
        self.m2=m2
        self.m3=m3
        self.iam=iam
    def avg(self):
        return (self.m1+self.m2+self.m3)/3
    def getname(cls):
        return cls.name
    def info(self):
        print("i am ="+self.iam)

##execution
>>> s1=student(12,55,2,"maonoj")
>>> s1=student(12,55,255,"maonoj")
>>> s1.info()
i am =maonoj
>>> s1.avg()
107.33333333333333
>>> s1.getname()
'manoj'
#-------------------------------------------------------------------------------

#innerclass
class student:
  def __init__(self,name,rollno):
    self.name=name
    self.rollno=rollno
  def show(self):
    print("the details is  "+self.name,self.rollno)
class laptop:
  def __init__(self):
    self.brand="lenovo"
    self.ram=8
    self.model="ideapad"
  def show(self):
    print(self.brand,self.ram,self.model)
## execution
s1=student("manoj",63)
>>> s1.show()
the details ismanoj 63
>>> s2=laptop()
>>> s2.show()
lenovo 8 ideapad
#-------------------------------------------------------------------------------

# inheritance
class A:
    def feature1(self):
        print("feature1 is working")
    def feature2(self):
        print("feature2 is working")
class B:  # for multisingle class b(a)
    def feature3(self):
        print("feature3 is working")
    def feature4(self):
        print("feature4 is working")
    # -- multiple
class C(A,B): # for multi level class c(b)
    def feature5(self):
        print("feature5 is working")
# execution
 c1=C()
>>> c1.feature3()
feature3 is working
#-------------------------------------------------------------------------------

# constructor in inheritance
class A:
    def __init__(self):
        print("in a class")
    def feature1(self):
        print("feature1-A is working")
class B:
    def __init__(self):
        print("in b class")
        def feature1(self):
            print("feature1-B is working")
class C(A,B):
    def __init__(self):
        super().__init__()
        print("in c class")
## execution
c1=C()
in a class
in c class
>>> c1.feature1()
feature1-A is working
#-------------------------------------------------------------------------------

# duck typing
class details:
   def execute(self):
      print("running")
      print("execution")

class laptop:
   def execute(self):
      print("running")
      print("execution")
      print("completion")

class final:
   def code(self,ide):
## execution
ide=laptop()
>>> l1=final()
>>> l1.code(ide)
running
execution
completion
#------------------------------------------------------------------------------
# ex  2
class Duck:
    def fly(self):
        print("Duck flying")

class Airplane:
    def fly(self):
        print("Airplane flying")

class Whale:
    def swim(self):
        print("Whale swimming")

for animal in Duck(), Airplane(), Whale():
    animal.fly()
##execution
Duck flying
Airplane flying
#-------------------------------------------------------------------------------

# method overloading
class student:
    def sum(self,a=None,b=None,c=None):

        if a!=None and b!=None and c!=None:
            s=a+b+c
        elif a!=None and b!=None:
            s=a+b
        else:
            s=a
        return s
## execution
 s=student()
 s.sum(8)
8
#-------------------------------------------------------------------------------

# method overriding
class A:
    def feature1(self):
        print("feature1-A is working")
class B(A):
    def featurel(self):
         print("feature1-B is working")
## execution
m=B()
m.featurel()
feature1-B is working
#-------------------------------------------------------------------------------

# iterator
nums=[2,8,9,5]
it=iter(nums) #iteration
print(it.__next__())# next inbult function
print(next(it))

for i in nums:
    print(i)
## output
2
8
2
8
9
5
#-------------------------------------------------------------------------------

# iterator in class
class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):# in bult iteration method
        return self
    def __next__(self):# in bult next  method
        if self.num<=10:
            val=self.num
            self.num+=1

            return val
        else:
            raise StopIteration
## execution
>>> t=topten()
>>> for i in t:
	print(i)
1
2
3
4
5
6
7
8
9
10
#-------------------------------------------------------------------------------

# generator
# it is used to create a iterator with different approach
def topten():
   n=1
   while n<=10:
      sq=n*n
      yield sq
      n+=1
##execution
t=topten()
for i in t:
    print(i)
1
4
9
16
25
36
49
64
81
100
#-------------------------------------------------------------------------------

# exception handling
a=5
b=0
k=int(input("enter a number="))
print(k)
try:
   print("resource open")
   print(a/b)

except ZeroDivisionError as e:
   print("hey, you cannot divide a number by zero",e)
except Exception as e:
   print("something went wrong",e)
except ValueError as e:
   print("invalid input",e)
finally:
   print("resource closed")
## execution
enter a number=88
88
resource open
hey, you cannot divide a number by zero division by zero
resource closed
#-------------------------------------------------------------------------------

# multithreading
from time import sleep
from threading import *
class hello(Thread):
   def run(self):
      for i in range(5):
         print("hii")
         sleep(1)

class hii(Thread):
   def run(self):
      for i in range(5):
         print("hello")
         sleep(1)

t1=hello()
t2=hii()
t1.start()
sleep(0.2)
t2.start()
t1.join()
t2.join()
print("bye")
## output
hii
hello
hii
hello
hii
hello
hii
hello
hii
hello
#-------------------------------------------------------------------------------

# linear search
pos=-1

def search(list,n):
    i=0
    while i<len(list):
        if list[i]==n:
            globals()['pos']=i
            return True
        i=i+1
    return True

list=[5,7,9,10]
n=10
if search(list,n):
    print("milgaya",pos)
else:
    print("nahi")
##output
milgaya 3
#-------------------------------------------------------------------------------

# binary search
pos=-1

def search(list,n):
    l=0
    u=len(list)-1
    while l<=u:
        mid=(l+u) // 2
        if list[mid]==n:
            globals()['pos']=mid
            return True
        else:
            if list[mid]<n:
                l=mid+1
            else:
                u=mid-1
    return False

list=[1,3,6,7,8,99,555,1112]
n=555
if search(list,n):
    print("milgaya",pos)
else:
    print("nahi")
##output
milgaya 6
#-------------------------------------------------------------------------------

# bubblesort
def sort(nums):
   for i in range(len(nums)-1,0,-1):
      for j in range(i):
         if nums[j]>nums[j+1]:
            temp=nums[j]
            nums[j]=nums[j+1]
            nums[j+1]=temp
nums=[4,5,8,2,1,6]
sort(nums)
print(nums)
##output
[1, 2, 4, 5, 6, 8]
#-------------------------------------------------------------------------------

# selection sort
def sort(nums):
   for i in range(5):
      minpos=i
      for j in range(i,6):
         if nums[j]<nums[minpos]:
            minpos=j


      temp=nums[i]
      nums[i]=nums[minpos]
      nums[minpos]=temp
nums=[5,3,8,6,7,2]
sort(nums)
print(nums)
##output
[2,3,5,6,7,8]
#-------------------------------------------------------------------------------
