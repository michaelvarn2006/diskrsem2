def ford(mat, start, end):
    n = len(mat)
    infinity = float('inf')
    dist = [infinity] * n  
    par = [-1] * n 
    dist[start] = 0
    for i in range(n - 1):
        for u in range(n):
            for v in range(n):
                if mat[u][v] != 0: 
                    ndist = dist[u] + mat[u][v]
                    if dist[u] != infinity and ndist < dist[v]:
                        dist[v] = ndist
                        par[v] = u
    for u in range(n):
        for v in range(n):
            if mat[u][v] != 0 and dist[u] + mat[u][v] < dist[v]:
                print("Обнаружен отрицательный цикл")
                return None, None
    return dist, par

def way(par, st, end):
    ways = []
    road = end
    while road != -1:
        ways.append(road)
        road = par[road]
    return ways if ways[-1] == st else []

n = int(input("Введите размер матрицы: "))
print("Введите матрицу смежности через пробел:")
mat = [list(map(int, input().split())) for i in range(n)]
st = int(input("Введите начальную вершину: ")) - 1
end = int(input("Введите конечную вершину: ")) - 1

dist, par = ford(mat, st, end)

if dist is None:
    print("Есть отрицательный цикл")
else:
    path = way(par, st, end)
    if path:
        print("Путь:","-".join(map(str, path)))
        print("Стоимость:", dist[end])
    else:
        print("Пути нет")
