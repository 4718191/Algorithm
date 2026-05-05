# 합이 0에 가장 가까운 두 수 x. y

def Find_xy(n, a):
  a.sort()
  left, right = 0, n - 1
  min = a[left] + a[right]

  while left < right:
    sum = a[left] + a[right]

    if min > sum:
      min = sum
      min_x, min_y = a[left], a[right]

    if sum < 0:
      left += 1
    elif sum > 0:
      right -= 1
    else:
      break
  return min_x, min_y


a = [30, 80, 90, 70, 50, 20, 60, 10, 40]
print(Find_xy(len(a), a))
