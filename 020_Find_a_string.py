def count_substring(string, sub_string):
    counter = 0
    for i in range(len(string)):
        if string[i] == sub_string[0]:
            if string.find(sub_string, i, i+len(sub_string)+1) > -1:
                counter+=1
    return counter

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
