#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        index = 0
        while index < x:
            print("{:d}".format(my_list[index]), end="")
            nb_print += 1
            index += 1
    except (ValueError, TypeError):
        pass
    finally:
        print()
    return nb_print
