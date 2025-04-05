class LinkedList:
    def __init__(self, nodes=None):
        self.head = None

        if nodes is not None:
            self.head = Node(nodes.pop(0))

            node = self.head
            while len(nodes)>0:
                node.next = Node(nodes.pop(0))
                node = node.next

    def addFirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def addLast(self, data):
        if self.head == None:
            self.head = Node(data)
            return
        
        node = self.head

        while node.next is not None:
            node = node.next

        node.next = Node(data)

    def __repr__(self):
        node = self.head
        nodes = []
        while node is not None:
            nodes.append(str(node.data))
            node = node.next

        nodes.append('None')
        return '-> '.join(nodes)
    
    def __iter__(self):
        node = self.head

        while node is not None:
            yield node.data
            node = node.next

class Node:
    def __init__(self, data):
        self.data = data
        self.previous = None
        self.next = None

    def __repr__(self):
        return self.data
    
if __name__ == "__main__":
    ll = LinkedList([3,4,5])
    ll.addLast(1)
    ll.addLast(2)
    ll.addFirst(7)
    print(ll)