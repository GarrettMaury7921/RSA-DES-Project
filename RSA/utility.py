"""
file: utility.py
author: Garrett Maury
"""
import random


def eea(r0, r1):
    """
    Pre-condition ro > r1 >=0
    :param r0: integer
    :param r1: integer
    :return: (gcd(r0, r1), s, t), where gcd(r0, r1) = s*r0 + t*r1
    """
    # r0 > r1
    # (r0, s0=1, t0=0), (r1, s1=0, t1=1), (r2, s2, t2)
    # using three formulas:
    # Q = r0 // r1
    # 1. r2 = r0-Q*r1
    # 2. s2 = s0-Q*s1
    # 3. t2 = t0 - Q * t1
    s0 = 1
    t0 = 0
    s1 = 0
    t1 = 1
    while True:
        if r1 == 0:
            # GCD, S, T
            return r0, s0, t0
        Q = r0 // r1
        r2 = r0 - Q * r1
        s2 = s0 - Q * s1
        t2 = t0 - Q * t1
        # update variables
        r0 = r1
        r1 = r2
        s0 = s1
        s1 = s2
        t0 = t1
        t1 = t2


def get_prime(bits, s):
    """
    Uses Miller Rabin primality test to generate a prime.
    You may use the random.randint() function.
    Do not use any built-in functions for generating prime numbers.
    :param bits: number of bits in generated primes
    :param s: security parameter
    :return: a probable prime of the length of the specified bits
    """

    # With the given number of bits, make a random number
    # Find the max number with given bits
    max_number = (2 ** bits) - 1

    while True:
        # Make random numbers until one is prime
        random_num = random.randint(1, max_number)

        # Small Prime Numbers
        if random_num == 1 or random_num == 2 or random_num == 3 or random_num == 5 or random_num == 7:
            return random_num

        else:
            p_minus_one = random_num - 1
            while p_minus_one % 2 == 0:
                p_minus_one //= 2

            # s is the security parameter
            for i in range(s):
                # Miller Rabin Primality Test
                # random_num^rand-1 % prime
                a = random.randint(2, random_num - 2)
                x = mod_pow(a, p_minus_one, random_num)

                # Check if prime
                if x == 1 or x == random_num - 1:
                    return random_num

                # Keep doing x^2, we are not checking if it is composite, we only want prime
                # when x == rand - 1 it's prime
                while p_minus_one != random_num - 1:
                    x *= x
                    x %= random_num
                    p_minus_one *= 2

                    if x == random_num - 1:
                        return random_num




def mod_pow(x, e, n):
    """
    Use the fast exponent algorithm to compute x^e mod n
    You are not allowed to use x**e or math.pow, or any other
    built-in function that may trivialize the given problem.
    :param x: base
    :param e: exponent
    :param n: modulus
    :return: x^e mod n
    """

    # Cannot do recursion as it takes too long

    # Take the modulus first so that we are in [0, n-1]
    x = x % n
    answer = 1

    # Binary exponentiation so the answer is when we get to 0 in the exponent
    while True:
        # Number is odd
        if e % 2 != 0:

            # Multiply and take modulus
            answer *= x
            answer %= n

        # Square without using functions and preform the modulus
        x *= x
        x %= n

        # Divide this until 0 so that we can do binary exponentiation
        e //= 2

        # If it's ever less than or equal to 0, break the loop
        if e <= 0:
            break

    return answer


if __name__ == "__main__":
    print(get_prime(100, 15))