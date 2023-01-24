# 206. Reverse Linked List

class Solution:
  def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
    reverse_list = None

    while head:
      temp = head.next
      head.next = reverse_list
      reverse_list = head
      head = temp
    
    return reverse_list