change = max(0, 1000 - int(input()))

count = [0 for i in range(6)]

for i, coin in enumerate([500, 100, 50, 10, 5, 1]):
    while change >= coin:
        change -= coin
        count[i] += 1
print(sum(count))
            