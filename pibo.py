n=int(input())
if n==1:
    print(1)
elif n==2:
    print(1)
else:
    d = [0 for _ in range(n+1)]
    d[0]=0
    d[1]=1
    for i in range(2,n+1):
        d[i]=d[i-2]+d[i-1]
    print(d[n])