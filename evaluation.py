"""
    Hackathon Google DSU-NU 2022
    Edge Weighted Digraph
    Hua Wang/ Triet Ngo/Senay Tilahun
"""


# create the main - eval function - will call lane_eval, flow_eval, Interconnected_eval, severity, recommendation
def main_eval(graph, graph_in, graph_out):
    """ Main evaluation function - takes two connected graphs and computes all evaluations and severity

        Params: 
            graph: full graph
            graph_in: graph of edges into the current vertex
            graph_out: graph of edges into the current vertex being evaluated

        returns: a dictionary of vertex_ids as keys, and a list of all evaluations/recommendations as values
    """
    # final dictionary to record most sever vertexes in graph
    final_rec = {}

    for vertex in graph_in.keys():
        # evaluate potential lane bottleneck of current vertex
        lane_score = lane_eval(graph, graph_in, graph_out, vertex)
        # print("lane score is: ", lane_score)

        # evaluates potential flow bottleneck of current vertex
        flow_score = flow_eval(graph, graph_in, graph_out, vertex)
        # print("flow score is: ", flow_score)

        # evaluates potential flow bottleneck of current vertex
        connect_score = i_connect_eval(graph_in, graph_out, vertex)
        # print(connect_score)

        # evaluates final severity score of vertex bottleneck
        severity = bottleneck_ranking(lane_score, flow_score, connect_score)

        # triages based on bottleneck severity and recommends next steps for vertex
        rec = recommendation(severity)

        # record vertex data point for further analysis
        if rec == 1:
            final_rec[vertex] = [lane_score, flow_score, connect_score, severity, rec]

    return final_rec


def lane_eval(graph, graph_in, graph_out, vertex):
    """ Lane evaluation function - takes two connected graphs and computes if there is a lane bottleneck 

        Params: 
            graph: full graph
            graph_in: graph of edges into the current vertex
            graph_out: graph of edges into the current vertex being evaluated
            vertex: current vertex/node of the graph 

        returns: 1 if lane bottleneck exists and 0 if it doesn't
    """
    # initialize the sum of lanes going into and out of the current vertex
    sum_lane_out = 0
    sum_lane_in = 0

    # Access output vertexes and compute sum of output lanes
    if vertex in graph_out.keys():
        for adj_v in graph_out[vertex]:
            sum_lane_out += graph.get_edgeTo(vertex, adj_v).get_lanes()

    # Access input vertexes and compute sum of input lanes
    if vertex in graph_in.keys():
        for adj_v in graph_in[vertex]:
            sum_lane_in += graph.get_edgeTo(adj_v, vertex).get_lanes()
    
    if sum_lane_out < sum_lane_in:
        return 1
    else:
        return 0


def flow_eval(graph, graph_in, graph_out, vertex):
    """ Flow evaluation function - takes two connected graphs and computes if there is a flow bottleneck

        Params:
            graph: full graph
            graph_in: graph of edges into the current vertex
            graph_out: graph of edges into the current vertex being evaluated
            vertex: current vertex/node of the graph

        returns: 1 if flow bottleneck exists and 0 if it doesn't
    """
    # initialize the sum of lanes going into and out of the current vertex
    max_speed_in = 0
    min_speed_out = 1000

    # Access output vertexes and compute min of output speeds
    if vertex in graph_out.keys():
        for adj_v in graph_out[vertex]:
            min_speed_out = min(min_speed_out, graph.get_edgeTo(vertex, adj_v).get_speed()[0])

    # Access input vertexes and compute max of input speed
    if vertex in graph_in.keys():
        for adj_v in graph_in[vertex]:
            max_speed_in = max(max_speed_in, graph.get_edgeTo(adj_v, vertex).get_speed()[0])

    if max_speed_in > min_speed_out:
        return 1
    else:
        return 0


def i_connect_eval(graph_in, graph_out, vertex):
    """ Interconnectedness evaluation function - takes two connected graphs
        and computes if there is an interconnectedness bottleneck

        Params:
            graph_in: graph of edges into the current vertex
            graph_out: graph of edges into the current vertex being evaluated
            vertex: current vertex/node of the graph

        returns: 1 if interconnect bottleneck exists and 0 if it doesn't
    """
    # check if either the edges going out of or going into a vertex 0
    if len(graph_out[vertex]) == 0 or len(graph_in[vertex]) == 0:
        return 0  # no bottleneck
    elif len(graph_out[vertex]) > 2 or len(graph_in[vertex]) > 2:
        return 1
    else:
        return 0


def bottleneck_ranking(lane_score, flow_score, connect_score):
    """ Severity evaluation function - takes three bottleneck scores
        and computes the overall severity of the vertex bottleneck

        Params:
            lane_score: individual vertex lane bottleneck score
            flow_score: individual vertex flow bottleneck score
            connect_score: individual vertex connect bottleneck score

        returns: the severity score

    """
    lane_weight = 0.35
    flow_weight = 0.5
    i_weight = 0.15
    # compute and return severity score
    return lane_score * lane_weight + flow_score * flow_weight + connect_score * i_weight


def recommendation(rating):
    """ Recommendation Engine - takes a severity ranking for a vertex
        and returns a recommendation for vertex triaging

        Params:
            rating: a combined bottleneck score

        returns: a recommendation for triaging severe bottleneck vertex
                most urgent action needed on 1
                lest urgent action needed on 5

    """
    if rating > 0.6:
        return 1
    elif rating > 0.3:
        return 2
    elif rating > 0:
        return 3
    elif rating == 0:
        return 4
    else:
        return 5
