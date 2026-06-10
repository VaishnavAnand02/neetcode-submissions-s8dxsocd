class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        maps = {"}":"{","]":"[",")":"("}

        for i in s:

            if i in maps:
                if not stack or stack.pop() != maps[i]:
                    return False

            else:
                stack.append(i)

        return len(stack)==0