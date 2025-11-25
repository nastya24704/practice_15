def combin(n: int, k: int) -> int:
    """
    Recursive calculation of binomial coefficient C(n, k).
    """
    if k == 0 or k == n:
        return 1
    return combin(n - 1, k - 1) + combin(n - 1, k)

def main():
    n = int(input())
    k = int(input())
    print(combin(n, k))

if __name__ == "__main__":
    main()
