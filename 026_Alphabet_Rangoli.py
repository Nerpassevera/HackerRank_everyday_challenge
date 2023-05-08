# The "Alphabet Rangoli" tsak: https://www.hackerrank.com/challenges/alphabet-rangoli/problem

import string


def print_rangoli(size):
    """this function prints an alphabet rangoli of given size."""
    pattern = string.ascii_lowercase[size-1:0:-1]+string.ascii_lowercase[0:size]
    center_line = '-'.join(pattern)
    # Printing of upper part of the pattern
    for i in range(1, size):
        left_upper = center_line[0: i*2 - 1]
        right_upper = center_line[0: i*2 - 2]
        print(str(left_upper+right_upper[::-1]).center(len(center_line), '-'))
    # Printing the central row
    print(center_line)
    # Printing the bottom part of the pattern
    for i in range(size-1, 0, -1):
        left_bottom = center_line[0: i*2 - 1]
        right_bottom = center_line[0: i*2 - 2]
        print(str(left_bottom+right_bottom[::-1]).center(len(center_line), '-'))


if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)

