class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        k = k % len(nums)

        if k == 0:
            return None

        # reverse entire list
        for i in range(len(nums)//2):
            j = len(nums)-i-1
            # swapping values
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        # rotate list till the length where its supposed to be rotated
        for i in range(k//2):
            j = k-i-1
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

        index = 1
        endRange = (len(nums) + k) // 2

        # reverse remaining parts of list
        for i in range(k, endRange):
            j = len(nums) - index
            temp = nums[i]
            nums[i] = nums[j]
            nums[j] = temp

            index += 1
