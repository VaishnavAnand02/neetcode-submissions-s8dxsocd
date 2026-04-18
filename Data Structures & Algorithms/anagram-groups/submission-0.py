class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagram = {}

        for word in strs:
            sorted_word_key = "".join(sorted(word))

            if sorted_word_key not in anagram:
                anagram[sorted_word_key] = []

            anagram[sorted_word_key].append(word)

        return list(anagram.values())