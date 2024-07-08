alphabet_string=input()
#알파벳을 1부터 26의 숫자에 대응
to_number={chr(i + 96): i for i in range(1, len(alphabet_string)+1)}
def assign_numbers_to_string(s):
    return [to_number[char] for char in s]
#alphabet_string의 문자를 숫자로 대응시켜 Hansoo_list의 0~ index에 저장
Hansoo_list=assign_numbers_to_string(alphabet_string)
print(Hansoo_list)
#숫자-->영어로 돌리기
to_alphabet = {i: chr(i + 64) for i in range(1, 27)}
def convert_numbers_to_string(lst):
    return ''.join(to_alphabet[num] for num in lst)
Former_Hansoo=[]
Latter_Hansoo=[]
#Hansoo_list내 각 숫자의 빈도를 세는 counter
from collections import Counter
Frequency_Hansoo=Counter(Hansoo_list)
#총 짝수 개 문자열이면 모든 문자가 짝수 개 존재해야 함
if len(alphabet_string)%2==0:
    if all(count % 2 == 0 for count in Frequency_Hansoo.values()):
        for i in range(len(alphabet_string)//2):
            Former_Hansoo.append(Hansoo_list[i])
            Half1_pal=sorted(Former_Hansoo)
            Half2_pal=sorted(Former_Hansoo, reverse=True)
            Even_pal_number=Half1_pal+Half2_pal
            Even_pal=convert_numbers_to_string(Even_pal_number)
            print(Even_pal)
    else:
        print("I'm Sorry Hansoo")
else:
    print("아직")