#!/usr/bin/env python3
# coding:utf-8
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Method 1: nums 过大时：超出时间限制
        # list_len = len(nums)
        # for i in range(list_len):
        #     for j in range(i+1, list_len):
        #         if nums[i] == target - nums[j]:
        #             return [i, j]
        #
        # Method2:
        hash_dict = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in hash_dict:
                return [hash_dict[diff], i]
            hash_dict[num] = i
