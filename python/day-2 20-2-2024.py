#1
def fun(x):
    x[3]=19
l=[1,2,3,4,5]
fun(l)
print(l)
#2
t=int(input())
for i in range(t):
    n=int(input())
    def sugcan(n):
        c=n*50
        c=(c/100)*30
        print(int(c))
    sugcan(n)
#3
t=int(input())
def sugcan(t):
    if t>0:
        n=int(input())
        print(int((n*50)-(n*50*0.7)))
        sugcan(t-1)
    else:
        return
sugcan(t)
#4
x,y=map(int,input().split())
def mov(x,y):
    print(x-(y//2))
mov(x,y)  
#5
t=int(input())
for i in range(t):
    n=int(input())
    def four(n,o=0):
        if n>0:
            if n%10==4:
                o=o+1
            four(n//10,o)
        else:
            print(o)
    four(n)
#6
t=int(input())
for i in range(t):
    n=int(input())
    def comp(n,f=1):
        if n>0:
           f=f*n
           comp(n-1,f)
        else:
            print(f)
    comp(n) 
#7
n=int(input())
f=1
for i in range(n):
    f=f*n
    n=n-1
print(f)
#8
n=int(input())
f=1
while n>0:
    f=f*n
    n=n-1
print(f)
#9
n=int(input())
def rev(n):
    r=0
    n=(n*10)+3
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
    return(r)
def rev2(n):
    for i in range(2):
        n=rev(n)
    print(n)
rev2(n)
#10
n=int(input())
def rev(n):
    r=0
    n=(n*10)+3
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
    return(r)
for i in range(2):
    n=rev(n)
print(n)
#11
n=int(input())
for i in range(2):
    n=(n*10)+3
    r=0
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
    n=r
print(n)