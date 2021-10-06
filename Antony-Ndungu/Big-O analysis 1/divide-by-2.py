# O(log n) time | O(1) space
def count_div_2(n):
    count = 0
    while n > 1:
        n = n // 2
        count += 1
    return count
