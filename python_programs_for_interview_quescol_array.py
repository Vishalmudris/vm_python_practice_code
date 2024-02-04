# Python program to find duplicates in an Array

def find_duplicated_number_in_array(arr_to_check):
    arr_updated = []
    for num in arr_to_check:
        if num in arr_updated:
            print(f"Number {num} is duplicate number")
        arr_updated.append(num)


find_duplicated_number_in_array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Write a program in Python for, How to find all pairs in array of integers whose sum is equal to given number.
# Like Input: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], target sum = 12


def find_pair_with_sum_given_number(arr_to_check):
    target_number = 11
    arr_updated_with_pair = []
    for num1 in range(len(arr_to_check)):
        for num2 in range(num1+1, len(arr_to_check)):
            if arr_to_check[num1] + arr_to_check[num2] == target_number:
                arr_updated_with_pair.append((arr_to_check[num1], arr_to_check[num2]))
    print(arr_updated_with_pair)


# find_pair_with_sum_given_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


def find_quadrant_with_sum_given_number(arr_to_check):
    target_number = 11
    arr_updated_with_pair = []
    for num1 in range(len(arr_to_check)):
        for num2 in range(num1+1, len(arr_to_check)):
            for num3 in range(num1+2, len(arr_to_check)):
                for num4 in range(num1+3, len(arr_to_check)):
                    if arr_to_check[num1] + arr_to_check[num2] + arr_to_check[num3] + arr_to_check[num4] == target_number:
                        arr_updated_with_pair.append((arr_to_check[num1], arr_to_check[num2], arr_to_check[num3], arr_to_check[num4]))
    print(arr_updated_with_pair)


# find_quadrant_with_sum_given_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])


# Write a program in Python for, How to compare two array is equal in size or not.

def compare_array_size(n1, n2):
    if len(n1) == len(n2):
        print("Array size is same")
    else:
        print("Array size is different")


# compare_array_size((1, 2, 3, 4), (5, 6, 7, 8, 9, 10))
# compare_array_size((1, 2, 3, 4), (5, 6, 7, 8))

# Write a program in Python to find largest and smallest number in array.


def find_largest_smallest_average_array(n1, n2):
    max_numer_n1, max_number_n2 = max(n1), max(n2)
    min_numer_n1, min_number_n2 = min(n1), min(n2)
    print(f"Smallest number in n1 is {min_numer_n1}, and Smallest number in n2 is {min_number_n2}")
    print(f"Largest number in n1 is {max_numer_n1}, and Largest number in n2 is {max_number_n2}")


# find_largest_smallest_average_array((11, 2222, 33, 444, 66, 88, 77, 99999), (555, 6666, 777777, 87887, 34523, 4565346432, 457346452353, 464645))

# Write a program in Python to find second highest number in an integer array.


def find_second_largest_smallest_number_array(n1, n2):
    sorted_numer_n1, sorted_number_n2 = sorted(n1), sorted(n2)
    min_numer_n1, min_number_n2 = sorted(n1, reverse=True), sorted(n2, reverse=True)
    print(f"Largest number in n1 is {min_numer_n1[1]}, and Largest number in n2 is {min_number_n2[1]}")
    print(f"Smallest number in n1 is {sorted_numer_n1[1]}, and Smallest number in n2 is {sorted_number_n2[1]}")


# find_second_largest_smallest_number_array((11, 2222, 33, 444, 66, 88, 77, 99999), (555, 6666, 777777, 87887, 34523, 4565346432, 457346452353, 464645))

# Python Program to find top two maximum and bottom two minimum number in array


def find_top_two_largest_smallest_number_array(n1, n2):
    sorted_number_n1, sorted_number_n2 = sorted(n1), sorted(n2)
    min_numer_n1, min_number_n2 = sorted(n1, reverse=True), sorted(n2, reverse=True)
    for largest in range(len(sorted_number_n1) - 1, 0, -1):
        if sorted_number_n1[largest] != sorted_number_n1[largest - 1]:
            print(f"Largest number in n1 is {sorted_number_n1[largest]}, and second Largest number in n1 is {sorted_number_n1[largest - 1]}")
            break
    for smallest in range(len(sorted_number_n1) + 1):
        if sorted_number_n1[smallest] != sorted_number_n2[smallest + 1]:
            print(f"Smallest number in n1 is {sorted_number_n1[smallest]}, and second Smallest number in n1 is {sorted_number_n1[smallest + 1]}")
            break


# find_top_two_largest_smallest_number_array((11, 2222, 33, 444, 66, 88, 77, 99999), (555, 6666, 777777, 87887, 34523, 4565346432, 457346452353, 464645))


# Python Program to remove duplicates from Array

def remove_duplicates_number_from_array(n1):
    updated_array_without_duplicates = []
    duplicates_number_array = []
    for num in n1:
        if num not in updated_array_without_duplicates:
            updated_array_without_duplicates.append(num)
        else:
            duplicates_number_array.append(num)
    print(updated_array_without_duplicates)
    print(duplicates_number_array)


# remove_duplicates_number_from_array((11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555))


# Python program to reverse an Array in two ways.


def reverse_array_two_ways(n1):
    reversed_array = []
    for num in range(len(n1)-1, -1, -1):
        reversed_array.append(n1[num])
    print(reversed_array)


# reverse_array_two_ways((11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555))


# Python Program to calculate length of an array.
def length_of_array(n1):
    print(len(n1))


# length_of_array((11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555))


# Python program to insert an element at end of an Array.
def insert_element_at_the_eng_of_array(n1):
    n1.append(1111)
    print(n1)


# insert_element_at_the_eng_of_array([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])


# Python program to insert element at a given location in Array.

def insert_element_in_between_array(n1):
    num_append, num_position = 888888888, 5
    if len(n1) >= num_position:
        print("Provided position is out of range")
    n1.insert(num_position, num_append)
    print(n1)


# insert_element_in_between_array([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])


def delete_element_in_between_array(n1):
    num_remove = 66
    if len(n1) >= num_remove:
        print("Provided position is out of range")
    n1.remove(num_remove)
    print(n1)


# delete_element_in_between_array([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])


def delete_element_from_index_using_pop(n1):
    num_remove_index = 0
    if len(n1) >= num_remove_index:
        print("Provided position is out of range")
    n1.pop(num_remove_index)
    print(n1)
    # For multiple indexes:
    array_number_remove_inedexes = [4, 6]
    for rem in array_number_remove_inedexes:
        if rem >= len(n1):
            print("Provided index is out of range")
        else:
            del n1[rem]
    print(n1)


# delete_element_from_index_using_pop([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])


def delete_element_end_of_array(n1):
    n1.pop(len(n1) - 1)
    print(n1)


# delete_element_end_of_array([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])


# Python Program to find sum of array elements.

def sum_of_array(n1):
    print(sum(n1))

# sum_of_array((11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555))


# Python Program to find sum of array elements using *args.

def sum_of_array_using_args(*args):
    print(args)
    print(sum(args[0]))

# sum_of_array_using_args([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])

# Python Program to find sum of array elements using user inputs.


def sum_of_array_user_input():
    array = []
    sum = 0
    size = int(input("Enter list of numbers : "))
    for num in range(size):
        elements = int(input("Enter numbers of the size : "))
        array.append(elements)
        sum += elements
    print(size)
    print(sum)
    print(array)


# sum_of_array_user_input()


# Python Program to print all even numbers in array.

def even_odd_numbers_array(n1):
    even_number_array = []
    odd_number_array = []
    for num in n1:
        if num % 2:
            odd_number_array.append(num)
        else:
            even_number_array.append(num)
    print(even_number_array)
    print(odd_number_array)


# even_odd_numbers_array((11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555))


# Python program to perform left rotation of array elements by two positions.
def left_rotation_by_two_elements_array(n1):
    array_for_left_rotation_by_two_elements = []
    for num in range(len(n1) - 1, -1, -2):
        array_for_left_rotation_by_two_elements.append(n1[num])
    print(array_for_left_rotation_by_two_elements)


# left_rotation_by_two_elements_array((11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555))


def left_rotation_by_two_elements_array_quescol(n1):
    for i in range(2):
        temp = n1[0]
        for j in range(len(n1)-1):
            n1[j] = n1[j+1]
        n1[-1] = temp
    print("After two left rotaion :", n1)

left_rotation_by_two_elements_array_quescol([11, 2222, 33, 444, 66, 88, 77, 99999, 2222, 33, 444, 55555, 6666666, 99999999, 55555])
