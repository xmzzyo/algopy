from typing import List


class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        in_degree = [0 for _ in range(numCourses)]
        for pre in prerequisites:
            in_degree[pre[1]] += 1
        visited = []
        while len(visited) < numCourses:
            cur = None
            for i, in_d in enumerate(in_degree):
                if in_d == 0 and i not in visited:
                    cur = i
                    break
            if cur is None and len(visited) < numCourses:
                return False
            visited.append(cur)
            for pre in prerequisites:
                if pre[0] == cur:
                    in_degree[pre[1]] -= 1
        return True


print(Solution().canFinish(2, [[1, 0]]))
print(Solution().canFinish(2, [[1, 0], [0, 1]]))
