# 💻 Coding Problems
This is a repository to store my attempts of solving problems and then analyzing them for improvements.
#### I also make sure to explain all my work inside their respective markdown files.
#
# 🧠 What I've learned from Leetcode challenges
## #️⃣ Arrays & Hashing
#### 217. Contains Duplicate Leetcode
- Learned about Python's set object which makes use of a hash table
- Set using Hash Tables uses fixed amount of memory beforehand which is more memory efficient than a list which needs to allocate memory for each new element
- Since we need to continuously check every new element we get to, set makes it easier and more efficient to search through it

#### 242. Valid Anagram
- Learned about the collection.defaultdict type, it's a dictionary that avoids KeyError from happening if a key were to not exist (For both inserts and searches)
- collection.defaultdict is perfect for this problem as we can just insert and check new keys and their values without needing there to be a pre-existing key

#### 347. Top K Frequent Elements
- I learned that for smaller data inputs, Big-O doesn't matter as much and we can see it clearly for my solution for this problem. I have an O(nlog(n)) solution for 347, however a O(n) solution on LeetCodes compiler has a greater runtime than my O(nlog(n)) solution

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
- If possible always attempt to create logic for going through a list or an array at O(n), some instances the logic is too complex to be able to make this possible, this is not one of those problems