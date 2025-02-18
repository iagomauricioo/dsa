class Solution(object):
    def search(self, nums, target):
        low = 0
        high = len(nums)

        while low < high:
            mid = int((low + high) // 2)
            if nums[mid] == target:
                break
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid
        if target in nums:
            index = nums.index(nums[mid])
            return index
        else:
            return -1