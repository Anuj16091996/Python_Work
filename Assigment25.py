class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def reverse(self, head, k):

        if head == None:
            return None
        current = head
        next = None
        prev = None
        count = 0

        # Reverse first k nodes of the linked list
        while current is not None and count < k:
            next = current.next
            current.next = prev
            prev = current
            current = next
            count += 1
        if next is not None:
            head.next = self.reverse(next, k)
        return prev

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def printList(self):
        temp = self.head
        while(temp):
            print (temp.data)
            temp = temp.next

list = LinkedList()

list.push(5)
list.push(4)
list.push(3)
list.push(2)
list.push(1)

k=2
print("linked list")
list.printList()

list.head = list.reverse(list.head, k)
print("\nReversed list k="+str(k))
list.printList()




