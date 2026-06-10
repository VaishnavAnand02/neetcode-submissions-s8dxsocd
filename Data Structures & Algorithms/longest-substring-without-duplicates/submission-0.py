class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_len = 0 
        left = 0
        char_set = set()
        
        for right in range(n):
            
            while s[right] in char_set:
                char_set.remove(s[left])
                left+=1

            char_set.add(s[right])

            curr_window_len = right-left + 1
            max_len = max(max_len,curr_window_len)

        return max_len