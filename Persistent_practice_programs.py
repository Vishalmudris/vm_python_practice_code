def list(val,list=[]):
    list.append(val)
    return list

list1 = list(1)
list2 = list(123,[])
list3 = list("a")

# print(f"Its l1 :{list1}, its l2 {list2}, and its l3{list3}")

#Fibonacci series is


def fibonacci(n):
    list = [0,1,1,2,3,5,8,13]
    feb_series = []
    a, b = 0, 1
    for i in range(0,n):
        if i <= 1:
            feb_series.append(i)
        c = a + b
        a, b = b, c
        feb_series.append(c)
    print(feb_series)

# fibonacci(8)


def reverse_by_for_str(n):
    result = ""
    for i in n:
        result = i + result
    print(result)


reverse_by_for_str("vishal")


#######################################################
'''From site https://www.prepbytes.com/blog/python/top-20-coding-questions-for-basic-python-programming/'''

# Write a program to print the given number is odd or even.


def print_even_or_odd_number(n):
    if n % 2 == 0:
        print(f"Number {n} is Even number")
    else:
        print(f"Number {n} is Odd number")


# print_even_or_odd_number(8)
# print_even_or_odd_number(11)

# Write a program to find the given number is positive or negative.


def print_positive_or_negative(n):
    if n >= 0:
        print(f"Number {n} is Positive number")
    else:
        print(f"Number {n} is Negative number")


# print_positive_or_negative(-8)
# print_positive_or_negative(11)


# Write a program to find the sum of two numbers.


def sum_of_numbers(*args):
    total = 0
    for arg in args:
        total += arg
    print(total)
    print(sum(args))


# sum_of_numbers(2, 4, 8, 11, 13, 20, 22, 31)


# Write a program to find if the given number is prime or not.

def check_number_is_prime(n):
    flag = False
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                flag = True
                break
    if flag is True:
        print("Number is NOT prime number")
    else:
        print("Number is prime Number")


'''check_number_is_prime(8)
check_number_is_prime(16)
check_number_is_prime(21)
check_number_is_prime(23)'''

# Write a program to check if the given number is palindrome or not.


def check_number_is_palindrome(n):
    a, b, c = 0, 0, 0
    temp = n
    while temp > 0:
        a = temp % 10
        b = c * 10
        c = a + b
        temp = temp//10
    print(c)
    if n == c:
        print("Number is palindrome")
    else:
        print("Number is not palindrome")


check_number_is_palindrome(202)


# Write a program to check if the given number is Armstrong or not.

def check_number_is_armstrong(n):
    a, b, c = 0, 0, 0
    temp = n
    c = len(str(n))
    while temp > 0:
        a = temp % 10
        b += a ** c
        temp = temp//10
    print(b)
    if n == b:
        print("Number is Armstrong")
    else:
        print("Number IS NOT armstrong")


# check_number_is_armstrong(345)
# check_number_is_armstrong(407)


# Write a program to check if the given strings are anagram or not.

def validate_string_anagram(n, m):
    if sorted(n) == sorted(m):
        print("Strings are anagram")
    else:
        print("String ARE NOT anagram")


# validate_string_anagram("anagram", "graamanna")
# validate_string_anagram("teststring", "stringtest")


# Write a program to find a factorial of a number.
'''Case1: If the user input the 5.

             then the output should be 120 ( 1*2*3*4*5= 120).

Case2: If the user input the 6.

            then the output should be 720 (1*2*3*4*5*6 =720).'''


def factorial_of_number(n):
    i = 1
    for num in range(1, n + 1):
        i *= num
    print(i)


# factorial_of_number(8)


# Write a program to find a fibonacci of a number.

def fibonacci_number(n):
    a, b = 0, 1
    fib_series = []
    for num in range(0, n):
        if num <= 1:
            fib_series.append(num)
        else:
            c = a + b
            a, b = b, c
            fib_series.append(b)
    print(fib_series)


# fibonacci_number(8)

# Write a program to find GCD of two numbers.

def gcd_of_two_number(n, m):
    smallest = 1
    if n < m:
        smallest = n
    else:
        smallest = m

    for i in range(2, smallest + 1):
        if n % i == 0 and m % i == 0:
            smallest = i
            break
    print(smallest)


# gcd_of_two_number(8, 15)


def prime_numer_from_range(n):
    prime_numbers = []
    for i in range(1, n):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_numbers.append(i)
    print(prime_numbers)


prime_numer_from_range(50)


def validate_ip(n):
    ip = n.split(".")
    count = 0
    if len(ip) == 4:
        for i in ip:
            if i.isdigit():
                i = int(i)
                if i >= 255:
                    print("number is not ip")
                    break
                count += 1
    else:
        print("Number is not IP")

    if count == 4:
        print("Number is IP")


'''validate_ip("10.1.1.13")
validate_ip("300.10.14.18")
validate_ip("14.18")
validate_ip("asdfsdafsafsd")'''

# Interview questions in persistent

'''Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.
 
An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

[2:20 PM] Navneet Mishra
Input: grid = [
  ["1","1","1","1","0"], 
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
  
  output: 1
  
  
  ["1","1","0","0","0"], 
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
  
  output: 3'''


def island_query_iterate_matrix():
    grid1 = [
  ["1","2","3","4","5"],
  ["11","22","33","44","55"],
  ["111","222","333","444","555"],
  ["1111","2222","3333","4444","5555"]]
    result = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    for row in range(len(grid1)):
        for column in range(len(grid1[row])):
            print(grid1[row][0])


# island_query_iterate_matrix()


def input_remove_special_characters_reverse():
    s = "th-e s@$ky i#s bl/ue"
    new_str = ""
    for char in s:
        if char == " ":
            new_str += char
        elif char.isalnum() is False:
            char = ""
        new_str += char
    reverse = ""
    for words in new_str.split(" "):
        reverse = " " + words + reverse
    print(reverse.strip())


# input_remove_special_characters_reverse()

# Sorting of list in ascending order
def sorting_of_list():
    input=[20,14,25,10,56,85,3]
    output=85,56,25,10,20,14
    new_input = []
    for i in range(len(input)):
        for j in range(i+1, len(input)):
            if input[i] >= input[j]:
                input[i], input[j] = input[j], input[i]

    print(input)


sorting_of_list()
