class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=1
        r=len(numbers)
        while l<r:
            if numbers[l]+numbers[r]==target:
                return [l,r]
                l+=1
                r-=1
            else:
                return -1
            


