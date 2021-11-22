import re
def reverse_string(A):
  words = ''.join(A)
  #using re.split() -> to preserve the white spaces as opposed to split()
  return list(''.join(re.split("(\s+)",words)[::-1]))


print(reverse_string(['t','h','i','s',' ','i','s',' ','g','o','o','d']))
 