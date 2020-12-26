from itertools import permutations

#map은 리스트의 요소를 지정된 함수로 처리해주는 함수
#map(함수,리스트)
#list(map(함수,리스트))

#'\n'.join 은 리스트를 '특정 구분자'를 포함해 문자열(str)로 변환 함수

#split("/")는 문자열(String)을 '특정 구분자'를 기준으로 리스트로 변환 함수

N, M = map(int, input().split())
A = map(str, range(1, N+1))

print('\n'.join(list(map(' '.join,permutations(A, M)))))

#print(list(map(' '.join,permutations(A, M))))