n=int(input())
r=0
for i in range(2):
    n=(n*10)+3
    while n!=0:
        k=n%10
        r=r*10+k
        n=n//10
    n=r*1
print(n)