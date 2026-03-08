import networkx as nx
import itertools as it


def equilibrium(graph, vehicles, start, end):
    """Function that determines the travel equilibrium of the given directed graph
    Inputs: the user graph, the number of vehicles, the start node, and the ending node
    Outputs: the travel equilibrium and paths taken for that equilibrium"""

    try:
        # check that there's a way to go from the starting node to the ending node
        if not nx.has_path(graph, start, end):
            print(f"Calculation of travel equilibrium isn't possible because there's no path from node '{start}' to node '{end}'.")
            return
        
        # get a list of every possible path a vehicle can take from start to end
        all_paths = list(nx.all_simple_paths(graph, start, end))
        path_count = len(all_paths)

        # calculate all the possible ways the vehicles can be distributed across the paths
        # each tuple in the list is one distribution, displayed as (v1, v2, v3, ...)
        # vi is an int representing the path chosen by vi
        all_path_dists = list(it.combinations_with_replacement(range(path_count), vehicles))

        # create a list of distributions where each list in all_vehicle_dists represents the number of vehicles on each path for the dist
        # for example, [2, 1, 3] means 2 vehicles took path 0, 1 took path 1, and 3 took path 2
        # this will make calculating the path potential energies much easier
        all_vehicle_dists = []
        for path in all_path_dists:
            # for each distribution, create a sublist the size of the number of paths
            path_dist = [0]*path_count
            # for each vehicle in the distribution, track which path it takes
            for v in path:
                path_dist[v] += 1
            all_vehicle_dists.append(path_dist)
        
        lowest_pe = float("inf")
        lowest_pe_dist = None

        # calculate the potential energy of every possible distribution
        for dist in all_vehicle_dists:
            current_pe = 0
            edge_flow = {}
            # for all the paths in the distribution, determine the number of times each edge is used
            for path, count in enumerate(dist):
                if count > 0:
                    current_path = all_paths[path]
                    for node in range(len(current_path) - 1):
                        n1 = current_path[node]
                        n2 = current_path[node + 1]
                        edge_flow[(n1, n2)] = edge_flow.get((n1, n2), 0) + count

            # calculate the potential energy of each edge and add it to the total energy for the distribution
            for (n1, n2), flow in edge_flow.items():
                a = graph[n1][n2]['a']
                b = graph[n1][n2]['b']
                for i in range(1, flow + 1):
                    current_pe += (a * i) + b

            # if the currently calculated potential energy is lower than the current lowest, replace the lowest and save the distribution
            if current_pe < lowest_pe:
                lowest_pe = current_pe
                lowest_pe_dist = dist
        
        # print and return all results
        print(f"The travel equilibrium has a potential energy of {lowest_pe}. Here are the path distributions:")
        for path, v in enumerate(lowest_pe_dist):
            print(f"{v} vehicles take path {path}: {all_paths[path]}")

        return lowest_pe_dist

    except Exception as e:
        print(f"Calculation of travel equilibrium was terminated because there was an error. Error:", e)
        return
    