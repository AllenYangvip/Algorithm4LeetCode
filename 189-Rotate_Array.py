class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # n = len(nums)
        # k %= n
        # for _ in range(k):
        #     nums.insert(0, nums.pop())
        n = len(nums)
        k %= n
        nums[:] = nums[-k:] + nums[:-k]
       
