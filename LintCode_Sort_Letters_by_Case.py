class Solution:
    def sortLetters(self, chars):
        """
        @param chars: The letters array you should sort.
        """
        p1 = 0; p2 = len(chars)-1
        while p1 < p2:
            if chars[p1].islower():
                p1 += 1
                continue
            if chars[p2].isupper():
                p2 -= 1
                continue
            chars[p1], chars[p2] = chars[p2], chars[p1]
            p1 += 1; p2 -= 1
