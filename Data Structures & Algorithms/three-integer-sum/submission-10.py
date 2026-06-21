class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            l=i+1
            r=len(nums)-1
            while l<r:
                target=a+nums[l]+nums[r]
                if target>0:
                    r-=1
                elif target<0:
                    l+=1
                else:
                    ans.append([a,nums[l],nums[r]])
        return ans