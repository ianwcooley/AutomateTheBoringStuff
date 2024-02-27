# This program prints the collatz sequence for a number
print('Enter a positive integer')
try:
    num = int(input())
except:
    print('That is not a positive integer')

def collatz(number):
    print(number)
    while (number != 1):
        if (number % 2 == 0):
            number = number // 2
        else:
            number = number * 3 + 1
        print(number)

collatz(num)
