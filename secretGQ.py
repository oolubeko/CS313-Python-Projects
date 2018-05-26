'''
def getMaxSize(s):
   
   portion = ''
   isMaxSize = False
   
   for i in range(len(s)):
      if isMaxSize:
         break
      portion += s[i]
      for j in range(i+1,len(s),len(portion)):
         isSame = s[j:j+len(portion)]
         if portion != isSame:
            break
         else:
            last = s[len(s) - len(portion):]
            if portion != last:
               break
            isMaxSize = True
            break
         
   return len(s) / len(portion)


def answer(total_lambs):
   minH = [1,1]
   maxH = [1]
   t = total_lambs
   while sum(minH) < total_lambs:
      newNum = minH[-2] + minH[-1]
      if sum(minH) + newNum > total_lambs:
         break
      minH.append(minH[-2] + minH[-1])
   while sum(maxH) < total_lambs:
      newNum = maxH[-1] * 2
      if sum(maxH) + newNum > total_lambs:
         break
      maxH.append(maxH[-1] * 2)
   return len(minH) - len(maxH)
   


def xVal(x):
   numToAdd = 1
   total = 0
   
   while x > 0:
      total += numToAdd
      numToAdd += 1
      x -= 1
   return total

def yVal(x,y):
   numToAdd = x
   if y == 1:
      return xVal(x)
   y_val = xVal(x)
   while y > 1:
      y_val += numToAdd
      numToAdd += 1
      y -= 1
   return y_val

def answer(x,y):
   return str(yVal(x,y))
'''

def isTrip(n1,n2,n3):
   return n2 % n1 == 0 and n3 % n2 == 0

def answer(l):
   numTrip = 0
   if len(l) < 3:
      return numTrip
   if len(l) == 3:
      if l[1] % l[0] == 0 and l[2] % l[1] == 0:
         numTrip += 1
      return numTrip

   for i in range(len(l) - 2):
      num1 = l[i]
      for j in range(i+1,len(l)-1):
         num2 = l[j]
         if num2 % num1 != 0:
            break
         for k in range(j+1,len(l)):
            num3 = l[k]
            if isTrip(num1,num2,num3):
               numTrip += 1
   return numTrip

def main():
   print(answer([1,2,3,4,5,6]))
   print(answer([1,3,5,7,9]))
   print(answer([1,3,5,7,9,12,15,18,21,24,27,30,36,40,55,76,80]))
  
   
main()
