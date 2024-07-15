#indentation주의
length=int(input())
if length==1:
    print(10)
else:
    d = [i for i in range(1, 11)]
    print(d)
    if length==2:
        print(sum(d))
    elif length>=3:
        for _ in range(length-2):
            new_d=[]
            
            for i in range(len(d)):
                current_sum=sum(d[:i+1])
                new_d.append(current_sum) 
            d=new_d
                      
        print(sum(d)%10007)
