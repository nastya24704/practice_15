def is_prime_helper(x: int, divisor: int) -> bool:
    '''
    Helper for prime check, recursive.
    '''
    if divisor * divisor > x:
        return True
    elif x % divisor == 0:
        return False
    else:
        return is_prime_helper(x, divisor + 1)

def function1(x: int) -> int:
    '''
    Returns 1 if x is prime, else 0.
    '''
    if x < 2:
        return 0
    return 1 if is_prime_helper(x, 2) else 0

def main():
    x = int(input())
    result = function1(x)
    print(bool(result))

if __name__ == "__main__":
    main()
