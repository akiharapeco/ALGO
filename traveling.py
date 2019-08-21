N = int(input())
timestamp = []
for i in range(N):
    timestamp.append(tuple(map(int, input().split())))

boolean_last = True

for count, x, y in timestamp:
    if abs(x) + abs(y) not in range(count, -1, -2):
        boolean_last &= False
        break

print("Yes") if boolean_last else print("No")