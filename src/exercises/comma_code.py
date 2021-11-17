def comma_code(my_list):
    if len(my_list) < 2:
        return ''.join([str(item) for item in my_list])
    else:
        my_list[-1] = 'and ' + str(my_list[-1])
        return ', '.join([str(item) for item in my_list])

if __name__ == '__main__':
    spam = ['apples', 'bananas', 'tofu', 'cats']
    print(comma_code(spam))
    test_case = list(range(100))
    print(comma_code(test_case))