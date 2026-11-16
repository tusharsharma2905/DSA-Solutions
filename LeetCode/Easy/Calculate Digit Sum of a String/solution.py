class Solution(object):
    def digitSum(self, s, k):
        while len(s) > k:
            new_groups = []
            for i in range(0, len(s), k):
                chunk = s[i:i + k]
                group_sum = sum(int(char) for char in chunk)
                new_groups.append(str(group_sum))
            s = "".join(new_groups)
        return s