class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        freq = {}
        count = 0

        for num in nums:
            if num in freq:
                count += freq[num]   # forms pairs with previous occurrences
                freq[num] += 1
            else:
                freq[num] = 1

        return count

