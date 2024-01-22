'''
You have a set of integers s, which originally contains all the numbers from 1 to n. Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set, which results in repetition of one number and loss of another number.

You are given an integer array nums representing the data status of this set after the error.

Find the number that occurs twice and the number that is missing and return them in the form of an array.

 

Example 1:

Input: nums = [1,2,2,4]
Output: [2,3]
Example 2:

Input: nums = [1,1]
Output: [1,2]
 

Constraints:

2 <= nums.length <= 104
1 <= nums[i] <= 104
'''

'''
Approaches
(Also explained in the code)

Approach 1 - Brute Force
Approach 2 - Vector
Approach 3 - Set + sum
Approach 4 - Maps
Approach 5 - XOR Operation


Approach 1(Brute Force)
Initialization:

Initialize variables dup and missing to -1. These will be used to store the duplicate and missing numbers.
Iteration through Possible Numbers:

Iterate through numbers from 1 to the length of the input array (nums).
Count Occurrences:

For each number, count the occurrences in the input array nums by iterating through it.
Identify Duplicate and Missing:

If the count is 2, set dup to the current number, indicating a duplicate.
If the count is 0, set missing to the current number, indicating a missing number.
Return Result:

After the iteration, return a vector containing the found duplicate (dup) and missing (missing) numbers.
Complexity
Time complexity:
O(n2)O(n^2)O(n 
2
 )

Space complexity:
O(1)O(1)O(1)

Code
class Solution:
    def findErrorNums(self, nums):
        dup, missing = -1, -1
        
        for i in range(1, len(nums) + 1):
            count = nums.count(i)
            if count == 2:
                dup = i
            elif count == 0:
                missing = i
        
        return [dup, missing]


Approach 2(Vector)
Array Initialization:

Initialize a vector v of size n+1 with all elements set to 0. This array will be used to keep track of the occurrences of each number.
Count Occurrences:

Iterate through the given nums array and update the count of each number in the v array.
Identify Duplicate and Missing:

Iterate through the v array.
If the count of a number is 2, it is the duplicate number.
If the count of a number is 0, it is the missing number.
Return Result:

Return a vector containing the duplicate and missing numbers.
Complexity
Time complexity:
O(n)O(n)O(n)

Space complexity:
O(n)O(n)O(n)

Code

class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        v = [0] * (n + 1)
        missing, duplicate = 0, 0

        for num in nums:
            v[num] += 1

        for i in range(1, len(v)):
            if v[i] == 2:
                duplicate = i
            if v[i] == 0:
                missing = i

        return [duplicate, missing]

Approach 3(Set + Sum)
Calculate Expected Sum:

Calculate the expected sum of numbers from 1 to n using the formula (n * (n + 1)) / 2. This assumes no duplicates and no missing numbers.
Calculate Array and Unique Sums:

Calculate the sum of all elements in the array (array_sum).
Use an unordered_set (s) to get the unique elements in the array and calculate their sum (unique_sum).
Find Missing and Duplicate:

The difference between the expected sum and the unique sum gives the missing number (missing).
The difference between the array sum and the unique sum gives the duplicate number (duplicate).
Return Result:

Return a vector containing the duplicate and missing numbers.
Complexity
Time complexity:
O(n)O(n)O(n)

Space complexity:
O(n)O(n)O(n)

Code
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        actual_sum = n * (n + 1) // 2
        array_sum = 0
        unique_sum = 0
        s = set()

        for a in nums:
            array_sum += a

        for a in nums:
            s.add(a)

        for a in s:
            unique_sum += a

        missing = actual_sum - unique_sum
        duplicate = array_sum - unique_sum

        return [duplicate, missing]


Approach 4(Maps)
Create an unordered_map mp to count the occurrences of numbers from 1 to n.
Iterate through numbers in the input vector nums:
Increment the count of each number in mp.
Decrement the count of each number in mp.
Iterate through the entries in mp:
Identify the number with a count of -1 as the duplicate.
Identify the number with a count of 1 as the missing number.
Complexity
Time complexity:
O(n)O(n)O(n)

Space complexity:
O(n)O(n)O(n)

Code
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        mp = {i: 0 for i in range(1, n + 1)}

        for a in nums:
            mp[a] -= 1

        duplicate, missing = 0, 0

        for key, value in mp.items():
            if value == -1:
                duplicate = key
            if value == 1:
                missing = key

        return [duplicate, missing]


Approach 5(XOR Operation)
Calculate the XOR of all numbers from 1 to n (denoted as xorAll) and the XOR of the array nums (denoted as xorArray).
XOR the xorAll and xorArray to obtain xorResult.
Find the rightmost set bit in xorResult and store it in rightmostSetBit.
Divide the numbers from 1 to n into two groups based on the rightmost set bit: xorSet for numbers with the set bit, and xorNotSet for numbers without the set bit.
XOR all numbers in nums with the rightmost set bit to find the duplicate and missing numbers.
Iterate through nums and compare each number with xorSet. If found, return {xorSet, xorNotSet}; otherwise, return {xorNotSet, xorSet}.
Complexity
Time complexity:
O(n)O(n)O(n)

Space complexity:
O(1)O(1)O(1)

Code
class Solution:
    def findErrorNums(self, nums):
        n = len(nums)
        xorAll = 0
        xorArray = 0

        for i in range(1, n + 1):
            xorAll ^= i

        for num in nums:
            xorArray ^= num

        xorResult = xorArray ^ xorAll

        rightmostSetBit = xorResult & -xorResult

        xorSet = 0
        xorNotSet = 0

        for i in range(1, n + 1):
            if (i & rightmostSetBit) != 0:
                xorSet ^= i
            else:
                xorNotSet ^= i

        for num in nums:
            if (num & rightmostSetBit) != 0:
                xorSet ^= num
            else:
                xorNotSet ^= num

        for num in nums:
            if num == xorSet:
                return [xorSet, xorNotSet]

        return [xorNotSet, xorSet]
