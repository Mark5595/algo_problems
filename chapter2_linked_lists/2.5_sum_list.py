import cc_linked_list as l

# You have two numbers represented by a ll, where each node contains
# a single digit. The digits are stored in reversed order, such that
# the 1's digit is at the head of the list. Write a function that
# adds the two numbers and returns the sum as a linked list


def sum_list_help(l1, l2, carry_over):
    # base case
    if (l1 == None and l2 == None):
        return None

    # get the values
    l1_val = 0
    l2_val = 0
    if(l1):
        l1_val = l1.data
    if(l2):
        l2_val = l2.data

    # sum them
    sum = l1_val + l2_val + carry_over

    digit = sum % 10
    carry = int(sum / 10)

    # we reccur down the list
    if(l1 and l2):
        return l.Node(digit, sum_list_help(l1.next, l2.next, carry))
    elif(l1):
        return l.Node(digit, sum_list_help(l1.next, l2, carry))
    else:
        return l.Node(digit, sum_list_help(l1, l2.next, carry))


def sum_list(l1, l2):
    '''
    function to sum two lists that are in reverse order.
    l1 is the first list to sum
    l2 the second list
    returns a loDigits
    '''
    return sum_list_help(l1, l2, 0)


list1 = l.Node(7, l.Node(1, l.Node(6, None)))
list2 = l.Node(5, l.Node(9, l.Node(2, None)))
listExp = l.Node(2, l.Node(1, l.Node(9, None)))

sum_list(list1, list2).to_string()
assert sum_list(list1, list2).to_string() == listExp.to_string()
assert sum_list(list2, list1).to_string() == sum_list(list1, list2).to_string()
assert sum_list(list1, None).to_string() == list1.to_string()
assert sum_list(None, list1).to_string() == list1.to_string()
print("sum list basic tests passed")
