from collections import defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        hashmap = defaultdict(list)
        output = []
        visit = set()
        cycle = set()

        for crs, pre in prerequisites:
            hashmap[crs].append(pre)
        
        def dfs(crs):
            if crs in cycle:
                return False
            if crs in visit:
                return True
            
            cycle.add(crs)
            for pre in hashmap[crs]:
                if dfs(pre) == False:
                    return False
            
            cycle.remove(crs)
            visit.add(crs)
            output.append(crs)
        
        for crs in range(numCourses):
            if dfs(crs)== False:
                return []
        return output
        