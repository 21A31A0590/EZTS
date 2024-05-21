#1
class classn:
    def __init__(self,n):
        self.n=n
    def isprime(self):
        c=0
        for j in range(2,int(self.n/2+1)):
            if self.n%j==0:
                c=c+1
                break
        if c>0:
            return('n is not prime')
        else:
            return("n is prime")
ob1=classn(22)
ob2=classn(13)
print(ob1.isprime())
print(ob2.isprime())
#2
class check:
    def __init__(self,s):
        self.s=s
    def pd(self):
        if self.s==self.s[::-1]:
            print("palindrom")
        else:
            print("not palindrom")
ob1=check("hello")
ob2=check("sis")
ob1.pd()
ob2.pd()
#3
class classn:
    def __init__(self,n):
        self.n=n
    def pd(self):
        r=0
        d=self.n
        while d!=0:
              k=d%10
              r=r*10+k
              d=d//10
        if self.n==r:
            return("palindrom")
        else:
            return("not palindrom")
    def isprime(self):
        c=0
        for j in range(2,int(self.n/2+1)):
            if self.n%j==0:
                c=c+1
                break
        if c>0:
            return('n is not prime')
        else:
            return("n is prime")
ob1=classn(22)
ob2=classn(13)
print(ob1.pd())
print(ob1.isprime())
print(ob2.pd())
print(ob2.isprime())
#4
class classn:
    def __init__(self,n):
        self.n=n
    def pd(self):
        r=str(self.n)
        if r==r[::-1]:
            return("palindrom")
        else:
            return("not palindrom")
    def isprime(self):
        c=0
        for j in range(2,int(self.n/2+1)):
            if self.n%j==0:
                c=c+1
                break
        if c>0:
            return('n is not prime')
        else:
            return("n is prime")
ob1=classn(22)
ob2=classn(13)
print(ob1.pd())
print(ob1.isprime())
print(ob2.pd())
print(ob2.isprime())
#5
class classn:
    def __init__(self,n,s):
        self.n=n
        self.s=s
    def pd(self):
        r=str(self.s)
        if r==r[::-1]:
            return("palindrom")
        else:
            return("not palindrom")
    def isprime(self):
        c=0
        for j in range(2,int(self.n/2+1)):
            if self.n%j==0:
                c=c+1
                break
        if c>0:
            return('n is not prime')
        else:
            return("n is prime")
ob1=classn(22,"hello")
ob2=classn(13,"sis")
print(ob1.isprime())
print(ob2.pd())
#6
class car:
    ms=0
    n=""
    def __init__(self):
        self.ms=200
        self.n="supername"
    def drive(self):
        print(self.ms)
class bike:
    def ride(self):
        print(self.ms)
c=car()
c.drive()
b=bike()
b.ms=100
b.ride()
#7
class car:
    ms=0
    n=""
    def __init__(self):
        self.ms=200
        self.n="supername"
    def drive(self):
        print(self.ms)
c=car()
c.drive()
c.ms=100
c.drive()
#8
class p:
    def __init__(self):
        print("parent class")
class cl(p):
    def __init__(self):
        super().__init__()
        print("child class")
c=cl()
class p:
    def __init__(self):
        print("parent class")
    def pd(self):
        print("2")
class cl(p):
    def __init__(self):
        super().__init__()
        print("child class")
        super().pd()
c=cl()
#9
class p:
    def __init__(self):
        print("parent class")
    def pd(self):
        print("2")
class cl(p):
    def __init__(self):
        super().__init__()
        print("child class")
c=cl()
c.pd()
#10
class dob:
    def __init__(self,d,m,y):
        self.d=d
        self.m=m
        self.y=y
    def dis1(self):
        l=["jan","feb","mar","apl","may","jun","jul","aug","sep","oct","nov","dec"]
        print(self.d)
        print(l[self.m-1])
        print(self.y)
class details(dob):
    def __init__(self,n,a,d,m,y):
        self.n=n
        self.a=a
        self.d=d
        self.m=m
        self.y=y
    def dis(self):
        print(self.n)
        print(self.a)
        print(self.d)
        print(self.m)
        print(self.y)
        super().__init__(self.d,self.m,self.y)
ob=details("abs",24,21,8,2001)
ob.dis()
ob.dis1()
#11
class p:
    def f1(self):
        print("parent class")
class c1(p):
    def f2(self):
        print("child class 1")
class c2(c1):
    def f3(self):
        print("child class 2")
c=c2()
c.f1()
c.f2()
c.f3()
#12
class vehile:
    def __init__(self,f):
        self.f=f
    def dis2(self):
        print(self.f)
class motor(vehile):
    def __init__(self,f,c):
        self.f=f
        self.c=c
    def dis1(self):
        print(self.f)
        print(self.c)
        super().__init__(self.f)
class car(motor):
    def __init__(self,f,c,m):
        self.f=f
        self.c=c
        self.m=m
    def dis(self):
        print(self.f)
        print(self.c)
        print(self.m)
        super().__init__(self.f,self.c)
ob=car("BMW","300cc","petrol")
ob.dis()
ob.dis1()
ob.dis2()
#13
class vehile:
    def __init__(self,f):
        self.f=f
    def dis2(self):
        print(self.f)
class motor(vehile):
    def __init__(self,f,c):
        self.f=f
        self.c=c
    def dis1(self):
        print(self.f)
        print(self.c)
class car(motor):
    def __init__(self,f,c,m):
        self.f=f
        self.c=c
        self.m=m
    def dis(self):
        print(self.f)
        print(self.c)
        print(self.m)
ob=car("BMW","300cc","petrol")
ob.dis()
ob.dis1()
ob.dis2()
#14
from abc import ABC
class shape(ABC):
    def area(self):
        pass
class rec(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def area(self):
        print(self.l*self.b)
class sq(shape):
    def __init__(self,s):
        self.s=s
    def area(self):
        print(self.s*self.s)
ob=sq(4)
ob.area()
ob1=rec(4,6)
ob1.area()