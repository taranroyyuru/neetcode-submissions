from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for word in strs:
            chars = [0] * 26
            for j in word:
                chars[ord(j) - ord("a")] += 1
            res[tuple(chars)].append(word)
        return list(res.values())