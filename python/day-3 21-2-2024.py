#1
n=int(input())
a=list(map(int,input().split()))[:n]
for i in range(n):
    if a[i] in a[i+1:]:
        print(a[i])
#2
n=int(input())
a=list(map(int,input().split()))[:n]
a.sort()
for i in range(n):
    if a[i]==a[i+1]:
        print(a[i])
        break
#3
n=int(input())
a=list(map(int,input().split()))[:n]
for i in a:
    c=a.count(a[i])
    if c>1:
        print(a[i])
        break
#4
n=int(input())
a=list(map(int,input().split()))[:n]
c=0
if c==0:
    for i in range(n):
        for j in range(n):
            if a[i]!=a[j+1]:
                j=j+1
            else:
                print(a[i])
                c=c+1
                break
#5
n=int(input())
a=list(map(int,input().split()))[:n]
for i in a:
    if a.count(i)==1:
        print(i,end=' ')
#6
n=int(input())
a=list(map(int,input().split()))[:n]
b=[]
for i in a:
    if a[i]==a[i+1]:
        b=a[i]
print(b)
#7
t=int(input())
for i in range(t):
    n=int(input())
    t1=[]
    t2=[]
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1.append(j)
            else:
                t2.append(j)
    if len(t1)==len(t2):
        print(1)
    else:
        print(0)
#8
t=int(input())
for i in range(t):
    n=int(input())
    t1=0
    t2=0
    for j in range(1,n+1):
        if n%j==0:
            if j%2==0:
                t1=t1+1
            else:
                t2=t2+1
    if t1==t2:
        print(1)
    else:
        print(0)
#9
t=int(input())
for i in range(t):
    t1=0
    t2=0
    n=int(input())
    def fac(n,t1=0,t2=0):
        t1=0
        t2=0
        if n%n-1==0:
            n=n-1
            t1=t1+1
            if n%2==0:
                t1=t1+fac(n,t1,t2)
            else:
                t2=t2+fac(n,t1,t2)
    if t1==t2:
        print(1)
    else:
        print(0)
#10
t=int(input())
for i in range(t):
    n,x=map(int,input().split())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:n]
    c=0
    for j in range(n):
        if a[j]>=x:
            c=c+b[j]
    print(c)
#11
t=int(input())
for i in range(t):
    n=int(input())
    c=0
    for j in range(2,int(n/2+1)):
        if n%j==0:
            c=c+1
            break
    if c>0:
        print('n is not prime')
    else:
        print("n is prime")
#12
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:n]
    c=0
    for j in range(n):
        if a[j]>b[j]*2 or b[j]>a[j]*2:
            c=c+0
        else:
            c=c+1
    print(c)
#13
t=int(input())
for i in range(t):
    n=int(input())
    a=list(map(int,input().split()))[:n]
    b=list(map(int,input().split()))[:n]
    c=0
    for j in range(n):
        if a[j]<=b[j]*2 and b[j]<=a[j]*2:
            c=c+1
    print(c)
#14
n=int(input())
t=[]
for i in range(1,n):
    if n%i==0:
        t.append(i)
if n==sum(t):
    print("perfect even")
else:
    print("not a perfect even")
