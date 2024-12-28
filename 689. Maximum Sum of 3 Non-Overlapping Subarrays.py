'''
Given an integer array nums and an integer k, find three non-overlapping subarrays of length k with maximum sum and return them.

Return the result as a list of indices representing the starting position of each interval (0-indexed). If there are multiple answers, return the lexicographically smallest one.

 

Example 1:

Input: nums = [1,2,1,2,6,7,5,1], k = 2
Output: [0,3,5]
Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.
Example 2:

Input: nums = [1,2,1,2,1,2,1,2,1], k = 2
Output: [0,2,4]
 

Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] < 216
1 <= k <= floor(nums.length / 3)
'''









  class Solution:
    def maxSumOfThreeSubarrays(self, nums, k):
        n = len(nums)
        sum1 = sum(nums[:k])
        sum2 = sum(nums[k:2*k])
        sum3 = sum(nums[2*k:3*k])

        max1 = sum1
        max12 = sum1 + sum2
        max123 = sum1 + sum2 + sum3

        index1 = 0
        index12_1 = 0
        index12_2 = k
        ans = [0, k, 2 * k]

        for i in range(1, n - 3 * k + 1):
            sum1 = sum1 - nums[i - 1] + nums[i + k - 1]
            sum2 = sum2 - nums[i + k - 1] + nums[i + 2 * k - 1]
            sum3 = sum3 - nums[i + 2 * k - 1] + nums[i + 3 * k - 1]

            if sum1 > max1:
                max1 = sum1
                index1 = i

            if max1 + sum2 > max12:
                max12 = max1 + sum2
                index12_1 = index1
                index12_2 = i + k

            if max12 + sum3 > max123:
                max123 = max12 + sum3
                ans = [index12_1, index12_2, i + 2 * k]

        return ans
