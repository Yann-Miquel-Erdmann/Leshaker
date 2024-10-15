lst = [(input().split(" ")) for _ in range(int(input()))]


m = max(lst, key=lambda x: int(x[1]))
take = []
for elem in lst:
    if elem[1] == m[1] :
        take.append(elem)

lst = take.copy()


m = max(lst, key=(lambda x: int(x[2])))
take = []
for elem in lst:
    if elem[2] == m[2]:
        take.append(elem)

lst = take.copy()

m = max(lst, key=(lambda x: int(x[3])))
take = []
for elem in lst:
    if elem[3] == m[3]:
        take.append(elem)

print(take[0][0])
