T = int(input())
for i in range(T):
    S = input()
    j = 0
    count = 0
    while S[j:]:
        if len(S[j:]) < 5:
            break
        if S[j:j+5] in ['tokyo', 'kyoto']:
            j+=5
            count+=1
            continue
        j+=1
    print(count)