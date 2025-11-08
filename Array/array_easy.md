# 🔍 Array problems - Easy

## 📘 Problems & Approaches

### 🟩 1. Check if the array is sorted and rotated
**Approach 1:**  
Get the smallest element (if multiple, then left most). If there are multiple elements with smallest number and the smallest number is the last element, get to the leftmost in the cycle.
Then traverse through the error with first element being the smallest (left most). If you come across right element being less than less, then return false

**Code (Python):**
```python
    def check(self, nums):
        smallest = 0
        leng = len(nums)

        for i in range(leng):
            if nums[i] < nums[smallest]:
                smallest = i

        if smallest == 0 and nums[leng-1]==nums[0]:
            smallest = leng - 1
            while smallest>0 and nums[smallest]==nums[smallest-1]:
                smallest -=1 

        curr = (smallest + 1)%leng

        while (curr+1)%leng!=smallest:
            if nums[curr] > nums[(curr+1)%leng]:
                return False
            curr = (curr + 1)%leng

        return True
```
**Time complexity:** O(n)

**Approach 2:**  
Count number of dips. Dip is when right element is less than left element. If number of dips are greater than 1, return false

**Code (Python):**
```python
  def check(self,nums):
        dips = 0
        leng = len(nums)

        for i in range(len(nums)):
            if nums[i] > nums[(i+1)%leng]:
                dips += 1

        return True if dips<=1 else False
```
**Time complexity:** O(n)

### 🟩 2. Remove duplicates from sorted array
**Approach:**  
Keep accumulating the distinct values on the left side

**Code (Python):**
```python
    def removeDuplicates(self, nums):
        ind = 0
        for i in range(1,len(nums)):
            if nums[ind]!=nums[i]:
                ind += 1
                nums[ind] = nums[i]
        return ind+1
```
**Time complexity:** O(n)
