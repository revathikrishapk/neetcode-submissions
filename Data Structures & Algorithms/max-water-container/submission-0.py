class Solution:
    def maxArea(self, heights: List[int]) -> int: 
        ans=0 
        lp=0
        rp=len(heights)-1
        while lp<rp:
            w=rp-lp
            h=min(heights[lp],heights[rp])
            currwater=w*h
            ans=max(currwater,ans)
            #minimum ulla height aan eppozum edukkuka
            #cuz maximum height eduthaal overflow aakum
            #so minimum height aan increment aakkunath
            if heights[lp]<heights[rp]:
                lp+=1
            else:
                rp-=1
        return ans