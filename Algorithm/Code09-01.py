class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = [[0 for _ in range(size)] for _ in range(size)]

G1 = Graph(4)
E1 = [(0, 1), (0, 2), (0, 3), (1, 2), (2, 3)]

for (i, j) in E1:
    G1.graph[i][j] = G1.graph[j][i] = 1

print('## G1 무방향 그래프 ##')
for row in range(G1.size):
    for col in range(G1.size):
        print(G1.graph[row][col], end=' ')
    print()

G3 = Graph(4)
E3 = [(0, 1), (0, 2), (3, 0), (3, 2)]

for (i, j) in E3:
    G3.graph[i][j] = 1

print('## G3 방향 그래프 ##')
for row in range(G3.size):
    for col in range(G3.size):
        print(G3.graph[row][col], end=' ')
    print()
    