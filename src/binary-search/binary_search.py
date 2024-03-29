

def binary_search(n, item) -> int:
    left, right= 0, len(n)
    while right > left:
        middle = (left + right) // 2
        if item[middle] > n:
            right = middle
        elif item[middle] <= n:
            left = middle + 1
        else:
            return left
    return None