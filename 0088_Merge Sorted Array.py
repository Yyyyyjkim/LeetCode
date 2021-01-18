class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1[:(m+n)] = sorted(nums1[:m] + nums2[:n])

nums1 = [1,2,3,0,0,0]
nums2 = [2,5,6]
m = 3
n = 3