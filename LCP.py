# LCP

def LCP(S):
  n = len(S)
  if n == 0:
     return 0

  DP = [[False] * n for _ in range(n)]
  max_len = 1
  start_idx = 0

  # 길이 1인 경우는 모두 회문 (기초 사례)
  for i in range(n):
    DP[i][i] = True # 대각선은 값이 다 같기 때문에 True

  # 길이 2부터 n까지 확인 (부분 문자열의 길이 L)
  for L in range(2, n+1):
    for i in range(1, n-L+1):
      j = i + L - 1 # 끝 인덱스

      # 조건 1: 양 끝 문자가 같아야 함
      if S[i] == S[j]:
        # 조건 2: 길이가 2이거나(미만 조건), 안쪽이 True여야 함
        if L == 2 or DP[i+1][j-1]:
          DP[i][j] = True
          if L > max_len:
            max_len = L
            start_idx = i

  print(f'''입력 문자열: {S} \n
가장 긴 연속 회문: {S[start_idx:start_idx + max_len]} \n
최대 길이: {max_len}''')

LCP('KBCDXBMBXCABAD')
