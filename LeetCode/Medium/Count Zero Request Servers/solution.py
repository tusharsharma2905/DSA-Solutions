from collections import Counter

class Solution(object):
    def countServers(self, n, logs, x, queries):
        logs.sort(key=lambda item: item[1])
        
        sorted_queries = sorted(enumerate(queries), key=lambda item: item[1])
        
        ans = [0] * len(queries)
        active_servers = Counter()
        
        j = 0  
        k = 0  
        
        for original_idx, q in sorted_queries:
            window_start = q - x
            window_end = q

            while k < len(logs) and logs[k][1] <= window_end:
                server_id = logs[k][0]
                active_servers[server_id] += 1
                k += 1

            while j < len(logs) and logs[j][1] < window_start:
                server_id = logs[j][0]
                active_servers[server_id] -= 1
                if active_servers[server_id] == 0:
                    del active_servers[server_id]
                j += 1

            ans[original_idx] = n - len(active_servers)
            
        return ans