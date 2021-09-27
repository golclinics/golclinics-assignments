# Time - O(n^2), Space - O(1)
def num_insertion_sort(num_list):

    for i in range(1, len(num_list)):
        key_value = num_list[i]
        j = i - 1

        while j >= 0 and key_value < num_list[j]:
            num_list[j + 1] = num_list[j]
            j -= 1

        num_list[j + 1 ] = key_value

    return num_list


# Time - O(n^2), Space - O(1)
def num_bubble_sort(num_list):

    for i in range(len(num_list)):
        for j in range(i+1, len(num_list)):
            if num_list[i] > num_list[j]:
                temp = num_list[i]
                num_list[i] = num_list[j]
                num_list[j] = temp

    return num_list


# Time - O(n^2), Space - O(n)
def num_selection_sort(num_list):
    result_list = []

    while len(num_list):
        min_value = min(num_list)
        result_list.append(min_value)
        num_list.remove(min_value)

    return result_list

print(num_insertion_sort([5,8,2,6,74,1,5,8, 82]))
print(num_bubble_sort([5,8,2,6,74,1,5,8, 82]))
print(num_selection_sort([5,8,2,6,74,1,5,8, 82]))


# Big-O Analysis
"""
a. num_insertion_sort
   - Time: O(n^2)
   - Space: O(1)
b. num_bubble_sort
   - Time: O(n^2)
   - Space: O(1)
c. num_selection_sort
   - Time: O(n^2)
   - Space: O(n)
"""