def biggerIsGreater(w):
    # Converting str into list for easier access
    word = list(w)

    # Assigning the length of word
    i = j = l = len(word) - 1

    # Determining swap index

    # Calculating the minimum swap index
    while i > 0 and word[i - 1] >= word[i]:
        i -= 1
    # If index is 0 or -ve, return
    if i <= 0:
        return 'no answer'

    while word[j] <= word[i - 1]:
        # Calculating the swap index
        j -= 1

    # Swapping i & jth position char
    word[i - 1], word[j] = word[j], word[i - 1]

    # Replacing the original word
    word[i:] = word[l:i - 1:-1]

    # Returning word
    return ''.join(word)