from collections import defaultdict
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        hashmap = defaultdict(list)

        def dfs(node, target, visited):
            if node == target:
                return True
            visited.add(node)
            for nei in hashmap[node]:
                if nei not in visited:
                    if dfs(nei, target, visited):
                        return True
            return False
        
        for a, b in edges:
            if dfs(a ,b , set()):
                return [a,b]
            hashmap[a].append(b)
            hashmap[b].append(a)                 



            


        
        