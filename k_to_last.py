#A Linked List is one of:
# cons(elm, LinkedList)
# Mt

class Mt:
    def __init__(self):
        pass

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return True
        else:
            return False
    def copy(self):
        return Mt()
    def length(self):
        return 0
    def get(self, index):
        return "ERROR"
    def __str__(self):
        return 'null'

class Cons:
    def __init__(self,first, rest):
        self.first = first
        self.rest = rest
    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.first == other.first and self.rest == other.rest
        else:
            return False
    def copy(self):
        return Cons(self.first, self.rest.copy())
    def length(self):
        return 1 + self.rest.length()
    def get(self, index):
        if index == 0:
            return self.first
        elif(index < 0):
            return "ERROR"
        else:
            return self.rest.get(index - 1)
    def __str__(self):
        return str(self.first) + '->' +  str(self.rest)




#Tests for Linked List
mt = Mt()
ll = Cons(1, mt)
ll2 = Cons(1, mt)
assert ll == ll2
ll3 = Cons(1, Cons(2, Mt()))
assert ll != ll3
assert ll3 != ll2
assert ll3 == ll3.copy()

#2.2 Kth to Last: Implement an algo to find the kth to last element
#in a singally linked list
def k_to_last(ll, k):
    '''
    to get the kth to last elm
    throws an error (for testing ease the string "ERROR") if k is invalid
    (i.e the number is less than 0 or k is larger than the length of the list)
    '''

    if k < 0:
        return "ERROR"
    k_index = ll.length() - k - 1
    return ll.get(k_index)

assert k_to_last(mt, 10) == "ERROR"
assert k_to_last(ll2, 0) == 1
assert k_to_last(ll3, 1) == 1
assert k_to_last(ll3, 0) == 2
assert k_to_last(ll3, 100) == "ERROR"

def k_to_last_v2(ll, k):
    '''
    non-Recrusive sliding fixed window
    '''
    k_th_elm = ll
    runner = ll

    for _i in range(0, k + 1):
        if runner.rest == Mt():
            return None
        runner = runner.rest

    while runner != Mt():
        runner = runner.rest
        k_th_elm = k_th_elm.rest

    return k_th_elm.first

assert k_to_last_v2(ll2, 0) == 1
assert k_to_last_v2(ll3, 1) == 1
assert k_to_last_v2(ll3, 0) == 2
