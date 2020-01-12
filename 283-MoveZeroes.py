#!/usr/bin/env python3
# coding: utf-8
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        flag = 0
        for i in nums:
            if i != 0:
                nums[flag] = i
                flag += 1
        for j in nums[flag:]:
            nums[flag] = 0
            flag += 1
