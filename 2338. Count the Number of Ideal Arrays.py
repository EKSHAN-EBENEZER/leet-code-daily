'''
You are given two integers n and maxValue, which are used to describe an ideal array.

A 0-indexed integer array arr of length n is considered ideal if the following conditions hold:

Every arr[i] is a value from 1 to maxValue, for 0 <= i < n.
Every arr[i] is divisible by arr[i - 1], for 0 < i < n.
Return the number of distinct ideal arrays of length n. Since the answer may be very large, return it modulo 109 + 7.

 

Example 1:

Input: n = 2, maxValue = 5
Output: 10
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (5 arrays): [1,1], [1,2], [1,3], [1,4], [1,5]
- Arrays starting with the value 2 (2 arrays): [2,2], [2,4]
- Arrays starting with the value 3 (1 array): [3,3]
- Arrays starting with the value 4 (1 array): [4,4]
- Arrays starting with the value 5 (1 array): [5,5]
There are a total of 5 + 2 + 1 + 1 + 1 = 10 distinct ideal arrays.
Example 2:

Input: n = 5, maxValue = 3
Output: 11
Explanation: The following are the possible ideal arrays:
- Arrays starting with the value 1 (9 arrays): 
   - With no other distinct values (1 array): [1,1,1,1,1] 
   - With 2nd distinct value 2 (4 arrays): [1,1,1,1,2], [1,1,1,2,2], [1,1,2,2,2], [1,2,2,2,2]
   - With 2nd distinct value 3 (4 arrays): [1,1,1,1,3], [1,1,1,3,3], [1,1,3,3,3], [1,3,3,3,3]
- Arrays starting with the value 2 (1 array): [2,2,2,2,2]
- Arrays starting with the value 3 (1 array): [3,3,3,3,3]
There are a total of 9 + 1 + 1 = 11 distinct ideal arrays.
 

Constraints:

2 <= n <= 104
1 <= maxValue <= 104
'''
from math import isqrt
from collections import defaultdict
from functools import lru_cache

MODULO = 10**9 + 7

class Solution:
    def idealArrays(self, array_length: int, max_value: int) -> int:
    
        def generate_primes(limit):
            is_prime = [True] * (limit + 1)
            primes = []
            for num in range(2, limit + 1):
                if is_prime[num]:
                    primes.append(num)
                    for multiple in range(num * num, limit + 1, num):
                        is_prime[multiple] = False
            return primes

        def build_factor_map(prime_list, limit):
            factor_map = defaultdict(list)
            prime_count = len(prime_list)

   
            for idx, prime in enumerate(prime_list):
                factor_map[prime] = [0] * prime_count
                factor_map[prime][idx] = 1

            for value in range(3, limit + 1):
                if value not in factor_map:
                    factor_map[value] = [0] * prime_count
                    for idx, prime in enumerate(prime_list):
                        if value % prime == 0:
                            factor_map[value] = factor_map[value // prime].copy()
                            factor_map[value][idx] += 1
                            break

            return factor_map

        @lru_cache(None)
        def calculate_combinations(x, y):
            if y == 0:
                return 1
            if y == 1:
                return x
            if y > x:
                return 0
            return (calculate_combinations(x - 1, y) + calculate_combinations(x - 1, y - 1)) % MODULO


        primes = generate_primes(max_value)
        factor_map = build_factor_map(primes, max_value)


        total_arrays = 0
        for value in range(1, max_value + 1):
            factors = factor_map[value]
            combinations_product = 1
            for factor_count in factors:
                if factor_count > 0:
                    combinations_product *= calculate_combinations(factor_count + array_length - 1, min(array_length - 1, factor_count))
                    combinations_product %= MODULO
            total_arrays = (total_arrays + combinations_product) % MODULO

        return total_arrays
