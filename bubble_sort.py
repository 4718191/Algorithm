# 버블 정렬

def BubbleSort(A):
    for p in range(0, len(A)-1):
        for i in range(0, len(A)-1-p):
            if A[i] > A[i+1]:
                A[i], A[i+1] = A[i+1], A[i]
    return A

A = [50,40,90,10]
print(BubbleSort(A))
