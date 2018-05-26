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
      return self.items[-1]

   def size (self):
      return len(self.items)

   def __str__(self):
      print(self.items)
      return ''

class Node (object):
   def __init__(self,initdata):
      self.data = initdata
      self.next = None            # always do this – saves a lot
                                  # of headaches later!
   def getData (self):
      return self.data            # returns a POINTER

   def getNext (self):
      return self.next            # returns a POINTER

   def setData (self, newData):
      self.data = newData         # changes a POINTER

   def setNext (self,newNext):
      self.next = newNext         # changes a POINTER


class OrderedList (object):

   def __init__(self):                # identical to OrderedList
      self.head = None

   def isEmpty (self):                # identical to OrderedList
      return self.head == None

   def length (self):                 # identical to OrderedList
      current = self.head
      count = 0

      while current != None:
         count += 1
         current = current.getNext()

      return count

   def remove (self,item):             # identical to OrderedList
      current = self.head
      previous = None
      found = False

      while not found:
         if current.getData() == item:
            found = True
         else:
            previous = current
            current = current.getNext()

      if previous == None:
         self.head = current.getNext()
      else:
         previous.setNext(current.getNext() )   


   def search (self,item):       # improved over UnorderedList.search()

      current = self.head
      found = False
      stop = False
      while current != None and not found and not stop:
         if current.getData() == item:
            found = True
         else:
            if current.getData() > item:
               stop = True
            else:
               current = current.getNext()

      return found

   def add (self,item):       # the only one with a major change from Unordered

      current = self.head
      previous = None
      stop = False

      while current != None and not stop:
         if current.getData() > item:
            stop = True
         else:
            previous = current
            current = current.getNext()

      temp = Node(item)
      if previous == None:
         temp.setNext(self.head)
         self.head = temp
      else:
         temp.setNext(current)
         previous.setNext(temp)


def isPalindrome(n):
    first = 0
    last = len(n) - 1
    isPalindrome = True

    while isPalindrome and last >= first:
        if n[first] != n[last]:
            isPalindrome = False
        else:
            first += 1
            last -= 1
    return isPalindrome

def sumFibList(j):
    first = 1
    second = 2
    total = 0
    while (first + second) < 4000000:
        j.append(first + second)
        first = second
        second = j[-1]

    for i in range(len(j)):
        if j[i] % 2 == 0:
            total += j[i]
    return total

def largestPal():
    largest = 0

    for i in range(1000):
        for j in range(1000):
            product = i * j
            product = str(product)
            if isPalindrome(product) and int(product) > largest:
                largest = int(product)

    return largest
            
def smallestMultiple():
    i = 2520
    divisible = False
    while not divisible:
        if (i % 1 == 0) and (i % 2 == 0) and (i % 3 == 0) and (i % 4 == 0) and (i % 5 == 0) and (i % 6 == 0) and (i % 7 == 0) and (i % 8 == 0) and (i % 9 == 0) and (i % 10 == 0) and (i % 11 == 0) and (i % 12 == 0) and (i % 13 == 0) and (i % 14 == 0) and (i % 15 == 0) and (i % 16 == 0) and (i % 17 == 0) and (i % 18 == 0) and (i % 19 == 0) and (i % 20 == 0):
            divisible = True
        else:    
            i += 1
    return i

def sumSquareDifference():
    sumSquare = 0
    squareSum = 0

    for i in range(101):
        sumSquare += i * i
        squareSum += i
    squareSum *= squareSum
    difference = squareSum - sumSquare
    return difference

def isPrime(n):
    limit = n // 2 + 1
    for i in range(2,limit):
        if n % i == 0:
            return False
    return True

def countPrimes():
    i = 4
    primesList = [2,3]
    total = 0

    while i < 2000000:
        if isPrime(i):
            primesList.append(i)
        i += 1

    for j in range(len(primesList)):
       total += primesList[j]

    return total

    




def prefix(n):
    expressions = {'+','-','*','/'}
    s = Stack()
    for i in range(len(n)):
        if n[i] in expressions:
            s.push(n[i])
            print(s)
        else:
            if s.peek().isdigit():
                total = 0
                num = int(s.pop())
                expr = s.pop()
                if expr == '+':
                    total = num + int(n[i])
                    s.push(str(total))
                if expr == '-':
                    total = num - int(n[i])
                    s.push(str(total))
                if expr == '/':
                    total = num // int(n[i])
                    s.push(str(total))
                if expr == '*':
                    total = num * int(n[i])
                    s.push(str(total))
                print(s)
            else:
                s.push(n[i])
                print(s)
                
    if s.size() == 1:
        return s.pop()

    while s.size() > 1:
        num1 = int(s.pop())
        num2 = int(s.pop())
        expr = s.pop()
        if expr == '+':
            total = num1 + num2
            s.push(str(total))
        if expr == '-':
            total = num1 - num2
            s.push(str(total))
        if expr == '/':
            total = num1 // num2
            s.push(str(total))
        if expr == '*':
            total = num1 * num2
            s.push(str(total))

    return s.pop()
                    

def sumNegatives(myList):
   if myList == None:
      return 0
   if myList.getData() >= 0:
      return 0
   else:
      return myList.getData() + sumNegatives(myList.getNext())



def largestProduct():
   num = "7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"
   numArray = []
   product = 0
   
   for i in range(len(num)):
      numArray.append(int(num[i]))
      
   for j in range(len(numArray) - 12):
      temp = 1
      for k in range(13):
         temp *= numArray[k+j]
      if temp > product:
         product = temp

   return product


def pythTriplet():
   a = 8
   b = 15
   c = 17
   i = 1
   found = False

   while not found:
      if (((a * i) + (b * i) + (c * i)) == 1000):
            found = True
      else:
         i += 1
   result = (a * i) * (b * i) * (c * i)
   return result
      

def  get_max_profit(stock):
   if len(stock) < 2:
      print("Need at least 2 prices")
      return
   
   minP = stock[0]
   maxP = stock[1] - stock[0]

   for i in range(1,len(stock) - 1):
      temp = stock[i + 1] - stock[i]
      if temp > maxP:
         maxP = temp
      if stock[i] - minP > maxP:
         maxP = stock[i] - minP
      if stock[i] < minP:
         minP = stock[i]

   return maxP

    

def main():
   stock = [10, 7, 5, 8, 11, 9]
   print(get_max_profit(stock))
   for i in range(10,110,10):
      print (i)
    

main()
