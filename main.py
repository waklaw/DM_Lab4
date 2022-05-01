from prettytable import PrettyTable


def getFile():
    text = []
    with open("data.txt", "r") as file:
        lines = file.readlines()
        for i in lines:
            text.append(i.replace('\n', ''))
    for i in range(len(text)):
        text[i] = text[i].split(" ")
    return text


class Graph:
    def __init__(self, graph):
        self.graph = graph
        self.ROW = len(graph)

    def BFS(self, s, t, parent):
        visited = [False] * self.ROW
        queue = [s]

        visited[s] = True

        while queue:
            u = queue.pop(0)
            for ind, val in enumerate(self.graph[u]):
                if visited[ind] == False and val > 0:
                    queue.append(ind)
                    visited[ind] = True
                    parent[ind] = u
                    if ind == t:
                        return True

        return False

    def FordFulkerson(self, source, sink):
        parent = [-1] * (self.ROW)

        max_flow = 0

        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            while s != source:
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]

            max_flow += path_flow
            v = sink
            while v != source:
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return max_flow


if __name__ == '__main__':
    array = getFile()
    array = [[int(j) if '.' not in j else float(j) for j in i] for i in array]
    numberOfNodes = int(array[0][0])
    matrix = array[1:]

    table = PrettyTable([chr(i) for i in range(65, 65 + numberOfNodes)])
    for i in matrix:
        table.add_row(i)
    print(table)

    graph = Graph(matrix)
    print('Max flow:', graph.FordFulkerson(0, 5))
