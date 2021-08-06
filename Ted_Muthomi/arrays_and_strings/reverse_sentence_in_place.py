def reverse_sentence(my_char):
    i = ' '
    order_at = my_char.index(i) 
    ordered_list = my_char[order_at:] + my_char[:order_at]
    for each in ordered_list:
      each = ordered_list[order_at:] + ordered_list[:order_at]
    return each