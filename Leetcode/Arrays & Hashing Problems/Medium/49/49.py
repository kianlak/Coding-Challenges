# 49. Group Anagrams

import collections

class Solution:
  def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
    anagram_groups = []
    anagram_dictionary = collections.defaultdict(int)
    dictionary_entries = 0

    while strs:
      word = strs[0]
      sort = ''.join(sorted(word))

      if sort in anagram_dictionary:
        anagram_groups[anagram_dictionary[sort]].append(word)
      else:
        anagram_dictionary[sort] = dictionary_entries
        anagram_groups.insert(dictionary_entries, [word])
        dictionary_entries += 1

      del strs[0]
    
    return anagram_groups