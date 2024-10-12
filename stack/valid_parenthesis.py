

class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1 or len(s) == 0:
            return False
        stack = []
        for i in range(len(s)):
            if s[i] not in [']', '}', ')']:
                stack.append(s[i])
            else:
                if stack:
                    top = stack[-1]
                    if (top == "(" and s[i] == ")") or (top == "[" and s[i] == "]") or (top == "{" and s[i] == "}"):
                        stack.pop()
                    else:
                        return False
                else:
                    return False
        return len(stack) == 0

# TC = O(N)