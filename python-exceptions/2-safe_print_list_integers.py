#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    nb_print = 0
    try:
        for item in my_list[:x]:
            if isinstance(item, int):
                print("{:d}".format(item), end="")
                nb_print += 1
    except (IndexError):
        pass
    finally:
        print()
    return nb_print
