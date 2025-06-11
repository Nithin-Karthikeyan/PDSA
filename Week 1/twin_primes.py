from math import sqrt

def is_prime(num):
    if num < 2:
        return False 
    for i in range(2, int(sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def twin_primes(n, m):
    # Declare variables
    primes_list = []
    twin_primes_list = []
    # Get all the primes between n and m, and put in a list
    for i in range(n, m+1):
        if is_prime(i):
            primes_list.append(i)

    print(f"Prime list: {primes_list}")
    prev_prime = primes_list[0]
    # check if adj elements have diff of 2
    for curr_prime in primes_list:
        if curr_prime-prev_prime == 2:
            twin_primes_list.append((prev_prime, curr_prime))
        prev_prime = curr_prime
    
    return twin_primes_list

n = int(input("Enter n: "))
m = int(input("Enter m: "))

print(twin_primes(n, m))

