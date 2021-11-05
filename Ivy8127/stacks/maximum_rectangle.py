class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        if m == 0:
            return 0
        n = len(matrix[0])
        if n == 0:
            return 0
        
        rec = [[0] * n for _ in range(m)]
        for i in range(n):
            if matrix[0][i] == '1':
                rec[0][i] = 1
                
        max_area = 0
        for i in range(m):
            for j in range(n):
                if i > 0 and matrix[i][j] != '0':
                    rec[i][j] = rec[i - 1][j] + 1
            
            stack = []
            heights = rec[i]
            for k, h in enumerate(heights):
                if not stack or stack[-1][1] < h:
                    stack.append((k, h))
                else:
                    while stack and stack[-1][1] >= h:
                        l, p = stack.pop()
                        max_area = max(max_area, (k - l) * p)
                    stack.append((l, h))
            while stack:
                l, p = stack.pop()
                max_area = max(max_area, (n - l) * p)  
                
        return max_area