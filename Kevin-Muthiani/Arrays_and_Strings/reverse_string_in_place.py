# Write a function reverseSentence(A) that takes in an array of characters, A,
# and reverses the the "words" (not individual characters).


# Helper function to reverse all elements within provided indices
def reverseArray(arr, first_index, last_index):
    length = last_index - first_index
    midway = first_index + (length//2)

    for i in range(first_index, midway):
      arr[i], arr[(last_index-1)-(i-first_index)] = arr[(last_index-1)-(i-first_index)], arr[i]


def reverseSentence(sentence):
    first_index = 0
    n = len(sentence)

    # Reverse all elements (characters) of array
    reverseArray(sentence, first_index, n)
    
    # Reverse all but last word
    for i in range(n):
        if sentence[i] == ' ':
            last_index = i
            reverseArray(sentence, first_index, last_index)
            first_index = last_index + 1
    
    # Reverse last word
    reverseArray(sentence, first_index, n)


# Test function
if __name__ == "__main__":
  mySentence = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
  reverseSentence(mySentence)
  print(mySentence)