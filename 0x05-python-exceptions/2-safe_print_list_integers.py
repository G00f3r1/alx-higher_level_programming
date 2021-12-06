def safe_print_list_integers(my_list=[], x=0):
    index = 0

    for item in range(x):
        try:
            if type(my_list[item]) is int and index != x:
                print("{:d}".format(my_list[item]), end='')
                index += 1
        except TypeError:
            continue
    print()
    return index
