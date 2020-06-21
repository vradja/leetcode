from collections import deque

class Solution:
    def flip(self, bit):
        if bit == 0:
            return 1
        else:
            return 0

    def minKBitFlips(self, bits, K):
        flips_needed = 0
        for window_start in range(len(bits)-K+1):
            if bits[window_start] == 0:
                if window_start + K - 1 < len(bits):
                    flips_needed += 1
                    for index in range(window_start, window_start + K):
                        bits[index] = self.flip(bits[index])
                else:
                    break
        return flips_needed if flips_needed != 0 else -1


sol = Solution()

# print(sol.minKBitFlips([0, 1, 0], 1))
# print(sol.minKBitFlips([0, 0, 0, 1, 0, 1, 1, 0], 3))
print(sol.minKBitFlips([1,1,0], 2))
# print(sol.minKBitFlips([1,1], 2))