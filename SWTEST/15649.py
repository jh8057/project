from itertools import permutations

N, M = list(map(int,input().split()))

num = list(range(1,N+1))

result = permutations(num,M)

a = len(result)
for i in range(a):
    for j in range(M):
        print(result[i][j], end =' ')
    print("",end ="\n")
