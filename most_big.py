n = int(input())
Seq = list(map(int, input().split()))
#print(Seq)
d=[0]*len(Seq)
d[0]=Seq[0]
for i in range(1,len(Seq)):
    sublist1 = Seq[:i+1]
    sublist2=Seq[:i]
    filtered_sublist = [x for x in sublist2 if x < Seq[i]]
    #print(filtered_sublist)
    
    
    sublist2 = d[:i]
    if min(sublist1)==sublist1[i]:
        d[i]=Seq[i]
    else:
        all_elements_from_d = []
        indices_dict = {elem: [] for elem in filtered_sublist}
        for index, value in enumerate(Seq):
            if value in indices_dict:
                indices_dict[value].append(index)
        for elem in filtered_sublist:
            indices = indices_dict[elem]
            elements_from_d = [d[idx] for idx in indices]
            all_elements_from_d.extend(elements_from_d)
        #print(all_elements_from_d)
        d[i]=Seq[i]+max(all_elements_from_d)
        
print(max(d))

