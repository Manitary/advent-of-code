from aocd import get_data, submit
from itertools import chain, cycle, accumulate, count

DAY = 20
YEAR = 2015

data = get_data(day=DAY, year=YEAR)

# Divisor function taken from https://rosettacode.org/wiki/Factors_of_an_integer
def prime_powers(n):
    """Generator function of all prime power divisors of n"""
    # c goes through 2, 3, 5, then the infinite (6n+1, 6n+5) series
    for c in accumulate(chain([2, 1, 2], cycle([2, 4]))):
        if c * c > n:  # Check up to sqrt(n)
            break
        if n % c:  # Skip non-divisors
            continue
        d, p = (), c
        while not n % c:
            n, p, d = (
                n // c,
                p * c,
                d + (p,),
            )  # Find all the powers of c dividing n, and store them in d. Divide n by the maximum power of c that divides it.
        yield d
    if n > 1:
        yield (n,)  # Yield whatever is left (e.g. if n is prime)


def factors(n):
    """List of factors of n, sorted by primes involved in the factorisation"""
    r = [1]
    for e in prime_powers(n):
        r += [
            a * b for a in r for b in e
        ]  # For each new prime power divisor p^k of n, add to the list all the possible combinations of products q_1^a_1 * ... * q_m^a_m for other primes q_i < p
    return r


m = int(data)
ans1, ans2 = None, None

for i in count():
    f = factors(i)
    if (not ans1) and 10 * sum(f) >= m:
        ans1 = i
    if not ans2:
        ans = 0
        for d in sorted(factors(i), reverse=True):
            if d * 50 >= i:
                ans += d * 11
            else:
                break
        if ans >= m:
            ans2 = i
            break

submit(ans1, part="a", day=DAY, year=YEAR)
submit(ans2, part="b", day=DAY, year=YEAR)
