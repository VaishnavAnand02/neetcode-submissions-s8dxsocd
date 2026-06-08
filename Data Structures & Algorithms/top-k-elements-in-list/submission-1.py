class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        val_count = {}
        ans= []
        for i in nums:
            
            if i in val_count:
                count =  val_count.get(i)
                val_count.update({i:count+1})
            else:
                val_count[i] = 1

        val_count =  sorted(val_count.items(),key = lambda item: item[1],reverse = True)

        for i in range(k):
            ans.append(val_count[i][0])

        return ans