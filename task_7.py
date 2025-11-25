def nod(a: int, b: int) -> int:
    '''
    Compute GCD of a and b recursively.
    '''
    if b == 0:
        return a
    return nod(b, a % b)

def main():
    a = int(input())
    b = int(input())
    print(nod(a, b))

if __name__ == "__main__":
    main()

