import networkx as nx

def social_optimal(graph, num_vehicles, source_node, target_node):
    # Social cost is the sum of travel time for all drivers
    # ax + b

    graph_copy = graph.copy()

    # Compute the weights of all the paths (ax+b) and add them to the copied graph
    for (u,v) in graph_copy.edges():
        graph_copy[u][v]['weight'] = graph_copy[u][v]['a'] * num_vehicles + graph_copy[u][v]['b']

    # Compute the total cost (length) of the shortest path
    try:
        shortest_path = nx.shortest_path(graph, source=source_node, target=target_node, weight='weight')
        # print(f"The social optimal from {source_node} to {target_node} is: {path_cost}")
    except nx.NetworkXNoPath:
        print(f"No path found between {source_node} and {target_node}.")

    # Create a set of edges in the shortest path as (u, v) tuples
    path_edges = set(zip(shortest_path, shortest_path[1:]))

    sum_edges = 0
    for (u,v) in path_edges:
        sum_edges += graph_copy[u][v]['weight']

    social_opt = sum_edges * num_vehicles
    print(f"Social Optimum: {social_opt}")

    return social_opt


