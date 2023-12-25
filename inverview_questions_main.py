''''======================'''


# decorator function to convert to lowercase
def lowercase_decorator(function):
    def wrapper():
        func = function()
        string_lowercase = func.lower()
        return string_lowercase
    return wrapper
# decorator function to split words


def splitter_decorator(function):
    def wrapper():
        func = function()
        string_split = func.split()
        return string_split
    return wrapper


def first_letter_capital_decorator(function):
    def wrapper():
        new_func = function()
        return [i.capitalize() for i in new_func]
    return wrapper


def all_capital_decorator(function):
    def wrapper():
        caps_func = function()
        all_caps = caps_func.upper()
        update_list = [x for x in all_caps.split()]
        return update_list
    return wrapper


@splitter_decorator # this is executed next
@lowercase_decorator # this is executed first
def hello():
    return 'Hello World'


@first_letter_capital_decorator  # this is executed
@splitter_decorator # this is executed next
def beauty():
    return 'This Is The BeautY of the Decorators That We Need To Test'


@all_capital_decorator
def caps_letter():
    return "Convert all to the capitals"


#print(hello())
#print(beauty())
#print(caps_letter())

#### Complicated Decorator Example:
# Factorial program with memoization using
# decorators.

# A decorator function for function 'f' passed
# as parameter
memory = {}
def memoize_factorial(f):
    def inner(num):
        if num not in memory:
            memory[num] = f(num)
            print('result saved in memory')
        else:
            print('returning result from saved memory')
        return memory[num]

    return inner


@memoize_factorial
def facto(num):
    if num == 1:
        return 1
    else:
        return num * facto(num-1)

#print(facto(5))
#print(facto(5))
# directly coming from saved memory


'''======================'''
#Multiple Iterators comprehensions:
#Comprehensions allow for multiple iterators and hence, can be used to combine multiple lists into one.


# Functionality of zip:
# For list:

def zip_for_list_return_tuples_list():
    first = ["a", "b", "c", "d"]
    second = [8, 88, 888, 8888]
    print(list(zip(first, second)))


def zip_for_set_return_tuples_dict():
    first_number_list = {2, 22, 222, 2222}
    second_number_list = {4, 44, 444, 4444}
    print(list(zip(first_number_list,second_number_list)))


#zip_for_set_return_tuples_dict()

# List Comprehension #

my_list = [2, 3, 5, 7, 11, 13, 16, 20]


def sq_rt_comp_list():
    square_root_comprehension = [x**2 for x in my_list]
    return square_root_comprehension


#sq_rt_comp_list()


def sq_rt_comp_list_even():
    square_root_comprehension = [x**2 for x in my_list if x%2 == 0]
    return square_root_comprehension


def sq_rt_comp_dict():
    square_root_comprehension_dict = {x:x**2 for x in my_list}
    return square_root_comprehension_dict


def sq_rt_comp_dict_even():
    square_root_comprehension_dict = {x: x**2 for x in my_list if x % 2 != 0}
    return square_root_comprehension_dict


def multiple_iterator_list_using_zip_comprehension1():
    a = [1, 2, 3]
    b = [7, 8, 9]
    only_zip = zip(a, b)
    print(list(only_zip))
    multiple_iterator = [(x + y) for (x, y) in zip(a, b)]  # parallel iterators
    print(multiple_iterator)
    #for x, y in zip(a, b):
    #    print(x, y)


#multiple_iterator_list_using_zip_comprehension1()


def multiple_iterator_dict_using_zip_comprehension1():
    a = [1, 2, 3]
    b = [7, 8, 9]
    for x, y in zip(a, b):
        print({x: y})


#multiple_iterator_dict_using_zip_comprehension1()


#Flattening a multi-dimensional list

#A similar approach of nested iterators (as above) can be applied to flatten a multi-dimensional list or work upon its inner elements.
def multiple_dimensional_list_zip_comprehension1():
    my_multi_dimension_list = [[10, 20, 30], [40, 50, 60], [70, 80, 90]]
    tupled_list = [(x, y, z) for x, y, z in my_multi_dimension_list]
    single_for_list = [x for x in my_multi_dimension_list]
    flattened_list = [x for temp in my_multi_dimension_list for x in temp]
    #flattened_tuple = [(x, y, z) for a, y, z in my_multi_dimension_list for x in a]
    print(tupled_list)
    print(single_for_list)
    print(flattened_list)
    #print(flattened_tuple)


#multiple_dimensional_list_zip_comprehension1()

# Lambda Function with wrapper:
def lamda_first():
    x = lambda a, b, c: a + b + c
    print(x(5, 6, 2))


#lamda_first()


def lambda_with_wrapper(n):
    return lambda a: a * n


double_wrapper = lambda_with_wrapper(2)
triple_wrapper = lambda_with_wrapper(3)

#print(double_wrapper(20))
#print(triple_wrapper(20))

# Difference between Def and Lambda


def cube_number(n):
    n = n*n*n
    return n


lambda_cube = lambda n: n*n*n


#print(f"value return with def function is {cube_number(5)}")
#print(f"value return with Lambda function is {lambda_cube(5)}")

# Learning range python:


def learn_range(n):
    for i in range(n):
        print(i)


#learn_range(10)


def learn_range_increment(n):
    for i in range(n):
        i = i + 1
        return i


#print(learn_range_increment(10))


def learn_range_from_to(x, y, z):
    for i in range(x, y, z):
        print(i)


#learn_range_from_to(1, 8, 2)


def learn_range_from_to_return(x, y, z):
    for i in range(x, y, z):
        return i


#print(learn_range_from_to_return(1, 8, 2))


def learn_range_from_to_return_increment(x, y, z):
    for i in range(x, y, z):
        i = i + 1
        return i


#print(learn_range_from_to_return_increment(1, 8, 2))


#=====================================
#Iter Items
class ArrayList:
   def __init__(self, number_list):
       self.numbers = number_list
   def __iter__(self):
       self.pos = 0
       return self
   def __next__(self):
       if(self.pos < len(self.numbers)):
           self.pos += 1
           return self.numbers[self.pos - 1]
       else:
           raise StopIteration
array_obj = ArrayList([1, 2, 3])
new_list = [1,2,3,4,5,6,7,8]
#it = iter(array_obj)
it = iter(new_list)
#print([it.__next__(), it.__next__(), it.__next__(), it.__next__()])
#print(next(it)) #output: 2
#print(next(it)) #output: 3
#Throws Exception
#Traceback (most recent call last):
#...
#StopIteration
#==================================


'''Generators with Fibonacci series '''


def generator_with_fibonacci(n):
    a, b = 0, 1
    while(a < n):
        yield b
        a, b = b, a+b


x = generator_with_fibonacci(8)
for n in generator_with_fibonacci(8):
    pass
    #print(n)

list_fib_comprehension = [n for n in generator_with_fibonacci(8)]
#print(list_fib_comprehension)


def fib(n):
   p, q = 0, 1
   while(p < n):
       yield p
       p, q = q, p + q
x = fib(10)    # create generator object

## iterating using __next__(), for Python2, use next()
x.__next__()    # output => 0
x.__next__()    # output => 1
x.__next__()    # output => 1
x.__next__()    # output => 2
x.__next__()    # output => 3
x.__next__()    # output => 5
x.__next__()    # output => 8
#x.__next__()    # error

## iterating using loop
for i in fib(10):
    pass
    #print(i)    # output => 0 1 1 2 3 5 8
list_fin_new_comprehension = [n for n in fib(10)]
#print(list_fin_new_comprehension)


####==============================================####
#Program for Split and Join string:
def string_split_join():
    test_string = "This is a test string to test how split and Join work"
    split_string = test_string.split()
    #print(split_string)
    #print("+ : +".join(split_string))


string_split_join()


####==============================================####
####Program for *args and **kwargs ####
'''*args
    *args is a special syntax used in the function definition to pass variable-length arguments.
    “*” means variable length and “args” is the name used by convention. You can use any other.

**kwargs

    **kwargs is a special syntax used in the function definition to pass variable-length keyworded arguments.
    Here, also, “kwargs” is used just by convention. You can use any other name.
    Keyworded argument means a variable that has a name when passed to a function.
    It is actually a dictionary of the variable names and its value.  '''


def for_args_and_kwargs(*args, **kwargs):
    for arg in args:
        pass
        #print(arg)
    for key, value in kwargs.items():
        pass
        #print(key, value)


for_args_and_kwargs("hi", "hello", "how", "are", "you", cricket="sachin", cricker="virat",  football1="messi", football2="ronaldo")

####==============================================####
####Program for Positive and Negative Array ####


def positive_negative_array():
    array_list = [1, 2, 3, 4, "Vishal", "Mudris"]
    #print(f"First and Last Number of array are {array_list[0]} and {array_list[-1]}")
    #print(f"Fourth and Last fourth Number of array are {array_list[3]} and {array_list[-4]}")


#positive_negative_array()


####=====================================================####
#CLASS Examples

class Person:
    def __new__(cls, *args, **kwargs):
        print("Creating new persons object")
        instance = super().__new__(cls)
        return instance

    def __init__(self, *args, **kwargs):
        self.employeename = args
        self.emloyeeage = kwargs.get("age")
        self.employeecity = kwargs.get("city")

    def for_module_in_class(self):
        print(f"this is the module method inside the class to check {self.employeename}, {self.emloyeeage}, {self.employeecity}")


#person = Person()
person1 = Person("name", "student", "scope", age=10, city="city")
person2 = Person("Vishal", "secondargs",age=40, city="Bhopal")

person_module_in_class_person1 = person1.for_module_in_class()
person_module_in_class_person2 = person2.for_module_in_class()






#comprehensive_list = [n for n in x]
#print(comprehensive_list)
#print(sq_rt_comp_list())
#print(sq_rt_comp_dict())
#print(sq_rt_comp_list_even())
#print(sq_rt_comp_dict_even())
