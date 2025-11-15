# 🔍 Single Linked List problems - Easy

### 🟩 1. Inserting a node into linked list

#### Subproblem 1: Inserting at head
**Approach:**  Create new node and node.next should be current head. Return new node as head

**Code (Python):**
```python
    def insertAtFront(self, head, x):
        newNode = Node(x)
        newNode.next = head
        return newNode
```

#### Subproblem 2: Inserting at the end
**Approach:**  Traverse the linked list and insert at the end

**Code (Python):**
```python
    def insertAtEnd(self, head, x):
        newNode = Node(x)
       
        if head is None:
           return newNode
           
        curr = head
        while curr.next:
            curr = curr.next
            
        curr.next = newNode
        return head
```

### 🟩 2. Deleting a node - https://leetcode.com/problems/delete-node-in-a-linked-list/description/

**Code (Python):**
```python
    def deleteNode(self, node):
        node.val = node.next.val
        node.next = node.next.next
```

### 🟩 3. Reversing a linked list - https://leetcode.com/problems/reverse-linked-list/

**Approach 1:**  Iterative
**Code (Python):**
```python
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            nxt = curr.next
            curr.next = prev
            prev = curr        
            curr = nxt
        
        return prev
```

**Approach 2:**  Recursive
**Code (Python):**
```python
    def reverseList(self, head):
        if head is None or head.next is None:
            return head

        newHead = self.reverseList(head.next)
        head.next.next = head
        head.next = None
        return newHead
```


### 🟩 4. Find middle of a linked list - https://leetcode.com/problems/middle-of-the-linked-list/

**Approach 1:**  Find length of linked list first and then traverse l//2 times

**Approach 2:**  Tortoise and Hare method
**Code (Python):**
```python
    def middleNode(self, head):
        node1 = head
        node2 = head

        while node2.next is not None:
            node1 = node1.next
            node2 = node2.next
            if node2.next:
                node2 = node2.next

        return node1
```

### 🟩 5. Linked list with a cycle 

**Approach:**  Tortoise and Hare method (Floyd’s Cycle Detection Algorithm)

**sub problem 1:** Find if linked list has a cycle - https://leetcode.com/problems/linked-list-cycle/

**Code (Python):**
```python
    def hasCycle(self, head):
        node1 = head
        node2 = head

        while node1 and node1.next:
            node1 = node1.next.next
            node2 = node2.next

            if node1 == node2:
                return True
        
        return False
```

**Sub problem 2:** Find the node where cycle starts - https://leetcode.com/problems/linked-list-cycle-ii/

**Code (Python):**
```python
    def detectCycle(self, head):
        slow = head
        fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                break

        if not (fast and fast.next):
            return None

        slow = head
        while slow!=fast:
            slow = slow.next
            fast = fast.next

        return fast
```

Explanation: When slow reaches head of cycle, fast is already L (length of head to cycle start) places ahead. So hypothetically, if you reverse L places of slow node, thats what slow and fast would have previously met. So this means that in our case when slow and fast met, we need to push fast node by L places to get to the start of cycle

**Sub problem 3:** Find length of cycle - https://www.geeksforgeeks.org/problems/find-length-of-loop/1

**Code (Python):**
```python
    def lengthOfLoop(self, head):
        slow = head
        fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if fast==slow:
                break
            
        if not (fast and fast.next):
            return 0
            
        count = 1
        slow = slow.next
        fast = fast.next.next
        while fast != slow:
            fast = fast.next
            count += 1
            
        return count
```

### 🟩 6. Check if linked list is a palindrome 

**Approach 1:**  Temporary space (store the values in stack in first traversal). During second traversal, pop the values of the stack

**Approach 2:**  Tortoise and Hare method (Floyd’s Cycle Detection Algorithm) and reverse the second part of the linked list

**Code (Python):**
```python
    def reverse(self, head):
        curr = head
        prev = None
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev

    def isPalindrome(self, head):
        if head is None or head.next is None:
            return True

        slow = head
        fast = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        newHead = self.reverse(slow.next)

        node1 = head
        node2 = newHead
        while node2:
            if node1.val!=node2.val:
                return False
            node1 = node1.next
            node2 = node2.next
        self.reverse(node1)

        return True
        
```
