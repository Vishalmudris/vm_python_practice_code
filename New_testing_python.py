def fibonacci_by_yield(n):
    a, b = 0, 1
    while a < n:
        yield a
        a, b = b, a + b


#x = fibonacci_by_yield(11)
#fib_list_by_yield = [i for i in x]
#print(fib_list_by_yield)


def fibonacci_by_iterator(n):
    a, b = 0, 1
    fib_series = []
    for i in range(n):
        fib_series.append(a)
        a, b = b, a + b
    print(fib_series)


fibonacci_by_iterator(11)


def reverse_function(n):
    reverse, a = 0, 0
    temp = n
    while temp > 0:
        reverse = temp % 10
        a = a * 10 + reverse
        temp = temp // 10
    print(a)


# reverse_function(1234)


