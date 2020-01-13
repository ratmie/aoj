# Binary Search

def binarySearch(l, key):
  left = 0
  right = len(l)
  index = (left + right) // 2
  for _ in range(100000000):
    if left == right:
      return -1
    if l[index] < key:
      left = index + 1
      index = (left + right) // 2
    elif l[index] > key:
      right = index
      index = (left + right) // 2
    else:
      return index


# def binarySearch(l, key):
#   left = 0
#   right = len(l)
#   index = (left + right) // 2
#   while left != right:
#     if l[index] == key:
#       return index
#     elif l[index] < key:
#       left = index + 1
#       index = (left + right) // 2
#     else:
#       right = index
#       index = (left + right) // 2
#   else:
#     return -1

def main():
  n = int(input())
  S = list(map(int, input().split()))
  m = int(input())
  T = list(map(int, input().split()))
  count = 0
  for i in T:
    if binarySearch(S, i) != -1:
      count += 1
  print(count)

main()

# でかいリストのコピーでTLEになる