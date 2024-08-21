from collections import deque

class BFS: 

    def __init__(self,graph): 
        self.graph = graph
        self.order = []
        self.visit = set()

    def bfs(self, v): 
        q = deque()
        q.append(v)
        self.visit.add(v)
        self.order.append(v)

        while q: 
            v = q.popleft()
            self.order.append(v)
            for nei in self.graph[v]: 
                if nei not in self.visit: 
                    q.append(nei)
                    self.visit.add(nei)
        return self.order


