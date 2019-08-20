N = int(input())
A = map(int, input().split())
print(min(map(lambda num: len(bin(num ^ (num - 1)))-3, A)))