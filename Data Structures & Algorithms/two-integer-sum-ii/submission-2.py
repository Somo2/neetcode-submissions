class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        j=len(numbers)-1
        i=0

        while i<j and numbers[i]+numbers[j]!=target:
            if numbers[i]+numbers[j]<target:
                i+=1
            else:
                j-=1
        return [i+1,j+1]