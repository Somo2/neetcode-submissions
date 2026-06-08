class Solution:
    def countSeniors(self, details: List[str]) -> int:
        age = [int(s[11:13]) for s in details]
        catch=[i for i in age if i>60]
        return len(catch)