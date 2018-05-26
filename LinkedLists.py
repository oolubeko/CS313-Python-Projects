#  File: LinkedLists.py
#  Description: Implement several methods for ordered and unordered linked lists
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/15/16
#  Date Last Modified:10/16/16

#Definition for Node from class
class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this â€“ saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER


#Create Linked List class
class LinkedList (object):

    #Init method creates an empty Linked list
    def __init__(self):
        tmp = Node("bleh")
        self.head = tmp
    
    def __str__ (self):
     # Return a string representation of data suitable for printing.
     #    Long lists (more than 10 elements long) should be neatly
     #    printed with 10 elements to a line, two spaces between
     #    elements

         row = 0
         current = self.head.getNext()
         while current != None:
            if row == 10:
                print()
                row = 0
            data = current.getData()
            print(data, end = '  ')
            row += 1
            current = current.getNext()
         print()
         return ''
  
    def addFirst (self, item): 
     # Add an item to the beginning of the list
     i = Node(item)     #Create a new node to store data
     
     #if self.isEmpty(): #If list is empty, first element is the item
      #   self.head = i
     #else:              
     i.setNext(self.head.getNext())   #New node points to old first node
     self.head.setNext(i)          #Head of list points to new node

    def addLast (self, item): 
     # Add an item to the end of a list
     i = Node(item)
     previous = self.head
     current = self.head.getNext()

     #if self.isEmpty(): #If list is empty, first element is the item
      #   self.head = i
       #  return
         
     #Loop iterates through the list and gets the last element
     while current != None:
         previous = current
         current = current.getNext()
         
     previous.setNext(i) #Last element points to new node

    def addInOrder (self, item): 
     # Insert an item into the proper place of an ordered list.
     # This assumes that the original list is already properly
     #    ordered.
     i = Node(item)
     previous = self.head
     found = False
     current = self.head.getNext()
     
     #if self.isEmpty(): #Empty List case
      #   self.head = i
       #  return

     #if i.getData() < current.getData(): #Adding smallest element case
      #   self.addFirst(item)
       #  return
        
     #if self.head.getNext() == None:     #Adding element to a list of size 1
      #   if self.head.getData() > i.getData():
       #      self.addFirst(item)
        # else:
         #    self.addLast(item)
         #return
        
     while current != None and not found: 

        #Found where to put element
         if current.getData() > i.getData():
             found = True
             i.setNext(current)
             previous.setNext(i)
         else:
             previous = current
             current = current.getNext()
             
     if not found:
         previous.setNext(i) #Element is the biggest(or same), so put at the end
     
             

    def getLength (self):
     # Return the number of items in the list
     current = self.head.getNext()
     count = 0
     while current != None:
         count += 1
         current = current.getNext()
     return count
     
    def findUnordered (self, item): 
     # Search in an unordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     current = self.head.getNext()
     found = False

     #Iterate through list and update found if item is found
     while current != None and not found:
         if current.getData() == item:
             found = True
         else:
             current = current.getNext()

     return found

    def findOrdered (self, item): 
     # Search in an ordered list
     #    Return True if the item is in the list, False
     #    otherwise.
     # This method MUST take advantage of the fact that the
     #    list is ordered to return quicker if the item is not
     #    in the list.

     current = self.head.getNext()
     found = False

     #Same as findUnordered, except extra check to see if current value if bigger than item
     while current != None and not found:
         if current.getData() == item:
             found = True
         if current.getData() > item:
             break
         else:
             current = current.getNext()
             
     return found
         

    def delete (self, item):
     # Delete an item from an unordered list
     #    if found, return True; otherwise, return False
     current = self.head.getNext()
     previous = self.head
     found = False

     #if self.isEmpty():     #Return false if list is empty
      #   return found

     #if self.head.getData() == item:    #Item to delete is the first item on the list
      #   self.head = self.head.getNext()
       #  current = self.head
        # found = True

     #Once current points to item, set previous to current's next node and set Found
     while current != None and not found:

         if current.getData() == item:
             found = True
             previous.setNext(current.getNext())
         else:
             previous = current
             current = current.getNext()
             
     return found

    def copyList (self):
     # Return a new linked list that's a copy of the original,
     #    made up of copies of the original elements

     current = self.head.getNext()
     newList = LinkedList()

     
     #Takes advantage of addLast method and simply appends data into newList
     while current != None:
         data = current.getData()
         newList.addLast(data)
         current = current.getNext()
         
     return newList

    def reverseList (self): 
     # Return a new linked list that contains the elements of the
     #    original list in the reverse order.

     current = self.head.getNext()
     revList = LinkedList()

     #Takes advantage of addFirst method and inserts every element to the front of newList
     while current != None:
         data = current.getData()
         revList.addFirst(data)
         current = current.getNext()


     return revList

     

    def orderList (self): 
     # Return a new linked list that contains the elements of the
     #    original list arranged in ascending (alphabetical) order.
     #    Do NOT use a sort function:  do this by iteratively
     #    traversing the first list and then inserting copies of
     #    each item into the correct place in the new list.

     current = self.head.getNext()
     oList = LinkedList()

     #Takes advantage of addInOrder to add elements in order to new list
     while current != None:
         data = current.getData()
         oList.addInOrder(data)
         current = current.getNext()

     return oList

    def isOrdered (self):
     # Return True if a list is ordered in ascending (alphabetical)
     #    order, or False otherwise

     inOrder = True
     if self.isEmpty(): #Empty list case
         return inOrder

     current = self.head.getNext()
     nextVal = current.getNext()
     
    
     

     #Uses a forward pointer to point to the next list val and check if current is less than next
     while current != None and inOrder:
         if nextVal == None:
             return inOrder
            
         if  current.getData() > nextVal.getData():
             inOrder = False

         else:
             current = nextVal
             nextVal = nextVal.getNext()

     return inOrder
             

    def isEmpty (self):
         # Return True if a list is empty, or False otherwise
         return self.head.getNext() == None

    def mergeList (self, b): 
         # Return an ordered list whose elements consist of the 
         #    elements of two ordered lists combined.

         mList = LinkedList()
         current = self.head.getNext()
         currentb = b.head.getNext()

         # Add the new list data in order to the list that calls the method
         while current != None:
             data = current.getData()
             mList.addInOrder(data)
             current = current.getNext()
             
         while currentb != None:
            data = currentb.getData()
            mList.addInOrder(data)
            currentb = currentb.getNext()

         return mList

    def isEqual (self, b):
         # Test if two lists are equal, item by item, and return True.
         isEqual = True
         current = self.head.getNext()
         bcurrent = b.head.getNext()
     
         if self.isEmpty() and b.isEmpty(): #If both lists empty return true
             return isEqual

         if self.getLength() != b.getLength(): #If the lists are of different length return False
             isEqual = False

         #Parse through both lists and check for equality
         while current != None and bcurrent != None and isEqual:
             data = current.getData()
             bdata = bcurrent.getData()

             if data != bdata:
                 isEqual = False

             else:
                 current = current.getNext()
                 bcurrent = bcurrent.getNext()

         return isEqual
     

    def removeDuplicates (self):
         # Remove all duplicates from a list, returning a new list.
         #    Do not change the order of the remaining elements.

         newList = LinkedList()
         
         if self.isEmpty(): #Case for empty list
             return newList
            
         current = self.head.getNext()

         while current != None:
             data = current.getData()

             #Take advantage of findUnordered method
             if not newList.findUnordered(data):
                 newList.addLast(data)  #Add data to newList if it is not already in there
                 
             current = current.getNext()

         return newList

     
     

# Copy and paste the following after your class definitions for
# Nodes and LinkedLists.  Do NOT change any of the code in main()!

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()
