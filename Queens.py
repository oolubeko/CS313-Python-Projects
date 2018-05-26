#  File: Queens.py
#  Description: Prompts user for input n, then prints all solution to Queen's problem for an nxn board
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 11/6/16
#  Date Last Modified:11/11/16



class QueensProblem():
   #Make an n x n board
   def __init__(self,n):
      self.grid = []
      self.count = 1
      for i in range(n):
         self.grid.append([])
      for i in range(n):
        for j in range(n):
                self.grid[i].append("*")

   #Prints out the board
   def __str__(self):
      for i in range(len(self.grid)):
         for j in range(len(self.grid[0])):
            print(self.grid[i][j], end = ' ')
         print()
      return ''

   def isValidPlace(self,row,col):
        # returns True if a queen can be safely placed at the square in row "row" and column "col".
        isValid = True
        k = 0
        # check column upwards
        while (k < row and isValid):
            if self.grid[k][col] == "Q":
                isValid = False
            k += 1
        # check forward diagonal
        k = row - 1
        l = col + 1
        length = len(self.grid)
        while (k >= 0 and l < length and isValid):
            if (self.grid[k][l] == "Q"):
                isValid = False
            k -= 1
            l += 1
        # check backward diagonal
        k = row - 1
        l = col - 1
        while (k >= 0 and l >= 0 and isValid):
            if (self.grid[k][l] == "Q"):
                isValid = False
            k -= 1
            l -= 1
            
        return (isValid)
        
   def solve(self, n):
      #Base case: Prints the board if we reach the last row
      if n == 0:
         print("Solution #" + str(self.count))
         self.count += 1
         print(self)
         return False
      
      row = len(self.grid) - n

      #Loop that will check every col of the row to see if its valid
      for col in range(len(self.grid)):
         self.grid[row][col] = "Q"
         #Recursive call for the row below
         if self.isValidPlace(row,col) and self.solve(n - 1):
            return True
         else:
            self.grid[row][col] = "*"
         
      return False
      
def main():
   n = input("Enter the size of the square board: ")
   n = int(n)
   while n < 4:
      print("Invalid input.")
      n = input("Enter the size of the square board: ")
      n = int(n)
   queen = QueensProblem(n)
   queen.solve(n)
   
main()
