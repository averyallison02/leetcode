class Solution:
    def isPalindrome(self, x: int) -> bool:
        return x == self.intPalindrome(x)

    def intPalindrome(self, x: int) -> int :
        r = 0
        while (x > 0) :
            r *= 10
            r += x % 10
            x //= 10
        return r
