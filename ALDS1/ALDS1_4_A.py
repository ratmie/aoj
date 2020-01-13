# ALDS1_4_A: Linear Search

# 愚直な実装
def linearSearch(l, key):
  for item in l:
    if item == key:
      return True

def main():
  n = int(input())
  S = list(map(int, input().split()))
  m = int(input())
  T = list(map(int, input().split()))
  count = 0
  for i in T:
    if linearSearch(S, i):
      count += 1
  print(count)

main()
