import bisect

class Solution(object):
    def findTheDistanceValue(self, arr1, arr2, d):
        arr2.sort()
        distance_count = 0
        
        for x in arr1:
            idx = bisect.bisect_left(arr2, x)
            valid = True
       
            if idx < len(arr2) and abs(arr2[idx] - x) <= d:
                valid = False
                
            if idx > 0 and abs(arr2[idx - 1] - x) <= d:
                valid = False
                
            if valid:
                distance_count += 1
                
        return distance_count