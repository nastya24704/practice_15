def sum_progress(a1: float, r: float, n: int) -> float:
    '''
    Calculate the sum of the first n terms of an arithmetic progression recursively.
    :param a1: First term
    :param r: Common difference
    :param n: Number of terms
    :return: Sum of the first n terms
    '''
    if n == 0:
        return 0
    else:
        return sum_progress(a1, r, n - 1) + a1 + (n - 1) * r

def main():
    a1 = float(input())
    r = float(input())
    n = int(input())
    result = sum_progress(a1, r, n)
    print(result)

if __name__ == "__main__":
    main()
