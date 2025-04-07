class BFSGraph:
    def __init__(self, size):
        self.size = size
        self.adj_matrix = [[0]*size for _ in range(size)]
        self.vertex_data = ['']*size

    def add_vertex_data(self, vertex, data):
        if 0<=vertex<self.size:
            self.vertex_data[vertex] = data

    def add_edge(self, vertex1, vertex2):
        if 0<=vertex1<self.size and 0<=vertex2<self.size:
            self.adj_matrix[vertex1][vertex2] = 1
            self.adj_matrix[vertex2][vertex1] = 1

    def print_graph(self):
        print('Adjacency matrix: ')
        for row in self.adj_matrix:
            print(' '.join(map(str, row)))

        print('\nVertex data: ')
        for vertex,data in enumerate(self.vertex_data):
            print(f"Vertex {vertex}: {data}")

    def bfs_utils(self, visited, q):
        v = q.pop(0)
        print(self.vertex_data[v], end=' ')
        visited[v] = True

        for i in range(self.size):
            if self.adj_matrix[v][i] == 1 and not visited[i]:
                q.append(i)
                visited[i] = True
                
        if q!=[]:
            self.bfs_utils(visited, q)

    def bfs(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        visited = [False]*self.size
        queue = [start_vertex]
        self.bfs_utils(visited, queue)

    def bfs_iter(self, start_vertex_data):
        start_vertex = self.vertex_data.index(start_vertex_data)
        visited = [False]*self.size
        queue = [start_vertex]

        while queue:
            v = queue.pop(0)
            print(self.vertex_data[v], end=' ')
            visited[v] = True

            for i in range(self.size):
                if self.adj_matrix[v][i] == 1 and not visited[i]:
                    queue.append(i)
                    visited[i] = True

g = BFSGraph(7)

g.add_vertex_data(0, 'A')
g.add_vertex_data(1, 'B')
g.add_vertex_data(2, 'C')
g.add_vertex_data(3, 'D')
g.add_vertex_data(4, 'E')
g.add_vertex_data(5, 'F')
g.add_vertex_data(6, 'G')

g.add_edge(3, 0)  # D - A
g.add_edge(0, 2)  # A - C
g.add_edge(0, 3)  # A - D
g.add_edge(0, 4)  # A - E
g.add_edge(4, 2)  # E - C
g.add_edge(2, 5)  # C - F
g.add_edge(2, 1)  # C - B
g.add_edge(2, 6)  # C - G
g.add_edge(1, 5)  # B - F

g.print_graph()  
g.bfs('B')
print()
g.bfs_iter('B')