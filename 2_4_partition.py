class Node:
    def __init__(self, data=0, next=None):
    # initializes the node
        self.data = data
        self.next = next

    def __str__(self):
        return str(self.data)

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.data == other.data and self.next == other.next
        else:
            return False

def printList(head):
# prints the entire list
    while(head):
        print(head, "->",)
        head=head.next

#2.4 Partition: write code to Partition a linked list around a value x,
#such that all nodes less than x come before all nodes greater than x or equal to x.
#if x is contained within the list, the values of x only need to be after the
#elms less than x. the partition element x can appear anywher in the right..
#it does not need to appear in between the left and right.
def app(l1, l2):
    if(l1 == None):
        return l2
    return Node(l1.data, app(l1.next, l2))

# def reverse(ll):
#     if (ll == None):
#         return ll
#     return Node(reverse(ll.next), Node(ll.data, None))

def partition(ll, x):
    def partition_help(current, left, right):
        if (current == None):
            return app(left, right)
        elif(current.data < x):
            left = Node(current.data, left)
        else:
            right = Node(current.data, right)
        return partition_help(current.next, left, right)
    return partition_help(ll, None, None)


#Tests/Example
testList = Node(3, Node(5, Node(8, Node(5, Node(10, Node(2, Node(1)))))))
printList(partition(testList, 5))
# assert (test1Exp == testList)
#
# try:
#     remove_middle_elm(None)
# except Exception as e:
#     print("pass ex 1")
#
# try:
#     remove_middle_elm(Node())
# except Exception as e:
#     print("pass ex 2")
