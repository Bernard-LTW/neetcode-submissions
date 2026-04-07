class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in nums:
            if str(i) in count.keys():
                return True
            else:
                count[str(i)]=1
        return False

        