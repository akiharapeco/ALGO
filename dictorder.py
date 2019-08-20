A = input()
ans = []
for char in A:
    ans.append('a')

if ans[:-1]:
    print(''.join(ans[:-1]))
elif A[0] > 'a':
    print(ans[0])
else:
    print(-1)