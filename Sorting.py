#  File: Sorting.py
#  Description: Write a driver that will sort various lists using 6 sorting algorithms and print a table 
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 11/13/16
#  Date Last Modified:11/14/16


#All the sorting functions, helper functions, and libraries needed
import random
import time
import sys
sys.setrecursionlimit(10000)

def bubbleSort(alist):
    for passnum in range(len(alist)-1,0,-1):
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                temp = alist[i]
                alist[i] = alist[i+1]
                alist[i+1] = temp

def selectionSort(alist):
    for fillslot in range(len(alist)-1,0,-1):
        positionOfMax = 0
        for location in range(1,fillslot+1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location
        temp = alist[fillslot]
        alist[fillslot] = alist[positionOfMax]
        alist[positionOfMax] = temp


def insertionSort(alist):
    for index in range(1,len(alist)):
        currentvalue = alist[index]
        position = index

        while position>0 and alist[position-1]>currentvalue:
            alist[position] = alist[position-1]
            position = position-1

        alist[position] = currentvalue

def shellSort(alist):
    sublistcount = len(alist)//2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist,startposition,sublistcount)
        sublistcount = sublistcount // 2

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        currentvalue = alist[i]
        position = i

        while position>=gap and alist[position-gap]>currentvalue:
            alist[position] = alist[position-gap]
            position = position - gap

        alist[position] = currentvalue

def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0

        while i<len(lefthalf) and j<len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i += 1
            else:
                alist[k] = righthalf[j]
                j += 1
            k += 1

        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i += 1
            k += 1

        while j < len(righthalf):
            alist[k] = righthalf[j]
            j += 1
            k += 1

def quickSort(alist):
    quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
    if first < last:
        splitpoint = partition(alist,first,last)
        quickSortHelper(alist,first,splitpoint-1)
        quickSortHelper(alist,splitpoint+1,last)

def partition(alist,first,last):
    pivotvalue = alist[first]
    leftmark = first + 1
    rightmark = last
    done = False

    while not done:

        while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
            leftmark += 1

        while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
            rightmark -= 1

        if rightmark < leftmark:
            done = True
        else:
            temp = alist[leftmark]
            alist[leftmark] = alist[rightmark]
            alist[rightmark] = temp

    temp = alist[first]
    alist[first] = alist[rightmark]
    alist[rightmark] = temp

    return rightmark

################################################################################

################################################################################

def main():

#################################################################################
############## The table for sort operations on unsorted lists ##################
#################################################################################
   print("Input type = Random")
   print("                    avg time   avg time   avg time")
   print("   Sort function     (n=10)    (n=100)    (n=1000)")
   print("-----------------------------------------------------")
   print("      bubbleSort    ",end = '')
         
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         random.shuffle(myList)
         startTime = time.perf_counter()
         bubbleSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   selectionSort    ",end = '')
   
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         random.shuffle(myList)
         startTime = time.perf_counter()
         selectionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   insertionSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         random.shuffle(myList)
         startTime = time.perf_counter()
         insertionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       shellSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         random.shuffle(myList)
         startTime = time.perf_counter()
         shellSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       mergeSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         random.shuffle(myList)
         startTime = time.perf_counter()
         mergeSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       quickSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         random.shuffle(myList)
         startTime = time.perf_counter()
         quickSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10
      
   print()
   print()
   print()
   
########################################################################################
##################### Table for sort operations on sorted lists ########################
########################################################################################

   print("Input type = Sorted")
   print("                    avg time   avg time   avg time")
   print("   Sort function     (n=10)    (n=100)    (n=1000)")
   print("-----------------------------------------------------")
   print("      bubbleSort    ",end = '')
         
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         startTime = time.perf_counter()
         bubbleSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   selectionSort    ",end = '')
   
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         startTime = time.perf_counter()
         selectionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   insertionSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         startTime = time.perf_counter()
         insertionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       shellSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         startTime = time.perf_counter()
         shellSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       mergeSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         startTime = time.perf_counter()
         mergeSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       quickSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         startTime = time.perf_counter()
         quickSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print()
   print()
   print()

########################################################################################
################# Table for sort operations on reversed lists ##########################
########################################################################################


   print("Input type = Reverse")
   print("                    avg time   avg time   avg time")
   print("   Sort function     (n=10)    (n=100)    (n=1000)")
   print("-----------------------------------------------------")
   print("      bubbleSort    ",end = '')
         
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         myList.reverse()
         startTime = time.perf_counter()
         bubbleSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   selectionSort    ",end = '')
   
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         myList.reverse()
         startTime = time.perf_counter()
         selectionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   insertionSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         myList.reverse()
         startTime = time.perf_counter()
         insertionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       shellSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         myList.reverse()
         startTime = time.perf_counter()
         shellSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       mergeSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         myList.reverse()
         startTime = time.perf_counter()
         mergeSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       quickSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         myList = [i for i in range(n)]
         myList.reverse()
         startTime = time.perf_counter()
         quickSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print()
   print()
   print()
   
########################################################################################
################ Table for sort operations on almost sorted lists ######################
########################################################################################

   print("Input type = Almost Sorted")
   print("                    avg time   avg time   avg time")
   print("   Sort function     (n=10)    (n=100)    (n=1000)")
   print("-----------------------------------------------------")
   print("      bubbleSort    ",end = '')
         
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         numSwaps = n // 10
         myList = [i for i in range(n)]
         while numSwaps > 0:
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            while randomIndex1 == randomIndex2:
               randomIndex1 = random.randint(0,len(myList)-1)
               randomIndex2 = random.randint(0,len(myList)-1)
            tmp = myList[randomIndex1]
            myList[randomIndex1] = myList[randomIndex2]
            myList[randomIndex2] = tmp
            numSwaps -= 1
         startTime = time.perf_counter()
         bubbleSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   selectionSort    ",end = '')
   
   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         numSwaps = n // 10
         myList = [i for i in range(n)]
         while numSwaps > 0:
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            while randomIndex1 == randomIndex2:
               randomIndex1 = random.randint(0,len(myList)-1)
               randomIndex2 = random.randint(0,len(myList)-1)
            tmp = myList[randomIndex1]
            myList[randomIndex1] = myList[randomIndex2]
            myList[randomIndex2] = tmp
            numSwaps -= 1
         startTime = time.perf_counter()
         selectionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("   insertionSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         numSwaps = n // 10
         myList = [i for i in range(n)]
         while numSwaps > 0:
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            while randomIndex1 == randomIndex2:
               randomIndex1 = random.randint(0,len(myList)-1)
               randomIndex2 = random.randint(0,len(myList)-1)
            tmp = myList[randomIndex1]
            myList[randomIndex1] = myList[randomIndex2]
            myList[randomIndex2] = tmp
            numSwaps -= 1
         startTime = time.perf_counter()
         insertionSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       shellSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         numSwaps = n // 10
         myList = [i for i in range(n)]
         while numSwaps > 0:
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            while randomIndex1 == randomIndex2:
               randomIndex1 = random.randint(0,len(myList)-1)
               randomIndex2 = random.randint(0,len(myList)-1)
            tmp = myList[randomIndex1]
            myList[randomIndex1] = myList[randomIndex2]
            myList[randomIndex2] = tmp
            numSwaps -= 1
         startTime = time.perf_counter()
         shellSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       mergeSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         numSwaps = n // 10
         myList = [i for i in range(n)]
         while numSwaps > 0:
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            while randomIndex1 == randomIndex2:
               randomIndex1 = random.randint(0,len(myList)-1)
               randomIndex2 = random.randint(0,len(myList)-1)
            tmp = myList[randomIndex1]
            myList[randomIndex1] = myList[randomIndex2]
            myList[randomIndex2] = tmp
            numSwaps -= 1
         startTime = time.perf_counter()
         mergeSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

   print("")
   print("       quickSort    ",end = '')

   n = 10
   while n <= 1000:
      avg = 0
      for i in range(5):
         numSwaps = n // 10
         myList = [i for i in range(n)]
         while numSwaps > 0:
            randomIndex1 = random.randint(0,len(myList)-1)
            randomIndex2 = random.randint(0,len(myList)-1)
            while randomIndex1 == randomIndex2:
               randomIndex1 = random.randint(0,len(myList)-1)
               randomIndex2 = random.randint(0,len(myList)-1)
            tmp = myList[randomIndex1]
            myList[randomIndex1] = myList[randomIndex2]
            myList[randomIndex2] = tmp
            numSwaps -= 1
         startTime = time.perf_counter()
         quickSort(myList)
         endTime = time.perf_counter()
         elapsedTime = endTime - startTime
         avg += elapsedTime
      avg /= 5
      avg = format(avg, '.6f')
      print(avg, end = '    ')
      n *= 10

      
main()
