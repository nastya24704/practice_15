def progress(a1: float, r: float, n: int) -> float:
    '''
    Calculate the nth term of an arithmetic progression recursively.
    :param a1: First term of the progression
    :param r: Common difference
    :param n: Term number
    :return: nth term value
    '''
    if n == 1:
        return a1
    else:
        return progress(a1, r, n - 1) + r

def main():
    a1 = float(input())
    r = float(input())
    n = int(input())
    result = progress(a1, r, n)
    print(result)

if __name__ == "__main__":
    main()
