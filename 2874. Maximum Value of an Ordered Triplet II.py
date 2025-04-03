'''
You are given a 0-indexed integer array nums.

Return the maximum value over all triplets of indices (i, j, k) such that i < j < k. If all such triplets have a negative value, return 0.

The value of a triplet of indices (i, j, k) is equal to (nums[i] - nums[j]) * nums[k].

 

Example 1:

Input: nums = [12,6,1,2,7]
Output: 77
Explanation: The value of the triplet (0, 2, 4) is (nums[0] - nums[2]) * nums[4] = 77.
It can be shown that there are no ordered triplets of indices with a value greater than 77. 
Example 2:

Input: nums = [1,10,3,4,19]
Output: 133
Explanation: The value of the triplet (1, 2, 4) is (nums[1] - nums[2]) * nums[4] = 133.
It can be shown that there are no ordered triplets of indices with a value greater than 133.
Example 3:

Input: nums = [1,2,3]
Output: 0
Explanation: The only ordered triplet of indices (0, 1, 2) has a negative value of (nums[0] - nums[1]) * nums[2] = -3. Hence, the answer would be 0.
 

Constraints:

3 <= nums.length <= 105
1 <= nums[i] <= 106

'''









from typing import List

class Solution:
    def maximumTripletValue(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3:
            return 0

        left_max = [0] * n
        left_max[0] = nums[0]
        for i in range(1, n):
            left_max[i] = max(left_max[i - 1], nums[i])

        right_max = [0] * n
        right_max[-1] = nums[-1]
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i + 1], nums[i])

        ans = 0
        for i in range(1, n - 1):
            left = left_max[i - 1]
            right = right_max[i + 1]
            ans = max(ans, (left - nums[i]) * right)

        return ans
