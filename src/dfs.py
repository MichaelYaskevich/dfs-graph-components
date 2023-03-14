from parso.parser import Stack
import sys


class Node:
    def __init__(self, vertex):
        self.vertex = vertex
        self.next = None
        self.previous = None


class LinkedList:
    def __init__(self):
        self.last: Node = None
        self.first: Node = None
        self.size = 0

    def popleft(self):
        left = self.first
        self.remove(left)
        return left.vertex

    def appendright(self, vertex):
        node = Node(vertex)
        if self.last is None:
            self.last = node
            self.first = node
        else:
            node.previous, self.last.next = self.last, node
            self.last = node
        self.size += 1

    def remove(self, vertex: Node):
        if vertex.next is None and vertex.previous is None:
            self.last = None
            self.first = None
        elif vertex.next is None:
            vertex.previous.next = None
            self.last = vertex.previous
        elif vertex.previous is None:
            vertex.next.previous = None
            self.first = vertex.next
        else:
            vertex.previous.next = vertex.next
            vertex.next.previous = vertex.previous
        self.size -= 1


class Graph:
    def __init__(self):
        self.adjacency_lists = []
        self.not_visited = LinkedList()
        self.vertices = [Node(-1)]

    def visit(self, vertex: int):
        self.not_visited.remove(self.vertices[vertex])


def read(filename):
    with open(filename, 'r') as f:
        graph = Graph()
        try:
            n = int(f.readline())
        except ValueError:
            return graph

        graph.adjacency_lists.append(-1)
        for line in f:
            graph.adjacency_lists.append(
                [v + 1 for v, x in enumerate(line.split()) if x == '1'])
        for i in range(1, n + 1):
            graph.not_visited.appendright(i)
            graph.vertices.append(graph.not_visited.last)

    return graph


def find_components(graph):
    components = []
    while graph.not_visited.size != 0:
        components = dfs(graph, components)

    return components


def dfs(graph: Graph, components):
    stack = Stack()
    components.append([])

    start_v = graph.not_visited.popleft()
    stack.append(start_v)
    components[-1].append(start_v)

    while len(stack) != 0:
        v = stack.pop()
        for w in graph.adjacency_lists[v]:
            if w not in components[-1]:
                stack.append(w)
                components[-1].append(w)
                graph.visit(w)

    return components


def write(components):
    with open(OUTPUT, 'w') as f:
        f.write(str(len(components)) + '\n')
        for com in components:
            for v in com:
                f.write(str(v) + ' ')
            f.write('0' + '\n')


if __name__ == '__main__':
    INPUT = sys.argv[1]
    OUTPUT = sys.argv[2]
    write(find_components(read(INPUT)))
