def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            # if left[i] == right[j]:
            #     result.append(left[i])
            #     i = i + 1
            #     j = j + 1
            # else:
            result.append(left[i])
            i = i + 1
        else:
            result.append(right[j])
            j = j + 1
    while i < len(left):
        result.append(left[i])
        i = i + 1
    while j < len(right):
        result.append(right[j])
        j = j + 1
    return result

def mergeSort(L):
    print L
    if len(L) < 2:
        return L[:]
    else:
        middle = len(L) / 2
        left = mergeSort(L[:middle])
        right = mergeSort(L[middle:])
        together = merge(left, right)
        print "merged", together
        return together

L = [12, 34134, 123, 34, 12321, 345, 12, 31, 234, 423, 453, 55, 22, 12, 312, 123, 52];
mergeSort(L)
