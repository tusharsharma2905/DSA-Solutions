class Solution(object):
    def combinationSum(self, candidates, target):
        res = []
        
        def backtrack(start_idx, current_comb, current_sum):
            if current_sum == target:
                res.append(list(current_comb))
                return
            if current_sum > target:
                return
                
            for i in range(start_idx, len(candidates)):
                current_comb.append(candidates[i])
                backtrack(i, current_comb, current_sum + candidates[i])
                current_comb.pop()  # Backtrack
                
        backtrack(0, [], 0)
        return res