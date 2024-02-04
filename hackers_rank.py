def is_leap(year):
    leap = False

    if len(str(year)) == 4 and year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                leap = True
            else:
                leap = False
        else:
            leap = True
    return leap

#year = int(input())
#print(is_leap(year))




if __name__ == '__main__':
    n = int(input())
    list = ""
    for k in range(1, n + 1):
        print(k, end='')


