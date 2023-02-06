// 128. Longest Consecutive Sequence

import java.util.HashSet;
import java.util.Set;

class Solution {
  public int longestConsecutive(int[] nums) {
    if (nums == null || nums.length == 0) return 0;

    Set<Integer> set = new HashSet<>();
    for (int num : nums) set.add(num);

    int longestStreak = 0;
    for (int num : set) {
      if (!set.contains(num - 1)) {
        int currentNum = num;
        int currentStreak = 1;

        while (set.contains(currentNum + 1)) {
          currentNum += 1;
          currentStreak += 1;
        }

        longestStreak = Math.max(longestStreak, currentStreak);
      }
    }

    return longestStreak;
  }
}