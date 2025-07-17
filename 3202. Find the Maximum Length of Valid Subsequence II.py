You are given an integer array nums and a positive integer k.
A subsequence sub of nums with length x is called valid if it satisfies:

(sub[0] + sub[1]) % k == (sub[1] + sub[2]) % k == ... == (sub[x - 2] + sub[x - 1]) % k.
Return the length of the longest valid subsequence of nums.
 

Example 1:

Input: nums = [1,2,3,4,5], k = 2

Output: 5

Explanation:

The longest valid subsequence is [1, 2, 3, 4, 5].

Example 2:

Input: nums = [1,4,2,3,1,4], k = 3

Output: 4

Explanation:

The longest valid subsequence is [1, 4, 1, 4].

 

Constraints:

2 <= nums.length <= 103
1 <= nums[i] <= 107
1 <= k <= 103

'''







class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        max_length = 2

        for target_mod in range(k):
            remainder_dp = [0] * k

            for num in nums:
                num_mod = num % k
                required_mod = (target_mod - num_mod + k) % k
                remainder_dp[num_mod] = remainder_dp[required_mod] + 1

            max_length = max(max_length, max(remainder_dp))

        return max_length
        
