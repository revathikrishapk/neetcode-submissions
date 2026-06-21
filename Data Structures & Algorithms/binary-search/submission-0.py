class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l=0
        h=len(nums)-1
        while l<h:
            mid=(l+h)//2
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                l+=1
            else:
                h-=1
        return -1