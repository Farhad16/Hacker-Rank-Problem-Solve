a = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
leftDiagonal = 0
rightDiagonal = 0
for i in range(len(a)):
    for j in range(len(a[i])):
        if i == j:
            leftDiagonal += a[i][j]
        if i == (len(a)-j-1):
            rightDiagonal += a[i][j]
print(abs(leftDiagonal - rightDiagonal))
