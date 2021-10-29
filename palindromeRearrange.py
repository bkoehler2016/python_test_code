# count the number of each individual character
# can form a palindrome only if:
#   at most one of the character counts is odd, all others must be even
#  if there are no odd counts, then the string must be a palindrome

def palindromeRearranging(inputString):
    count = {}
    for char in inputString:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
