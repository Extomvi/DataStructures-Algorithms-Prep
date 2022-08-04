"""Check if a sentence is a valid palindrome"""
def isPalindrome(s):
    word = []
    for i in s:
        if (
            ord('A')<=ord(i)<=ord('Z') 
            or ord('a')<=ord(i)<=ord('z') 
            or ord('0')<=ord(i)<=ord('9')
        ):
            word.append(i.lower())
            
    left, right = 0, len(word) - 1
    while left < right:
        if word[left] != word[right]:
            return False
        left, right = left + 1, right - 1
    return True 
print(isPalindrome("A man, a plan, a canal: Panama"))