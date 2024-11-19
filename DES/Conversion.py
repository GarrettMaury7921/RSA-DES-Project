class Conversion:
    """
    The Conversion class provides two utility functions for string conversion:
    1. strToBits - converts a text of 8 characters to a binary string pf 64-bits
    2. bitsToStr - inverse operation of strToBits
    """
    @staticmethod
    def strToBits(s):
        """
        Converts a text of 8 characters to 64-bits
        :param s: a string of 8 characters e.g. "ABCD-xyz"
        :return: a string of 64 bits e.g. "0100...."
        """
        result = ''.join([bin(ord(c))[2:].rjust(8, '0') for c in s])
        # Each byte has 8 bits, checking to make sure the conversion is correct
        assert(len(result) == len(s) * 8), "Conversion is incorrect"
        return result


    @staticmethod
    def bitsToStr(bits):
        """
        Converts a binary string of 64-bits to a text of 8 characters
        :param bits: A string of 64-bits e.g. "01000001..."
        :return: A string of 8-characters  e.g. "ABCD-xyz"
        """
        assert(len(bits) == 64), "The length of the parameter bit-string must be 64"
        result = ''.join([chr(int(c, 2)) for c in [bits[idx : idx + 8] for idx in range(0, len(bits), 8)]])
        assert(len(result) * 8 == len(bits)), "Conversion is incorrect"
        return result