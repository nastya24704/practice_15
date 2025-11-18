def degree5(n: int) -> int:
    '''
    Find the exponent of 5 in the prime factorization of n.
    Returns -1 if 5 is not a factor.
    '''
    if n == 1:
        return 0
    elif n % 5 != 0:
        return -1
    else:
        res = degree5(n // 5)
        if res >= 0:
            return res + 1
        else:
            return -1

def main():
    n = int(input())
    result = degree5(n)
    print(result)

if __name__ == "__main__":
    main()

