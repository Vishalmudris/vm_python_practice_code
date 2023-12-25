# Interview Question from : https://quescol.com/interview-preparations/python-coding-question
import math


# Write a program to reverse an integer in Python.

def reverse_integer():
    integer_list = [1, 2, 3, 4, 5]
    print(integer_list[::-1])


# reverse_integer()


# Write a program in Python to check whether an integer is Armstrong number or not.
'''It is a number that is equal to the sum of its own digits raised to the power of the number of digits.
Here's an algorithm to determine if a given number is an Armstrong number:
For eg: 153, is an Armstrong number because it has 3 digits, and 1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153

Algo:
    Input: Take an integer as input from the user or the program.
    Count the number of digits:
        Convert the number to a string.
        Measure the length of the string. This will give you the number of digits.
    Calculate the sum of the nth power of individual digits:
        Iterate through each digit in the number.
        Raise each digit to the power of the total number of digits.
        Sum up these results.

    Compare the sum with the original number:
        If the calculated sum is equal to the original number, then it's an Armstrong number.
        If they're not equal, it's not an Armstrong number.

Here's a Python program to check Armstrong's number
'''


def armstrong_number():
    number_four_digit = 8421
    get_length = len(str(number_four_digit))
    sum = 0
    temp = number_four_digit
    while temp > 0:
        temp1 = temp % 10  # % 10 is to get the last digit like 8421%10 last digit is 1 and 84%10 last digit is 4
        sum += temp1 ** get_length  # Multiply length with the last digit number and then add and update value of sum
        print(sum)
        print(temp//10)
        temp //= 10  # Remove last digit for the number
    if sum == number_four_digit:
        print(f"The given number {number_four_digit} is ARMSTRONG")
    else:
        print(f"Ohh no the given number {number_four_digit} is NOT ARMSTRONG")


#armstrong_number()


# Armstrong number using list comprehension
def armstrong_number_comprehension():
    number_four_digit = 8421
    create_list_of_digits = [int(n) for n in str(number_four_digit)]
    print(create_list_of_digits)
    get_length_of_digits = len(create_list_of_digits)
    print(get_length_of_digits)
    get_list_test = [int(n ** get_length_of_digits) for n in create_list_of_digits]
    print(get_list_test)
    armstrong_test_number = sum([int(n ** get_length_of_digits) for n in create_list_of_digits])
    print(armstrong_test_number)
    if sum == number_four_digit:
        print(f"Yeah The given number {number_four_digit} is ARMSTRONG")
    else:
        print(f"Ohh no the given number {number_four_digit} is NOT ARMSTRONG")


# armstrong_number_comprehension()


# Fibonacci Series for n numbers Iterative and Recursive both methods

# A Fibonacci series is a series in which next number is a sum of previous two numbers.
def fibonacci_series_n_numbers_iterative():
    n = 10
    first, second = 0, 1
    #febonacci_list = []
    print("fibonacci series are : ")
    for i in range(0, n):
        if i <= 1:
            result = i
        else:
            result = first + second
            first, second = second, result
        print(result)


# fibonacci_series_n_numbers_iterative()


def fibonacci_series_n_numbers_recursive(n):
    first, second = 0, 1

    def fib_recursive(i):
        if i <= 0:
            return 0
        elif i == 1:
            return 1
        else:
            return fib_recursive(i-1) + fib_recursive(i-2)
    for j in range(0, n):
        print(fib_recursive(j))


# fibonacci_series_n_numbers_recursive(8)


# Write a program in Python to check whether a number is palindrome or not using iterative and Recursive both the method.

# Palindrome:
# A Palindrome number is a number which reverse is equal to the original number means number itself.

# A Palindrome word is a word which reverse is equal to the original word means word itself.

# Example : 121, 111, 1223221, kayak, rotator, peep, deed, noon

def palindrome_check_slicing(*args):
    for arg in args:
        if str(arg) == str(arg)[::-1]:
            print(f"{arg} is Palindrome")
        else:
            print(f"ohh no {arg} is not a Palindrome")


# palindrome_check_slicing(121, 232, 4578, "deed", "peep", "test", "check")


def palindrome_check_iteration(n):
    reverse = 0
    while n > 0:
        print("Initial reverse and n : ", reverse, n)
        a = reverse * 10
        b = n % 10
        print("Next reverse and n : ", reverse, n)
        reverse = a + b
        n = n // 10

    print(reverse)


# palindrome_check_iteration(13679)


def palindrome_check_recursion(n):
    def reverse_string(reverse):
        if reverse < 10:
            return reverse
        else:
            print(reverse % 10, reverse_string(reverse//10))
            reverse2 = str(reverse % 10) + str(reverse_string(reverse//10))
            print(reverse2)
            return int(reverse2)

    def check_palindrome(test_string):
        if test_string == reverse_string(test_string):
            return True
        return False

    if check_palindrome(n) is True:
        print(f"Wow the number {n} is palindrome")
    else:
        print(f"Ohh no the number {n} is not an palindrome")


# palindrome_check_recursion(101)

############################

# Program to check given number representation is in binary or not

# Just like the binary representation of 2 is 0010.

# So we will check only if given input number has 0 and 1 or is any other digits.

def check_binary_number(n):
    while n > 0:
        get_last_digit_of_number = n % 10
        print(get_last_digit_of_number)
        if get_last_digit_of_number != 0 and get_last_digit_of_number != 1:
            print(f"The number {n} is not at all binary number")
            break
        n = n//10
        if n == 0:
            print(f"Wow its a binary number")


# check_binary_number(1011)

#######################################


# Write a program in Python to find sum of digits of a number using recursion?

def sum_of_digits_iteration_method(n):
    a,b = 0, 0
    while n > 0:
        a = n % 10
        b += a
        n = n // 10

    print(f"Total of {n} is {b}")


# sum_of_digits_iteration_method(254)


def sum_of_digits_recursion_method(n):
    if n == 0:
        return 0
    print(f"{n % 10} and  {sum_of_digits_recursion_method(int(n // 10))}")
    return (n % 10) + sum_of_digits_recursion_method(int(n // 10))
    # Driven code to check above


# print("Sum of digits is ", sum_of_digits_recursion_method(12345))

#########################

# Swap two variables without using the third variable in Python


def swap_two_variables_without_third_variable(a, b):
    a, b = b, a
    return a, b


# print(swap_two_variables_without_third_variable(20, 40))


##############
# Python program to find the Prime factors of a given input integer.
# Prime factorization is a mathematical process of breaking down a number into its prime factors.
# Enter a number: 24
# Prime factors of 24 are: [2, 2, 2, 3]
def prime_factors(n):
    i = 2
    factors = []
    while i <= n:
        print(i, n, n % i, n // i)
        if n % i:
            i += 1
            print(i, n)
        else:
            n //= i
            factors.append(i)
            print(factors)
    if n > 1:
        factors.append(n)
    return factors


# print("Prime factors of", 44, "are:", prime_factors(1122))

#############################

# Calculate average of the numbers in the list
# Using SUM and LEN
list_of_numbers = [11, 22, 33, 44, 55, 66, 77, 88, 99]


def average_using_length_sum():
    print(sum(list_of_numbers)//len(list_of_numbers))

# average_using_length_sum()

# Using FOR loop:


def average_using_for_loop(n):
    p, q = 0, 0
    for i in n:
        p = p + i
        q += 1

    return p // q


# print(average_using_for_loop(list_of_numbers))

###############################################################
# Python Program to calculate factorial using iterative method.


def factorial_of_number_iterative(n):
    fact = 1
    if n <= 0:
        print("Number is negative or zero, so factorial cant be calculated")
    elif n == 1:
        print("Factorial Number is 1")
        return 1
    else:
        for i in range(2, n+1):
            fact *= i
            print(fact, i)
    print(f"Factorial of {n} is {fact}")


# factorial_of_number_iterative(8)

# Python Program to calculate factorial using Recursive method.
# Recursive method is a method in which function called itself


def factorial_of_number_recursive(n):
    if n == 1:
        return n
    else:
        print(n * factorial_of_number_recursive(n-1))
        return n * factorial_of_number_recursive(n-1)


num = 8
# print(factorial_of_number_recursive(num))

#####################################

# Python Program to check a given number is even or odd.


def check_number_is_even_or_odd(*args):
    for arg in args:
        if arg % 2:
            print(f"Number {arg} is odd number")
        print(f"Number {arg} is Even number")


# check_number_is_even_or_odd(22, 33, 44, 55, 66, 77, 88, 99, 100)


############################

# Python program to print first n Prime Number with explanation.

# Prime Numbers are the numbers that have only 2 factors 1 and the number itself.
# It is only defined for the number which is greater than ‘1’.
# ‘2’ is the smallest prime number.

def first_n_prime_numbers(n):
    prime_no_list = []
    for i in range(1, n):
        for j in range(2, i):
            print(1, j)
            if i % j == 0:
                break
        else:
            prime_no_list.append(i)
    print(prime_no_list)


# first_n_prime_numbers(50)


def prime_number():
    prime_number_list = []
    start = 10
    end = 100
    for x in range(start, end + 1):
        for y in range(2, x):
            if (x % y) == 0:
                break
        else:
            prime_number_list.append(x)

    return prime_number_list


# print(prime_number())


######################################

# Python Program to find smallest number among three.

def smallest_of_three_numbers(a, b, c):
    if a <= b and a <= c:
        print(f"{a} is smallest number")
    elif b <= a and b <= c:
        print(f"{b} is smallest number")
    else:
        print(f"{c} is smallest number")


# smallest_of_three_numbers(49, 46, 44)


# Python program to calculate the power using the POW method.

'''For any two numbers that are inputs given by the user, 
one is the base value let’s say it as ‘x’ and the other is the exponent let’s say it as ‘y’, 
we have to print xy.
Case1: If the user inputs the base of the number as 2 and exponent as 3.
Then the output should be ‘8’.

Case2: If the user inputs the base of the number as 5 and exponent as 2.
Then the output should be ‘25’.
'''

# Python Program to calculate the power without using POW function.(using for loop).


def calculate_pow_for_loop(a, b):
    pow = 1
    for i in range(1, b+1):
        pow *= a
    print(pow)


# calculate_pow_for_loop(5, 4)


# Python Program to calculate the power without using POW function.(using while loop).


def calculate_pow_while_loop(a, b):
    count, pow = 1, 1
    while b != 0:
        pow *= a
        b -= 1
    print(pow)


# calculate_pow_while_loop(5, 4)

# Python Program to calculate the power using ‘pow()’ method


def calculate_pow_using_pow_method(base, exponent):
    print(base, "to power ", exponent, "=", end=' ')
    print(pow(base, exponent))


# calculate_pow_using_pow_method(5, 5)


#######################################################

# Python Program to calculate the square of a given number.
# Python Program to calculate the cube of a given number.
# Python Program to calculate the square root of a given number.
# Square of the number without using math function:

def square_cube_square_root_of_number_without_math(**kwargs):
    for key, value in kwargs.items():
        square_number = {key: value*value}
        cube_number = {key: value*value*value}
        square_root = int(math.sqrt(value))
        square_root_number = {key: square_root}
        print("Square of Number :", square_number, "Cube of number :", cube_number, "Square root of number :", square_root_number)


data = {"a": 2, "b": 3, "c": 4, "d": 5, "e": 6, "f": 7, "g": 8, "h": 9, "i": 10}
square_cube_square_root_of_number_without_math(**data)
