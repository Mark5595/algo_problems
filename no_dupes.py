#June 28 2018 Programing Problems


class Node:
    ''''
    Here a Node is One of None or Node
    ''''

    def __init__(self,first, rest):
        self.first = first
        self.rest = rest
    def eq(self, that):
        '''
        checks to see if the values in self and that are the same
        '''
        if(self.rest == None or that.rest == None):
            return self.first == that.first and that.rest == self.rest
        return self.first == that.first and self.rest.eq(that.rest)
    def copy(self):
        if(self.rest == None):
            return Node(self.first, self.rest)
        else:
            return Node(self.first, self.rest.copy())

    def __str__(self):
        if self.rest == None:
            return str(self.first)
        else:
            return str(self.first) + ' ' +  str(self.rest)


def inList(elm, ll):
    '''
    Recrusive, is the elm in ll?
    returns: boolean, anwsering the question
    '''
    if ll == None:
        return False
    else:
        return elm == ll.first or inList(elm, ll.rest)


#Remove DUPs
def rm_dups_rec(ll):
    '''
    returns a new ll with no dupes. O(n^2) but more memory eff O(1).
    '''
    if ll == None:
        return None
    elif inList(ll.first, ll.rest):
        #print("here")
        return rm_dups_rec(ll.rest)
    else:
        return Node(ll.first, rm_dups_rec(ll.rest))


def rm_dups_in_place_non_rec(ll):
    '''
    removes in place and non-Recrusive, O(n)
    '''
    if ll == None:
        return ll
    #non-empty
    prev = ll
    seen = set()
    while ll:
        if ll.first in seen:
            prev.rest = ll.rest
        else:
            prev = ll

        seen.add(ll.first)

        ll = ll.rest


ll = Node(10, Node(20, Node(1, Node(10, None))))
ll2 = Node(20, Node(1,  Node(10, None)))
ll3 = Node(10, Node(20, Node(1, None)))

ll4 = Node(10, Node(20, Node(1, Node(10, ll))))
rv = rm_dups_rec(ll)
assert rv.eq(ll2)
assert not rv.eq(ll)
rv = ll.copy();
rm_dups_in_place_non_rec(rv)
assert rv.eq(ll3)
assert not rv.eq(ll)

print(ll4)
rv = rm_dups_rec(ll4)
print(rv)
assert rv.eq(ll2)
assert not rv.eq(ll)

rv = ll4.copy();
rm_dups_in_place_non_rec(rv)
print(rv)
assert rv.eq(ll3)
assert not rv.eq(ll)

rv = rm_dups_rec(None)
assert rv == None

rv = None
rm_dups_in_place_non_rec(None)
assert None == rv
