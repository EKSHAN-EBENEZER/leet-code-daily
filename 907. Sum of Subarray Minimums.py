'''
Given an array of integers arr, find the sum of min(b), where b ranges over every (contiguous) subarray of arr. Since the answer may be large, return the answer modulo 109 + 7.

 

Example 1:

Input: arr = [3,1,2,4]
Output: 17
Explanation: 
Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4]. 
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.
Sum is 17.
Example 2:

Input: arr = [11,81,94,43,3]
Output: 444
 

Constraints:

1 <= arr.length <= 3 * 104
1 <= arr[i] <= 3 * 104
'''


'''
Intuition
To arrive at the solution, we must track two things for each element arr[i]:

left[i]: the index of the first smaller element to the left of arr[i]
right[i]: the index of the first element that is less than or equal to arr[i] to the right
With left[i] and right[i] determined, the number of subarrays in which arr[i] is the minimum can be calculated by (i - left[i]) * (right[i] - i).

Approach
The implementation leverages two main concepts: the "Monotonic Stack" pattern and the "Prefix Sum" pattern, to efficiently solve the problem without having to evaluate every subarray explicitly. Here's the walk-through of the implemented solution, step-by-step:

Initialize two arrays, left and right, of the same length as arr to n, with -1 and n respectively. These arrays will hold for each element the index of the previous smaller element (left) and the next smaller or equal element (right).

Initialize a stack stk which we'll use to iterate over the array to find the left and right indices. The stack approach efficiently maintains a decreasing order of elements and their indices.

Iterate through the elements of arr from left to right. For each element, while the stack is not empty and the top element of the stack is greater than or equal to the current element, pop elements from the stack. This process is maintaining the stack in a strictly decreasing order.

After elements larger than the current one are popped off stk, if the stack is not empty, set left[i] to the index of the top element of stk, which is the closest previous element smaller than arr[i]. Then, push the current index i onto the stack.

Clear the stack and then iterate through the elements of arr from right to left to similarly identify right[i] for each element. The process mirrors step 3 and 4, but in the reversed direction and with the condition that any equal value element could also terminate the loop, maintaining strict decreasing order up to equal values.

Once both left and right arrays are filled with proper indices, calculate the sum. By iterating over all indices i, find the product of the count of subarrays where arr[i] is the minimum ((i - left[i]) * (right[i] - i)) and arr[i]. This represents the sum of arr[i] for all i in its valid subarrays.

Sum these products for all i. As the final sum might be very large, each addition is taken modulo 10^9 + 7 to prevent integer overflow.

By combining the Monotonic Stack to find bounds for each element and the Prefix Sum pattern to calculate each element's contribution to the total sum, the algorithm achieves an efficient solution that operates in O(n) time complexity, where n is the size of the input array arr.

Complexity
Time complexity: The time complexity of the code is O(n).
Space complexity: The space complexity of the code is O(n).
'''


class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        left = [-1] * n 
        right = [n] * n
        stack = []

        for i, value in enumerate(arr):
            while stack and arr[stack[-1]] >= value:  
                stack.pop()  
            if stack:
                left[i] = stack[-1]  
            stack.append(i) 

        stack = [] 

        
        for i in range(n - 1, -1, -1):  
            while stack and arr[stack[-1]] > arr[i]: 
                stack.pop()  
            if stack:
                right[i] = stack[-1]  
            stack.append(i) 

        mod = 10**9 + 7 

        result = sum((i - left[i]) * (right[i] - i) * value for i, value in enumerate(arr)) % mod
      
        return result 
