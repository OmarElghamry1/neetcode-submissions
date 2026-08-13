class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        num = 0
        i = 0
        l = len(s)
        while i < l:
            if i + 1 < l:
                a, b = roman[s[i]], roman[s[i + 1]]
                if a < b:
                    num += (b - a)
                    i += 2
                else:
                    num += a
                    i += 1
            else:
                num += roman[s[i]]
                i += 1

        return num

