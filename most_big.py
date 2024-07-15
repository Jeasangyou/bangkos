n = int(input())
Seq = list(map(int, input().split()))
#print(Seq)
#해당 요소까지의 최대 증가 수열의 합을 d라는 list에 저장할 것
d=[0]*len(Seq)
d[0]=Seq[0]
for i in range(1,len(Seq)):
    #sublist1은 이 부분 집합 중에 i번째 친구가 최소일 때의 경우를 따로 설정하려고 정의함
    sublist1 = Seq[:i+1]
    #sublist2는 ~i-1까지의 친구들 중 Seq값이 Seq[i]보다 작은 인덱스를 선별한 후(filtered_sublist로 정의)
    #그 인덱스에 해당하는 d 요소들 중 최대인 친구를 찾고자 만든 부분집합
    sublist2=Seq[:i]
    filtered_sublist = [x for x in sublist2 if x < Seq[i]]
    #print(filtered_sublist)
    
    
    sublist2 = d[:i]
    #sublist1 중에 sublist1[i]가 최소면 어차피 증가수열을 만들 수 없으므로 자기자신
    if min(sublist1)==sublist1[i]:
        d[i]=Seq[i]
    #아닌 경우 
    else:
        #filtered_sublist에서 i보다 작은 인덱스를 가지면서 Seq[i]보다 Seq 값도 작은 친구들을 선별했으니
        #그 요소들이 Seq 리스트에서 가지는 인덱스를 얻은 후 다시 d에 넣어주면 Seq[i]보다 앞에 존재하고 값도 작은 친구들까지의 최대 증가 수열 합을 얻음
        #그런 친구들이 여럿 있을 테니 그 중 최댓값과 Seq[i]를 더하면 i 인덱스까지의 최대 증가 수열 합
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
#d의 각 요소가 Seq 각 요소까지의 최대 증가 수열 합이므로 그 중 최대를 구하면 됨     
print(max(d))

