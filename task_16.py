def ten_to_n(x: int, n: int) -> str:
    '''
    Recursively converts a natural number x from decimal to base n (2 <= n <= 16) without using nested functions.
    '''
    digits = "0123456789ABCDEF"  
    if x < n:
        return digits[x]
    else:
        return ten_to_n(x // n, n) + digits[x % n]


def main():
    x = int(input())
    n = int(input())
    result = ten_to_n(x, n)
    print(result)


if __name__ == "__main__":
    main()
