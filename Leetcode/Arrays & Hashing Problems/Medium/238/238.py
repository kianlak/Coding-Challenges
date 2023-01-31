# 238. Product of Array Except Self

class Solution:
  def productExceptSelf(self, nums: List[int]) -> List[int]:
    answer, suffix, prefix = [1] * len(nums), 1, 1
    
    for i in range(len(nums)):
      answer[i] *= prefix
      prefix *= nums[i]
      answer[-1 - i] *= suffix
      suffix *= nums[-1 - i]

    return answer