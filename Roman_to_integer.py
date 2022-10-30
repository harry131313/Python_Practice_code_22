class Solution: 
    def romantoint(self, s: str) -> int:
        dic = {"M":1000,
               "CM":900,
               "D":500,
               "CD":400,
               "C":100,
               "XC":90,
               "L":50,
               "XL":40,
               "X":10,
               "V":5,
               "IV":4,
               "I":1}
        total = 0
        curr = 0
        prev = 0
        
        for i in range(len(s)):
            curr = dic[s[i]]
            if curr > prev:
                total = total + curr - 2*prev
            else:
                total += curr
            prev = curr
        return total
a = Solution()
print(a.romantoint('XLIXX'))