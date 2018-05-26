



class Queue:

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()

    def size (self):
        return len(self.items)

    def report(self):
        return self.items

    def __str__(self):
        print (self.items)
        return " "
    
def addPatient(allCommands, Critical, Serious, Fair):

    general = allCommands[2]
    d = allCommands[1]
    print (">>>Add patient "+ str(d) + "to" + str(general) + " queue")
    if allCommands[2] == "Critical":
        Critical.enqueue(allCommands[1])
        
    if allCommands[2] == "Serious":
        Serious.enqueue(allCommands[1])

    if allCommands[2] == "Fair":
        Fair.enqueue(allCommands[1])
                         
    print ("Queues are: ")
    print ("    %-10s" % ("Critical: ")  + str(Critical))
    print ("    %-10s" % ("Serious: ") + str(Serious))
    print ("    %-10s" % ("Fair: ") + str(Fair))
    

def treat(allCommands, Critical, Serious, Fair):

    if Critical.isEmpty() and Serious.isEmpty() and Fair.isEmpty():
        print ("No patients in queues")

    if not Critical.isEmpty():
        print("Treat next patient on Critical queue")
        print ("Treating "+ Critical.dequeue() + "on Critical queue")
        
        print ("Queues are: ")
        print ("    %-10s" % ("Critical: ")  + str(Critical))
        print ("    %-10s" % ("Serious: ") + str(Serious))
        print ("    %-10s" % ("Fair: ") + str(Fair))

    if not Serious.isEmpty() and Critical.isEmpty():
        print("Treat next patient on Serious queue")
        print ("Treating " + Serious.dequeue()+ "on Serious queue")
        
        print ("Queues are: ")
        print ("    %-10s" % ("Critical: ")  + str(Critical))
        print ("    %-10s" % ("Serious: ") + str(Serious))
        print ("    %-10s" % ("Fair: ") + str(Fair))

    if not Fair.isEmpty() and Serious.isEmpty() and Critical.isEmpty():
        print("Treat next patient on Fair queue")
        print ("Treating " + Fair.dequeue()+ "on Fair queue")
        
        print ("Queues are: ")
        print ("    %-10s" % ("Critical: ")  + str(Critical))
        print ("    %-10s" % ("Serious: ") + str(Serious))
        print ("    %-10s" % ("Fair: ") + str(Fair))

def treatSer(allCommands, Critical, Serious, Fair):
    
    if Serious.isEmpty():
        print("No patients in queue")
    
    print ("    Treat next patient on Serious queue")
    print ("    Treating " + Serious.dequeue()+ "on Serious queue")
        
    print ("    Queues are: ")
    print ("    %-10s" % ("Critical: ")  + str(Critical))
    print ("    %-10s" % ("Serious: ") + str(Serious))
    print ("    %-10s" % ("Fair: ") + str(Fair))


def main():

    ERsim = open("ERsim.txt", "r")

    
    Critical = Queue()
    Serious = Queue()
    Fair = Queue()
    
    for line in ERsim:
        allCommands = line.split(" ")

        instruction = allCommands[len(allCommands)-1]
        instruction = instruction[:len(instruction)-1]
        allCommands[-1] = instruction

        if allCommands[0] == "add":
            addPatient(allCommands, Critical, Serious, Fair)

        if allCommands[0] == "treat":
            if allCommands[1] == "next":
           #only will call it once
               treat(allCommands, Critical, Serious, Fair)
               
            if allCommands[1] == "all":
               while not Critical.isEmpty() and not Serious.isEmpty() and not Fair.isEmpty():
                   print("Treat all patients")
                   treat(allCommands, Critical, Serious, Fair)
                   

            if allCommands[1] == "Serious":
           #always put param bc you are updaating it each time
               treatSer(allCommands, Critical, Serious, Fair)

        if allCommands[0] == "exit":
           print("exit")

            

                   
           
main()
    
