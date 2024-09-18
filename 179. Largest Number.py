'''
Given a list of non-negative integers nums, arrange them such that they form the largest number and return it.

Since the result may be very large, so you need to return a string instead of an integer.

 

Example 1:

Input: nums = [10,2]
Output: "210"
Example 2:

Input: nums = [3,30,34,5,9]
Output: "9534330"
 

Constraints:

1 <= nums.length <= 100
0 <= nums[i] <= 109
'''






qclass Solution:
    def largestNumber(self, nums: List[int]) -> str:
        s=[str(x) for x in nums]
        def cmp(x, y):
            return -1 if x+y>y+x else 1
        s.sort(key=cmp_to_key(cmp))
        ans="".join(s)
        return '0' if ans[0]=='0' else ans
        
        
