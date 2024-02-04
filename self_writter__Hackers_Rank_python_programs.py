# Write a program to reverse an integer in Python.


def reverse_integer(n):
    a, b = 0, 0
    temp = n
    while temp > 0:
        b = temp % 10
        a = a*10 + b
        temp = temp // 10
    if str(n)[::-1] == str(a):
        print("Number is reversed")


# Write a program in Python to check whether an integer is Armstrong number or not.
def armstrong_number_check(number):
    temp = number
    get_length = len(str(number))
    a, b = 0, 0
    while temp > 0:
        b = temp % 10
        a += b ** get_length
        temp = temp // 10
    if number == a:
        print(f"{number} is Armstrong")
    else:
        print(f"{number} is not Armstrong")

# Fibonacci Series for n numbers Iterative and Recursive both methods

# A Fibonacci series is a series in which next number is a sum of previous two numbers like 0,1,1,2,3,5,8,13.
def fibonacci_series(n):
    a,b = 0, 1
    fib_list = []
    for i in range(1, n + 1):
        fib_list.append(a)
        temp = a + b
        a, b = b, temp
    print(fib_list)


# palindrome check for Integers
def palindrome_check_integers(n):
    a, b = 0, 0
    temp = n
    while temp > 0:
        b = temp % 10
        a = a*10 + b
        temp = temp // 10
    print(a)
    if n == a:
        print(f"{n} is Palindrome")
    else:
        print(f"No {n} is Not a Palindrome")


# Write a program in Python to find sum of digits of a number
def sum_of_digits(n):
    a, b = 0, 0
    temp = n
    while temp > 0:
        b = temp % 10
        a += b
        temp = temp // 10
    print(a)


def average_using_loop(n):
    a, b, c = 0, 0, 0
    temp = n
    while temp > 0:
        b = temp % 10
        a += b
        temp = temp // 10
        c += 1
    average = a // c
    print(average)


# Python Program to calculate factorial using iterative method.
# Factorial of number 5 are 5 * 4 * 3 * 2 * 1
def factorial_of_number(n):
    a, b = 1, 1
    for i in range(a, n + 1):
        b *= i
    print(b)


# Python program to print provided number n is prime or not
def check_number_is_prime(n):
    status = False
    for i in range(2, n):
        if n % i == 0:
            status = True
            break
        status = False
    if status is False:
        print("Number is Prime Number")
    else:
        print("No the number is not at all prime number")


# Python program to print first n Prime Number with explanation.
# Prime numbers list 2,3,5,7,11,13, 17, 19
# It is only defined for the number which is greater than ‘1’.
# ‘2’ is the smallest prime number.
def print_first_n_prime_numbers(n, m):
    prime_list = []
    for i in range(n, m):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            prime_list.append(i)
    print(prime_list)


# Python Program to arrange list in Ascending Order (Sorting)
def arrange_list_ascending():
    list_to_arrange = [2, 44, 22, 55, 11, 66, 88, 9999, 4444, 5, 77]
    for i in range(len(list_to_arrange)):
        for j in range(i + 1, len(list_to_arrange)):
            if list_to_arrange[i]>= list_to_arrange[j]:
                list_to_arrange[i], list_to_arrange[j] = list_to_arrange[j], list_to_arrange[i]
    print(list_to_arrange)

# Python program for LCM of two number like for 8 and 26 LCM is 104
def lcm_of_two_numbers(n,m):
    counter = 2
    if n > m:
        largest = n
    else:
        largest = m
    while True:
        if largest % n == 0 and largest % m == 0:
            lcm = largest
            break
        largest += 1
    print(largest)


# Python program for HCF or GCP of two number like for 4 and 8 HCG is 2
def hcf_gcd_two_number(n,m):
    hcf = 1
    if n < m:
        smallest = n
    else:
        smallest = m

    for i in range(2, smallest + 1):
        if n % i == 0 and m % i == 0:
           hcf = i
           break
    print(hcf)


# Python program for the perfect number
'''A perfect number is a positive integer that is equal to the sum of its positive divisors, excluding the number itself.
Let’s understand it with an example
6 is a positive number and its divisor is 1,2,3'''
def perfect_number(n):
    list_divisors = []
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            list_divisors.append(i)
    print(list_divisors)
    for j in list_divisors:
        sum += j
    if n == sum:
        print("Its a perfect number")
    else:
        print("Its not at all a perfect one")


# In a given string, remove all the vowels and then trim the empty spaces on either side of the string
def string_remove_vowels_and_trim(n):
    vowels = "aeiouAEIOU"
    new_string = ""
    for i in n:
        if i in vowels:
            i = ""
        new_string += i
    print(new_string)


# Given two numbers, always print the last two digits of the product
def print_last_two_digit_of_product_two_numbers(n, m):
    product = n * m
    print(product % 100)


# Python Program to count all characters in string
def count_all_char_in_string(n):
    char_count = {}
    for i in n:
        if i != " ":
            if i in char_count:
                char_count[i] += 1
            else:
                char_count[i] = 1
    print(char_count)
    maximum = max(char_count.values())
    minimum = min(char_count.values())
    print(maximum, minimum)
    for key, value in char_count.items():
        if value == maximum:
            print(key)


# Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.
def replace_first_occurrence_vowel(n):
    new_string = ""
    vowels = "aeiou"
    for i in range(len(str(n))):
        if n[i] in vowels:
            new_string = n[:i] + "-" + n[i+1:]
            break
    print(new_string)


def slicing_negative_numbers():
    list = [1,3,5,6,7,8,11,14,18,19,20]
    print(list[-3:1:-2])


def matrix_using_triple_for_loop():
    x,y,z,n = 2,2,2,3
    for i in range(x + 1):
        for j in range(y + 1):
            for k in range(z + 1):
                if i + j + k != 3:
                    print([i, j, k])


def matrix_using_triple_for_loop_with_comprehension():
    x, y, z, n = 2, 2, 2, 3
    matrix = [[i, j, k] for i in range(x + 1) for j in range(y + 1) for k in range(z + 1) if i + j + k != n]
    print(matrix)


# Given the participants' score sheet for your University Sports Day, you are required to find the runner-up score. You are given  scores. Store them in a list and find the score of the runner-up.
# Program to find second runner up
def second_runner_up():
    n = int(input())
    arr = map(int, input().split())
    # My Solution without sorted function
    list_arr = list(arr)
    for i in range(len(list_arr)):
        for j in range(i + 1, len(list_arr)):
            if list_arr[i]>=list_arr[j]:
                list_arr[i],list_arr[j] = list_arr[j],list_arr[i]
    print(list_arr[-2])
    '''     # Actual Solution:
        list_arr = list(arr)
        arr1 = set(list_arr)
        arr2 = sorted(arr1)
        print(arr2[-2])'''


#Given the names and grades for each student in a class of  students, store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade, order their names alphabetically and print each name on a new line.
'''Sample Input 0
5
Harry
37.21
Berry
37.21
Tina
37.2
Akriti
41
Harsh
39'''
def second_lowest_grade_nested_list():
    nested_list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nested_list.append([name, score])
    sorting = sorted([value for key,value in nested_list])
    sorting2 = sorted(set([value for key,value in nested_list]))
    print(sorting2)
    minimum = sorting[0]
    maximum = sorting[-1]
    second_minimum = sorting[1]
    second_maximum = sorting[-2]
    print(minimum,second_minimum,maximum,second_maximum)
    answer_score = []

    for key,value in nested_list:
        if value == second_minimum:
            answer_score.append(key)
    sorted_answer_score = sorted(answer_score)
    print(answer_score)
    print(sorted_answer_score)
    for a in sorted_answer_score:
        print(a)

    '''Hacker rank solution
    alist = []
    for i in range(int(input())):
        name = input()
        score = float(input())
        alist.append([name, score])
    second_highest = sorted(set([score for name, score in alist]))[1]
    print('\n'.join(sorted([name for name, score in alist if score == second_highest])))'''


'''The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students. Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example




The query_name is 'beta'. beta's average score is (30 + 50 + 70) / 3 = 50.00.
Sample Input 0

3
Krishna 67 68 69
Arjun 70 98 63
Malika 52 56 60
Malika

Sample Output 0

56.00
'''
def dictionary_for_average_marks():
    ''' n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    print(student_marks)
    for key, value in student_marks.items():
        if query_name in key:
            avg = sum(value) / len(value)
            print(f"{avg:.2f}")'''

    # Hackers Rank Solution:
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    list_of_marks_for_queried = student_marks[query_name]
    avg = sum(list_of_marks_for_queried)/len(list_of_marks_for_queried)
    print('%.2f'% avg)
'''Task
The students of District College have subscriptions to English and French newspapers. Some students have subscribed only to English, some have subscribed to only French and some have subscribed to both newspapers.

You are given two sets of student roll numbers. One set has subscribed to the English newspaper, and the other set is subscribed to the French newspaper. The same student could be in both sets. Your task is to find the total number of students who have subscribed to at least one newspaper.
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

13
Explanation

Roll numbers of students who have at least one subscription:
 and . Roll numbers:  and  are in both sets so they are only counted once.
Hence, the total is  students.

'''

def union_of_set_newspaper_problem():
    english = int(input())
    english_subscription = list(map(int,input().split()))
    french = int(input())
    french_subscription = list(map(int,input().split()))
    print(len(set().union(english_subscription, french_subscription)))
    test_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 1, 2, 3, 11, 21, 55, 6, 8]
    print(set(test_list))

'''.intersection()
The .intersection() operator returns the intersection of a set and the set of elements in an iterable.
Sometimes, the & operator is used in place of the .intersection() operator, but it only operates on the set of elements in set.
The set is immutable to the .intersection() operation (or & operation).
Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8
Sample Output
5
'''
def intersection_of_set_newspaper_problem():
    english = int(input())
    english_subscriptions = set(map(int,input().split()))
    french = int(input())
    french_subscription = set(map(int,input().split()))
    both_subscription = english_subscriptions.intersection(french_subscription)
    print(len(list(both_subscription)))

'''.difference()
The tool .difference() returns a set with all the elements from the set that are not in an iterable.
Sometimes the - operator is used in place of the .difference() tool, but it only operates on the set of elements in set.
Set is immutable to the .difference() operation (or the - operation).

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output

4
'''
def difference_of_set_newspaper_problem():
    english = int(input())
    english_subscriptions = set(map(int,input().split()))
    french = int(input())
    french_subscription = set(map(int,input().split()))
    diff_subscription = english_subscriptions.difference(french_subscription)
    print(len(diff_subscription))

'''.symmetric_difference()
The .symmetric_difference() operator returns a set with all the elements that are in the set and the iterable but not both.
Sometimes, a ^ operator is used in place of the .symmetric_difference() tool, but it only operates on the set of elements in set.
The set is immutable to the .symmetric_difference() operation (or ^ operation).

Output Format

Output total number of students who have subscriptions to the English or the French newspaper but not both.

Sample Input

9
1 2 3 4 5 6 7 8 9
9
10 1 2 3 11 21 55 6 8

Sample Output
8

'''
def symmetric_difference_of_set_newspaper_problem():
    english = int(input())
    english_subscriptions = set(map(int,input().split()))
    french = int(input())
    french_subscription = set(map(int,input().split()))
    symmetric_diff_subscription = english_subscriptions.symmetric_difference(french_subscription)
    symmetric_update_diff_subscription = english_subscriptions.symmetric_difference_update(french_subscription)
    print(len(symmetric_diff_subscription))
    print(symmetric_update_diff_subscription)


'''We have seen the applications of union, intersection, difference and symmetric difference operations, but these operations do not make any changes or mutations to the set.

We can use the following operations to create mutations to a set:

.update() or |=
Update the set by adding elements from an iterable/another set.

>>> H = set("Hacker")
>>> R = set("Rank")
>>> H.update(R)
>>> print H
set(['a', 'c', 'e', 'H', 'k', 'n', 'r', 'R'])
.intersection_update() or &=
Update the set by keeping only the elements found in it and an iterable/another se
Input Format

The first line contains the number of elements in set .
The second line contains the space separated list of elements in set .
The third line contains integer , the number of other sets.
The next  lines are divided into  parts containing two lines each.
The first line of each part contains the space separated entries of the operation name and the length of the other set.
The second line of each part contains space separated list of elements in the other set.

 len(set(A)) 
 len(otherSets) 

Output Format

Output the sum of elements in set .

Sample Input

 16
 1 2 3 4 5 6 7 8 9 10 11 12 13 14 24 52
 4
 intersection_update 10
 2 3 5 6 8 9 1 4 7 11
 update 2
 55 66
 symmetric_difference_update 5
 22 7 35 62 58
 difference_update 7
 11 22 35 55 58 62 66
Sample Output

38
'''
def set_update_test():
    len_set = int(input())

    storage = set(map(int, input().split()))

    op_len = int(input())

    for i in range(op_len):
        operation = input().split()
        if operation[0] == 'intersection_update':
            temp_storage = set(map(int, input().split()))
            storage.intersection_update(temp_storage)
        elif operation[0] == 'update':
            temp_storage = set(map(int, input().split()))
            storage.update(temp_storage)
        elif operation[0] == 'symmetric_difference_update':
            temp_storage = set(map(int, input().split()))
            storage.symmetric_difference_update(temp_storage)
        elif operation[0] == 'difference_update':
            temp_storage = set(map(int, input().split()))
            storage.difference_update(temp_storage)
        else :
            assert False

    print(sum(storage))
# Set Mutations in python - Hacker Rank Solution END


'''Mr. Anant Asankhya is the manager at the INFINITE hotel. The hotel has an infinite amount of rooms.

One fine day, a finite number of tourists come to stay at the hotel.
The tourists consist of:
→ A Captain.
→ An unknown group of families consisting of  members per group where  ≠ .

The Captain was given a separate room, and the rest were given one room per group.

Mr. Anant has an unordered list of randomly arranged room entries. The list consists of the room numbers for all of the tourists. The room numbers will appear  times per group except for the Captain's room.

Mr. Anant needs you to help him find the Captain's room number.
The total number of tourists or the total number of groups of families is not known to you.
You only know the value of  and the room number list.

Input Format

The first line consists of an integer, , the size of each group.
The second line contains the unordered elements of the room number list.
Sample Input

5
1 2 3 6 5 4 4 2 5 3 6 1 6 5 3 2 4 1 2 5 1 4 3 6 8 4 3 1 5 6 2 
Sample Output

8
Explanation

The list of room numbers contains  elements. Since  is , there must be  groups of families. In the given list, all of the numbers repeat  times except for room number .
Hence,  is the Captain's room number.
'''
def find_captains_room():
    '''family_count = int(input())
    rooms_details = list(map(int, input().split()))
    members_count = 1
    room_members_count_details = {}
    for i in rooms_details:
        if i in room_members_count_details:
            room_members_count_details[i] += 1
        else:
            room_members_count_details[i] = 1
    for key, value in room_members_count_details.items():
        if value == 1:
            print(key)'''

    # Hackers rank solution
    N = input()
    ROOM_LIST = input().split()
    ROOM_SET = set(ROOM_LIST)
    print(ROOM_SET)
    for ele in list(ROOM_SET):
        ROOM_LIST.remove(ele)
    print(ROOM_LIST)
    CAPTAIN_ROOM_NUM = ROOM_SET.difference(set(ROOM_LIST)).pop()
    print(CAPTAIN_ROOM_NUM)

'''You are given two sets,  and .
Your job is to find whether set  is a subset of set .

If set  is subset of set , print True.
If set  is not a subset of set , print False.
Sample Input

3
5
1 2 3 5 6
9
9 8 5 6 3 2 1 4 7
1
2
5
3 6 5 4 1
7
1 2 3 5 6 8 9
3
9 8 2
Sample Output

True 
False
False
'''
def set_subset_A_B():
    boolean = True
    A_count = int(input())
    A = set(map(int, input().split()))
    B_count = int(input())
    B = set(map(int, input().split()))
    union = A.union(B)
    intersection = A.intersection(B)
    difference = A.difference(B)
    symmetric_diff = A.symmetric_difference(B)
    if len(list(A)) == len(intersection):
        print(boolean)
    else:
        boolean = False
        print(boolean)


    
'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print
'''
def list_operations_with_inputs():
    list = []
    list_items = int(input())
    for items in range(list_items):
        inputs = input().split()
        if inputs[0] == 'insert':
            list.insert(int(inputs[1]), int(inputs[2]))
        elif inputs[0] == 'print':
            print(list)
        elif inputs[0] == 'remove':
            list.remove(int(inputs[1]))
        elif inputs[0] == 'append':
            list.append(int(inputs[1]))
        elif inputs[0] == 'sort':
            list.sort()
        elif inputs[0] == 'pop':
            list.pop()
        elif inputs[0] == 'reverse':
            list.reverse()

    '''#Hacker Rank Solution:
    N = int(input())

    List=[]

    for i in range(N):

        command=input().split()

        if command[0] == "insert":

            List.insert(int(command[1]),int(command[2]))

        elif command[0] == "append":

            List.append(int(command[1]))

        elif command[0] == "pop":

            List.pop()

        elif command[0] == "print":

            print(List)

        elif command[0] == "remove":

            List.remove(int(command[1]))

        elif command[0] == "sort":

            List.sort()

        else:

            List.reverse()'''


################################################

'''Task
Given an integer, , and  space-separated integers as input, create a tuple, , of those  integers. Then compute and print the result of .

Note: hash() is one of the functions in the __builtins__ module, so it need not be imported.

Input Format

The first line contains an integer, , denoting the number of elements in the tuple.
The second line contains  space-separated integers describing the elements in tuple .

Output Format

Print the result of .

Sample Input 0

2
1 2
Sample Output 0

3713081631934410656
'''
def tuple_create_with_builtin_hash():
    '''n = int(input())
    integer_list = map(int, input().split())
    print(hash(tuple(integer_list)))'''

    # Hacker rank solution
    n = int(input())

    Tuple1 = map(int, input().split())

    t = tuple(Tuple1)

    print(hash(t))


'''You are given a 1-D array, . Your task is to print the ,  and  of all the elements of .

Note
In order to get the correct output format, add the line  below the numpy import.

Input Format

A single line of input containing the space separated elements of array .

Output Format

On the first line, print the  of A.
On the second line, print the  of A.
On the third line, print the  of A.

Sample Input

1.1 2.2 3.3 4.4 5.5 6.6 7.7 8.8 9.9
Sample Output

[ 1.  2.  3.  4.  5.  6.  7.  8.  9.]
[  2.   3.   4.   5.   6.   7.   8.   9.  10.]
[  1.   2.   3.   4.   6.   7.   8.   9.  10.]

'''
import numpy
def numpy_floor_ceil_rint():
    numpy.set_printoptions(sign=' ')
    n = numpy.array(input().split(),float)
    print(numpy.floor(n))
    print(numpy.ceil(n))
    print(numpy.rint(n))


'''Task

You are given a 2-D array with dimensions X.
Your task is to perform the  tool over axis  and then find the  of that result.

Input Format

The first line of input contains space separated values of  and .
The next  lines contains  space separated integers.

Output Format

Compute the sum along axis . Then, print the product of that sum.

Sample Input

2 2
1 2
3 4
Sample Output

24
'''
def numpy_by_axis_sum_prod():
    '''N,M = map(int, input().split())
    list_num_array = numpy.array([input().split() for i in range(N)], int)
    sum_axis0 = numpy.sum((list_num_array), axis=0)
    product_axis1 = numpy.product(sum_axis0, axis=0)
    print(sum_axis0)
    print(product_axis1)'''
    N,M = map(int, input().split())
    list_num_array = numpy.array([input().split() for i in range(N)], int)
    sum_axis0 = numpy.sum((list_num_array), axis=0)
    product_axis1 = numpy.product(sum_axis0, axis=0)
    print(product_axis1)


if __name__ == '__main__':
    n, palindrome, prime_number = 4, 2244884422, 43
    string = "And this is the new string to test vowelsu"
    #reverse_integer(n)
    #armstrong_number, not_armstrong = 153, 1224
    #armstrong_number_check(armstrong_number)
    #armstrong_number_check(not_armstrong)
    #fibonacci_series(8)
    #palindrome_check_integers(n)
    #palindrome_check_integers(palindrome)
    #sum_of_digits(n)
    #average_using_loop(n)
    #factorial_of_number(n)
    #check_number_is_prime(prime_number)
    #print_first_n_prime_numbers(100, 200)
    #arrange_list_ascending()
    #lcm_of_two_numbers(8,26)
    #hcf_gcd_two_number(4,12)
    #perfect_number(16)
    #string_remove_vowels_and_trim(string)
    #print_last_two_digit_of_product_two_numbers(12, 18)
    #count_all_char_in_string(string)
    #replace_first_occurrence_vowel(string)
    #slicing_negative_numbers()
    #matrix_using_triple_for_loop()
    #matrix_using_triple_for_loop_with_comprehension()
    #second_runner_up()
    #second_lowest_grade_nested_list()
    #dictionary_for_average_marks()
    #union_of_set_newspaper_problem()
    #intersection_of_set_newspaper_problem()
    #difference_of_set_newspaper_problem()
    #symmetric_difference_of_set_newspaper_problem()
    #set_update_test()
    #find_captains_room()
    #set_subset_A_B()
    #list_operations_with_inputs()
    #tuple_create_with_builtin_hash()
    #numpy_floor_ceil_rint()
    numpy_by_axis_sum_prod()
