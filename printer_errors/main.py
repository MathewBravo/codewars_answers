from re import error


def printer_error(s):
    charstr='abcdefghijklmnopqrstuvwxyz'
    error_count = 0
    for i in s:
        if charstr.index(i) > 12:
            error_count += 1
    return "{err}/{len}".format(err = error_count, len = len(s))



if __name__ == "__main__":
    s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    if printer_error(s) == "3/56":
        print("t1 pass")
    else:
        print("t1 fail")
    s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz"
    if printer_error(s) == "6/60":
        print("t2 pass")
    else:
        print("t2 fail")
    s = "kkkwwwaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyzuuuuu"
    if printer_error(s) == "11/65":
        print("t3 pass")
    else:
        print("t3 fail")
