class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dicts={}
        n = len(s)
        left = 0
        max_len,max_freq= 0,0

        for right in range(n):
            dicts[s[right]] = dicts.get(s[right],0) + 1 

            max_freq = max(max_freq,dicts[s[right]])

            win_len = right - left + 1

            while win_len - max_freq > k:
                dicts[s[left]] -=1
                left +=1
                win_len = right - left + 1

            max_len = max(win_len,max_len)

        return max_len
