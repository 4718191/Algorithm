def WTF(A, B):
    total = 0
    for i in A:
        for j in B:
            if i == j:
                total += 1
    return total

A = [1, 3, 2, 4, 5, 8, 5]
B = [4, 2, 55, 23, 99, 1]
print(WTF(A, B))