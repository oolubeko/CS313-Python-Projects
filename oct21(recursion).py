#oct 21st
#Euclids method

def toStr(n,base):
    convString = "0123456789ABCDEF"

    if n < base:
        return(convString[n])
    else:
        return (toStr(n//base,base)+convString[n%base])



#you need to be able to take a repeating sequence like tis, and do it recursively
#not necessarily be tested on euclids methods



#Towers of Hanoi: 


def moveTower(height,fromPole,toPole,withPole):

    if height ==1:
        moveDisk(fromPole, toPole)

    else:
        moveTower(height-1,fromPole,withPole,toPole)
        moveDisk(fromPole,toPole)
        moveTower(height-1,withPole,toPole,fromPole)

#he used awesome turtle graphics for the towers


#pebbles game
#this is MUTUAL recursive, bc it gets smaller each time
        #these methods dont CALL ITSELF???
        
def playAlice(n):
    if n == 0:
        print("alice wins")
    else:
        playBob(n-1)

def playBob(n):
    if n == 0:
        print("Bob wins!")
    elif n%2 == 0:
        playAlice(n-2)
    else:
        playAlice(n-1)

def main():
    for i in range(20):
        print ("If i is: ", i+1)
        playAlice(i+1)

    print(toStr(2862, 2))
    print(toStr(2862, 16))
    print(toStr(2862, 8))


main()
