'''
Given an integer array nums, return the number of all the arithmetic subsequences of nums.

A sequence of numbers is called arithmetic if it consists of at least three elements and if the difference between any two consecutive elements is the same.

For example, [1, 3, 5, 7, 9], [7, 7, 7, 7], and [3, -1, -5, -9] are arithmetic sequences.
For example, [1, 1, 2, 5, 7] is not an arithmetic sequence.
A subsequence of an array is a sequence that can be formed by removing some elements (possibly none) of the array.

For example, [2,5,10] is a subsequence of [1,2,1,2,4,1,5,10].
The test cases are generated so that the answer fits in 32-bit integer.

 

Example 1:

Input: nums = [2,4,6,8,10]
Output: 7
Explanation: All arithmetic subsequence slices are:
[2,4,6]
[4,6,8]
[6,8,10]
[2,4,6,8]
[4,6,8,10]
[2,4,6,8,10]
[2,6,10]
Example 2:

Input: nums = [7,7,7,7,7]
Output: 16
Explanation: Any subsequence of this array is arithmetic.
 

Constraints:

1  <= nums.length <= 1000
-231 <= nums[i] <= 231 - 1
'''


'''
Intuition
The problem requires counting the number of arithmetic subsequences in the given array. A sequence is considered arithmetic if it has at least three elements, and the difference between any two consecutive elements is the same.
Approach
One way to solve this problem is to use dynamic programming. We can maintain a 2D array dp, where dp[i][j] represents the number of arithmetic subsequences ending at index i with a common difference of j. We can then iterate through the array, updating the dp array and counting the total number of arithmetic subsequences.
Here's a step-by-step breakdown of the approach:
1. Initialize a variable total_count to 0, which will keep track of the total number of arithmetic subsequences.
2. Initialize a 2D array dp with dimensions n x n, where n is the length of the input array nums. Each element dp[i][j] will represent the number of arithmetic subsequences ending at index i with a common difference of j.
3. Iterate through the array nums with two nested loops:
The outer loop (i) goes from 1 to n - 1.
The inner loop (j) goes from 0 to i - 1.
4. For each pair of indices (i, j), calculate the common difference diff = nums[i] - nums[j].
5. Update dp[i][diff] by incrementing it by 1, indicating that we have found a new arithmetic subsequence ending at index i with a common difference of diff.
6. If there is an existing subsequence ending at index j with the common difference diff, extend it to form a longer subsequence ending at index i. Increment dp[i][diff] by the value of dp[j][diff].
7. Update the total_count by adding the value of dp[j][diff] to it.
8. After the loops, the total_count will contain the total number of arithmetic subsequences.
Complexity
Time complexity:
O(n2)O(n^2)O(n 
2
 ) - The nested loops iterate through each pair of indices, leading to a quadratic time complexity.
Space complexity:
O(n2)O(n^2)O(n 
2
 ) - The 2D array dp has dimensions n x n, contributing to a quadratic space complexity.
 '''


class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        n = len(nums)
        total_count = 0  
        dp = [defaultdict(int) for _ in range(n)]

        for i in range(1, n):
            for j in range(i):
                diff = nums[i] - nums[j]
                dp[i][diff] += 1  
                if diff in dp[j]:
                    dp[i][diff] += dp[j][diff]
                    total_count += dp[j][diff]

        return total_count
