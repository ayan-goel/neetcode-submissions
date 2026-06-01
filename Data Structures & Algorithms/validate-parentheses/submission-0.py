class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedAndOpened = { '}' : '{', ')' : '(', ']' : '[' }

        for char in s:
            if char in closedAndOpened:
                if stack and stack[-1] == closedAndOpened[char]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(char)
        if stack == []:
            return True
        else:
            return False