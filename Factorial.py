def iFactorial(num):
    #iterative version

    i = num
    fact = 1
    while i > 1:
        fact *= i
        i -= 1

    return fact


def rFactorial(num):

    if num == 1:
        return 1

    else:
        return num * rFactorial(num - 1)


def main():

    print ("Factorial of 6 is ", iFactorial(6))
    print ("Factorial of 6 is ", rFactorial(6))

main()
