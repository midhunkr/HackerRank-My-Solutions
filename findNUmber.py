def pickingNumbers(a):
    # get character counts (can use Counter from collections)
    cd = dict()
    for c in a:
        if c in cd:
            cd[c] += 1
        else:
            cd[c] = 1
    vals = sorted(cd.keys())
    print(cd)

    # current value
    cv = vals[0]
    mx = cd[vals[0]]
    
    # test the entire list of adjacent keys
    for v in vals[1:]:
        print(v)
        # result may be based on only 1 element count
        mx = max(mx, cd[v])
        print(mx)
        # check situation with 2 elements
        if v - cv == 1:
            mx = max(mx, cd[v]+cd[cv])
            print(mx)
        
        cv = v
        print(cv)
    return mx

ls=[1,2,2,3,1,2]
s=pickingNumbers(ls)
print(s)