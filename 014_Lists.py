if __name__ == '__main__':
    N = int(input())
    command = []
    for _ in range(N):
        command.append(input())
    my_list = []

    for i in command:
        if 'insert' in i:
            insert_command = i.split()
            my_list.insert(int(insert_command[1]), int(insert_command[2]))
        elif i == 'print':
            print(my_list)
        elif 'remove' in i:
            remove_command = i.split()
            my_list.remove(int(remove_command[1]))
        elif 'append' in i:
            append_command = i.split()
            my_list.append(int(append_command[1]))
        elif i == 'sort':
            my_list.sort()
        elif i == 'pop':
            my_list.pop()
        elif i == 'reverse':
            my_list.reverse()
        else:
            print(f'{i} command is unknown')
