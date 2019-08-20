depandences = [[]]*N

for e in edges:
    curNode = e[0]
    depandences[curNode].append(e[1])
    
queue = deque()

for i in range(len(depandences)):
    if len(depandences[i]) == 0:
        queue.append(i)
    

res = []    
while queue:
    queueSize = len(queue)
    for _ in range(size):
        node = queue.popleft()
        res.append(res)
        for i in range(len(depandences)):
            if node in depandences[i]:
                depandences[i].remove(node)
                if (len(depandences[i]) == 0):
                    queue.append(i)    
return res 