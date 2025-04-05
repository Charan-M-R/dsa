class LinkedList:
    def __init__(self, nodes=None):
        self.head = None
        
        if nodes is not None and len(nodes)>0:
            node = Node(nodes.pop(0))
            self.head = node

            while len(nodes) > 0:
                node.next = Node(nodes.pop(0))
                node = node.next


    def __repr__(self):
        node = self.head
        nodes = []
        while node!=None:
            nodes.append(str(node.data)) 
            node = node.next

        nodes.append("None")
        return " -> ".join(nodes)
    

    def __iter__(self):
        node = self.head

        while node is not None:
            yield node.data
            node = node.next

    def addFirst(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def addLast(self,data):
        node = self.head

        if node is None:
            self.head = Node(data)
            return

        while node.next is not None:
            node = node.next

        node.next = Node(data)

    def removeNode(self,data_remove):
        prev = self.head

        if prev is None:
            print('Data not found, linked list is empty')
            return

        next = prev.next

        if prev.data == data_remove:
            print('Data removed')
            self.head = next
            return

        while next is not None:
            if next.data == data_remove:
                prev.next = next.next
                print('Data removed')
                return
            
            prev = next
            next = next.next
            
        print('Data not found')
        
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return self.data

if __name__ == "__main__":
    ll = LinkedList()
    node1 = Node('hello')
    node2 = Node(2)
    node3 = Node(3)

    ll.head = node1
    node1.next = node2
    node2.next = node3

    print(ll)

    ll2 = LinkedList([1,2,3,4])
    print(ll2)

    for i in ll2:
        print(i)

    ll2.addFirst(5)
    print(ll2)

    ll2.addLast(6)
    print(ll2)

    ll2.removeNode(2)
    print(ll2)

    ll2.removeNode(7)
    print(ll2)