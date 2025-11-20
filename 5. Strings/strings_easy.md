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
```

### 🟩 5. Isomorphic Strings - https://leetcode.com/problems/isomorphic-strings/description/

**Approach 1:** Using 2 hash maps to save mappings
**Code (Python):**
```python
    def isIsomorphic(self, s, t):
        hashMapS = {}
        hashMapT = {}

        for i in range(len(s)):
            if (s[i] in hashMapS and hashMapS[s[i]] != t[i]) or (t[i] in hashMapT and hashMapT[t[i]] != s[i]):
                return False
            else:
                hashMapS[s[i]] = t[i]
                hashMapT[t[i]] = s[i]

        return True
```
**Time complexity:** O(n)

**Approach 2:** Use 2 arrays to store last seen index of an alphabet
**Code (Python):**
```python
    def isIsomorphic(self, s, t):
        m1 = [-1]*130
        m2 = [-1]*130

        for i in range(len(s)):
            if m1[ord(s[i])]!=m2[ord(t[i])]:
                return False

            m1[ord(s[i])] = i
            m2[ord(t[i])] = i
        
        return True
```
**Time complexity:** O(n)

### 🟩 6. Rotate String - https://leetcode.com/problems/rotate-string/

**Approach 1:** Loop through 0 to n and generate all substring to compare with goal
**Code (Python):**
```python
    def rotateString(self, s, goal):
        for i in range(len(s)):
            if s[i:] + s[:i] == goal:
                return True

        return False
```
**Time complexity:** O(n^2)

**Approach 2:** Use 2 arrays to store last seen index of an alphabet
**Code (Python):**
```python
    def isIsomorphic(self, s, t):
        m1 = [-1]*130
        m2 = [-1]*130

        for i in range(len(s)):
            if m1[ord(s[i])]!=m2[ord(t[i])]:
                return False

            m1[ord(s[i])] = i
            m2[ord(t[i])] = i
        
        return True
```
**Time complexity:** Average case: O(n), Worse case: O(n^2)

### 🟩 7. Valid Anagram - https://leetcode.com/problems/valid-anagram/description/

**Approach 1:** Sort the strings and compare
**Time complexity:** O(n*log(n))

**Approach 2:** Use freq array
**Code (Python):**
```python
    def isAnagram(self, s, t):
        if len(s)!=len(t):
            return False
            
        word_freq = [0]*26

        for i in s:
            word_freq[ord(i)-ord('a')] += 1
        for i in t:
            word_freq[ord(i)-ord('a')] -= 1
            if word_freq[ord(i)-ord('a')] == -1:
                return False

        return True
```
**Time complexity:** O(n)
