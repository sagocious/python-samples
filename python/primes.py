def primes():
    [x for x in range(2, 20)
         if all(x % y != 0 for y in range(2, x))] [x for x in range(2, 20) if all(x % y != 0 for y in range(2, x))]

print primes(1000000)
