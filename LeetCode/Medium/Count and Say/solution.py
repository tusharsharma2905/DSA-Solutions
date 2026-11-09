class Solution(object):
    def countAndSay(self, n):
        if n == 1:
            return "1"
            
        curr = "1"
        for _ in range(2, n + 1):
            next_str = []
            i = 0
            length = len(curr)
            
            while i < length:
                count = 1
                while i + 1 < length and curr[i] == curr[i + 1]:
                    i += 1
                    count += 1
                next_str.append(str(count) + curr[i])
                i += 1
            curr = "".join(next_str)
            
        return curr