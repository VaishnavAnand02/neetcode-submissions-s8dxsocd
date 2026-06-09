class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        res = []
        for i in range(n-2):

            if i>0 and nums[i] == nums[i-1]:
                continue

            lp = i+1
            rp = n-1

            required_sum = 0 - nums[i]

            while lp < rp:
                if nums[lp] + nums[rp] == required_sum:
                    res.append([nums[i],nums[lp],nums[rp]])
                    lp += 1
                    rp -= 1

                    while lp < rp and nums[lp] == nums[lp-1]:
                        lp +=1
                    while lp<rp  and nums[rp] == nums[rp+1]:
                        rp -= 1

                elif nums[lp] + nums[rp] < required_sum:
                    lp+=1
                else:
                    rp-=1
        
        return res