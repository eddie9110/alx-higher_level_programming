#usr/bin/python3

def safe_print_list(value):
    try:
        print("{:d}".format(value))
        return True
    except Exception:
        return False
