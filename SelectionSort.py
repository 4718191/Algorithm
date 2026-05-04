# 선택 정렬

def SelectionSort(A):
    for i in range(len(A)):
        min = i
        for j in range(i+1, len(A)):
            if A[min] > A[j]:
                min = j
    return A

A = [40,10,50,90,20,80,30,60]
print(SelectionSort(A))