#!/usr/bin/env python
# -*- coding: utf-8 -*-
# File  : 1_Two_Sum.py
# Author: ZhouZijian
# Date  : 2018/9/24

"""
给定一个整数数组和一个目标值，找出数组中和为目标值的两个数。
你可以假设每个输入只对应一种答案，且同样的元素不能被重复利用。
"""

# 暴力法
# class Solution:
#     def twoSum(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: List[int]
#         """
#         count = len(nums)
#         for i in range(count):
#             if nums[i] > target:
#                 pass
#             for j in range(i+1, count):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#                     break


# 哈希表
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        nums_dict = {}
        for index1, number1 in enumerate(nums):
            number2 = target - number1
            if number2 in nums_dict:
                return nums_dict[number2], index1
                break
            nums_dict[number1] = index1


# a = Solution()
# print(a.twoSum(nums=[2, 7, 11, 15], target=9))