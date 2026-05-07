import random

def partition(A, left, right):
    # 피봇을 랜덤 선택 후 A[left]와 자리를 바꿈
    pivot_idx = random.randint(left, right)
    A[left], A[pivot_idx] = A[pivot_idx], A[left]
    pivot = A[left]

    i = left + 1
    j = right

    while True:
        while i <= right and A[i] < pivot:
            i += 1
        while j > left and A[j] > pivot:
            j -= 1
        if i >= j:
            break
        A[i], A[j] = A[j], A[i]
        i += 1
        j -= 1

    # 피봇을 A[p]에 놓기
    A[left], A[j] = A[j], A[left]
    return j  # p 반환

def QuickSort(A, left, right):
    # 입력: 배열 A[left]~A[right]
    # 출력: 정렬된 배열 A[left]~A[right]
    if left < right:
        p = partition(A, left, right)   # 2. 피봇 기준으로 분할
        QuickSort(A, left, p - 1)       # 3. 피봇보다 작은 그룹
        QuickSort(A, p + 1, right)      # 4. 피봇보다 큰 그룹

# 테스트
A = [38, 27, 43, 3, 9, 82, 10]
print("정렬 전:", A)
QuickSort(A, 0, len(A) - 1)
print("정렬 후:", A)