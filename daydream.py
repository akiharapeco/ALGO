import sys
sys.setrecursionlimit(20000)

def backtrack(index):
    global boolean
    global S
    if not S[index:]:
        return
    for i, substr in enumerate(('dream', 'dreamer', 'erase', 'eraser')):  
        if S[index:] == substr:
            boolean = True
            return
        elif len(S[index:]) < len(substr):
            continue        
        elif len(S[index:]) > len(substr) and S[index:index+len(substr)] == substr:
            backtrack(index+len(substr))

S = input()
boolean = False
backtrack(0)
print('YES') if boolean else print('NO')