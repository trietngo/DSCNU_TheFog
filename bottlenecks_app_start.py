"""
    Hackathon Google DSU-NU 2022
    Edge Weighted Digraph
    Hua Wang/ Triet Ngo/Senay Tilahun
"""

from create_random_graph import create_random_graph
from evaluation import *


def main():
    """ Main function to test bottlenecks -
        a transit network diagnostics software

    """
    # selected random nuber of vertexes
    num_vertex = 10
    # selected random nuber of edges
    num_edges = 20
    # create a random graph
    graph = create_random_graph(num_vertex, num_edges)

    # create "to" adjacent dict
    adj_list_input = graph.get_input_vert_dict()
    # create "from" adjacent dict
    adj_list_output = graph.get_output_vert_dict()

    final_rec = main_eval(graph, adj_list_input, adj_list_output)

    for key in final_rec.keys():
        print(f"Area {key} has priority 1 urgency "
              f"with severity score of {final_rec[key][3]}: "
              f"Immediate action recommended")
        if final_rec[key][0] == 1:
            print(f"...{key} has lane bottleneck: lane consistency recommended")
        if final_rec[key][1] == 1:
            print(f"...{key} has flow bottleneck: more gradual reduction in speed limit recommended")
        if final_rec[key][2] == 1:
            print(f"...{key} has interconnectedness bottleneck: route conversion recommended")
        print()


if __name__ == '__main__':
    main()
