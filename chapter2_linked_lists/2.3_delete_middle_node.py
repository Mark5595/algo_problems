import cc_linked_list as l

# delete a node in the middle of a ll given that node


def delete_middle_node(n):
    '''
    to delete a middle node of a ll
    n: the node
    returns: true on success and false on failure
    '''
    if (n == None | | n.next == None):
        return false
    next = n.next
    n.data = next.data
    n.next = next.next
    return true


list1 = l.Node('a', l.Node('b', l.Node('c', l.Node('d', None))))
copy = list1.copy()
delete_middle_node(copy.next.next)
exp = l.Node('a', l.Node('b', l.Node('d', None)))
assert copy.to_string() == exp.to_string()
