#1
s=input()
s=set(s)
n="qwertyuiopasdfghjklzxcvbnm"
n=set(n)
if s.intersection(n)==n:
    print("panagram")
else:
    print("not panagram")
#2
s=input()
s=set(s)
if len(s)==27:
    print("panagram")
else:
    print("not panagram")
#2
s=input()
n="qwertyuiopasdfghjklzxcvbnm"
n=set(n)
d={}
v=0 
c=0
for i in s:
    k=i
    v=v+1
    d[k]=v
for i in s:
    if i in n and s.count(i)==1:
        c=c+1
if c==26:
    print("panagram")
else:
    print("not panagram")
#3
t=int(input())
for i in range(t):
    k=0
    d={}
    s=input()
    for j in s:
        d[k+1]=j
    for j in s:
        if s.count(j)>1:
            print(j)
            k=1
            break
    if k!=1:
        print(".")
#4
n=int(input())
d={}
for i in range(n):
    k=input()
    v=input()
    d[k]=v
k=0
while(1):
    q=input()
    if q in d:
        print(f"{q}={d[q]}")
    else:
        print("not found")
#5
n=int(input())
d={}
for i in range(n):
    k=input()
    v=input()
    d[k]=v
while(1):
    q=input()
    if q in d:
        print(q+"="+d.get(q))
    else:
        print("not found")
#6
n=int(input())
d={}
for i in range(n):
    r=input()
    if r in d:
        d[r]+=1
    else:
        d[r]=1
m=max(d.values())
l=[]
for i in d:
    if d.get(i)==m:
        l.append(i)
print(max(l),m)
#7
t=int(input())
for i in range(t):
    n,r=map(int,input().split())
    d={}
    for j in range(r):
        i,c=map(int,input().split())
        if i in d:
            d[i].append(c)
        else:
            d[i]=[c]
    c=0
    for j in d:
        if len(d[j])>n or len(set(d[j]))!=len(d[j]):
            print(f"scenerio #(j+1):impossible")
            c=c+1
            break
    if c==0:
            print(f"scenerio #(j+1):possible")
#8
n=int(input())
d={}
for i in range(n):
    c1,c2=input().split()
    if c1 in d:
        d[c1].append(c2)
    else:
        d[c1]=[c2]
t=input()
if t in d:
    print(*d[t])
else:
    print("none")