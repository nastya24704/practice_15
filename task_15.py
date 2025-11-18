def ten_to_bin(x: int) -> str:
    '''
    Recursively converts the decimal number x to its binary representation as a string without using an auxiliary function.
    '''
    if x == 0:
        return '0'
    if x == 1:
        return '1'
    return ten_to_bin(x // 2) + str(x % 2)

def main():
    x = int(input())
    print(ten_to_bin(x))

if __name__ == "__main__":
    main()
