#  File: Bowling.py
#  Description: Read a file containing bowling scores and display them on a table
#  Student's Name: Tomi Olubeko
#  Student's UT EID: oeo227
#  Course Name: CS 313E 
#  Unique Number: 51325
#
#  Date Created: 9/6/16
#  Date Last Modified:9/9/16

def main():
    #Open scores.txt and make it read only
    scores = open('scores.txt', 'r')

    #Parse through all the lines in scores.txt and display the table

    #Initialize variables
    for line in scores:
        total = 0
        frame = 1
        psum1 = 0
        psum2 = 0
        psum3 = 0
        psum4 = 0
        psum5 = 0
        psum6 = 0
        psum7 = 0
        psum8 = 0
        psum9 = 0

        #Print out the top 2 lines
        print("  1   2   3   4   5   6   7   8   9    10")
        print("+---+---+---+---+---+---+---+---+---+-----+")

        #Remove all the spaces between scores so its easier to parse 
        currline = line.replace(" ","")
        i = 0

        #Logic to print out the third row, first 9 frames
        while frame <= 9:
            if currline[i] == "X":
                total += 10
                print("|" + currline[i] + "  ", end='')
                addStrike1 = currline[i+1]
                addStrike2 = currline[i+2]
                if addStrike1 == "X" and addStrike2 == "X":
                    total += 20
                if addStrike1 == "X" and addStrike2 == "-":
                    total += 10
                if ((addStrike1 == "X") and (addStrike2.isdigit())):
                    total += 10 + int(addStrike2)
                if addStrike1 == "-" and addStrike2 == "/":
                    total += 10
                if ((addStrike1 == "-") and (addStrike2.isdigit())):
                    total += int(addStrike2)
                if (addStrike1 == "-") and addStrike2 == "-":
                    total += 0
                if ((addStrike1.isdigit()) and (addStrike2 == "/")):
                    total += 10
                if ((addStrike1.isdigit()) and (addStrike2.isdigit())):
                    total += int(addStrike1) + int(addStrike2)
                if ((addStrike1.isdigit()) and (addStrike2 == "-")):
                    total += int(addStrike1)
                if frame == 1:
                    psum1 = total
                if frame == 2:
                    psum2 = total
                if frame == 3:
                    psum3 = total
                if frame == 4:
                    psum4 = total
                if frame == 5:
                    psum5 = total
                if frame == 6:
                    psum6 = total
                if frame == 7:
                    psum7 = total
                if frame == 8:
                    psum8 = total
                if frame == 9:
                    psum9 = total
                i += 1
                frame += 1
                continue
                
            if currline[i] == "-":
                print("|" + currline[i] + " " + currline[i + 1], end='')
                nextPt = currline[i+1]
                if nextPt == "-":
                    total += 0
                if nextPt.isdigit():
                    total += int(nextPt)
                if nextPt == '/':
                    total += 10
                    addedPt = currline[i+2]
                    if addedPt == "-":
                        total += 0
                    if addedPt == "X":
                        total += 10
                    if addedPt.isdigit():
                        total += int(addedPt)
                if frame == 1:
                    psum1 = total
                if frame == 2:
                    psum2 = total
                if frame == 3:
                    psum3 = total
                if frame == 4:
                    psum4 = total
                if frame == 5:
                    psum5 = total
                if frame == 6:
                    psum6 = total
                if frame == 7:
                    psum7 = total
                if frame == 8:
                    psum8 = total
                if frame == 9:
                    psum9 = total
                i += 2
                frame += 1
                continue

            if currline[i].isdigit():
                print("|" + currline[i] + " " + currline[i + 1], end='')
                nextPt = currline[i+1]
                if nextPt.isdigit():
                    total += int(currline[i]) + int(currline[i+1])
                if nextPt == "-":
                    total += int(currline[i])
                if nextPt == "/":
                    total += 10
                    addedPt = currline[i+2]
                    if addedPt == "-":
                        total += 0
                    if addedPt == "X":
                        total += 10
                    if addedPt.isdigit():
                        total += int(addedPt)
                if frame == 1:
                    psum1 = total
                if frame == 2:
                    psum2 = total
                if frame == 3:
                    psum3 = total
                if frame == 4:
                    psum4 = total
                if frame == 5:
                    psum5 = total
                if frame == 6:
                    psum6 = total
                if frame == 7:
                    psum7 = total
                if frame == 8:
                    psum8 = total
                if frame == 9:
                    psum9 = total
                i += 2
                frame += 1
                continue


        #Handles the 10th frame, including all special cases
        if currline[i] == "X":
            total += 10
            print("|" + currline[i] + " " + currline[i + 1] + " " + currline[i + 2] + "|")
            addStrike1 = currline[i+1]
            addStrike2 = currline[i+2]
            if addStrike1 == "X" and addStrike2 == "X":
                total += 20
            if addStrike1 == "X" and addStrike2 == "-":
                total += 10
            if ((addStrike1 == "X") and (addStrike2.isdigit())):
                total += 10 + int(addStrike2)
            if addStrike1 == "-" and addStrike2 == "/":
                total += 10
            if ((addStrike1 == "-") and (addStrike2.isdigit())):
                total += int(addStrike2)
            if (addStrike1 == "-") and addStrike2 == "-":
                total += 0
            if ((addStrike1.isdigit()) and (addStrike2 == "/")):
                total += 10
            if ((addStrike1.isdigit()) and (addStrike2.isdigit())):
                total += int(addStrike1) + int(addStrike2)
            if ((addStrike1.isdigit()) and (addStrike2 == "-")):
                total += int(addStrike1)
                
        if currline[i] == "-":
            nextPt = currline[i+1]
            if nextPt == "-":
                print("|" + currline[i] + " " + currline[i + 1] + "  |")
            if nextPt.isdigit():
                print("|" + currline[i] + " " + currline[i + 1] + "  |")
                total += int(nextPt)
            if nextPt == "/":
                print("|" + currline[i] + " " + currline[i + 1] + " " + currline[i + 2] + "|")
                total += 10
                addPt = currline[i+2]
                if addPt == "X":
                    total += 10
                if addPt.isdigit():
                    total += int(addPt)

        if currline[i].isdigit():
            nextPt = currline[i+1]
            if nextPt == "-":
                print("|" + currline[i] + " " + currline[i + 1] + "|")
            if nextPt.isdigit():
                print("|" + currline[i] + " " + currline[i + 1] + "  |")
                total += int(nextPt) + int(currline[i])
            if nextPt == "/":
                print("|" + currline[i] + " " + nextPt + " " + currline[i + 2] + "|")
                total += 10
                addPt = currline[i+2]
                if addPt == "X":
                    total += 10
                if addPt.isdigit():
                    total += int(addPt)


        #Put all the frame scores in an array and display them in the 4th row
        frameArray = [psum1,psum2,psum3,psum4,psum5,psum6,psum7,psum8,psum9]
        for i in range(len(frameArray)):
            if len(str(frameArray[i])) == 1:
                print("|  " + str(frameArray[i]),end='')
            if len(str(frameArray[i])) == 2:
                print("| " + str(frameArray[i]),end='')
            if len(str(frameArray[i])) == 3:
                print("|" + str(frameArray[i]),end='')
        if len(str(total)) == 1:
            print("|    " + str(total) + "|")
        if len(str(total)) == 2:
            print("|   " + str(total) + "|")
        if len(str(total)) == 3:
            print("|  " + str(total) + "|")

        #Print out the last row
        print("+---+---+---+---+---+---+---+---+---+-----+")

main()
                    
                
        
