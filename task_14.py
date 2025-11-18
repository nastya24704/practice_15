def numbers(x: int) -> None:
    '''
    Print digits of x in reverse order.
    '''
    print(x % 10)
    if x >= 10:
        numbers(x // 10)

def main():
    x = int(input())
    print("Digits in reverse order:")
    numbers(x)

if __name__ == "__main__":
    main()

