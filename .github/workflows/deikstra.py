def deikstra(mat, st, end):
    n = len(mat)
    infinity = float('inf')
    dist = [infinity] * n 
    mas = [-1] * n 
    vis = [False] * n  
    dist[st] = 0
    for j in range(n):
        mindist = infinity
        minind = -1
        for i in range(n):
            if not vis[i] and dist[i] < mindist:
                mindist = dist[i]
                minind = i
        if minind == -1:
            break
        vis[minind] = True
        for sos in range(n):
            if mat[minind][sos] > 0: 
                ndist = dist[minind] + mat[minind][sos]
                if ndist < dist[sos]:
                    dist[sos] = ndist
                    mas[sos] = minind
    return dist, mas

def way(par, start, end):
    ways = []
    road = end
    while road != -1:
        ways.append(road)
        road = par[road]
    return ways if ways[-1] == start else []

n = int(input("Введите размер матрицы: "))
print("Введите матрицу смежности через пробел:")
mat = [list(map(int, input().split())) for i in range(n)]
start = int(input("Введите начало: ")) - 1
end = int(input("Введите конец: ")) - 1
dist, par = deikstra(mat, start, end)
path = way(par, start, end)
for i in range(len(path)):
    path[i] = path[i] + 1
if path:
    print("Путь:","-".join(map(str, path)))
    print("Стоимость:", dist[end])
else:
    print("Пути нет")
