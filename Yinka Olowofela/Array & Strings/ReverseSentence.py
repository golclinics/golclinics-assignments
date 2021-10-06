def reverseA(sentence, start, end):

  sentence_length = end - start
  mid_sentence = (sentence_length//2)+start
  
  for i in range(start, mid_sentence):
    temp = sentence[i]
    sentence[i] = sentence[(end-1)-i+start]
    sentence[(end-1)-i+start] = temp


def reverseSentence(sentence):

  reverseA(sentence, 0, len(sentence))

  first_part = 0
  second_part = 0
  
  len_sentence = len(sentence)

  while second_part < len_sentence:
    while second_part < len_sentence and sentence[second_part] != ' ':
      second_part += 1
  
    reverseA(sentence, first_part, second_part)
    second_part += 1
    first_part = second_part

  print (sentence)
  return sentence


reverseSentence(['g','o','o','d',' ','i','s',' ', 'b','a','d'])
