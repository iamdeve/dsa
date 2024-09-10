import queue
q = queue.Queue()

q.put(14)
q.put(28)
q.put(11)
q.put(7)
q.put(9)


n = q.qsize()

for i in range(n):
    x = q.get()
    for j in range(n - 1):
        y = q.get()
        if x > y:
            q.put(y)
        else:
            q.put(x)
            x = y
    q.put(x)

while q.empty() == False:
    print(q.queue[0], end=" ")
    q.get()