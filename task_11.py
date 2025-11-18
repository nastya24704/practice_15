def ind_maxlist(a: list, index: int = 0) -> int:
    '''
    Recursively find index of max element in list.
    '''
    if len(a) == 1:
        return index
    else:
        max_idx_rest = ind_maxlist(a[1:], index + 1)
        return index if a[index] > a[max_idx_rest] else max_idx_rest

def main():
    a = []
    idx = ind_maxlist(a)
    print(idx)

if __name__ == "__main__":
    main()

