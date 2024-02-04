#!/bin/python3

import math
import os
import random
import re
import sys

def test_input(n):
    if n % 2 != 0:
        print("Weird")
    else:
        if n >= 20:
            print("Not Weird")
        elif n <= 5:
            print("Not Weird")
        else:
            print("Weird")


if __name__ == '__main__':
    test_input(17)
