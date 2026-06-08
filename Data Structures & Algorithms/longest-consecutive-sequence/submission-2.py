class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        num_set = set(nums)
        long_streak = 0

        for i in nums:

            if i-1 not in nums:
                current_num = i
                current_streak = 1

                while current_num+1 in num_set:
                    current_num = current_num + 1
                    current_streak +=1

                long_streak = max(current_streak,long_streak)

        return long_streak