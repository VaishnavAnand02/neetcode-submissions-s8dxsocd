class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        vals_seen  = {}
        n = len(nums)
        for i in range(0,n):
            
            comp = target - nums[i]

            if comp in vals_seen:
                
                return [vals_seen[comp],i]

            vals_seen[nums[i]] = i

        return []