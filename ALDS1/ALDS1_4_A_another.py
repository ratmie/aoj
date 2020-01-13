# ALDS1_4_A: Linear Search

# 番兵 はやくなってなくない？？？
def linearSearch(l, key):
  index = 0
  l.append(key)
  while l[index] != key:
    index += 1
  else:
    if index == (len(l) -1):
      return -1
    else:
      return index

def main():
  n = int(input())
  S = list(map(int, input().split()))
  m = int(input())
  T = list(map(int, input().split()))
  count = 0
  for i in T:
    if linearSearch(list(S), i) != -1:
      count += 1
  print(count)

main()
