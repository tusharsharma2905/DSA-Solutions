class Solution(object):
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        
        def backtrack(start_idx, current_comb, current_sum):
            if current_sum == target:
                res.append(list(current_comb))
                return
                
            for i in range(start_idx, len(candidates)):
                if i > start_idx and candidates[i] == candidates[i - 1]:
                    continue
                if current_sum + candidates[i] > target:
                    break
                    
                current_comb.append(candidates[i])
                backtrack(i + 1, current_comb, current_sum + candidates[i])
                current_comb.pop()  
                
        backtrack(0, [], 0)
        return res