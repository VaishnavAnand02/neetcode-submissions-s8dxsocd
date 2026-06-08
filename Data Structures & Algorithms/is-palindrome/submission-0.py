class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = "".join([x for x in s if x.isalnum()])
        s = s.lower()
        return s == s[::-1]