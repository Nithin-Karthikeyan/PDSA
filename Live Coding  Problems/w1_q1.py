from math import sqrt, ceil

def prime_product(m):
    # The number can only have 2 factors.
    # f1, f2 = None, None
    # count = 0
    # for i in range(2, sqrt(m)):
    #     if m%i != 0 and count != 2:
    #         pass
    #     elif count > 2:
    #         return False
    #     else:
    #         count += 1
    #         if f1 is None:
    #             f1 = i
    #         else:
    #             f2 = i
    if m < 0:
        return False
    factor_count = 0
    for i in range(2, m):
        if m%i == 0:
            factor_count += 1
    if factor_count == 2:
        print("PRIMEPROD")
        return True
    print("FALSE")
    return False

print(prime_product(9))