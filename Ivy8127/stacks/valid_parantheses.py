class Solution:
    def isValid(self, s: str) -> bool:
        bracket_pairs = {'(': ')', '[': ']', '{': '}'}

        brackets = []
        for ch in s:
            if ch in bracket_pairs:
                brackets.append(ch)
            elif not brackets or ch != bracket_pairs[brackets.pop()]:
                return False

        return not brackets