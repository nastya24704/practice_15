def search(a: list, x: int) -> int:
    '''
    Search for element x in list recursively.
    Return 1 if found, else 0.
    '''
    if not a:
        return 0
    elif a[0] == x:
        return 1
    else:
        return search(a[1:], x)

def main():
    a = []
    x = int(input())
    print(bool(search(a, x)))

if __name__ == "__main__":
    main()

