#usr/bin/python3

def safe_print_list_integers(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
