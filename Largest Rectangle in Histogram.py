class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        ans = 0
        stack = []

        for i,h in enumerate(heights):
            start = i
            while stack and stack[-1][1]>=h:
                index,hei = stack.pop()
                start = index
                ans = max(ans,(i-index)*hei)
            stack.append((start,h))

        for i,h in stack:
            ans = max(ans,(len(heights)-i)*h)

        return ans