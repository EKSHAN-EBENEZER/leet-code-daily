'''
Given a list of 24-hour clock time points in "HH:MM" format, return the minimum minutes difference between any two time-points in the list.
 

Example 1:

Input: timePoints = ["23:59","00:00"]
Output: 1
Example 2:

Input: timePoints = ["00:00","23:59","00:00"]
Output: 0
 

Constraints:

2 <= timePoints.length <= 2 * 104
timePoints[i] is in the format "HH:MM".
'''




class Solution:
    def findMinDifference(self, a: List[str]) -> int:
        return min(map(sub,(q:=sorted(int(s[:2])*60+int(s[3:]) for s in a))[1:]+[q[0]+1440],q))
