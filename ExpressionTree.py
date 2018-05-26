#  File: ExpressionTree.py
#  Description: Read an algebraic expression from a file, store it in a binary tree, then evaluate it 
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 11/18/16
#  Date Last Modified:11/19/16
   

#Binary tree class
class BinaryTree (object):

   #Init method includes a parent variable
   def __init__ (self,data,parent=None):
      self.data = data
      self.left = None
      self.right = None
      self.parent = parent
      

   def insertLeft(self,newNode):
      #Case for if there is no left child
      if self.left == None:
         self.left = BinaryTree(newNode,self) #Creates a left child of the node
         #self.left.parent = self    #Set the parent of the left child to the current node
      else:
         t = BinaryTree(newNode,self) #Create a new node
         t.left = self.left #Point new node to left child of current node 
         t.left.parent = t #Set the parent variable of current node's old left node to new node 
         self.left = t #Set left child of current node to new node
         #t.parent = self #Set parent of new node to current node


   #Same implementation as insertLeft, but applied to the right child
   def insertRight(self,newNode):
      if self.right == None:
         self.right = BinaryTree(newNode,self)
         #self.right.parent = self
      else:
         t = BinaryTree(newNode,self)
         t.right = self.right
         t.right.parent = t
         self.right = t
         #t.parent = self
         
   def getLeftChild(self):
      return self.left

   def getRightChild(self):
      return self.right

   def setRootVal(self,value):
      self.data = value

   def getRootVal(self):
      return self.data

   def getParent(self):
      return self.parent

   def createTree (self, expr):
      operators = {'+', '-', '*', '/'}
      current = self
      expr = expr.split(" ")
      last = expr[-1]
      last = last[len(last) - 2]
      expr[-1] = last 
      for i in range(len(expr)):
         token = expr[i]
         if token == ')':
            current = current.getParent()
         elif token == '(':
            current.insertLeft(token)
            current = current.getLeftChild()
         elif token in operators:
            current.setRootVal(token)
            current.insertRight("new")
            current = current.getRightChild()
         else:
            current.setRootVal(token)
            current = current.getParent()
            

   def evaluate (self, root):
      if root != None:
         if root.getRootVal() == "+":
            op1 = self.evaluate(root.getLeftChild())
            op2 = self.evaluate(root.getRightChild())
            return op1 + op2
         elif root.getRootVal() == "-":
            op1 = self.evaluate(root.getLeftChild())
            op2 = self.evaluate(root.getRightChild())
            return op1 - op2
         elif root.getRootVal() == "*":
            op1 = self.evaluate(root.getLeftChild())
            op2 = self.evaluate(root.getRightChild())
            return op1 * op2
         elif root.getRootVal() == "/":
            op1 = self.evaluate(root.getLeftChild())
            op2 = self.evaluate(root.getRightChild())
            return op1 / op2
         else:
            return eval(root.getRootVal())
      return ''
      

   def preOrder (self, root):
      if root != None:
         print(root.getRootVal(), end = ' ')
         self.preOrder(root.getLeftChild())
         self.preOrder(root.getRightChild())
      return ''

   def postOrder (self, root):
      if root != None:
         self.postOrder(root.getLeftChild())
         self.postOrder(root.getRightChild())
         print(root.getRootVal(), end = ' ')
      return ''
         

def main():
   treedata = open('treedata.txt','r')
   for line in treedata:
      tree = BinaryTree("root")
      print("Infix expression: " + line)
      tree.createTree(line)
      #print()
      print("   Value:   ",end = '')
      print(tree.evaluate(tree))
      print("   Prefix expression:   ",end = '')
      print(tree.preOrder(tree))
      #print()
      print("   Postfix expression:   ",end = '')
      print(tree.postOrder(tree))
      print()
      print()
      

main()
