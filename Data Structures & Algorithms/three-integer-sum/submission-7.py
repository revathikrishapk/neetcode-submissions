class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        i=0
        l=1
        r=len(nums)-1
        for i in range(nums):
            l+=1
            r-=1
        while l<r:
            total=nums[i]+nums[l]+nums[r]
            if total==0:
                ans.append([nums[i],nums[l],nums[r]])
            elif total>0:
                l+=1
            else:
                r-=1
        return ans