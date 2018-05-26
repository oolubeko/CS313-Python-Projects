#  File: LinkedLists.py
#  Description: Simulate a hot potato game using Circular Linked Lists
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/21/16
#  Date Last Modified:10/23/16

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


class CircularList(object):

   #Initialize an empty circular linked list
   def __init__ (self): 
      # the circular list constructor method.
      self.head = None
      
   
   def add (self,item):
      # Insert an element in the list.  You will need this to build your
      # circular list from the data strings in the input file.  Hint:  figure
      # out which of the "add" methods we've discussed in class to use is
      # useful here and use it as a template for this method.
      tmp = Node(item)
      current = self.head

      #If list is empty, add an item to it and point the item to itself
      if self.isEmpty():
          self.head = tmp
          tmp.setNext(tmp)
          return

      #Iterate through the list until you find the last node
      while current.getNext() != self.head:
          current = current.getNext()

      #Point the last node to the new node, and the new node to the first node
      current.setNext(tmp)
      tmp.setNext(self.head)

   def isEmpty (self):
      # Return True if the circular list is empty.
      return self.head == None
  
   def onlyOneNode (self):
      # Return True if there is only one node left in the circular list.
      # This would be the "survivor".
      return self.head.getNext() == self.head

   def remove (self,current,previous):
      # Delete the node pointed to by "current" from the circular list.
      # Pass the "previous" pointer along for convenience.  This method
      # would only be called if there are at least 2 nodes in the list.
      # Return a pointer to the node immediately following the deleted
      # one.  Hint:  be sure to correctly handle the case where you delete
      # the first node in the circular list.

      #Fuctionally unnecessary, but the case for only one node
      if self.onlyOneNode():
          self.head = None
          return self.head
      
      ptr = current.getNext()       #Get the pointer to the next node

      #Case for deleting the first item
      if current == self.head:
          last = current.getNext()
          
          while last.getNext() != current:
              last = last.getNext()
          last.setNext(current.getNext())   #Get the last node and point it to the node after the first
          self.head = current.getNext() #Point self.head to the next node
          return ptr

      previous.setNext(current.getNext()) #Regular deletion, point previous node to the node after current node
      return ptr
          

   def __str__ (self):
      # Return a string representation of the circular list.  It should
      # include line breaks after every ten elements in the list.

      current = self.head
      row = 0

      #This while loop will miss the last node for regular cases, or the only node for a list with one item
      while current.getNext() != self.head:
          if row == 10:
              print()
              row = 0
              
          data = current.getData()
          print(data, end = '  ')
          current = current.getNext()
          row += 1

      #Print out the last node or the only node
      data = current.getData()
      print(data)
      print()

      return ''

def main():
    hotPotato = open('HotPotatoData.txt', 'r') #Open the file for reading

    for line in hotPotato:  #Iterate through the file
        numList = line.split(' ')
        last = numList[-1]
        last = last[:len(last) - 1]     #This is to remove the \n the split method adds from the line
        numList[-1] = last

        #Initialize necessary variables
        numPeople = int(numList[0]) #Number of people in the list
        hitNumber = int(numList[-1]) #Number to count to
        circList = CircularList()
        iterationNum = 0

        print("Number of People: ", numPeople)

        #Read numPeople lines and add the data to a Circular Linked List
        while numPeople > 0:
            data = hotPotato.readline()
            data = data[:len(data) - 1]
            circList.add(data)
            numPeople -= 1

        print(circList)

        current = circList.head
        previous = circList.head
        count = 1
        while not circList.onlyOneNode():

            #Deleting the hitNumber node
            if count == hitNumber:
                iterationNum += 1
                print("Iteration Number: ", str(iterationNum))
                print("Deleting " + current.getData())
                current = circList.remove(current,previous)  #remove the hitNumber node, and get the pointer to the node after it
                count = 1
                print("Updated List: ")
                print(circList)
                #print("Starting with ", current.getData())
            else:
                previous = current
                current = current.getNext()
                count += 1

        #Output the sole survivor
        print("The sole survivor is: ", current.getData())
        print()

main()
                
                
                
            

     
          
