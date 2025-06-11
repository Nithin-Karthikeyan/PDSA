def odd_one(L):
    # loop thru the list with the first element
    # p = L[0]
    # count = 0
    # for i in range(1, len(L)):
    #     if type(p) == type(L[i]):
    #         count += 1
    #     if type(p) != type(L[i+1]):

    l = [type(t) for t in L]
    l_set_list = list(set([type(t) for t in L]))
    t1 = l_set_list[0]
    t2 = l_set_list[1]
    count_t1 = l.count(t1)

    if count_t1 == 1:
        if t1 == type(420):
            return "int"
        elif t1 == type("kadvule ajithey"):
            return "str"
        elif t1 == type(6.9):
            return "float"
        else:
            return "bool"
    else:
        if t2 == type(420):
            return "int"
        elif t2 == type("kadvule ajithey"):
            return "str"
        elif t2 == type(6.9):
            return "float"
        else:
            return "bool"
    
    # check its data type with the others
    # if one match, then not odd
    # if one also dont match, then odd

print(odd_one([1,2,3,5,"str"]))