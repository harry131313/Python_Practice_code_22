class Solution:
    def Max_subarray(self, lists: list[int]) -> list[int]:
        
        # s = 0
        # m = []
        # for i in lists:
        #     s+=i
        #     p = max(s, i)
        #     s = p
        # return s
        t = m = lists[0]
        for i in lists[1:]:
            t = max(i, t+i)
            m = max(m, t)
        return m
        
a = Solution()
print(a.Max_subarray([-2,1,-3,4,-1,2,1,-5,4]))
    
        
        