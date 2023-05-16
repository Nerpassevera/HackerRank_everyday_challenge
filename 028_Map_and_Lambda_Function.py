# The "Map and Lamda Functions": https://www.hackerrank.com/challenges/map-and-lambda-expression/problem
cube = lambda x: x ** 3  # complete the lambda function


def fibonacci(n):
    """Return a Fibonacci sequence with n components"""
    fibonacci_list = [0, 1, 1]
    while len(fibonacci_list) < n:
        fibonacci_list.append(fibonacci_list[-1]+fibonacci_list[-2])
    # return a list of fibonacci numbers
    return fibonacci_list
if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
