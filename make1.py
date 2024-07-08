#0번 index 무시할 수 있도록 비워놓기
n=int(input())
if n==1:
     print(0)
elif n==2:
     print(1)
elif n==3:
     print(1)
else:
    d=[0 for _ in range(n+2)]
    d[0]=0
    d[1]=0
    d[2]=1
    d[3]=1
    for i in range(4,n+1):
            if i%3==0 and i%2!=0:
                d[i]=min(d[i-1]+1,d[int(i/3)]+1)
            elif i%3!=0 and i%2==0:
                d[i]=min(d[i-1]+1,d[int(i/2)]+1)
            elif i%3==0 and i%2==0:
                d[i]=min(d[i-1]+1,d[int(i/3)]+1,d[int(i/2)]+1)
            elif (i%3!=0) and (i%2!=0):
                d[i]=d[i-1]+1
    print(d[n])