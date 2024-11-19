"""
file name: rsa.py
author: Garrett Maury
"""

import random
import utility
import sys


def key_generation(bits, s):
    """
    Use the utility functions you wrote to generate RSA keys
    :param bits: the number of bits in n
    :param s: security parameter
    :return: (n,e,d), where (n,e) is a public key and d is a private key
    """
    p = utility.get_prime(bits, s)
    q = utility.get_prime(bits, s)
    print("p=" + str(p))
    print("q=" + str(q))

    # n and phi_n
    n = p * q
    phi_n = (p - 1) * (q - 1)

    # Other variables
    d = 0
    e = 0

    # print("n=" + str(n))
    # print("phi_n=" + str(phi_n))

    # Do a loop until gcd(e, phi_n) = 1
    # Compute a value for d so that (d * e) % phi_n = 1
    gcd = 0
    while gcd != 1 or (d <= 0) or (d * e) % phi_n != 1:
        e = random.randint(1, phi_n - 1)
        gcd, d, t = utility.eea(e, phi_n)
        # print(d)

    # Return all of the keys
    return n, e, d


def encrypt(x, e, n):
    """
    Use the mod_pow function to encrypt x
    :param x: plaintext
    :param e: public key
    :param n: public key
    :return: x^e mod n
    """

    # print(str(x) + " ^ " + str(e) + " % " + str(n))
    y = utility.mod_pow(x, e, n)

    return y


def decrypt(y, d, n):
    """
    Use the mod_pow function to decrypt y
    :param y: ciphertext
    :param d: private key
    :param n: public key
    :return: y^d mod n
    """

    # print(str(y) + " ^ " + str(d) + " % " + str(n))
    x = utility.mod_pow(y, d, n)

    return x


def main():
    """
    Test RSA key generation, encryption, and decryption.
    :return: None
    """
    (n, e, d) = key_generation(100, 15)
    print("public keys: (", n,",", e,")")
    print("private key:", d)
    x = int(sys.argv[1])
    print("x =", x)
    y = encrypt(x, e, n)
    print("y =", y)
    z = decrypt(y, d, n)
    print(z == x)


if __name__ == "__main__":
    main()

