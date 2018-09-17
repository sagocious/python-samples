class Graph:
    def __init__(self):
        self.dic = {}

    def addVertex(self, vert):
        if vert not in self.dic:
            self.dic[vert] = []

    def addEdge(self, start, end):
        if end not in self.dic[start]:
            self.dic[start].append(end)
        if start not in self.dic[end]:
            self.dic[end].append(start)

    def removeVertex(self, vert):
        if vert in self.dic:
            for i in self.dic.values():
                if vert in i:
                    i.remove(vert)
            del self.dic[vert]

    def findPath(graph, start, end, path = []):
        path.append(start)
        if start == end:
            return path
        if start not in graph.dic:
            return None
        for node in graph.dic[start]:
            if node not in path:
                newPath = Graph.findPath(graph, node, end, path)
                if newPath:
                    return newPath
        return None

    def __str__(self):
        s = ""
        for i in self.dic:
            s += str(i) + " : " + str(self.dic[i]) + "\n"
        return s

g = Graph()
g.addVertex(1)
g.addVertex(2)
g.addVertex(3)
g.addVertex(4)
g.addEdge(1,3)
g.addEdge(1,4)
g.addEdge(2,1)
g.addEdge(3,2)
g.addEdge(2,4)
print(g)

print(Graph.findPath(g,1,4))
