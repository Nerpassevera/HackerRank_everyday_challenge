# Enter your code here. Read input from STDIN. Print output to STDOUT
m, n = map(int, input().split())


def door_mat(height, width):
    """Prints the pattern for the door mat with defined height and width"""
    print(*(((i + 1)*'.|.').center(width, '-') for i in range(0, height - 1, 2)), sep='\n')  # Printing the upper part
    print('WELCOME'.center(width, '-'))  # Printing the center line
    print(*(((i - 1)*'.|.').center(width, '-') for i in range(height - 1, 0, -2)), sep='\n')  # Printing the bottom part

door_mat(m, n)
