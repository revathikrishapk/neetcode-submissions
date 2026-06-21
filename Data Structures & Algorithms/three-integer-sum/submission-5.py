class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        n=len(nums)

        for i in range(n):
            l=i+1
            r=n-1

            while l<r:
                total=nums[i]+nums[l]+nums[r]

                if total==0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l+=1
                    r-=1
                elif total<0:
                    l+=1
                else:
                    r-=1
        return ans
