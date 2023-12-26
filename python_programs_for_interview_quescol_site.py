
# Python program to calculate LCM of given two numbers.

'''For any two numbers given by the user as an input, we have to calculate and print the l.c.m. of that numbers using python programming language.

 For example:

Case1: If the user inputs the numbers 4 and 6.

             then the output should be ‘12’.

Case2: If the user inputs the numbers 5 and 7 '''


def lcm_of_two_numbers(num1, num2):
    if num1 > num2:
        largest_number = num1
    else:
        largest_number = num2

    while True:
        if largest_number % num1 == 0 and largest_number % num2 == 0:
            lcm_of_numbers = largest_number
            break
        largest_number += 1
    print(lcm_of_numbers)


#lcm_of_two_numbers(36, 8)


#######################
# Python Program to find GCD or HCF of two numbers using iterative method
#
'''For any two numbers that are inputs given by the user, we have to calculate and print the h.c.f. of that numbers.

 For example:

Case1: If the user inputs the numbers 4 and 6.

            then the output should be ‘2’.

Case2: If the user inputs the numbers 5 and 7.'''


def hcf_of_two_number_iterative(num1, num2):
    hcf = 1
    if num1 > num2:
        smallest = num2
    else:
        smallest = num1

    for i in range(2, smallest + 1):
        if num1 % i == 0 and num2 % i == 0:
            hcf = i
            break
    print(hcf)


#hcf_of_two_number_iterative(8, 22)

# HFC of two numbers using recustion, where function calls itself


def gcd(num1, num2):
    if num2 == 0:
        return num1
    return gcd(num2, num1 % num2)


#print("hcf/gcd of", 8, "and", 16, "=", gcd(8, 16))


# Python Program to Convert Decimal Number into Binary.
'''For example, to convert the decimal number 13 to binary:

13 / 2 = 6 remainder 1
6 / 2 = 3 remainder 0

Ezoic
3 / 2 = 1 remainder 1
1 / 2 = 0 remainder 1
The binary digits are 1101 (in reverse order)'''


def convert_number_to_binary(n):
    binary = ""
    temp = n
    while temp > 0:
        remainder = temp % 2
        binary = str(remainder) + binary
        temp = temp // 2
    print("Binary number is ", binary, " for ", n)


# convert_number_to_binary(18)


def check_year_is_leap_year(n):
    if n % 4 == 0 and n % 100 != 0 or n % 400 == 0:
        print(f"Year {n} is the Leap year")
    else:
        print(f"Year {n} is the Not a Leap year")


check_year_is_leap_year(2000)
