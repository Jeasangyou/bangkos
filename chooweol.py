Car_number = int(input())
Car_in= [input() for _ in range(1,Car_number+1)]
Car_out=[input() for _ in range(Car_number+1,Car_number*2+1)]
#print(Car_in)
#print(Car_out)
if Car_number==1:
    print(0)
else:
    Car_in_number=[0]*len(Car_in)
    for i in range(len(Car_in)):
        Car_in_number[i]=i
    Car_out_number=[0]*len(Car_in)
    for i in range(len(Car_in)):
        Car_out_number[i]=Car_in.index(Car_out[i])

    #print(Car_in_number)
    #print(Car_out_number)
    Choo=0
    for i in range(len(Car_in_number)-1):
        if Car_out_number[i]>min(Car_out_number[(i+1):]):
            Choo+=1


    print(Choo)

