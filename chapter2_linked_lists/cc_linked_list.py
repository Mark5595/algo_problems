class Node:
    def __init__(self, data=0, next=None):
        # initializes the node
        self.data = data
        self.next = next

    def printList(self):
        print(self)
        if(self.next):
            self.next.printList()

    def __str__(self):
        return str(self.data)

    def to_string(self):
        if self.next:
            return str(self.data) + '->' + self.next.to_string()
        else:
            return str(self.data)

    def copy(self):
        if self.next:
            return Node(self.data, self.next.copy())
        else:
            return Node(self.data, self.next)
