def evaluation(graph_in, graph_out, edge_list_attribute_in, edge_list_attribute_out):
    edge_list_out = []

    for key in graph_out.keys():
        for value in graph_out[key]:
            edge_list_out.append((int(key), value))
    
    print("List of outgoing edges:", edge_list_out)

    edge_list_in = []

    for key_in in graph_in.keys():
        for value_in in graph_in[key_in]:
            edge_list_in.append((value_in, int(key_in)))

    #print("List of incoming edges:", edge_list_in)

    full_vertex_list = [key for key in graph_out.keys()]

    print(full_vertex_list)

    #['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

    # Lane problems
    lane_eval(graph_in, graph_out, full_vertex_list, edge_list_out, edge_list_in)
    print()

    speed_eval(graph_in, graph_out, full_vertex_list, edge_list_out, edge_list_in)
    print()

    connected_eval(graph_in, graph_out, full_vertex_list)

def lane_eval(graph_in, graph_out, full_vertex_list, edge_list_out, edge_list_in):

    for v in full_vertex_list:
        sum_lane_out = 0
        sum_lane_in = 0

        for adj_v in graph_out[v]:
            current_egde_out = (int(v), adj_v)
            #print("Current edge out:", current_egde_out)

            if current_egde_out in edge_list_out:
                edge_pos_out = edge_list_out.index(current_egde_out)
                sum_lane_out += edge_list_attribute_out[edge_pos_out][0]
            
        #print("Total lane going out of node", int(v), "is", sum_lane_out)

        for prev_v in graph_in[v]:
            current_egde_in = (prev_v, int(v))
            #print("Current edge in:", current_egde_in)

            if current_egde_in in edge_list_in:
                edge_pos_in = edge_list_in.index(current_egde_in)
                sum_lane_in += edge_list_attribute_in[edge_pos_in][0]
        
        #print("Total lane going into node", int(v), "is", sum_lane_in)
        
        if sum_lane_out < sum_lane_in:
            print("Node", v, "is a lane bottleneck")
        else:
            print("Node", v, "is not a lane bottleneck.")
    

def speed_eval(graph_in, graph_out, full_vertex_list, edge_list_out, edge_list_in):

    for v in full_vertex_list:
        max_speed_in = 0
        min_speed_out = 1000

        for adj_v in graph_out[v]:
            current_egde_out = (int(v), adj_v)
            #print("Current edge out:", current_egde_out)

            if current_egde_out in edge_list_out:
                edge_pos_out = edge_list_out.index(current_egde_out)
                min_speed_out = min(min_speed_out, edge_list_attribute_out[edge_pos_out][1])
            
        #print("Min speed going out of node", int(v), "is", min_speed_out)

        for prev_v in graph_in[v]:
            current_egde_in = (prev_v, int(v))
            #print("Current edge in:", current_egde_in)

            if current_egde_in in edge_list_in:
                edge_pos_in = edge_list_in.index(current_egde_in)
                max_speed_in = max(max_speed_in, edge_list_attribute_in[edge_pos_in][1])
        
        #print("Max speed going into node", int(v), "is", max_speed_in)
        
        if max_speed_in > min_speed_out:
            print("Node", v, "is a flow bottleneck")
        else:
            print("Node", v, "is not a flow bottleneck.")


def connected_eval(graph_in, graph_out, full_vertex_list):

    for i in full_vertex_list:
        if len(graph_out[i]) == 0 or len(graph_in[i]) == 0:
            print("Node", i, "is not an interconnectedness bottleneck")
        elif len(graph_out[i]) > 2 or len(graph_in[i]) > 2 :
            print("Node", i, "is an interconnectedness bottleneck")
        else:
            print("Node", i, "is not an interconnectedness bottleneck")


graph_out = {
    "0" : [1, 4],
    "1" : [0, 2],
    "2" : [1, 3],
    "3" : [2],
    "4" : [0, 5],
    "5" : [4, 6, 8, 11],
    "6" : [5, 7],
    "7" : [],
    "8" : [5, 9],
    "9" : [8],
    "10" : [6],
    "11" : [1],
    "12" : [10],
    "13" : [10],
    "14" : [8]
}

graph_in = {
    "0" : [1, 4],
    "1" : [0, 2, 4],
    "2" : [1, 3],
    "3" : [2],
    "4" : [0, 5],
    "5" : [4, 6, 8],
    "6" : [5, 10],
    "7" : [6],
    "8" : [5, 9, 14],
    "9" : [8],
    "10" : [12, 13],
    "11" : [5],
    "12" : [],
    "13" : [],
    "14" : []
}

# each edge = (from, to, lanes, speed_limit)

edge_list_attribute_out = [
    (1, 25), (2, 20), (3, 25), (1, 25), (2, 25), (3, 5), \
    (3, 5), (2, 20), (3, 25), (1, 25), (2, 40), (3, 30), \
    (3, 20), (2, 50), (3, 65), (2, 30), (2, 10), (3, 10), \
    (3, 55), (3, 20), (1, 40), (3, 70), (2, 60)
]

edge_list_attribute_in = [
    (3, 25), (2, 20), (1, 25), (2, 25), (3, 20), (1, 25), \
    (3, 5), (3, 5), (2, 20), (1, 25), (3, 25), (2, 50), \
    (2, 30), (2, 40), (3, 55), (3, 65), (3, 30), (3, 10), \
    (2, 60), (2, 10), (1, 40), (3, 70), (3, 20)
]

evaluation(graph_in, graph_out, edge_list_attribute_in, edge_list_attribute_out)