def is_perfect_square(number):
     """
     Created a function to check if a number is a perfect square
     :param number:
     :return: boolean
     """
#Then wrote a formular to get the square-root of the given number
     sqr_root = number ** 0.5

#I returned the formular to check if a number is a perfect square
     return int(sqr_root + 0.5)**2 == number

#Prompts the user to enter a number
number = int(input("Enter the number: "))

if is_perfect_square(number):
    print('True')
else:
    print('False')
