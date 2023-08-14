import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        base_num = [2, 3, 5]
        res = []
        tmp = [1]
        while len(res) < n:
            cur = heapq.heappop(tmp)
            if cur in res:
                continue
            res.append(cur)
            for b in base_num:
                heapq.heappush(tmp, b * cur)
        return res[-1]
