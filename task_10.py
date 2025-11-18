def maxlist(a: List[int]) -> int:
    '''
    Recursively find the maximum element in a list.
    '''
    if len(a) == 1:
        return a[0]
    else:
        max_rest = maxlist(a[1:])
        return a[0] if a[0] > max_rest else max_rest

def main():
    a = []
    result = maxlist(a)
    print(result)

if __name__ == "__main__":
    main()

