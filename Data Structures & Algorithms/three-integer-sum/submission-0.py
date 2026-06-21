class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        n=len(nums)
        for i in range(0,n):
            for j in range(i+1,n):
                for k in range(i+2,n):
                    if nums[i]+nums[j]+nums[k]==0:
                        return[i,j,k]