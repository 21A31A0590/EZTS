#1
a,b=map(int,input().split())
if a>b:
    print(a)
else:
    print(b)
#2
a,b,c=map(int,input().split())
if(a>b and a>c):
    print(a)
elif (b>a and b>c):
    print(b)
else:
    print(c)
#3
a,b=map(int,input().split())
if a<b:
    print(a)
else:
    print(b)
#4
a,b,c=map(int,input().split())
if(a>b and b>c) or (c>b and b>a):
    print(b)
elif(a>c and c>b) or (b>c and c>a):
    print(c)
elif(c>a and a>b) or (b>a and a>c):
    print(a)
#5
a,b,c=map(int,input().split())
if (a > b and a>c) :
    a=0
elif b>c:
    b=0
else:
    c=0
if (a > b and a>c) :
    print(a)
elif b>c:
    print(b)
else:
    print(c)
#6
for i in range(1000):
    print("hello world")
#8
a,b=map(int,input().split())
if(a>b):
    print("a>b")
elif b>a:
    print("a<b")
else:
    print("a=b")
#9
a,b,c=map(int,input().split())
if(a+b>c and a+c>b and b+c>a):
    print("yes")
else:
    print("no")
#10
n,k=map(int,input().split())
while(k>n):
    k=k-n
print(k)
#11
n=int(input())
r=0
while n!=0:
    k=n%10
    r=r*10+k
    n=n//10
print(r)
#12
n=int(input())
e=n
if n<0:
    n=n*(-1)
r=0
while n!=0:
    k=n%10
    r=r*10+k
    n=n//10
if e>0:
    print(r)
else:
    print(r*(-1))
#13
n=int(input())
r=0
if n<0:
    n=n*(-1)
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
elif n>0:
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
    r=r*(-1)
else:
    print(n)
#14
w=int(input())
if w>2 and w%2==0:
    print("Yes")
else:
    print("No")
#15
t=int(input())
for i in range(t):
    x=int(input())
    if x>98:
        print("YES")
    else:
        print("NO")
#16
t=int(input())
while t>0:
    t=t-1
    x=int(input())
    if x>98:
        print("YES")
    else:
        print("NO")  
#17
t=int(input())
for i in range(t):
    x=int(input())
    print(100-x)
#18
t=int(input())
for i in range(t):
    x=int(input())
    x=(1200//100)*x
    print(x)
#19
t=int(input())
for i in range(t):
    a,b,c,d=map(int,input().split())
    a=a-c
    b=b-d
    if(b>a):
        print("first")
    elif a>b:
        print("second")
    else:
        print("any")
#20
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    if n>x:
        n=n-x
        x=0
        while(n>0):
            n=n-4
            x=x+1
        print(x)
    else:
        print("0")
#21
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    n=n-x
    
    if n>0 and n%4==0:
        print(n//4)
    elif n<=0:
        print("0")
    else:
        print((n//4)+1)
#22
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    n=n*x
    if n%4==0:
       print(n//4)
    else:
        print((n//4)+1)
#23
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    n=n*x
    x=0
    while n>0:
        n=n-4
        x=x+1
    print(x)