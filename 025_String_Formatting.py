# The "Strinf Formatting" task: https://www.hackerrank.com/challenges/python-string-formatting/problem


def print_formatted(number):
    identetion = len("{0:b}".format(number))

    for i in range(1, number + 1):
        print('{0:d}'.format(i).rjust(identetion),
              '{0:o}'.format(i).rjust(identetion),
              '{0:X}'.format(i).rjust(identetion),
              '{0:b}'.format(i).rjust(identetion),
              sep=' ')


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)
