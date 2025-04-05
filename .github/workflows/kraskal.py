def kraskal(mat):
    n = len(mat)
    def find(u):
        while par[u] != u:
            par[u] = par[par[u]]
            u = par[u]
        return u
    edges = []
    for i in range(n):
        for j in range(i + 1, n):
            if mat[i][j] > 0:
                edges.append((mat[i][j], i, j))
    edges.sort()
    par = list(range(n))
    res = 0
    added = 0
    for weight, u, v in edges:
        ru = find(u)
        rv = find(v)
        if ru != rv:
            par[rv] = ru
            res += weight
            added += 1
            if added == n - 1:
                break
    return res

n = int(input("Введите размер матрицы: "))
print("Введите элементы матрицы смежности")
mat = [list(map(int, input().split())) for i in range(n)]
res = kraskal(mat)
print(res)
