'''
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.

 

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output: 
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output: 
[
[1,2,2],
[5]
]
 

Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
'''





class Solution:
    def combinationSum2(self, cand, target):
        cand.sort()
        res = []
        path = []
        self.dfs(cand, 0, target, path, res)
        return res
    
    def dfs(self, cand, cur, target, path, res):
        if target == 0:
            res.append(path.copy())
            return
        if target < 0:
            return
        
        for i in range(cur, len(cand)):
            if i > cur and cand[i] == cand[i - 1]:  
                continue
            path.append(cand[i])
            self.dfs(cand, i + 1, target - cand[i], path, res)
            path.pop() 
