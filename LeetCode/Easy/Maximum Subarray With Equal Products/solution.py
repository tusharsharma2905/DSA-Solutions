import math
class Solution(object):
    def maxLength(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        def lcm(a, b):
            return (a * b) // gcd(a, b)

        n = len(nums)
        max_len = 0
        overall_lcm = 1
        for x in nums:
            overall_lcm = lcm(overall_lcm, x)
        max_bound = overall_lcm * max(nums)

        for i in range(n):
            prod = 1
            curr_gcd = 0
            curr_lcm = 1
            
            for j in range(i, n):
                val = nums[j]
                prod *= val
                curr_gcd = gcd(curr_gcd, val)
                curr_lcm = lcm(curr_lcm, val)

                if prod == curr_lcm * curr_gcd:
                    max_len = max(max_len, j - i + 1)

                if prod > max_bound:
                    break

        return max_len