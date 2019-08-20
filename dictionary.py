import sys
input = sys.stdin.readline

M = 
L = 14

H = [[None] * L] * M

def getChar(char):
    if char == "A":
        return 1
    elif char == "C":
        return 2
    elif char == "G":
        return 3
    elif char == "T":
        return 4

def getKey(string):
    sum = 0
    p = 1
    for i in range(len(string)):
        sum += p * getChar(string[i])
        p *= 5
    return sum

def h1(key):
    pass

def h2(key):
    pass

def find(value):
    pass

def insert(string):
    pass

string = [None] * L
com = [None] * 9                

for i in range(M):
    H[i][0] = None

N = int(input())

count = 0
for i in range(N):
    line = input().strip().split()
    if line[0] == "insert":
        insert(line[1])
    elif line[0] == "find":
        if find(line[1]):
            print("yes")
        else:
            print("no")

print(count)
