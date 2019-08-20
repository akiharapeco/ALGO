def dfs(res, depth, path, num, K):
    if depth == K:
        res.add(''.join(path))
        return
    for i in range(len(num)):
        if i == len(num) - 1:
            dfs(res, depth + 1, path + [num[i]], num[:i], K)
        else:
            dfs(res, depth + 1, path + [num[i]], num[:i] + num[i+1:], K)

N = int(input())
K = int(input())
num = []
for i in range(N):
    num.append(input())
res = set([])
dfs(res, 0, [], num, K)
print(len(res))