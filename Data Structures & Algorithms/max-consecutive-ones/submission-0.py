class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maximum = 0
        cur = 0
        for digit in nums:
            if digit == 1:
                cur += 1
                maximum = max(cur,maximum)

            else:
                cur = 0

        return maximum
        