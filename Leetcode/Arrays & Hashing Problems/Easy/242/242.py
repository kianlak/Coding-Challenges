# 242. Valid Anagram

import collections

class Solution:
  def isAnagram(self, s: str, t: str) -> bool:
    tracker = collections.defaultdict(int)

    for _ in s: 
      tracker[_] += 1

    for _ in t: 
      tracker[_] -= 1

    return all(x == 0 for x in tracker.values())