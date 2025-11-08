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

**Approach 1:**  
Use set to get distinct values. Traverse through the array - if element not present in set, add it to the set and accumulate the value in left side of nums

**Code (Python):**
```python
    def removeDuplicates(self, nums):
        dist = set()
        ind = 0
        for i in range(len(nums)):
            if nums[i] not in dist:
                dist.add(nums[i])
                nums[ind] = nums[i]
                ind += 1

        return ind
```
**Time complexity:** O(n)
**Space complexity:** O(n)

**Approach 2:**  
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

### 🟩 3. Right rotate an array by k places

**Approach 1:**  
Create a temp array which is copy of nums. Traverse through 0,len-1 and for each ind get ind-k

**Code (Python):**
```python
    def rotate(self, nums, k):
        temp = nums[:]
        for i in range(len(nums)):
            nums[i] = temp[(i-k)%len(nums)]
```
**Time complexity:** O(n)
**Space complexity:** O(n)

**Approach 2:**  
Reverse the arr. Reverse 0 to k-1 and Reverse k to len(nums)-1

**Code (Python):**
```python
    def rotate(self, nums, k):
        nums.reverse()
        k = k%len(nums)
        i = 0
        j = k-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1

        i = k
        j = len(nums)-1
        while i<j:
            nums[i], nums[j] = nums[j], nums[i]
            i+=1
            j-=1
```
**Time complexity:** O(n)

### 🟩 4. Move zeroes to the end

**Approach:**  
Keep accumulating the non zero values on the left side

**Code (Python):**
```python
    def moveZeroes(self, nums):
        ind = 0

        for i in range(len(nums)):
            if nums[i]!=0:
                nums[i], nums[ind] = nums[ind], nums[i]
                ind += 1
```
**Time complexity:** O(n)

### 🟩 5. Second Largest Element in an Array without sorting

**Approach:**  
Keep two vars - largest and second largest

**Code (Python):**
```python
def secondLargest(arr, n):
    if (n < 2):
        return -1
    large = float('-inf')
    second_large = float('-inf')
    for i in range(n):
        if (arr[i] > large):
            second_large = large
            large = arr[i]
        elif (arr[i] > second_large and arr[i] != large):
            second_large = arr[i]
    return second_large
```
**Time complexity:** O(n)

### 🟩 6. Find union of two sorted arrays

### 🟩 7. Find the missing number in an array - https://leetcode.com/problems/missing-number/description/

**Approach 1:**  
Find XOR of 1 to n. Then traverse through the array and apply xor with values of arr. Resulting value is missing number

**Code (Python):**
```python
def missingNumber(a, N):
    xor1 = 0
    xor2 = 0

    for i in range(N - 1):
        xor2 = xor2 ^ a[i]  # XOR of array elements
        xor1 = xor1 ^ (i + 1)  # XOR up to [1...N-1]
    
    xor1 = xor1 ^ N  # XOR up to [1...N]

    return xor1 ^ xor2  # the missing number
```
**Time complexity:** O(n)

**Approach 2:**  
n*(n+1)/2 - sum(nums)

**Code (Python):**
```python
    def missingNumber(self, nums):
        return len(nums)*(len(nums)+1)//2 - sum(nums)
```
**Time complexity:** O(n)

### 🟩 8. Find the number that appears once, and the other numbers twice - https://leetcode.com/problems/single-number/description/

**Approach 1:**  
Use hash to store frequence

**Code (Python):**
```python
    def singleNumber(self, nums):
        freq = {}
        for i in nums:
            freq.setdefault(i, 0)
            freq[i] += 1
        for i in freq.keys():
            if freq[i]==1:
                return i
```
**Time complexity:** O(n)
**SPace complexity:** O(n)

**Approach 2:**  
XOR of all elements

**Code (Python):**
```python
    def singleNumber(self, nums):
        res = 0
        for i in range(len(nums)):
            res = res ^ nums[i]
        return res
```
**Time complexity:** O(n)

### 🟩 9. Longest subarray with given sum K (positives)

### 🟩 10. Longest subarray with given sum K (positives + negatives)


