class Solution:

    def alpha_count(self, string):
        output  = [0]*26
        for char in string:
            output[(ord(char)-97)] += 1
        return str(output)


    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count = {}

        for i in strs:
            if self.alpha_count(i) in count.keys():
                count[self.alpha_count(i)] += [i]
            else:
                count[self.alpha_count(i)] = [i]

        output = []
        for j in count.values():
            output.append(j)

        return output