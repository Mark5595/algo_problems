#BFS and DFS

# BFS -> QUEUE
# DFS -> STACK


#defualt dictionary creates an entry if something is not found
from collections import defaultdict
from collections import deque
class MyGraph:
    '''
    Simple unweight graph that has graph traversal capablities!
    '''


    def __init__(self):
        ''' constructor '''
        self.graph = defaultdict(list) #key -> mtlist


    def addEdge(self, fromMe, to):
        ''' add a directed edge to self '''
        self.graph[fromMe].append(to) # from | to, ...

    def _fsHelp(self, startNode, worklist):
        '''
            startNode : int repsenting the start start node
            worklist: the list of things to work on pass in a stack or queue
            return:

            generatic search helper method
            worklist is a Queue (BFS) or Stack (DFS)
        '''
        visitedNodes = set()

        worklist.add(startNode)
        visitedNodes.add(startNode)

        while worklist.notEmpty():
            curr = worklist.remove()
            print(curr, end = " ")

            for buddy in self.graph[curr]:
                if buddy not in visitedNodes:
                    worklist.add(buddy)
                    visitedNodes.add(buddy)

    def DFS(self, startNode):
        self._fsHelp(startNode, self.Stack())

    def BFS(self, startNode):
        self._fsHelp(startNode, self.Queue())

    class Queue:
        def __init__(self):
            self.items = deque([])

        def remove(self):
            return self.items.popleft()

        def add(self, toAdd):
            self.items.append(toAdd)

        def notEmpty(self):
            return len(self.items) != 0

    class Stack:
        def __init__(self):
            self.items = []

        def remove(self):
            return self.items.pop()

        def add(self, toAdd):
            self.items.append(toAdd)

        def notEmpty(self):
            return len(self.items) != 0
def runTests():
    g = MyGraph()
    g.addEdge(0, 1)
    g.addEdge(0, 4)
    g.addEdge(0, 5)
    g.addEdge(5, 6)

    g.addEdge(1, 3)
    g.addEdge(1, 4)


    g.addEdge(2, 1)

    g.addEdge(3, 2)
    g.addEdge(3, 4)

    print("DFS")
    g.DFS(0)

    print("BFS")
    g.BFS(0)


#Tests
runTests()
