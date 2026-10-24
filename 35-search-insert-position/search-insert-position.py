class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        start = 0
        end = len(nums)-1
        while(start<=end):
            mid = start+(end-start)//2
            if(nums[mid]==target):
                return mid
                break
            elif(nums[mid]>target):
                end = mid-1
            else:
                start = mid+1
        return start

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna