# 347. Top K Frequent Elements

class Solution:
  def topKFrequent(self, nums: List[int], k: int) -> List[int]:
    dict = {}

    for _ in nums:
      if _ in dict:
        dict[_] = dict[_] + 1
      else:
        dict[_] = 1
    
    arr = sorted(dict, key = dict.get, reverse = True)

    return arr[:k]