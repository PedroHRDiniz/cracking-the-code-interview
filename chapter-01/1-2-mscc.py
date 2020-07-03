def dictCharacters(string):
  output = {}
  for character in string:
    if character in output:
      output[character] += 1
    else:
      output[character] = 1
  return output

def permutationString(str1,str2):
  isPermutation = True
  dict1 = dictCharacters(str1)
  dict2 = dictCharacters(str2)
  for char in dict1:
    if char not in dict2:
      return False
    else:
      isPermutation = isPermutation and dict2[char] == dict1[char]
  return isPermutation
#Milena Carneiro