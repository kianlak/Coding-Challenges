# 121. Best Time to Buy and Sell Stock

import sys

class Solution:
  def maxProfit(self, prices: List[int]) -> int:
    best_roi = 0
    buy = sys.maxsize

    for sell in prices:
      if sell < buy:
        buy = sell
      best_roi = max(best_roi, sell - buy)

    return best_roi