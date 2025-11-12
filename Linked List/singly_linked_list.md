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

### 🟩 3. Reversing a linked list 

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
