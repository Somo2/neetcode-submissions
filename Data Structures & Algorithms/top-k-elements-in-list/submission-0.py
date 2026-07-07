class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:


        count1 = {}
        for num in nums:
            if num in count1:
                count1[num] += 1
            else:
                count1[num] = 1

        sorted_count = sorted(count1.items(), key=lambda x: x[1], reverse=True)
        result = [item[0] for item in sorted_count[:k]]
        return result