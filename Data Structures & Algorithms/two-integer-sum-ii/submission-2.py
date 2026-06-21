class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l=1
        r=len(numbers)-1
        while l<r:
            if numbers[l]+numbers[r]==target:
                return numbers[l]+numbers[r]
                l+=1
                r-=1

            


