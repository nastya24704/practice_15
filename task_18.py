def simmetr(s: str, i: int, j: int) -> bool:
    '''
    Checks if substring s[i:j+1] is a palindrome recursively.
    '''
    if i >= j:
        return True
    elif s[i] != s[j]:
        return False
    else:
        return simmetr(s, i + 1, j - 1)

def main():
    s = input()
    i, j = 0, len(s) - 1
    result = simmetr(s, i, j)
    print(result)

if __name__ == "__main__":
    main()
