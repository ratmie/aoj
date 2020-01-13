class Node:
  def __init__(self):
    self.parent = -1
    self.leftChild = None
    self.rightSibling = None
    self.depth = None
    self.getSublings = None

  def getKind(self):
    if self.parent = -1:
      return "root"
    else if self.leftChild = None:
      return "node"
    else:
      return "leaf"

class RTree:
  def __init__(self, n):
    self.nodes = [Node()] * n
  
  def out(self):
    for i, node in enumerate(self.nodes):
      print('node {}: parent = {}, depth = {}, {}, [{}]'.format(i, node.parent, node.depth, node.getKind(), node.getSublings()))
  
  def setDepth(u, p):
    self.nodes[u].depth = p
    if self.nodes[u].right is not None:
      setDepth(self.nodes[u].rignt, p)
    if self.nodes[u].left is not None:
      setDepth(self.nodes[u].left, p + 1)
   def getSublings():


def RootedTrees():
  n = input()
  tree = RTree(n)
  for i in range(n):
    a = input().split()
    degree = a[1]
    for j, k in enumlate(a[2:]):
      if degree is not 0:
        tree.nodes[i].leftChild = a[2]
        tree.nodes[a[j]].rightSibling = a[j + 1]
        tree.nodes[a[j]].parent = i
  tree.out()


RootedTrees()