class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        result = []
        for sub in grid:
            for num in sub:
                result.append(num)

        freq={}
        for i in result:
            if i in freq:
                freq[i]+=1
            else:
                freq[i]=1

        for key,value in freq.items():
            if value==2:
                    repeat=key

        n=len(result)        
        new= list(range(1, n+1))
       

        result2=list(set(new)-set(result))
        print(result2)
        for k in result2:
            not_avl=k

        return [repeat,not_avl]