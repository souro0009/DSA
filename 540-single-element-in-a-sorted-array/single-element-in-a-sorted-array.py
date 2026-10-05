class Solution(object):
    def singleNonDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        j = 0
        #temp=0
        while j<len(nums)-1:
            if(nums[j+1] != nums[j]):
                return nums[j]
            j +=2
        return nums[j]