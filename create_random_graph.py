"""
    Hackathon Google DSU-NU 2022
    Edge Weighted Digraph
    Hua Wang/ Triet Ngo/Senay Tilahun
"""

from graph import *


def create_random_graph(num_vert: int, num_edge: int):
    """
    Create a random graph with the defined number of edges and nodes.
    :param num_vert: number of nodes
    :param num_edge: number of edges
    :return: the randomly generated graph
    """
    graph = EdgeWeightDigraph()

    # add vertices
    for i in range(num_vert):
        graph.add_vertex(i)

    # add edges
    i = 0
    visited = {}
    while i < num_edge:
        from_v = randint(0, num_vert-1)
        to_v = randint(0, num_vert - 1)

        if from_v not in visited:
            visited[from_v] = set()
        while to_v in visited[from_v]:
            to_v = randint(0, num_vert - 1)

        if from_v == to_v:
            continue

        visited[from_v].add(to_v)
        graph.add_edge(from_v, to_v)
        i += 1
    return graph
