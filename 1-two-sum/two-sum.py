class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                #if num[i]!=num[j]:
                    if nums[i]+nums[j] == target:
                        return [i,j]
            i = i+1
            j=j+1

        