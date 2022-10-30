#contigious sum of arrays whoes sum is k
class Solution:
     def subarraySum(self, nums: list[int], k: int) -> int:
         
         sumdict = {0:1} #set initail state key and value pair, cummulative sum
         n = len(nums)
         count = 0
         s = 0
         
         for num in nums:                    
             s += num
             if s - k in sumdict:
                count += sumdict[s-k]
             if s in sumdict:
                 sumdict[s] += 1
             else:
                 sumdict[s] = 1
         return count

a = Solution()            
print(a.subarraySum([3,4,7,2,-3,1,4,2,1], 7))
    
         
         