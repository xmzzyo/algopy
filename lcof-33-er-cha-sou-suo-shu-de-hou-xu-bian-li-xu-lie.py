from typing import List


class Solution:
    def verifyPostorder(self, postorder: List[int]) -> bool:
        if not postorder:
            return True
        post = postorder[-1]
        l, r = 0, len(postorder) - 2
        while postorder[l] < post:
            l += 1
        while postorder[r] > post:
            r -= 1
        # print(postorder[:l], postorder[l:-1], post, l, r)
        if l < r:
            return False
        else:
            left = True
            if l > 0:
                left = self.verifyPostorder(postorder[:l])
            right = True
            if l < len(postorder) - 1:
                right = self.verifyPostorder(postorder[l:-1])
            return left and right


print(Solution().verifyPostorder([1, 6, 3, 2, 5]))
print(Solution().verifyPostorder([1, 3, 2, 6, 5]))
