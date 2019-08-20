amounts = []

for coin in (500, 100, 50):
    amounts.append([i * coin for i in range(int(input())+1)])

res = [[int(input())]]

for i in range(len(amounts)):
    buffer = []
    for remainder in res[-1]:
        for amount in amounts[i]:
            if remainder - amount >= 0:
                buffer.append(remainder - amount)
    res.append(buffer)

print(len(list(filter(lambda x: x == 0, res[-1]))))