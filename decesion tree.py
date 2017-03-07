def maxVal(w, v, i, aw):
    # print "maxVal called with", i, aw
    global numberCalls
    numberCalls = numberCalls + 1
    # print numberCalls,"times"
    if i == 0:
        if w[i] <= aw: return v[i]
        else: return 0
    without_i = maxVal(w, v, i - 1, aw)
    if w[i] > aw:
        return without_i
    else:
        with_i = v[i] + maxVal(w, v, i - 1, aw - w[i])
    return max(without_i, with_i)


def fastMaxVal (w, v, l, i, aw, al, m):
    global numberCalls
    numberCalls = numberCalls + 1
    try: return m[(i, aw)]
    except KeyError:
        if i == 0:
            if w[i] <= aw and l[i] <= al:
                m[(i, aw)] = v[i]
                return v[i]
            else:
                m[(i, aw)] = 0
                return 0
        without_i = fastMaxVal(w, v, l, i - 1, aw, al, m)
        if w[i] > aw or l[i] > al:
            m[(i, aw)] = without_i
            return without_i
        else:
            with_i = v[i] + fastMaxVal(w, v, l, i - 1, aw - w[i], al - l[i], m)
        res = max(without_i, with_i)
        m[(i, aw)] = res
        return res

def maxVal0(w, v, l, i, aw, al):
    m = {}
    return fastMaxVal(w, v, l, i, aw, al, m)

numberCalls = 0;
w = [2,4,4,5,6,2,4,3,4,3,5,1,3,5,1,3,2,3,4,1,2,2,4,4,5,6,2,4,3,2,4];
v = [7,8,5,9,9,4,7,8,5,9,9,4,8,3,8,5,9,5,6,9,5,6,8,5,7,5,5,8,3,1,5];
l = [2,4,4,5,6,2,4,3,4,3,5,1,3,5,1,3,2,3,4,1,2,2,4,4,5,6,2,4,3,2,4];


# res = maxVal(w, v, len(w) - 1, 35)
print "i:", len(w) - 1
# print "maxVal is", res, "called", numberCalls

numberCalls = 0;
res = maxVal0(w, v, l, len(w) - 1, 28, 50)
print "maxVal is", res, "called", numberCalls