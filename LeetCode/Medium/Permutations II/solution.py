class Solution(object):
    def permuteUnique(self, nums):
        nums.sort()
        res = []
        visited = [False] * len(nums)
        
        def backtrack(current_perm):
            if len(current_perm) == len(nums):
                res.append(list(current_perm))
                return
                
            for i in range(len(nums)):
                if visited[i]:
                    continue
                
                if i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]:
                    continue
                    
                visited[i] = True
                current_perm.append(nums[i])
                backtrack(current_perm)
                current_perm.pop()
                visited[i] = False
                
        backtrack([])
        return res