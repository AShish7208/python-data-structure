class LinkedList():
    def __init__(self):
        self.head = None

    def append(self,value):
        if self.head is None:
            self.head = Node(value)
        else:
            current_node = self.head
            while current_node.next is not none:
                current_node = current_node.next
            current_node.next = Node(value)


    def show_element(self):
        current = self.head
        while current is not None:
            print(current.data)
            current = current.next


list2 = LinkedList()
list2.append(2)
list2.append(3)
list2.append(5)

list2.show_elements()
