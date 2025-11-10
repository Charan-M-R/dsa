# 🔍 Sorting techniques

### 🟩 Selection sort
**Approach:**  
Each iteration, select minimum element and push it to the left

**Code (Python):**
```python
    def selectionSort(self, arr):
        n = len(arr)
        for i in range(n-1):
            min_ind = i
            for j in range(i+1, n):
                if arr[min_ind] > arr[j]:
                    min_ind = j
                    
            arr[min_ind], arr[i] = arr[i], arr[min_ind]
            
        return arr
```
**Time complexity:** O(n^2) for worst and average cases

### 🟩 Bubble sort
**Approach:**  
Start from right most index. Iterate from 0 to that index: Greater number should be on the right
Basically bubbling up number to the right

**Code (Python):**
```python
    def bubbleSort(self,arr):
        n = len(arr)
        
        for i in range(n-1, 0, -1):
            for j in range(0, i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    
        return arr
```
**Time complexity:** O(n^2) for worst and average cases

### 🟩 Bubble sort
**Approach:**  
Start from right most index. Iterate from 0 to that index: Greater number should be on the right
Basically bubbling up number to the right

**Code (Python):**
```python
    def insertionSort(self, arr):
        for i in range(1,len(arr)):
            for j in range(i,0,-1):
                if arr[j] > arr[j-1]:
                    break
                arr[j], arr[j-1] = arr[j-1], arr[j]
        return arr
```
**Time complexity:** O(n^2) for worst and average cases. Best case is O(n)

### 🟩 Merge sort
**Approach:**  
Split arr into two -> sort the arr recursively -> Merge the sorted arrays

**Code (Python):**
```python
   def merge(self, arr, l, mid, r):
        temp = []
        i = l
        j = mid + 1
        
        while i<=mid and j<=r:
            if arr[i] > arr[j]:
                temp.append(arr[j])
                j+=1
            else:
                temp.append(arr[i])
                i+=1
                
        while i<=mid:
            temp.append(arr[i])
            i+=1
            
        while j<=r:
            temp.append(arr[j])
            j+=1
            
        for i in range(l,r+1):
            arr[i] = temp[i-l]
        
        
    def mergeSort(self,arr, l, r):
        if l>=r:
            return
        
        mid = (l+r)//2
        
        self.mergeSort(arr,l,mid)
        self.mergeSort(arr,mid+1,r)
        self.merge(arr,l,mid,r)
  ```
**Time complexity:** O(n*log(n))
