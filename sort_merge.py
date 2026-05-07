def merge(A, p, k, q):
  left = A[p:k+1]
  right = A[k+1:q+1]
  i = j = 0
  idx = p
  while i < len(left) and j < len(right):
    if left[i] <= right[j]:
      A[idx] = left[i]; i += 1
    else:
      A[idx] = right[j]; j += 1
    idx += 1
  while i < len(left):
    A[idx] = left[i]; i += 1; idx += 1
  while j < len(right):
    A[idx] = right[j]; j += 1; idx += 1

def MergeSort(A, p, q):
  if p < q:
    k = (p + q) // 2
    MergeSort(A, p, k)
    MergeSort(A, k+1, q)
    merge(A, p, k, q)

# 테스트

A = [38, 27, 43, 3, 9, 82, 10]
print(f'정렬 전: {A}')
MergeSort(A, 0, len(A) - 1)
print(f'정렬 후: {A}')