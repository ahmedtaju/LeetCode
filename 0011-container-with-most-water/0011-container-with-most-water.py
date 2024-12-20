class Solution:
    def maxArea(self, height: List[int]) -> int:
        n=len(height)
        max_area=0
        left=0
        right=n-1
        while right>left:
            area=(right-left)*min(height[left],height[right])
            if area>=max_area:
                max_area=area
            if height[left]>height[right]:
                right-=1
            else:
                left+=1
        return max_area