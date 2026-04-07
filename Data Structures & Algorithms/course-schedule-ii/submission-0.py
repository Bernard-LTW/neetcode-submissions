class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        hashmap = {i:[] for i in range(numCourses)}
        for i in prerequisites:
            crs, pre = i
            hashmap[crs] = hashmap.get(crs,[])+[pre]

        visited = set()
        output = []

        def dfs(i):
            if i in visited:
                return False

            if hashmap[i] == []:
                if i not in output:
                    output.append(i)
                return True

            visited.add(i)

            for cours in hashmap[i]:
                if not dfs(cours):
                    return False
            
            visited.remove(i)
            hashmap[i] = []
            if i not in output:
                output.append(i)
            return True
        
        for i in range(numCourses):
            if not dfs(i):return []
        
        return output
                    
                