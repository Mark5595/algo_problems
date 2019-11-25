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
        print(head, "->")
        head=head.next

#2.3 delete middle node: Implement an algo to delete a node in the middle
#(i.e. any node but the first and loast node, not necessarily the exact
#middle). of a singally linked list, given only acess to that node
def remove_middle_elm(elm_to_remove):
    '''
    removes a non-first/last element from a ll
    elm_to_remove(Node) - the element to removes
    return: void (the list is mutated)
    '''
    if elm_to_remove == None or elm_to_remove.next == None:
         raise Exception("non-none element, non-last element")
    new_next = elm_to_remove.next.next
    elm_to_remove.data = elm_to_remove.next.data
    elm_to_remove.next = new_next

#Tests/Example
testList = Node('a', Node('b', Node('c', Node('d', Node('e', Node('f'))))))
test1Exp = Node('a', Node('b', Node('d', Node('e', Node('f')))))
remove_middle_elm(testList.next.next)
printList(testList)
assert (test1Exp == testList)

try:
    remove_middle_elm(None)
except Exception as e:
    print("pass ex 1")

try:
    remove_middle_elm(Node())
except Exception as e:
    print("pass ex 2")
