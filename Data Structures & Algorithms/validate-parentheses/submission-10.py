class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        cto = {
    "}": "{",
    "]": "[",
    ")": "(",
    ">": "<"
}
        for char in s:
            if char in "{[(<":
                stack.append(char)
            else:
                if not stack:
                    return False
                else:
                    if stack.pop()!=cto[char]:
                        return False
        return not stack
            