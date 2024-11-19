"""
Author: Garrett Maury 2023
"""


class FeistelNetwork:
    """
    FeistelNetwork consists of 16 rounds.
    Each round performs identical operations.
    """
    # Initialize lookup tables
    Expansion = [
        [32, 1, 2, 3, 4, 5],
        [4, 5, 6, 7, 8, 9],
        [8, 9, 10, 11, 12, 13],
        [12, 13, 14, 15, 16, 17],
        [16, 17, 18, 19, 20, 21],
        [20, 21, 22, 23, 24, 25],
        [24, 25, 26, 27, 28, 29],
        [28, 29, 30, 31, 32, 1]
    ]

    SBoxes = [
        [
            [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7],
            [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
            [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0],
            [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]
        ],
        [
            [15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10],
            [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
            [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15],
            [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]
        ],
        [
            [10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8],
            [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
            [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7],
            [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]
        ],
        [
            [7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15],
            [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
            [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4],
            [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]
        ],
        [
            [2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9],
            [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
            [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14],
            [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]
        ],
        [
            [12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11],
            [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
            [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6],
            [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]
        ],
        [
            [4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1],
            [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
            [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 8, 0, 5, 9, 2],
            [6, 11, 13, 8, 1, 4, 10, 7, 9, 5, 0, 15, 14, 2, 3, 12]
        ],
        [
            [13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7],
            [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
            [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8],
            [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]
        ]
    ]

    PPermutation = [
        [16, 7, 20, 21, 29, 12, 28, 17],
        [1, 15, 23, 26, 5, 18, 31, 10],
        [2, 8, 24, 14, 32, 27, 3, 9],
        [19, 13, 30, 6, 22, 11, 4, 25],
    ]


    @staticmethod
    def iterate(inputstring, subkeys):
        """
        The main part of DES encryption
        In each round, left-half of the input is XORed with the output
        of the f function, and then the two halves are swapped.
        :param inputstring: 64-bit output of IP
        :param subkeys: an array of 16 subkeys
        :return: a 64-bit string generated after round 16.
        """
        count = 0
        while count < 16:
            # Get both halves of the string
            first_half, second_half = inputstring[:len(inputstring) // 2], inputstring[len(inputstring) // 2:]

            # Do the F function and grab the result of it for XOR
            f_func = FeistelNetwork.fFunction(second_half, subkeys[count])

            # DO THE XOR with both values (need both)
            xor_result = FeistelNetwork.xor(first_half, f_func)

            # New input string is second half as L1, XOR result is R1
            inputstring = second_half + xor_result

            # Increment the counter
            # print("COUNTER: " + str(count))
            # print("ROUND " + str(count) + ": " + str(inputstring))
            count += 1

        # On the last round, swap them!
        return xor_result + second_half


    @staticmethod
    def fFunction(r, key):
        """
        F function - expands r from 32-bit to 48-bit. The result is XORed
        with the key. That result is divided into 8 6-bit blocks and fed into
        8 different substitution boxes that each output 4-bit blocks. The 8
        4-bit blocks are combined to be 32-bit and fed into permutation P
        :param r: - 32-bit right half of the input used for this round
        :param key: - 48-bit subkey used for this round
        :return: a 32-bit string generated
        """

        # Go through the f function
        expandedStr = FeistelNetwork.expansion(r)
        xorStr = FeistelNetwork.xor(expandedStr, key)
        sboxStr = FeistelNetwork.sBoxes(xorStr)
        permutedStr = FeistelNetwork.pPermutation(sboxStr)

        return permutedStr
    

    @staticmethod
    def xor(firstInput, secondInput):
        """
        Performs the XOR operation between 2 equal length strings
        :param firstInput: - first string to XOR
        :param secondInput: - second string to XOR
        :return: resulting string of the XOR operation
        """
        output = ""

        # Iterate over the chars, lengths are the same (doesn't matter what we choose)
        for characters in range(len(firstInput)):
            firstValue = int(firstInput[characters])
            secondValue = int(secondInput[characters])

            # XOR in a nutshell
            newValue = firstValue + secondValue
            if newValue == 2:
                newValue %= 2
            output += str(newValue)

        # print("XOR: " + output)
        return output

    @staticmethod
    def expansion(r):
        """
        Expand 32-bit input to 48-bit result
        :param r: right half of the input to expand
        :return: a 48-bit string
        """

        # For Reference
        '''
        Expansion = [
            [32, 1, 2, 3, 4, 5],
            [4, 5, 6, 7, 8, 9],
            [8, 9, 10, 11, 12, 13],
            [12, 13, 14, 15, 16, 17],
            [16, 17, 18, 19, 20, 21],
            [20, 21, 22, 23, 24, 25],
            [24, 25, 26, 27, 28, 29],
            [28, 29, 30, 31, 32, 1]
        ]
        '''
        # Make the length 48
        r = str(r)
        r = r.ljust(48)

        expandedStr = ""
        for i in range(8):
            for j in range(6):
                # Return the permuted string of bits
                expandedStr += r[FeistelNetwork.Expansion[i][j] - 1]
                expandedStr = expandedStr.strip()

        # print("EXPANSION: " + expandedStr)
        return expandedStr
    

    @staticmethod
    def sBoxes(inputString):
        """
        Divide the 48-bit input into 8 6-bit blocks and feed those blocks into
        8 different substitution boxes that each output 4-bit blocks. The 8
        4-bit blocks are combined to be a 32-bit string
        :param input: - 48-bit string to feed into the S-boxes
        :return: a 32-bit string; combined outputs of the S-boxes
        """

        # Make the length 48
        inputString = str(inputString)
        inputString = inputString.ljust(48)
        index = 0
        sixbit = 6
        output = ""
        output = output.ljust(32)

        # We need 8 6-bit blocks
        for i in range(8):
            # Get the 6 bit block
            sixbitblk = inputString[index:index + sixbit]

            # Get the Rows
            row1 = sixbitblk[0]
            row2 = sixbitblk[5]
            row = row1 + row2
            row = row.strip()
            # Put into base10
            row_base10 = int(row, 2)

            # Get the Columns
            col = sixbitblk[1:5]

            # Put into base10
            col_base10 = int(col, 2)

            # Put everything into the s boxes
            s_box_result_base10 = FeistelNetwork.SBoxes[i]
            s_box_result_base10 = s_box_result_base10[row_base10][col_base10]

            # Convert to binary
            s_box_result = format(s_box_result_base10, '04b')

            output += s_box_result
            output = output.strip()

            # Increment the index
            index += sixbit

        # print("SBOXES: " + output)
        return output
    

    @staticmethod
    def pPermutation(inputString):
        """
        Permutes 32-bit input using the P permutation table
        :param input: - 32-bit string to feed into the P permutation table
        :return: a 32-bit string
        """

        # For reference
        '''
        PPermutation = [
        [16, 7, 20, 21, 29, 12, 28, 17],
        [1, 15, 23, 26, 5, 18, 31, 10],
        [2, 8, 24, 14, 32, 27, 3, 9],
        [19, 13, 30, 6, 22, 11, 4, 25],
        ]
        '''
        permutedStr = ""

        # i = rows, j = columns
        for i in range(4):
            for j in range(8):
                # Similar to the other ones again
                permutedStr += inputString[FeistelNetwork.PPermutation[i][j] - 1]

        # print("PERMUTATION: " + permutedStr)
        return permutedStr
