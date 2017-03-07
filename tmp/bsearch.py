def bserach(s, e, first, last, calls):
    print first, last, calls
    if (last-first) < 2 :return last == s or first == s
    mid = first + (last - first)/2
    if mid == s: return True
    if mid > s: return bserach(s, e, first, mid - 1, calls + 1)
    return bserach(s, e, mid + 1, last, calls + 1)

def serach(s, e):
    print bserach(s, e, 0, e, 1)

serach(200,1000000)