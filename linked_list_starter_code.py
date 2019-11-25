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
