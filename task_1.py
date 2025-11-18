def pownum(a: float, n: int) -> float:
    """
    Recursive function to calculate the power of a real number.

    Args:
        a: Base number (real number)
        n: Exponent (natural number)

    Returns:
        The result of a raised to the power of n

    Raises:
        RecursionError: If n is too large (exceeds recursion depth)
    """
    if n == 1:
        return a
    return a * pownum(a, n - 1)


def main() -> float:
    """
    Main function to get user input and calculate power.

    Returns:
        Result of the power calculation or None if input is invalid
    """
    a = float(input('Enter a real number: '))
    n = int(input('Enter a natural number: '))

    if n <= 0:
        print('Exponent must be a natural number, please enter n > 0')
        return None
    print(pownum(a, n))


if __name__=='__main__':
    main()

