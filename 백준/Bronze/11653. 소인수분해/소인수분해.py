import sys
read = sys.stdin.readline

N = int(read())

def prime_factors(n):
    factors = []
    i = 2
    while i<=n:
        if n%i==0:
            print(i)
            factors.append(i)
            n = n/i
        else:
            i = i+1
    return factors

output = prime_factors(N)

