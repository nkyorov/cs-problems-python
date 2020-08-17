def binary_search(sequence, key): 
    low = 0
    high = len(sequence) - 1

    while low <= high:
        mid = (low + high) // 2

        if sequence[mid] < key:
            low = mid + 1
        elif sequence[mid] > key:
            high = mid - 1
        else:
            return True
    else:
        return False
