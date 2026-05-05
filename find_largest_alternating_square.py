# 가장 큰 교대 정사각형의 크기 구하기
def find_largest_alternating_square(A):
  # n x n 크기의 DP 테이블을 0으로 초기화
  n = len(A)
  DP = [[0] * n for _ in range(n)]
  max_size = 0

  for i in range(n):
    for j in range(n):
      # 첫 번째 행이나 첫 번째 열은 자기 자신인 1로 초기화
      if i == 0 or j == 0:
        DP[i][j] = 1
      else:
        # 교대 패턴 확인(상, 좌와 다르고 대각선과는 같아야 함)
        if (A[i][j] != A[i-1][j] and
            A[i][j] != A[i][j-1] and
            A[i][j] == A[i-1][j-1]):
          DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
        else:
          DP[i][j] = 1
      # 전체 최댓값 갱신
      if DP[i][j] > max_size:
        max_size = DP[i][j]
  return max_size

A = [
    [0, 0, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 1, 0, 1, 0],
    [1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0]
]
result = find_largest_alternating_square(A)
print(f'가장 큰 교대 정사각형의 크기는 {result} x {result} 입니다.')
