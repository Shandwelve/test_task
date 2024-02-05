from typing import Self
from pprint import pprint


class Node:
    def __init__(self, value: str):
        self.value = value
        self.links = []

    def add_link(self, node: Self) -> Self:
        if node not in self.links:
            self.links.append(node)
        node.links.append(self)

        return node


class WordGraph:
    def __init__(self, nodes: list[Node]):
        self.nodes = nodes
        self.words = []

    def dfs(self, current_node: Node, path: str, visited: set):
        path += current_node.value
        visited.add(current_node)

        if self.is_word(path):
            self.words.append(path)

        for neighbor in current_node.links:
            if neighbor not in visited:
                self.dfs(neighbor, path, visited.copy())

    def find_words(self) -> list[str]:
        for node in self.nodes:
            self.dfs(node, "", set())

        return sorted(self.words)

    def is_word(self, path: str) -> bool:
        word_list = ["pop", "rom", "corn", "popcorn", "rock", "mock", "ok"]
        return path in word_list


if __name__ == "__main__":
    p1 = Node("p")
    p2 = Node("p")
    o1 = Node("o")
    c = Node("c")
    n = Node("n")
    r = Node("r")
    o2 = Node("o")
    k = Node("k")
    m = Node("m")

    p1.add_link(p2)
    p1.add_link(o1)
    p2.add_link(o1)
    p2.add_link(c)
    o1.add_link(n)
    n.add_link(r)
    o2.add_link(r)
    o2.add_link(m)
    o2.add_link(k)
    o2.add_link(c)
    c.add_link(k)

    graph = WordGraph([p1, p2, o1, c, n, r, o2, k, m])
    pprint(graph.find_words())
