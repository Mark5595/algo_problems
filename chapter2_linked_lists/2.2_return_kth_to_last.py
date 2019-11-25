import cc_linked_list as l

#Implement an algo to find the k-th to last element in a singally linked list
def k_to_last(n, k):
    '''
    n is the node, k is the number to Last
    '''
    if(n == None):
        return n

    head = n
    last = n
    #first we will find the k-th element
    for _i in range(0, k):
        if(head.next == None ):
            return None
        head = head.next

    #now we move the window down the list
    while(head.next):
        head = head.next
        last = last.next

    #finally return the node
    return last


#Examples
list1 = l.Node(0, l.Node(1, l.Node(2, l.Node(3, None))))
list1.printList()
assert k_to_last(list1, 0).data == 3
assert k_to_last(list1, 1).data == 2
assert k_to_last(list1, 2).data == 1
assert k_to_last(list1, 3).data == 0
assert k_to_last(list1, 4) == None

list2 = l.Node(0, None)
assert k_to_last(list2, 0).data == 0
assert k_to_last(list2, 1) == None
