class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        mapper = {
            ")" : "(",
            "}" : "{",
            "]" : "["
        }

        for i in s:
            if i in "[{(":
                stack.append(i)
            else:
                if stack:
                    if stack[-1] == mapper[i]:
                        stack.pop()
                    else: return False

                else:
                    return False

        return not stack
            
        