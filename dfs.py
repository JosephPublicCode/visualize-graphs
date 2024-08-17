class DFS: 

    def __init__(self,graph): 
        self.graph = graph
        self.order = []
        self.visit = set()


    def dfs_recursive_pre(self, v:int) -> list: 
        
        self.order.append(v)
        self.visit.add(v)
        for nei in self.graph[v]: 
            if nei not in self.visit: 
                self.dfs_recursive_pre(nei)
        return self.order

    

    def dfs_recursive_post(self, v:int) -> list: 
        self.visit.add(v)
        for nei in self.graph[v]: 
            if nei not in self.visit: 
                self.dfs_recursive_post(nei)
        self.order.append(v)
        
        return self.order

    def dfs_iterative_pre(self, v:int) -> list: 

        stack = []
        stack.append(v)
        self.visit.add(v)

        while stack: 
            v = stack.pop()
            self.order.append(v)
            self.visit.add(v)
            for nei in self.graph[v]: 
                if nei not in self.visit: 
                    stack.append(nei)
                   
        return self.order


    def dfs_iterative_post(self, v:int) -> list: 

        stack = []
        stack.append(v)

        while stack: 
            v = stack.pop()

            if v not in self.visit: 
                stack.append(v)
                self.visit.add(v)
                
                for nei in self.graph[v]: 
                    if nei not in self.visit: 
                        stack.append(nei)
                        
                        
            else: 
                self.order.append(v)
        return self.order