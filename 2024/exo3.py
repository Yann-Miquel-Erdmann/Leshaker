N, M = list(map(int, input().split()))

matrix = [input() for _ in range(N)]

def parcours(depart):
    visite = [[False for i in range(M)]for _ in range(N)]
    x,y = depart, 0
    count = 0
    while not visite[y][x]:
        visite[y][x] = True
        match matrix[y][x]:
            case ">":  
                if x+1<M :
                    x+=1
            case "<":  
                if x-1>=0 :
                    x-=1
            case "v":  
                if y + 1 == N:
                    return count+1
                if y+1<N :
                    y+=1
            case "^":  
                if y-1 >=0:
                    y-=1
        count +=1
    return None
        

temps  = [(parcours(i),i) for i in range(M)]
temps = [elem for elem in temps if elem[0] != None]
m = min(temps, key= lambda x: x[0])
for elem in temps:
    if elem[0] == m[0]:
        print(elem[1]+1, end=" ")