# 동적 계획 알고리즘: 거스름돈 동전 개수 구하기

def DPCoinChange(n, d, C):
  for i in range(n + 1):
    C[i] = float('inf') # 무한대로 초기화

  C[0] = 0
  for i in range(1, n + 1):
    for j in range(len(d)):
      if d[j] <= i and C[i - d[j]] + 1 < C[i]:
        C[i] = C[i - d[j]] + 1
  return C[n]

n  = int(input()) # 거스름돈 n
d = [80, 50, 10]
C = [0] * (n + 1) # Initialize C with n+1 elements
print(DPCoinChange(n, d, C))
