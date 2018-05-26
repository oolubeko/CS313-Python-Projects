#  File: htmlChecker.py
#  Description: Parse through a html document and use a Stack class to check to see if all the opening tags have a closing tag
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/3/16
#  Date Last Modified:10/7/16


#Import the Stack object
class Stack (object):
   def __init__(self):
      self.items = [ ]

   def isEmpty (self):
      return self.items == [ ]

   def push (self, item):
      self.items.append (item)

   def pop (self):
      return self.items.pop ()

   def peek (self):
      return self.items [len(self.items)-1]

   def size (self):
      return len(self.items)

   def __str__(self):
      print(self.items)
      return ''

#Parse through html file char by char and return string containing tags
def getTag(htmlFile):
    tag = ''        #string that contains tag
    isTag = False    #set flag
    while not isTag:
        leftTag = htmlFile.read(1)
        if leftTag == '':  #end of file condition
           return ''
        if leftTag == '<': #flag is triggered, < is found
            isTag = True   #loop exit condition
            isRightTag = False #set flag
            while not isRightTag:
                word = htmlFile.read(1)
                if ((word == '>') or (word == ' ')):
                    isRightTag = True #flag is triggered, > or ' ' is found
                else:
                    tag += word #gets the tag
    return tag
    
    

def main():
#Declare main variables
   tagList = []
   VALIDTAGS = []
   EXCEPTIONS = ['br', 'meta', 'hr']
   tagStack = Stack()
   htmlFile = open('htmlfile.txt', 'r')
   doneParsing = False

#Fill tagList with tags    
   while not doneParsing:
      tag = getTag(htmlFile)
      if len(tag) == 0:
         doneParsing = True
      else:
         tagList.append(tag)
            
   print(tagList)

#Go through tagList and match the tags         
   for i in range(len(tagList)):
      tag = tagList[i]
      
      if VALIDTAGS.count(tag) == 0 and tag[0] != '/': #Adds new tags to VALIDTAGS
         VALIDTAGS.append(tag)
         print("New tag " + tag + " found and added to list of valid tags")
         
      if tag[0] != '/': #front tag, push on stack

         #Check if tag is in exceptions list
         if EXCEPTIONS.count(tag) == 1:
            print("Tag " + tag + " does not need to match: stack is still ",end = '')
            print(tagStack)
         else:
            tagStack.push(tag)
            print("Tag " + tag + " is pushed: stack is now ",end = '')
            print(tagStack)
         
      else: #back tag, pop or exit
         if tag[1:] == tagStack.peek():
            tagStack.pop()
            print("Tag " + tag + " matches top of stack: stack is now",end = '')
            print(tagStack)
         else:
            print("Error: tag is " + tag + " but top of stack is " + tagStack.peek())
            return
         
#Print completion message and VALIDTAGS, EXCEPTIONS
   if tagStack.isEmpty(): 
      print("Processing complete. No mismatches found.")
   else:
      print("Processing complete. Unmatched tags remain on stack: ",end = '')
      print(tagStack)

   EXCEPTIONS.sort()
   VALIDTAGS.sort()
   
   print("EXCEPTIONS: ",end = '')
   print(EXCEPTIONS)
   print("VALID TAGS: ",end='')
   print(VALIDTAGS)
          
    
main()
