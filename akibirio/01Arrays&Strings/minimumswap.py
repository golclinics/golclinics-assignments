def minimumSwaps(arr):
    ref_arr = sorted(arr)
    index_dict = {value: index for index, value in enumerate(arr)}
    swaps = 0

    for i, v in enumerate(arr):
        correct_value = ref_arr[i]
        if v != correct_value:
            to_swap_ix = index_dict[correct_value]
            arr[to_swap_ix], arr[i] = arr[i], arr[to_swap_ix]
            index_dict[v] = to_swap_ix
            index_dict[correct_value] = i
            swaps += 1

    return swaps


if __name__ == '__main__':
    arra = [7, 1, 3, 2, 4, 5, 6]
    print(minimumSwaps(arra))
