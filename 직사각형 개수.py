import time
start_time = time.time()
import math
n=int(input())
op=[]

for b in range (0, ((n+1)//2)+1):
    op.append(math.comb(n-b,b))
  

print(sum(op)%10007)
end_time = time.time()
time3 = end_time - start_time
print(time3)