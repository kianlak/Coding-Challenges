# 💻 Coding Problems
This is a repository to store my attempts of solving problems and then analyzing them for improvements

# 🧠 What I've learned from Leetcode challenges
## #️⃣ Arrays & Hashing
#### 217. Contains Duplicate Leetcode
- Learned about Python's set object which makes use of a hash table
- Set using Hash Tables uses fixed amount of memory beforehand which is more memory efficient than a list which needs to allocate memory for each new element
- Since we need to continuously check every new element we get to, set makes it easier and more efficient to search through it

## 📍Two Pointers
#### 125. Valid Palindrome
- Learned that use of Regex is actually very inefficient for memory optimizations due to it's backtracking nature
- Only use regex for specific patterns over more broad patterns

## 📚 Stack
#### 20. Valid Parentheses
- My runtime and memory wasn't great due to creating a class from scratch for the Stack, however the logic is optimal
- We can imitate the behaviour of a Stack with a list to get better runtimes (This can be done with append() which acts as push, and the inbuilt pop())

## 🪟 Sliding Window
#### 121. Best Time to Buy and Sell Stock
- My previous solution for this problem had correct logic but made use of a nested for-loop which was not necessary at all, this resulted in a Runtime Error for much larger data inputs (Current solution for this problem is mostly copied from another persons solution, with some minor runtime improvement)
- I generally have a bad habit of defaulting to for-loops to solve problems that require going through a list, this habit is not good especially when I need to be able to access two different points for comparison
- If possible always attempt to create logic for going through a list or an array at O(n), some instances the logic is too complex to be able to make this possible, this is not one of those problems

# H