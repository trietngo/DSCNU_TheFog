"""
    Hackathon Google DSU-NU 2022
    Edge Weighted Digraph
    Hua Wang/ Triet Ngo/Senay Tilahun
"""

import random
from random import randint

speed = [5 * i for i in range(5, 17)]


class Edge:
    """
    Edge object containing all attributes, which are randomized
    """
    def __init__(self, from_v, to_v):
        self.length = randint(10, 100)
        self.lanes = randint(2, 5)
        self.speed_limit = random.sample(speed, 1)
        self.condition = random.sample([0, 1], 1)
        self.from_v = from_v
        self.to_v = to_v

    def __str__(self):
        return f"Edge from {self.from_v} to {self.to_v} has length {self.length}, " \
               f"lanes {self.lanes}, abnormal conditions {self.condition} and speed limit {self.speed_limit}"

    def get_lanes(self):
        return self.lanes
    
    def get_speed(self):
        return self.speed_limit


class Vertex:
    """
    Vertex Object
    """

    def __init__(self, key):
        self.id = key
        # a dictionary of vertices: key is to_id, value is the edge
        self.edgeTo = {}
        self.edgeFrom = {}

    def __str__(self):
        return f"{self.id} connected to: {[x for x in self.edgeTo.keys()]}"

    def add_edgeTo(self, to_id, edge: Edge):
        """
        add the edge to the vertex
        :param to_id: the vertex_id
        :param edge: teh edge to add
        :return:
        """
        self.edgeTo[to_id] = edge

    def add_edgeFrom(self, from_id, edge: Edge):
        self.edgeFrom[from_id] = edge

    def get_connectionTo(self):
        return self.edgeTo.keys()

    def get_connectionFrom(self):
        return self.edgeFrom.keys()

    def get_edgeTo(self, to_id):
        """
        get the edge from the current vertex given by the to_id
        :param to_id:
        :return:
        """
        return self.edgeTo[to_id]

    def get_edgeFrom(self, from_id):
        return self.edgeFrom[from_id]

    def get_id(self):
        """
        get the id of the vertex
        :return:
        """
        return self.id


class EdgeWeightDigraph:
    """
    An edge weighted directed graph with randomized weight of edges
    """
    def __init__(self):
        self.vertex_list = {}  # a dictionary: key is vertex id, value is a vertex object
        self.num_vertices = 0

    def add_vertex(self, vertex_id):
        self.num_vertices += 1
        new_vertex = Vertex(vertex_id)
        self.vertex_list[vertex_id] = new_vertex

    def add_edge(self, from_id, to_id, edge: Edge = None):
        if from_id not in self.vertex_list:
            self.add_vertex(from_id)
        if to_id not in self.vertex_list:
            self.add_vertex(to_id)

        if edge is None:
            edge = Edge(from_id, to_id)

        self.vertex_list[from_id].add_edgeTo(to_id, edge)
        self.vertex_list[to_id].add_edgeFrom(from_id, edge)

    def __contains__(self, item):
        return item in self.vertex_list

    def get_vertex(self, vertex_id):
        """
        get a specific vertex by id
        :param vertex_id:
        :return:
        """
        if vertex_id not in self.vertex_list:
            return None
        else:
            return self.vertex_list[vertex_id]

    def get_vertices(self):
        """
        return all vertices in the graph as a list
        :return:
        """
        return list(self.vertex_list.values())

    def get_edgeTo(self, from_id, to_id):
        """
        return output edge starting from 'from_id' to 'to_id'
        :param from_id:
        :param to_id:
        :return:
        """
        return self.get_vertex(from_id).get_edgeTo(to_id)
    
    def get_edgeFrom(self, to_id, from_id):
        return self.get_vertex(to_id).get_edgeFrom(from_id)

    def get_output_vert_dict(self):
        """
        get a dictionary containing all output edges
        (keys are the vertex, values are all output edges from the vertex)
        :return:
        """
        connection = {}
        for key in self.vertex_list.keys():
            connection[key] = list(self.vertex_list[key].get_connectionTo())
        return connection

    def get_input_vert_dict(self):
        """
        get a dictionary containing all input edges
        (keys are the vertex, values are all input edges from the vertex)
        :return:
        """
        connection = {}
        for key in self.vertex_list.keys():
            connection[key] = list(self.vertex_list[key].get_connectionFrom())
        return connection

    def __iter__(self):
        return iter(self.vertex_list.values())
