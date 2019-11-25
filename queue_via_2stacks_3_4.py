#3.4 stack impl with two queue

#DATA def
# A Thing is an Object

class MyQueue():
    def __init__(self):
        self.unprocStack = []
        self.procStack = []

    def push(self, thing):
        '''
        Thing -> void (adds to queue)
        '''
        self.unprocStack.append(thing)
    def pop(self):
        '''
        void -> MaybeThing
        None is provided if this is empty (i.e. len == 0)
        '''
        if self.len() == 0:
            return None
        #we having something that we must return and remove
        if len(self.procStack) == 0:
            self._proc()

        return self.procStack.pop()

    def _proc(self):
        '''
        private function to do proccessing when the procStack is empty
        '''
        if len(self.procStack) > 0:
            raise Exception("_proc should only be called when the procStack is empty!")
        end =  len(self.unprocStack)
        for i in range(0, end):
            self.procStack.append(self.unprocStack.pop())



    def len(self):
        '''
        void -> int
        '''
        return len(self.unprocStack) + len(self.procStack)

def Test1():
    print("--- Running Tests --- ")
    qu = MyQueue()
    assert qu.len() == 0
    assert qu.pop() is None
    qu.push("a")
    qu.push("b")
    qu.push("c")
    assert qu.pop() == "a"
    qu.push("d")
    assert qu.pop() == "b"
    assert qu.pop() == "c"
    qu.push("2")
    assert qu.pop() == "d"
    assert qu.pop() == "2"
    print("--- DONE! ---")

Test1()
