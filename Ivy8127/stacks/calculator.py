class Solution:
    def calculate(self, s: str) -> int:
        nrm = []
        for c in s:
            if nrm and c.isdigit() and nrm[-1].isdigit():
                    nrm[-1] += c
            elif c != " ":
                nrm.append(c)
        q, sign, out = [], 1, 0
        for d in nrm:
            if d == "+":
                sign = 1
            elif d == "-":
                sign = -1
            elif d == "(":
                # current sum and calu parenthese first
                q.append(out)
                q.append(sign)
                out = 0
                sign = 1
            elif d == ")":
                # pop previous sum
                out = q.pop()*out
                out += q.pop()
            else:
                out += int(d)*sign
        return out