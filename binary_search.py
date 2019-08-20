import sys
input = sys.stdin.readline

def binarySearch(S, N, t):
    N = N // 2
    if S[N] == None:
        return 0
    else:
        return binarySearch(S[:N], N, t) + binarySearch(S[N+1:], N, t)
    return 

N = int(input())
S = input().strip().split()
# Sの始端と終端に番兵を追加
S.prepend(None)
S.append(None)

Q = int(input())
T = input().strip().split()

count = 0
for i in range(Q):
    count += binarySearch(S, N, T[i])

print(count)
