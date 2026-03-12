import networkx as nx
import itertools as it

def social_optimal(graph, num_vehicles, source_node, target_node):

    # graph_copy = graph.copy()

    # Compute the weights (time costs) of all the paths (ax+b) and add them to the copied graph
    # for (u,v) in graph_copy.edges():
    #     if graph_copy[u][v]['a'] is not 0:
    #         graph_copy[u][v]['weight'] = graph_copy[u][v]['a'] * num_vehicles + graph_copy[u][v]['b']
    #     elif graph_copy[u][v]['a'] is 0 and graph_copy[u][v]['b'] is 0:
    #         graph_copy[u][v]['weight'] = num_vehicles

    # get a list of every possible path a vehicle can take from start to end
    try:
        # get a list of every possible path a vehicle can take from start to end
        all_paths = list(nx.all_simple_paths(graph, source_node, target_node))
        path_count = len(all_paths)

        # calculate all the possible ways the vehicles can be distributed across the paths
        # each tuple in the list is one distribution, displayed as (v1, v2, v3, ...)
        # vi is an int representing the path chosen by vi
        all_path_dists = list(it.combinations_with_replacement(range(path_count), num_vehicles))

    except nx.NetworkXNoPath:
        print(f"No path found between {source_node} and {target_node}.")

    # create a list of distributions where each list in all_vehicle_dists represents the number of vehicles on each path for the dist
    # for example, [2, 1, 3] means 2 vehicles took path 0, 1 took path 1, and 3 took path 2
    # this will make calculating the path potential energies much easier
    all_vehicle_dists = []
    counter = 0
    for path in all_path_dists:
        # for each distribution, create a sublist the size of the number of paths
        path_dist = [0]*path_count
        # for each vehicle in the distribution, track which path it takes
        for v in path:
            path_dist[v] += 1
        all_vehicle_dists.append(path_dist)
    
    lowest_so = float("inf")
    lowest_so_dist = None

    # calculate the social optimum of every possible distribution
    for dist in all_vehicle_dists:
        current_so = 0
        edge_flow = {}
        # for all the paths in the distribution, determine the number of times each edge is used
        for path, count in enumerate(dist):
            if count > 0:
                current_path = all_paths[path]
                for node in range(len(current_path) - 1):
                    n1 = current_path[node]
                    n2 = current_path[node + 1]
                    edge_flow[(n1, n2)] = edge_flow.get((n1, n2), 0) + count

        # calculate the time cost of each edge and add it to social optimum for the distribution
        for (n1, n2), flow in edge_flow.items():
            a = graph[n1][n2]['a']
            b = graph[n1][n2]['b']

            current_so += flow * ((a * flow) + b)

        # if the currently calculated potential energy is lower than the current lowest, replace the lowest and save the distribution
        if current_so < lowest_so:
            counter = counter + 1
            print(counter)
            print(current_so)
            print(lowest_so)
            lowest_so = current_so
            lowest_so_dist = dist

    # print and return all results
    print(f"The social optimum of the path is {lowest_so}. Here are the path distributions:")
    for path, v in enumerate(lowest_so_dist):
        print(f"{v} vehicles take path {path}: {all_paths[path]}")
    print("\n")
    
    return lowest_so


