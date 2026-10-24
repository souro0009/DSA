class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        start = 0
        end = x-1
        ans = start
        while(start<=end):
            mid = start+((end-start)//2)
            if(mid*mid==x):
                return mid
            elif(mid*mid>x):
                end = mid-1
            else:
                ans = mid
                start = mid+1
                if x==1:
                    return start
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna