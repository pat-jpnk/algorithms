'''

task: 

You're given a string of available characters
and a string representing a document that you
need to generate. Write a function that
determines if you can generate the document
using the available characters. If you can
generate the document, your function should
return "true" ; otherwise, it should return
"false".

You're only able to generate the document if
the frequency of unique characters in the
characters string is greater than or equal to
the frequency of unique characters in the
document string. For example, if you're given
[characters = "abcabc"] and
[document = "aabbccc"] you cannot
generate the document because you're
missing one "c".

The document that you need to create may
contain any characters, including special
characters, capital letters, numbers, and
spaces.

Note: you can always generate the empty
string [""].

'''

def document(characters, document):
  if(len(document) < 1):
    return True

  d = dict()

  for i in characters:
    if i in d:
      d[i] += 1

    else:
      d[i] = 1

  for j in document:
    if j not in d or d[j] == 0:
      return False
    
    else:
      d[j] -= 1

  return True


print(document("A","a"))

print(document("car", "ddcrae"))

print(document("Bste!hetsi ogEAxpelrt x ","AlgoExpert is the Best!"))

print(document("estssa","testing"))
