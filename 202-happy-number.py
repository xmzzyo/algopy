class Solution:

    def get_number(self, num):
        res = []
        while num > 9:
            res.append(num % 10)
            num = num // 10
        res.append(num)
        return reversed(res)

    def isHappy(self, n: int) -> bool:
        visit = set()
        cur_sum = sum([x ** 2 for x in self.get_number(n)])
        while cur_sum not in visit:
            if cur_sum == 1:
                return True
            visit.add(cur_sum)
            cur_sum = sum([x ** 2 for x in self.get_number(cur_sum)])
        return False


print(Solution().isHappy(2))
