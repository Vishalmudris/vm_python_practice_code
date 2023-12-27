# Python program to remove and count given character from String.

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


check_char_is_vowel_or_consonant("a")
check_char_is_vowel_or_consonant("b")
