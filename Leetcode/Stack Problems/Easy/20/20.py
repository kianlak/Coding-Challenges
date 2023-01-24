# 20. Valid Parentheses

class Solution:
  def isValid(self, s: str) -> bool:
    class Stack:
      def __init__(self):
        self.items = []

      def push(self, item):
        self.items.append(item)

      def pop(self):
        if not self.is_empty():
          return self.items.pop()

      def peek(self):
        if not self.is_empty():
          return self.items[-1]

      def is_empty(self):
        return len(self.items) == 0

      def get_stack(self):
        return self.items
      
    
    parenth_match = {')': '(', '}': '{', ']': '['}
    stack = Stack()
    popped = ''

    for _ in range(len(s)):
      if parenth_match.get(s[_]) and not stack.is_empty():
        popped = stack.pop()
        if popped != parenth_match[s[_]]:
          return False
      else:
        stack.push(s[_])
    
    if stack.is_empty():
      return True
    else:
      return False