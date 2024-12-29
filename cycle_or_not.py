class Graph:
    def __init__(self,n):
        self.graph={}
        self.n=n
        for i in range(self.n):
            self.graph[i]=[]
    def edge(self, x, y):
        self.graph[x].append(y)
    
    def cycle_util(self, value, visited, restack):
        visited[value]=True
        restack[value]=True
        for node in self.graph[value]:
            if not visited[node]:
                if self.cycle_util(node,visited, restack):
                    return True
            elif restack[node]:
                return True
        restack[value]=False
        return False

    def cycle(self):
        visited=[False]*self.n
        restack=[False]*self.n
        for node in range(self.n):
            if not visited[node]:
                if self.cycle_util(node,visited,restack):
                    return True
        return False
    
graph=Graph(5)
graph.edge(0,1)
graph.edge(1,2)
graph.edge(2,3)
graph.edge(3,4)
graph.edge(3,1)

if graph.cycle():
    print("The graph is a cycle.")
else:
    print("The graph isn't a cycle.")
