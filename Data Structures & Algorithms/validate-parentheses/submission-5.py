class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if char in ["(", "{", "["]:
                stack.append(char)
            else:
                if len(stack)==0:
                    return False
                top = stack.pop()
                if (top == "(" and char == ")") or (top == "{" and char == "}") or (top == "[" and char == "]"):
                    continue
                return False
        return True if len(stack)==0 else False