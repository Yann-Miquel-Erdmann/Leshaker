from math import sqrt
from queue import Queue
reach = int(input())
s = tuple(map(int, input().split()))
a = tuple(map(int, input().split()))
N = int(input())



prises = set([tuple(map(int, input().split())) for _ in range(N)]+[a])

vus = set()

prec = {
    s: None
}

todo = Queue(N)
todo_set = set()

todo.put(s)
todo_set.add(s)


while not todo.empty():
    elem = todo.get()
    if elem in vus:
        continue
    

    for p in prises:
        if p not in todo_set and p not in vus:
            
            if (elem[0]-p[0])**2 + (elem[1]-p[1])**2 <= reach**2:

                prec[p] = elem
                todo.put(p)
                todo_set.add(p)

                if p == a:
                    e = p
                    lst = [e]
                    while prec[e] != None:
                        lst.append(prec[e])
                        e = prec[e]

                    for e in lst[::-1]:
                        print(f"{e[0]} {e[1]}")

                    exit()
    
    vus.add(elem)
    todo_set.remove(elem)

print(-1)