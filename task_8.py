def fib(k: int) -> int:
    '''
    Recursive Fibonacci sequence.
    '''
    if k == 0:
        return 0
    elif k == 1:
        return 1
    else:
        return fib(k - 1) + fib(k - 2)

def main():
    k = int(input())
    result = fib(k)
    print(result)

if __name__ == "__main__":
    main()

