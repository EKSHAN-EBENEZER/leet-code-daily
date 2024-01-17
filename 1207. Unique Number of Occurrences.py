'''
Given an array of integers arr, return true if the number of occurrences of each value in the array is unique or false otherwise.

 

Example 1:

Input: arr = [1,2,2,1,1,3]
Output: true
Explanation: The value 1 has 3 occurrences, 2 has 2 and 3 has 1. No two values have the same number of occurrences.
Example 2:

Input: arr = [1,2]
Output: false
Example 3:

Input: arr = [-3,0,1,-3,1,1,1,-3,10,0]
Output: true
 

Constraints:

1 <= arr.length <= 1000
-1000 <= arr[i] <= 1000
'''

'''
Approaches
(Also explained in the code)

Approach 1 (Without Sets and Maps)
Sort the input array arr to group identical elements together.
Traverse the sorted array, counting occurrences of each element.
Store the counts in a separate vector v.
Sort the vector v to make it easier to check for duplicates.
Iterate through v and check if adjacent elements are equal. If so, return false.
If the loop completes, it means all counts are unique, and the function returns true.
Complexity
Time complexity:
O(nlogn)O(nlogn)O(nlogn)

Space complexity:
O(n)O(n)O(n)
'''


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr.sort()
        v = []

        i = 0
        while i < len(arr):
            cnt = 1

            # Count occurrences of the current element
            while i + 1 < len(arr) and arr[i] == arr[i + 1]:
                cnt += 1
                i += 1

            v.append(cnt)
            i += 1

        v.sort()

        for i in range(1, len(v)):
            if v[i] == v[i - 1]:
                return False

        return True

