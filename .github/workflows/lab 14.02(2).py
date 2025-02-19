n = int(input("Введите размер матрицы "))
print("Введите матрицу смежности через пробел")
mat = [list(map(int, input().split())) for i in range(n)]
mas = [n] * n
mas[0] = 1
c = 2
for i in range(1, n):
    flag = False
    for j in range(i):
        if mat[i][j] == 1:
            if  mas[i] != mas[j] and mas[i] != n and mas[j] != n:
                r = min(i, j) 
                s = max(i, j)
                for r in range(len(mas)):
                    if mas[r] == s:
                        mas[r] = r
                flag = True
            else:
                mas[i] = mas[j]
                flag = True
    if not flag:
        mas[i] = c
        c += 1
print(len(set(mas)))
