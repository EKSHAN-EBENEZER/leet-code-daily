'''
You are climbing a staircase. It takes n steps to reach the top.

Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?

 

Example 1:

Input: n = 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps
Example 2:

Input: n = 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 1 step + 1 step
2. 1 step + 2 steps
3. 2 steps + 1 step
 

Constraints:

1 <= n <= 45
'''

'''
Approaches
(Also explained in the code)

Approach 1(Math)
Initialization: Start with ways = 1, considering the default way of taking all steps at once.

Iterative Approach:

Iterate from 1 to n / 2 to explore different step sizes.
For each step size, calculate a product using a nested loop, involving a combinatorial formula (C(n, k) = n! / (k! * (n - k)!)).
Accumulation: Accumulate the product in the sum variable.

Result: Add the sum to the ways variable for each step size.

Return: The final value of ways represents the total number of distinct ways to climb the stairs.

Complexity
Time complexity:
O(n2)O(n^2)O(n 
2
 )

Space complexity:
O(1)O(1)O(1)
'''


class Solution:
    def climbStairs(self, n: int) -> int:
        ways = 1

        for i in range(1, (n // 2) + 1):
            product = 1

            for j in range(i, 2 * i):
                product *= (n - j) / (j - i + 1)

            ways += product

        return int(ways)

