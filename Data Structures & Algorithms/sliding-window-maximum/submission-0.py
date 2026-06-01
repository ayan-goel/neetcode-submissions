class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res = []
        i = 0

        for i in range(len(nums) - k + 1):
            max_val = nums[i]
            for j in range(i, i + k):
                max_val = max(nums[j], max_val)
            res.append(max_val)

        return res

            