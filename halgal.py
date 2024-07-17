n=int(input())
Hal=[]
fruit=[]
number=[]
for _ in range(n):
    raw_input=input().split()
    Hal.append(raw_input)
Final_Hal=[]
for j in range(len(Hal)):
    Final_Hal+=Hal[j]
for i in range(len(Final_Hal)):
    if Final_Hal.index(Final_Hal[i])%2==0:
        fruit.append(Final_Hal[i])
    else:
        number.append(Final_Hal[i])

Hal_dict={}
Hal_dict[fruit[0]]=int(number[0])
for k in range(1, len(fruit)):
    if fruit[k] in Hal_dict:
        Hal_dict[fruit[k]]+= int(number[k])
    else:
        Hal_dict[fruit[k]]=int(number[k])
#print(Final_Hal)
#print(fruit)
#print(number)
#print(Hal_dict)
if any(value == 5 for value in Hal_dict.values()):
    print("YES")
else:
    print("NO")

