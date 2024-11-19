"""
Main simulation engine.
Do not modify class/method names used in supplied code.
Usage: python3 DES_Simulation plaintext.txt key.txt
"""

from DES import *
from Conversion import *
import sys

def main():
    if len(sys.argv) != 3:
        print("Usage: python3 DES_Simulation.py <plaintext file> <key file>")
        print("Example: python3 DES_Simulation.py plaintext.txt key.txt")
        return
    
    plaintextFile = sys.argv[1]
    keyFile = sys.argv[2]
    key = open(keyFile).readline().strip()
    plaintext = open(plaintextFile).readline().strip()

    x = Conversion.strToBits(plaintext)
    y = DES.encrypt(x, key)
    print("ciphertext: {}".format(y))

    decrypted = DES.decrypt(y, key)
    print("Successful" if decrypted == x else "Failed")
    recoveredText = Conversion.bitsToStr(decrypted)
    print("recovered Text: {}".format(recoveredText))

if __name__ == '__main__':
    main()
