def mod_number(a: int, b: int) -> int:
    '''
    Compute a mod b using recursion.
    :param a: Dividend
    :param b: Divisor
    :return: Remainder of division
    '''
    if a < b:
        return a
    return mod_number(a - b, b)

def main():
    a = int(input())
    b =  int(input())
    print(mod_number(a, b))

if __name__ == '__main__':
    main()
