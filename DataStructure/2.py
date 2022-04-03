#Baekjoon10845 큐

from collections import deque

queue = deque()
command = []

n = int(input())

for _ in range(n) :
    command.append(list(map(str, input().split())))

for i in command :
    
    if i[0] == "push" :
        queue.append(i[1])
        
    elif i[0] == "pop" :
        if queue :
            print(queue.popleft())
        else :
            print(-1)
            
    elif i[0] == "size" :
        print(len(queue))
        
    elif i[0] == "empty" :
        if queue :
            print(0)
        else :
            print(1)
            
    elif i[0] == "front" :
        if queue :
            print(queue[0])
        else :
            print(-1)
            
    elif i[0] == "back" :
        if queue :
            print(queue[-1])
        else : 
            print(-1)