class Graph:
    """

    """

    def __init__(self, initial_graph=None):
        if initial_graph is None or not self._is_valid_graph(initial_graph):
            self.graph = dict()
        else:
            self.graph = initial_graph

    @staticmethod
    def _is_valid_graph(initial_graph):
        if not isinstance(initial_graph, dict):
            return False
        elif any([isinstance(x, set) for x in initial_graph.values()]):
            return False
        else:
            if set().union(*initial_graph.values()) <= set(initial_graph.keys()):
                return True
            else:
                return False

    def add_vertex(self, vertex):
        if vertex in self.graph.keys():
            pass
        else:
            self.graph[vertex] = set()

    def add_edge(self, v1, v2):
        if v1 in self.graph.keys() and v2 in self.graph.keys() and v1 != v2:
            if v2 in self.graph[v1]:
                print('edge already in graph')
            else:
                self.graph[v1].add(v2)
                self.graph[v2].add(v1)
        else:
            print('cannot add edge!')

    def delete_vertex(self, vertex):
        try:
            for v in self.graph[vertex]:
                self.graph[v].remove(vertex)
            del self.graph[vertex]
        except KeyError as e:
            print('vertex doesnt seem to exist')
            print(e)

    def delete_edge(self, v1, v2):
        try:
            self.graph[v1].remove(v2)
            self.graph[v2].remove(v1)
        except KeyError as e:
            print('edge doesnt seem to exist')
            print(e)

    def get_neighbours(self, vertex):
        try:
            return self.graph[vertex]
        except KeyError as e:
            print('vertex doesnt seem to exist')
            print(e)

    def dfs(self, vertex, visited=None):
        if visited is None:
            visited = set()
        if vertex not in self.graph.keys():
            print('vertex not in graph')
        yield vertex
        visited.append(vertex)
        for v in self.graph[vertex]:
            self.dfs(vertex, visited)

    def bfs(self, vertex):
        visited = {vertex}
        queue = []
        if vertex not in self.graph.keys():
            print('vertex not in graph')
        queue.append(vertex)
        while len(queue) > 0:
            v = queue.pop()
            yield v
            for v2 in self.graph[v]:
                if v2 not in visited:
                    queue.append(v2)
