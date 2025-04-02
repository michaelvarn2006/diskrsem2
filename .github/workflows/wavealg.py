from collections import deque
def wavealg(mat):
    n = len(mat)
    st = None
    end = None
    for i in range(n):
        for j in range(n):
            if mat[i][j] == -2:
                st = (i, j)
            elif mat[i][j] == -3:
                end = (i, j)
    queue = deque([st])
    mat[st[0]][st[1]] = 1 
    while queue:
        x, y = queue.popleft()
        if (x, y) == end:
            return mat[x][y] - 1
        if x - 1 >= 0 and (mat[x-1][y] == 0 or mat[x-1][y] == -3):
            newv = mat[x][y] + 1
            mat[x-1][y] = newv
            queue.append((x-1, y))
            if (x-1, y) == end:
                return newv - 1
        if x + 1 < n and (mat[x+1][y] == 0 or mat[x+1][y] == -3):
            newv = mat[x][y] + 1
            mat[x+1][y] = newv
            queue.append((x+1, y))
            if (x+1, y) == end:
                return newv - 1
        if y - 1 >= 0 and (mat[x][y-1] == 0 or mat[x][y-1] == -3):
            newv = mat[x][y] + 1
            mat[x][y-1] = newv
            queue.append((x, y-1))
            if (x, y-1) == end:
                return newv - 1
        if y + 1 < n and (mat[x][y+1] == 0 or mat[x][y+1] == -3):
            newv = mat[x][y] + 1
            mat[x][y+1] = newv
            queue.append((x, y+1))
            if (x, y+1) == end:
                return newv - 1
    return None

n = int(input("Введите размер матрицы: "))
print("Введите матрицу, оставляя на месте камней - (-1), стартовую позицию - (-2), конечную позицию - (-3), а в остальных местах - 0")
mat = [list(map(int, input().split())) for _ in range(n)]

dist = wavealg(mat)

if dist is not None:
    print(dist)
else:
    print("Нет пути")
