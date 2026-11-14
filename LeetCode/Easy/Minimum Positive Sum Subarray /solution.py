class Solution(object):
    def minimumSumSubarray(self, nums, l, r):
        n = len(nums)
        min_pos_sum = float('inf')
        pref = [0] * (n + 1)
        for i in range(n):
            pref[i + 1] = pref[i] + nums[i]
         
        for length in range(l, r + 1):
            for i in range(n - length + 1):
                sub_sum = pref[i + length] - pref[i]
                if sub_sum > 0:
                    min_pos_sum = min(min_pos_sum, sub_sum)
                    
        return min_pos_sum if min_pos_sum != float('inf') else -1