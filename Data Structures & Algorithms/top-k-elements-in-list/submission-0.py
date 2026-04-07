class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        bucket ={}

        for i in nums:
            bucket[i] = bucket.get(i, 0) + 1

        a = []
        for num, count in bucket.items():
            a.append([count,num])

        a.sort()

        output=[]
        while len(output)<k:
            output.append(a.pop()[1])
        
        return output
        
        