import cc_linked_list as ll

# Implement a function to check if a ll is a palindrome


def rev(l):
    '''function to reverse the list into a new list
    Args:
        l (Node): the singally linked list
    Return:
        Node: a *new* linked list reversed
    '''
    if (l == None):
        return l

    last = ll.Node(l.data)
    l = l.next
    while (l):
        last = ll.Node(l.data, last)
        l = l.next
    return last


def palindrome_list_help(l, l_rev):
    if (l == None and l_rev == None):
        return True
    elif (l != None and l_rev != None and l.data == l_rev.data):
        return palindrome_list_help(l.next, l_rev.next)
    else:
        return False


def palindrome_list(l):
    '''function that checks if a ll is a palindrome
    Args:
        l (Node): the singally linked list

    Return:
        booL: anwser to the question, is l a palindrome list?
    '''
    return palindrome_list_help(l, rev(l))


# Examples
assert palindrome_list(None) == True
assert palindrome_list(ll.Node('a')) == True
assert palindrome_list(ll.Node('a', ll.Node('b'))) == False
assert palindrome_list(ll.Node('b', ll.Node('a'))) == False
assert palindrome_list(ll.Node('b', ll.Node('a', ll.Node('a')))) == False
assert palindrome_list(ll.Node('b', ll.Node('a', ll.Node('b')))) == True
assert palindrome_list(ll.Node('b', ll.Node('b', ll.Node('b')))) == True
assert palindrome_list(
    ll.Node('b', ll.Node('b', ll.Node('b', ll.Node('b'))))) == True
