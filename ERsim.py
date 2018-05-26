#  File: ERsim.py
#  Description: Simulate an ER, with 3 queues for patients in varying conditions
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 50940
#
#  Date Created: 10/7/16
#  Date Last Modified:10/9/16



#Create the queue class, implemeted in a way that has the last element on the left
class Queue:

    def __init__(self):
        self.items = []

    def enqueue(self,item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def peek(self):
        return self.items[len(self.items) - 1]

    def __str__(self):
        print(self.items)
        return ''


#Takes three ER queues and treats the patient in the highest priority queues
def treat(Crit,Ser,Fair):

    if (Crit.isEmpty()) and (Ser.isEmpty()) and (Fair.isEmpty()): 
        print("   No patients in queues")
        return None
    
    if not Crit.isEmpty():
        print("   Treating " + Crit.peek() + " from Critical queue")
        Crit.dequeue()
        print("   Queues are:")
        print("   Critical: ", end = '')
        print(Crit)
        print("   Serious: ", end = '')
        print(Ser)
        print("   Fair: ", end = '')
        print(Fair)
        return

    if Crit.isEmpty() and not Ser.isEmpty():
        print("   Treating " + Ser.peek() + " from Serious queue")
        Ser.dequeue()
        print("   Queues are:")
        print("   Critical: ", end = '')
        print(Crit)
        print("   Serious: ", end = '')
        print(Ser)
        print("   Fair: ", end = '')
        print(Fair)
        return

    if Crit.isEmpty() and Ser.isEmpty() and not Fair.isEmpty():
        print("   Treating " + Fair.peek() + " from Fair queue")
        Fair.dequeue()
        print("   Queues are:")
        print("   Critical: ", end = '')
        print(Crit)
        print("   Serious: ", end = '')
        print(Ser)
        print("   Fair: ", end = '')
        print(Fair)
        return


    
def main():

    #Initialize the necessary variables
    Critical = Queue()
    Serious = Queue()
    Fair = Queue()
    ERfile = open('ERsim.txt', 'r')

    for line in ERfile:
        splitLine = line.split(' ') #The new line char is added to the string, need to remove it
        condition = splitLine[len(splitLine) - 1]
        condition = condition[:len(condition) - 1]
        splitLine[len(splitLine) - 1] = condition

        #Instruction given is add
        if splitLine[0] == "add":
            person = splitLine[1]
            condition = splitLine[2]
            print(">>> Add patient " + person + " to " + condition + " queue")

            if condition == "Critical":
                Critical.enqueue(person)

            if condition == "Serious":
                Serious.enqueue(person)

            if condition == "Fair":
                Fair.enqueue(person)
    
            print("   Queues are: ")
            print("   Critical: ", end = '')
            print(Critical)
            print("   Serious: ", end = ' ')
            print(Serious)
            print("   Fair: ", end = '   ')
            print(Fair)

        #Instuction is treat
        if splitLine[0] == "treat":
            who = splitLine[1]

            if who == "next":
                print(">>> Treat next patient")
                treat(Critical,Serious,Fair)

            if who == "Serious":
                print(">>> Treat next patient on Serious queue")
                
                if not Serious.isEmpty():
                    print("   Treating " + Serious.peek() + " from Serious queue")
                    Serious.dequeue()
                    print("   Queues are:")
                    print("   Critical: ", end = '')
                    print(Critical)
                    print("   Serious: ", end = '')
                    print(Serious)
                    print("   Fair: ", end = '')
                    print(Fair)

                else:
                    print("   No patients in queues")
                

            if who == "Critical":
                print(">>> Treat next patient on Critical queue")
                if not Critical.isEmpty():
                    print("   Treating " + Critical.peek() + " from Critical queue")
                    Critical.dequeue()
                    print("   Queues are:")
                    print("   Critical: ", end = '')
                    print(Critical)
                    print("   Serious: ", end = '')
                    print(Serious)
                    print("   Fair: ", end = '')
                    print(Fair)

                else:
                    print("   No patients in queue")

            if who == "Fair":
                print(">>> Treat next patient on Fair queue")
                
                if not Fair.isEmpty():
                    print("   Treating " + Fair.peek() + " from Fair queue")
                    Fair.dequeue()
                    print("   Queues are:")
                    print("   Critical: ", end = '')
                    print(Critical)
                    print("   Serious: ", end = '')
                    print(Serious)
                    print("   Fair: ", end = '')
                    print(Fair)

                else:
                    print("   No patients in queue")

            if who == "all":
                print(">>> Treat all patients")
                while not (Critical.isEmpty() and Serious.isEmpty() and Fair.isEmpty()):
                    treat(Critical,Serious,Fair)


        #Instruction is Exit
        if splitLine[0] == "exit":
            print("Exit")
        
        
                







main()
