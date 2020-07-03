import re 

def urlify(string):
  regexBlank = '^(\s)*|(\s)*$'
  cleanBlanks = re.sub(regexBlank,'',string)
  singleBlankSpace = re.sub('(\s)+',' ',cleanBlanks)
  urlifyed = re.sub('\s','%20',singleBlankSpace)
  return urlifyed
#Milena Carneiro