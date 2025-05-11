n = int(input("Введите размер матрицы "))
print("Введите матрицу смежности через пробел")
mat = [list(map(int, input().split())) for i in range(n)]
spis = list(range(n))  
c = 0  
while spis:
    st = spis[0]
    queue = [st]  
    vis = [st]  
    while queue:
        k = queue.pop(0)  
        for i in range(n):  
            if  i in spis and i not in vis and mat[k][i] == 1:
                queue.append(i)
                vis.append(i)
    for v in vis:
        spis.remove(v)
    c += 1  
print(c)
