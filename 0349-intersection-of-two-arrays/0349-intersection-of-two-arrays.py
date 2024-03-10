class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = set(nums1)
        nums2 = set(nums2)
        res = set()
        for i in nums2:
            if i in nums1:
                res.add(i)
        return list(res)