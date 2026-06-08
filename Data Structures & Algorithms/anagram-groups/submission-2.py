class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        ang = {}

        for i in strs:
            sorted_string =  "".join(sorted(i))

            ang.setdefault(sorted_string,[]).append(i)
            
        return list(ang.values())