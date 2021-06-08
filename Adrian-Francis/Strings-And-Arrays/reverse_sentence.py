def reverse(item, start, end):
    len_item = end - start
    midway = (len_item//2) + start
    for i in range(start, midway):
        item[i], item[(end-1)-i+start] = item[(end-1)-i + start], item[i]

def reverseSentence(sentence):
    reverse(sentence, 0, len(sentence))
    print(sentence)

    # reverse each word
    p1 = 0
    p2 = 0
    len_sen = len(sentence)

    while p2 < len_sen:
    # reverse each word ("characters before space")
        while p2 < len_sen and sentence[p2] !=  ' ':
            p2 += 1

        reverse(sentence, p1, p2)
        p2 += 1
        p1 = p2
        print(sentence)

reverseSentence(['t','h','i','s',' ','i','s',' ','g','o','o','d'])
