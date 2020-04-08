all_edge=[("A","B"),("A","C"),("B","D"),("C","D"),("C","E"),("D","E")]


class Graph:
    def __init__(self,Nodes,is_directed=False):
        self.nodes=Nodes
        self.adj_list={}
        self.is_directed=is_directed

        for node in self.nodes:
            self.adj_list[node]=[]
    def add(self,u,v):
        self.adj_list[u].append(v)
        if not self.is_directed:
            self.adj_list[v].append(u)
    def degree(self,v):
        count=0
        for i in self.adj_list[v]:
            count=count+1
        print(count)
    def print(self):
        for node in self.nodes:
            print(node,"->",self.adj_list[node])
node=["A","B","C","D","E"]
graph=Graph(node,is_directed=True)
for u,v in all_edge:
    graph.add(u,v)
for v in node:
    graph.degree(v)
graph.print()
