class Solution:
    def frequency_sort(self, s: str) -> str:
        s_list = list(s)
        s_dict = {}
        result_list = []

        for char in s_list:
            if char in s_dict:
                s_dict[char] += 1
            else:
                s_dict[char] = 1

        while (s_dict):
            max_char = next(iter(s_dict))
            for char in s_dict:
                if s_dict[char] > s_dict[max_char]:
                    max_char = char
            count = s_dict.pop(max_char)
            for _ in range(count):
                result_list.append(max_char)

        return "".join(result_list)


# Complexity Analysis
# Time: O(n^2)
# Space: O(n)

# Tests
S = Solution()

print(S.frequency_sort("tree"))
print(S.frequency_sort("cccaaa"))
print(S.frequency_sort("Aabb"))