class IP:
    """
    IP - Initial Permutation
    The first operation of DES encryption
    """
    InitialPermutation = [
        [58, 50, 42, 34, 26, 18, 10, 2],
        [60, 52, 44, 36, 28, 20, 12, 4],
        [62, 54, 46, 38, 30, 22, 14, 6],
        [64, 56, 48, 40, 32, 24, 16, 8],
        [57, 49, 41, 33, 25, 17, 9, 1],
        [59, 51, 43, 35, 27, 19, 11, 3],
        [61, 53, 45, 37, 29, 21, 13, 5],
        [63, 55, 47, 39, 31, 23, 15, 7]
    ]


    @staticmethod
    def permute(bits):
        """
        Use the lookup table to produce permuted bits
        pre-condition: input is a binary string of 64-bits
        :param bits: a String of 64 bits
        :return: permuted string of 64 bits
        """

        output = ""

        # Block size of 64
        for i in range(8):
            for j in range(8):
                # Return the permuted string of bits
                output += bits[IP.InitialPermutation[i][j] - 1]
        # print("IP: " + str(output))
        return output
