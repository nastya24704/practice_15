def odd_list(a: list, n: int) -> list:
    '''
    Return list of even numbers from first n elements of a.
    '''
    if n == 0:
        return []
    else:
        result = odd_list(a, n - 1)
        if a[n - 1] % 2 == 0:
            result.append(a[n - 1])
        return result

def main():
    a = []
    n = len(a)
    print(odd_list(a, n))

if __name__ == "__main__":
    main()

