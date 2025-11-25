def count(n: int) -> int:
    '''
    Recursive function to count the number of digits in a natural number.

    Args:
        n: Natural number (positive integer)

    Returns:
        Number of digits in the given number
    '''
    if n <= 0:
        print('Input must be a natural number (n > 0)')
        return None
    if n < 10:
        return 1
    return 1 + count(n//10)


def main():
    '''
        Main function to demonstrate the digit counting.
    '''
    n = int(input('Enter a natural number: '))
    print(count(n))

if __name__ == '__main__':
    main()



