'''

task:
  
Write a function that takes a non-empty string and returns a boolean
representing whether that string is a palindrome (same forward and backward)

'''


def isPalindrome(string):
  if(len(string) == 1):
    return true

  s = 0
  e = len(string) - 1
  k = string

  stri = list(string)

  while(s < e):
    stri[e], stri[s] = stri[s], stri[e]
    s += 1 
    e -= 1
  

  stri = ''.join(stri)
  return (k == stri)

def isPalindromeTWO(string):
	rev = string[::-1]
	return(rev == string)



t1 = "abcdcba"
t2 = "car"



print(isPalindrome(t1))
print(isPalindrome(t2))


print(isPalindromeTWO(t1))
print(isPalindromeTWO(t2))
