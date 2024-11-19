"""
Includes DES encryption and decryption algirithms
"""
from KeySchedule import *
from IP import *
from FeistelNetwork import *
from IPinverse import *

class DES:

    @staticmethod
    def encrypt(x, key):
        """
         DES encryption algorithm
         :param x: 64-bit plaintext
         :param key: 64-bit key
         :return: 64-bit encrypted text
         """
        subkeys = KeySchedule.generateSubkeysForEncryption(key)
        initialPermutedOutput = IP.permute(x)
        FeistelOutput = FeistelNetwork.iterate(initialPermutedOutput,subkeys)
        finalOutput = IPinverse.permute(FeistelOutput)
        return finalOutput


    @staticmethod
    def decrypt(y, key):
        """
        DES decryption algorithm
        :param y: 64-bit ciphertext
        :param key: 64-bit key
        :return: 64-bit decrypted text
        """
        subkeys = KeySchedule.generateSubkeysForDecryption(key)
        initialPermutedOutput = IP.permute(y)
        FeistelOutput = FeistelNetwork.iterate(initialPermutedOutput, subkeys)
        finalOutput = IPinverse.permute(FeistelOutput)
        return finalOutput