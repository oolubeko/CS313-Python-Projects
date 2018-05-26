def main():
   foo = open('foo.txt', 'r')
   gridList = []
   for line in foo:
      row = line.split(' ')
      for i in range(len(row)):
         num = row[i]
         if num[0] == '0':
            num = num[1:]
            row[i] = num
         row[i] = int(row[i])
      gridList.append(row)

   maxProd = 0
   for i in range(len(gridList)):
      for j in range(len(gridList[0])):
         horProd = 1
         if j + 3 < len(gridList[0]):
            horProd *= gridList[i][j] * gridList[i][j+1] * gridList[i][j+2] * gridList[i][j+3]
         if horProd > maxProd:
            maxProd = horProd

         vertProd = 1
         if i + 3 < len(gridList):
            vertProd *= gridList[i][j] * gridList[i+1][j] * gridList[i+2][j] * gridList[i+3][j]
         if vertProd > maxProd:
            maxProd = vertProd

         ldProd = 1
         if (i + 3 < len(gridList)) and (j - 3 >= 0):
             ldProd *= gridList[i][j] * gridList[i+1][j-1] * gridList[i+2][j-2] * gridList[i+3][j-3]
         if ldProd > maxProd:
             maxProd = ldProd

         rdProd = 1
         if (i + 3 < len(gridList)) and (j + 3 < len(gridList[0])):
             rdProd *= gridList[i][j] * gridList[i+1][j+1] * gridList[i+2][j+2] * gridList[i+3][j+3]
         if rdProd > maxProd:
             maxProd = rdProd

   print (maxProd)

main()
             
         
