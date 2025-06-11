def Goldbach(n):
    primes_list = []
    goldbach_list = []
    # get a list of all primes before n
    for i in range(2, n):
        if is_prime(i):
            primes_list.append(i)

    for p in primes_list:
        q = n-p
        if q in primes_list and q >= p:
            goldbach_list.append((p,q))
    return goldbach_list

    
    # iterate thru list to get the sum
    
def is_prime(n):
    for i in range(2, n):
        if n%i == 0:
            return False
    return True

n=int(input())
print(sorted(Goldbach(n)))