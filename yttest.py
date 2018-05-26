class Node:
   
   def __init__(self,data,parent=None):
      self.data = data
      self.left = None
      self.right = None
      self.parent = parent

   def isRoot(self):
      return self.parent == None

   def insertRight(self,data):
      if self.right == None:
         self.right = Node(data,self)
      else:
         t = Node(data,self)
         t.right = self.right
         t.right.parent = t
         self.right = t

   def insertLeft(self,data):
      if self.left == None:
         self.left = Node(data,self)
      else:
         t = Node(data,self)
         t.left = self.left
         t.left.parent = t
         self.left = t

   def getRootVal(self):
      return self.data

   def setRootVal(self,data):
      self.data = data
      

def firstCommonAncestor(n1,n2):
   p1 = []
   p2 = []
   current = n1
   
   while not current.isRoot():
      p1.insert(0,current.getRootVal())
      current = current.parent
   p1.insert(0,current.getRootVal())

   current = n2

   while not current.isRoot():
      p2.insert(0,current.getRootVal())
      current = current.parent
   p2.insert(0,current.getRootVal())

   i = 0

   while i < len(p1) and i < len(p2):
      if p1[i] != p2[i]:
         break
      i += 1

   return p1[i-1]

def main():
   t = Node("A")
   t.insertRight("C")
   t.right.insertRight("H")
   t.insertLeft("B")
   t.left.insertLeft("D")
   t.left.insertRight("E")
   t.left.left.insertLeft("G")
   t.left.left.insertRight("F")

   print("Common Ancestor(D,F) = ", firstCommonAncestor(t.left.left, t.left.left.right))
   print("Common Ancestor(C,G) = ", firstCommonAncestor(t.right, t.left.left.left))
   print("Common Ancestor(E,B) = ", firstCommonAncestor(t.left.right, t.left))


main()
         

   

   
