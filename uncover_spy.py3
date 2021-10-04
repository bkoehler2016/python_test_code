def uncover_spy(n, trust):
    if n==1 and trust==[]:
        return 1
    trustdict={}
    for t in trust:
        if t[1] not in trustdict.keys():
            trustdict[t[1]]=[t[0]]
        else:
            trustdict[t[1]].append(t[0])
    for k in trustdict.keys():
        if len(trustdict[k])==n-1 and k not in [n[0] for n in trust]:
            return k
    return -1
