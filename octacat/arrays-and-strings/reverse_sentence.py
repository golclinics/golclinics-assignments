def reverseSentence(A):
    word = ""
    for i in A: 
        word += i
    
    sentence_parts = list(word.split(' '))
    sentence_parts[0], sentence_parts[2] = sentence_parts[2], sentence_parts[0]
    sentence = ' '.join(sentence_parts)

    sentence = list(sentence)

    return(sentence)

A = ['t','h','i','s',' ','i','s',' ','g','o','o','d']
print(reverseSentence(A))