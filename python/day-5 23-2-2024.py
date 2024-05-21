#1
s=input()
print(s[1::2]+s[::2])
#2
s=input()
c=0
ch=input()
for i in range(len(s)):
    if s[i]==ch:
        c=c+1
print(c)
#3
s=input()
c=0
ch=input()
for i in s:
    if i==ch:
        c=c+1
print(c)
#4
s=input()
ch=input()
c=0
for i in range(len(s)):
    if i%2==0:
        if s[i]==ch:
            c=c+1
print(c)
#5
s=input()
v="aeiouAEIOU"
c=0
for i in range(len(s)):
    if s[i] in v:
        c=c+1
if c==len(s):
    print("yes")
else:
    print("no")
#6
s=input()
v="aeiouAEIOU"
c=0
for i in s:
    if i not in v:
        print("no")
        c=1
        break
if c==0:
    print("yes")
#7
s=input()
v="aeiouAEIOU"
for i in s:
    if i not in v:
        print("no")
        break
else:
    print("yes")
#8
s=input()
v="0123456789"
c=0
for i in range(len(s)):
    if s[i] in v:
        c=c+1
if c==len(s):
    print("yes")
else:
    print("no")
#9
s=input()
v="0123456789"
for i in s:
    if i not in v:
        print("no")
        break
else:
    print("yes")
#10
s=input()
v="0123456789"
c=0
for i in s:
    if i not in v:
        print("no")
        c=1
        break
if c==0:
    print("yes")
#11
s=input()
if s.isdigit():
    print("yes")
else:
    print("no")
#12
s=input()
v="aeiouAEIOU"
c="qwrtypsdfghjklzxcvbnm"
b=0
a=0
for i in s:
    if i in v:
        b=b+1
    elif i in c:
        a=a+1
print(b,a)
#13
s=input()
v="aeiouAEIOU"
b=0
a=0
for i in s:
    if i.isalpha():
        if i in v:
            b=b+1
        else:
            a=a+1
print(b,a)
#14
s=list(input().split())
v="aeiouAEIOU"
b=0
a=0
for i in s:
    if i.isalpha():
        if i in v:
            b=b+1
        else:
            a=a+1
print(b,a,len(s))
#15
t=int(input())
for i in range(t):
    a,b=list(input().split())
    c=""
    for j in b:
        if j not in a:
            c=c+j
    print(c)
#16
t=int(input())
for i in range(t):
    a,b=input().split()
    b=int(b)
    c="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
    c=list(c)
    d=""
    for j in range(len(a)):
        if a[j] in c:
            d=d+c[c.index(a[j])+b]
    print(d)