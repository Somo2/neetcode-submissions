class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        freq={}

        result=[]
        for i in nums:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        items = list(freq.items())

        def sort_rule(item):
            return (item[1],-item[0])
        items.sort(key=sort_rule)

        
        for key,count in items:
            for j in range(count):
                result.append(key)
        return result