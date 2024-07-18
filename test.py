#자료구조는 최고야 문제 진짜로 푼 파일
import sys

m, n = map(int, sys.stdin.readline().rstrip().split())

for i in range(2*n):
    BookNo = list(map(int, sys.stdin.readline().rstrip().split()))
    #print(BookNo)
    if BookNo!=sorted(BookNo, reverse=True):
        print("No")
        sys.exit()

print("Yes")

