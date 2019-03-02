#Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
def longestPalindrome(s: str) -> str:
    left, right = 0, len(s) - 1

    def is_palindrome(sub):
        left, right = 0, len(sub) - 1
        while left <= right:
            if sub[left] != sub[right]:
                return False
            else:
                left += 1
                right -= 1
        return True

    if is_palindrome(s):
        return s
    else:
        left_advance = longestPalindrome(s[left + 1:])
        right_advance = longestPalindrome(s[:right])
    if len(left_advance) >= len(right_advance):
        return left_advance
    else:
        return right_advance

print(longestPalindrome("babaddtattarraaaaa"))