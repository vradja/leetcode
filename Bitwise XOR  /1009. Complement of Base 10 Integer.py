# Approach 1.
def calculate_bitwise_complement_1(num):
    bitcount = 0
    temp_num = num

    # this step, we left shit the number till it becomes zero. At each shift, we increment bitcount.
    # This gives total number of bits in the number
    while temp_num:
        bitcount += 1
        # temp_num = temp_num >> 1
        temp_num >>= 1

    # now that we found the number of bits in num, we make all of them 1's
    # using power of 2
    all_ones_bits = pow(2, bitcount) - 1 if bitcount > 0 else 1  # IMPORTANT IF ELSE CONDITION HERE. all_ones_bits will
    # become 0 if bitcount is 0. if num is 0, then bitcount is zero and hence all_ones_bits becomes 0. We manually set
    # all_ones_bits to 1 to find the complement.

    return num ^ all_ones_bits


# Merge approach 1 into single loop.
def calculate_bitwise_complement(num):
    if num == 0: return 1  # IMPORTANT base condition. Do not miss

    bit, temp_num = 1, num

    # Here, xor each bit that is moved left by num for bitcount times.
    while temp_num:
        num ^= bit
        bit <<= 1  # moves bit to the left
        temp_num >>= 1  # moves right till bitcount or num becomes 0

    return num


def main():
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(8)))
    print('Bitwise complement is: ' + str(calculate_bitwise_complement(10)))


main()
