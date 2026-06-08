class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left_product_array = [1]*n
        right_product_array = [1]*n
        res = [0]*n

        for i in range(1,n):
            left_product_array[i] = nums[i-1] * left_product_array[i-1]
        for j in range(n-2,-1,-1):
            right_product_array[j] = nums[j+1] * right_product_array[j+1]
        for i in range(n):
            res[i] = left_product_array[i] * right_product_array[i]

        return res

        