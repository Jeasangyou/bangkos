Candi = int(input())
Votes= [int(input()) for _ in range(Candi)]
#print(Votes)
Times=0
if len(Votes)==1:
    print(0)
elif Votes[0]>max(Votes[1:]):
    print(0)
elif Votes[0]==max(Votes[1:]):
    print(1)
else:
    while Votes[0] < max(Votes[1:]):
        Times += 1
        max_index = Votes.index(max(Votes[1:]))
        Votes[max_index] -= 1
        Votes[0] += 1
        #print("Revised Votes:", Votes)

        if Votes[0] > max(Votes[1:]):
            #print("Final Votes:", Votes)
            print(Times)
            break
        elif Votes[0] == max(Votes[1:]):
            Times += 1
            Votes[max_index] -= 1
            Votes[0] += 1
            #print("Final Votes:", Votes)
            print(Times)
            break


   
