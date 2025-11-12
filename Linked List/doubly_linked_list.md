# 🔍 Doubly Linked List problems - Easy

### 🟩 1. Inserting a node into doubly linked list

#### Subproblem 1: Inserting at a pos

**Code (Python):**
```python
    def insertAtPos(self, head, p, x):
        pos = 0
        curr = head
        newNode = Node(x)
        
        while pos!=p:
            if curr==None:
                return head
            curr = curr.next
            pos+=1
            
        if curr.next is None:
            curr.next = newNode
            newNode.prev = curr
        else:
            newNode.next = curr.next
            newNode.prev = curr
            
            curr.next.prev = newNode
            curr.next = newNode
            
        return head
```

#### Subproblem 2: Inserting at the end
**Approach:**  Traverse the linked list and insert at the end

**Code (Python):**
```python
def insert_end(head, new_data):
  	
    new_node = Node(new_data)
    if head is None:
        head = new_node
    else:
        curr = head
        while curr.next is not None:
            curr = curr.next
        
        curr.next = new_node
        new_node.prev = curr
    
    return head
```

### 🟩 2. Deleting a node

**Code (Python):**
```python
    def delPos(self, head, x):
        pos = 1
        curr = head
        
        if x==1:
            if curr.next is None:
                return None
            else:
                curr.next.prev = None
                return curr.next
                
        while (x-1)!=pos:
            curr = curr.next
            pos += 1
        
        delNode = curr.next
        curr.next = delNode.next
        if delNode.next:
            delNode.next.prev = curr
            
        return head
```

### 🟩 3. Reverse linked list - https://leetcode.com/problems/delete-node-in-a-linked-list/description/

**Code (Python):**
```python
    def reverse(self, head):
        prev = None
        curr = head
        
        while curr is not None:
            curr.prev, curr.next = curr.next, curr.prev
            prev = curr
            curr = curr.prev
            
        return prev
```
