# 거스름돈

def CoinChange(W):
  change = W
  n500, n100, n50, n10, n1 = 0, 0, 0, 0, 0
  while change >= 500:
    n500 += 1
  while change >= 100:
    n100 += 1
  while change >= 50:
    n50 += 1
  while change >= 10:
    n10 += 1
  while chagne >= 1:
    n1 += 1
  return n500 + n100 + n50 + n10 + n1

n = int(input('거스름돈 액수: '))
print(f'동전 개수는 {CoinChange(n)}')
