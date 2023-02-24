class Solution:
    def isValid(self, s: str) -> bool:
        brackets = []
        brackets_another = {')': '(', ']': '[', '}': '{'}
        for sym in s:
            if sym in ')}]':
                if not brackets or brackets[-1] != brackets_another[sym]:
                    return False
                brackets.pop()
            else:
                brackets.append(sym)
        return not brackets