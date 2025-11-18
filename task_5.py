def mod_number(a: int, b: int) -> int:
    '''
    Compute a mod b using recursion.
    :param a: Dividend
    :param b: Divisor
    :return: Remainder of division
    '''
    if a < b:
        return a
    else:
        return mod_number(a - b, b)

def main():
    a = 17
    b = 5
    result = mod_number(a, b)
    print(result)

if __name__ == "__main__":
    main()
