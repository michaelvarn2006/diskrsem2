def prima(mat):
    res = 0
    vis = [1]
    while len(vis) != len(mat):
        min_edge = 0
        ind = 0
        for i in vis:
            k = i - 1  
            for j in range(len(mat)):
                if (mat[k][j] < min_edge or min_edge == 0) and ((j + 1) not in vis) and (mat[k][j] != 0):
                    min_edge = mat[k][j]
                    ind = j + 1
        vis.append(ind)
        res += min_edge
    
    return res

n = int(input("Введите размер матрицы смежности: "))
print("Введите элементы матрицы смежности: ")
mat = [list(map(int, input().split())) for i in range(n)]
res = prima(mat)
print(res)
