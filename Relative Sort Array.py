class Solution:
    def relativeSortArray(self, a: List[int], b: List[int]) -> List[int]:
        return sorted(a,key=lambda v,d=dict(zip(b,count())):d.get(v,len(b)+v))