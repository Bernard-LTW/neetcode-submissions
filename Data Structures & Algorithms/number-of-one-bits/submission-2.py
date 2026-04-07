class Solution:
    def hammingWeight(self, n: int) -> int:
        out = 0
        rem = n
        while rem != 0:
            out += rem%2
            rem = rem // 2

        return out
        