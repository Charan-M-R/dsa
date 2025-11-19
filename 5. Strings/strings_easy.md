# 🔍 Strings problems - Easy

## 📘 Problems & Approaches

### 🟩 1. Remove outermost Paranthesis - https://leetcode.com/problems/remove-outermost-parentheses/description/
  
**Code (Python):**
```python
    def removeOuterParentheses(self, s):
        res = ""
        count = 0
        currStart = 0

        for i in range(len(s)):
            if s[i]=='(':
                count+=1
            else:
                count-=1

            if count==0:
                res += s[currStart+1:i]
                currStart = i+1

        return res
```
**Time complexity:** O(n)

### 🟩 2. Reverse words in a string - https://leetcode.com/problems/reverse-words-in-a-string/
  
**Code (Python):**
```python
    def reverseWords(self, s):
        ans = ''
        word = ''

        for i in s:
            if i==' ':
                if word!='':
                    ans = word + ' ' + ans
                    word = ''
            else:
                word += i
        if word!='':
            ans = word + ' ' + ans
        return ans[:-1]
```
**Time complexity:** O(n)

### 🟩 3. Largest odd number in a string - https://leetcode.com/problems/largest-odd-number-in-string/description/
  
**Code (Python):**
```python
    def largestOddNumber(self, num):
        l = len(num)-1
        while l>=0:
            if int(num[l])%2:
                break
            l-=1
        
        return num[:l+1]
```
**Time complexity:** O(n)

### 🟩 4. Longest common prefix - https://leetcode.com/problems/longest-common-prefix/description/

**Approach 1:** Double loop - keep finding the common prefix across all strings
**Code (Python):**
```python
    def longestCommonPrefix(self, strs):
        smallest = 0

        for i in range(len(strs)):
            if len(strs[i]) < len(strs[smallest]):
                smallest = i

        for i in range(len(strs[smallest])):
            for j in strs:
                if j[:i+1]!=strs[smallest][:i+1]:
                    return strs[smallest][:i]

        return strs[smallest]
```
**Time complexity:** O(n^2)

**Approach 2:** sort the strings lexographically and compare the first and last in the list
**Code (Python):**
```python
    def longestCommonPrefix(self, strs):
        strs.sort()
        l = strs[0]
        r = strs[-1]

        for i in range(min(len(l),len(r))):
            if l[i]!=r[i]:
                return l[:i]

        return l
```
**Time complexity:** O(n*log(n))
