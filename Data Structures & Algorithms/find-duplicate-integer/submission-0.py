class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        in_list = set()

        for num in nums:

            if num in in_list:
                return num
            
            in_list.add(num)
        return -1