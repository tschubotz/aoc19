
def could_be_pw(x):
    if len(str(x)) != 6:
        return False

    str_x = str(x)
    i0 = int(str_x[0])
    i1 = int(str_x[1])
    i2 = int(str_x[2])
    i3 = int(str_x[3])
    i4 = int(str_x[4])
    i5 = int(str_x[5])
    if not (i0 == i1 or i1 == i2 or i2 == i3 or i3 == i4 or i4 == i5):
        return False

    if not (i0 <= i1 and i1 <= i2 and i2 <= i3 and i3 <= i4 and i4 <= i5):
        return False

    if i0 == i1 and i1 != i2:
        print(x)
        return True

    if i1 == i2 and (i0 != i1 and i2 != i3):
        print(x)
        return True

    if i2 == i3 and (i1 != i2 and i3 != i4):
        print(x)
        return True

    if i3 == i4 and (i2 != i3 and i4 != i5):
        print(x)
        return True

    if i4 == i5 and i4 != i3:
        print(x)
        return True

    return False


def main():
    start = 145852
    end = 616942


    n = 0
    for i in range(start, end + 1):
        if could_be_pw(i):
            n += 1
    print(n)

if __name__ == '__main__':
    main()