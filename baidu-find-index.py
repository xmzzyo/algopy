def find_index(A):
    """ A: list of integers，升序排列
    	find an index i: A[i] == i
    """
    l, r = 0, len(A)
    res = []
    while l < r:
        mid = l + (r - l) // 2
        if A[mid] == mid:
            res.append(mid)
        if A[mid] < mid:
            l = l + 1
        if A[mid] > mid:
            r = mid - 1

    if len(res) > 0:
        return res
    return -1