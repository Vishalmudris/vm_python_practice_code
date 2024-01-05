# Python program to remove and count given character from String.
import os
'''Input String: Quescol

Input Character : e

Output: Quscol (After removing ‘e’) '''


def remove_and_count_char_from_string():
    test_string = "This is the test string need to first count and then remove all s from the string"
    count = 0
    char = "s"
    char_list = {}
    for i in range(len(test_string)):
        if test_string[i] == char:
            count += 1
    test_string = test_string.replace(char, "( Removed )")
    print(f"Count of s in the string is {count} and the new test string is {test_string}")


# remove_and_count_char_from_string()


# Python program to count all characters in program.

'''Input String: teststring
count t = 2, s = 2 rest 1
 '''


def count_all_characters_count_in_string():
    test_string = "This is the test string need to first count and then remove all s from the string"
    count = 0
    char_list = {}
    for i in test_string:
        if i in char_list:
            char_list[i] += 1
        else:
            char_list[i] = 1
    print(f"Count of characters in the list is {char_list} in the test string")


# count_all_characters_count_in_string()

# Python Program to check if two Strings are Anagram.
'''Two strings can be called Anagram if the same character with the same occurrence, present in both string. 
In this case position of characters not matters.
For eg:  “quescol” and “colsque” both strings are anagram. 
As you can see here, both the string have same character with same time of occurrence at different position and it is an anagram.
But if we take another example like “love” and “like”.
In the both string only two character ‘l’ and ‘e’ are common and rest are not. So this two strings are not an anagram'''


def test_string_is_anagram():
    test_string1 = "stringtest"
    test_string2 = "teststringz"
    sorted_string1 = sorted(test_string1)
    print(sorted_string1)
    sorted_string2 = sorted(test_string2)
    print(sorted_string2)
    if sorted_string1 == sorted_string2:
        print(f"strings {test_string1} and {test_string2} are Anagram strings")
    else:
        print(f"strings {test_string1} and {test_string2} are not at all Anagram strings")


# test_string_is_anagram()


# python program to check given character is a vowel ( a, e, i, o, u) or any other alphabet other than vowels(consonant) .

def check_char_is_vowel_or_consonant(char):
    vowel_list = ["a", "e", "i", "o", "u"]
    if char in vowel_list:
        print(f"Input character {char} is vowel")
    else:
        print(f"Input char {char} is not a vowel")


# check_char_is_vowel_or_consonant("a")
# check_char_is_vowel_or_consonant("b")


# Python program to check provided input is Integar or String.
def check_string_or_int(n):
    get_type = type(n)
    if get_type is int:
        print(f"The provided input {n} is Integer")
    elif get_type is float:
        print(f"The provided input {n} is Float")
    else:
        print(f"The provided input {n} is String")


# check_string_or_int(9)
# check_string_or_int(9.99)
# check_string_or_int("test")


# Python program to check given character is digit or not.
# Digit are the number between 0-9.
def check_digit(n):
    if 0 <= n <= 9:
        print(f"The provided input {n} is digit")
    else:
        print(f"The provided input {n} is not a digit")


# check_digit(9)
# check_string_or_int(999)


# Python program to check given character is digit or not using isdigit() method.
def check_digit_using_ifdigit(n):
    if str(n).isdigit():
        print(f"The provided input {n} is digit")
    else:
        print(f"The provided input {n} is not a digit")


# check_digit_using_ifdigit(9)
# check_digit_using_ifdigit(999)


# Python program to replace the string space with a given character using replace().

def replace_space_with_character(n):
    string_to_update = "Replace the space with the given character"
    print(string_to_update.replace(" ", n))


# replace_space_with_character("-REPLACED-")

# Python program to replace the string space with a given character using Iterator


def replace_space_with_character_using_iterator():
    string_to_update = "Replace the space with the given character using iterator"
    updated_string = ""
    for n in string_to_update:
        if n == ' ':
            n = "-REPLACED-ITERATOR-"
        updated_string += n
    print(updated_string)


# replace_space_with_character_using_iterator()

# Python Program to Convert lowercase to uppercase character

def lower_to_upper_case_characters(n):
    print(n.upper())
    print(n.lower())


# lower_to_upper_case_characters("String to convert to Upper Case")

def lower_to_upper_by_quescol(n):
    upper_char_string = ""
    for char in n:
        if char.islower():
            char = char.upper()
        upper_char_string += char
    print(upper_char_string)


# lower_to_upper_by_quescol("String to convert to Upper Case")


def lower_to_upper_case_vowels(n):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for char in n:
        if char in vowels:
            char = char.upper()
        new_string += char
    print(new_string)


# lower_to_upper_case_vowels("String to convert to upper case")


# Python Program to Convert lowercase vowel to uppercase using replace()

def lower_to_upper_case_vowels_using_replace(n):
    vowels = ["a", "e", "i", "o", "u"]
    new_string = ""
    for char in n:
        if char in vowels:
            new_char = char.upper()
            n = n.replace(char, new_char)
    print(n)


# lower_to_upper_case_vowels_using_replace("String to convert to upper case")

# Python program to remove vowels from the string

def remove_vowels_from_string_using_replace(n):
    vowels = ("aeiou")
    for char in n:
        if char in vowels:
            n = n.replace(char, "")
    print(n)


# remove_vowels_from_string_using_replace("String to convert to upper case")


def remove_vowels_from_string_normal(n):
    vowels = ("aeiou")
    new_string = ""
    for char in n:
        if char in vowels:
            char = ""
        new_string += char
    print(new_string)


# remove_vowels_from_string_normal("String to convert to upper case")

# Python program to count the Occurrence Of Vowels & Consonants in a String.


def count_vowels_and_consonants(n):
    vowels = ("aeiouAEIOU")
    vowels_count = 0
    consonant_count = 0
    for char in n:
        if char in vowels:
            vowels_count += 1
        else:
            consonant_count += 1
    print(f"Total number of vowels are {vowels_count} and consonant are {consonant_count}")


# count_vowels_and_consonants("String to count to vowels and consonants in this line")


# Python program to print the highest frequency character in a String.

def find_highest_frequency_character_in_string(n):
    letters_count_dict = {}
    for char in n:
        if char in letters_count_dict:
            letters_count_dict[char] += 1
        else:
            letters_count_dict[char] = 1
    max_frequency_char = max(letters_count_dict.values())
    print(letters_count_dict)
    print(max_frequency_char)
    for key, value in letters_count_dict.items():
        if value == max_frequency_char:
            print(key)


# find_highest_frequency_character_in_string("Stringtocounttovowelsandconsonantsinthislineandfindhighestfreq")


# Python program to Replace First Occurrence Of Vowel With ‘-‘ in String.

def replace_first_occurrence_vowel_with_hiphen(n):
    vowels = ("aeiouAEIOU")
    for char in range(len(n)):
        print(char)
        if n[char] in vowels:
            print(n[char])
            print(n[:char])
            print(n[char+1:])
            n = n[:char] + '-' + n[char+1:]
            break
    print(n)


# replace_first_occurrence_vowel_with_hiphen("Stringtocounttovowelsandconsonantsinthislineandfindhighestfreq")

# Python program to count alphabets, digits, special characters and spaces.

def calculate_alphabets_digits_special_character_spaces(n):
    char_count = 0
    digit_count = 0
    spaces_count = 0
    special_character_count = 0
    for char in n:
        if char.isalpha():
            char_count += 1
        elif char.isdigit():
            digit_count += 1
        elif char == " ":
            spaces_count += 1
        else:
            special_character_count += 1
    print(f"In the provided string character count is {char_count}, digit count is {digit_count}, spaces count is {spaces_count} and special character count is {special_character_count}")


# calculate_alphabets_digits_special_character_spaces("$# 1) String to count to alphabest, 2) digits, 3) special characters means !@#$%^&* and spaces in this line*&")


# Python program to separate characters in a given string.

def separate_characters_from_string(n):
    updated_string = ""
    for char in n:
        char = char + "\n"
        updated_string += char
    print(updated_string)


# separate_characters_from_string("Program to separate the characters from the string")


# Python program to remove blank space from string.
def remove_spaces_from_string(n):
    string_without_spaces = ""
    for char in n:
        if " " in char:
            char = ""
        string_without_spaces += char
    print(string_without_spaces)


# remove_spaces_from_string("Program to remove spaces from the provided string")


# Python program to concatenate two strings using join() method.

def concatenate_using_join_function(*args):
    concatenate_string = ""
    concatenate_string += " ".join(args)
    print(concatenate_string)


concatenate_using_join_function("Program", "To", "Concatenate", "All", "Strings")


# Python program to concatenate two strings without using join() method.
def concatenate_all_the_args(*args):
    concatenated_string = ""
    for arg in args:
        concatenated_string += " " + arg
    print(concatenated_string)


# concatenate_all_the_args("Program", "To", "Concatenate", "All", "Strings")

