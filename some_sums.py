N, A, B = map(int, input().split())
digitsum = 0
for num in range(1, N+1):
    a =  sum(map(int, list(str(num))))
    if A<= a <= B:
        digitsum += num
print(digitsum)