class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i=0
        #j=i+1
        for j in range(1,len(nums)):
            if (nums[i]==nums[j]):
                j=j+1
            else:
                i=i+1
                nums[i]=nums[j]
                #i=i+1
                j=j+1
        return i+1
        for k in range(i+1,len(nums)-1):
            nums[k] = 0
            k = k+1
