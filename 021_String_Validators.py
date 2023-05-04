if __name__ == '__main__':
    s = input()

    def validation(string, method):
        print(any(getattr(symbol, method)() for symbol in string))

    validation(s, 'isalnum')
    validation(s, 'isalpha')
    validation(s, 'isdigit')
    validation(s, 'islower')
    validation(s, 'isupper')
