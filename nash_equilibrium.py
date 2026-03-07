import networkx as nx


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

        # calculate the potential energy for if the vehicles all take the first path in the all_paths list
        # use this path as the starting potential energy for the rest of the program
        lowest_pe = 0
        first_path = all_paths[0]
        
        for node in range(len(first_path) - 1):
            # determine 'a' and 'b' for each edge in the path
            n1 = first_path[node]
            n2 = first_path[node + 1]
            a = graph[n1][n2]['a']
            b = graph[n1][n2]['b']

            # calculate the potential energy of each edge and add it to the total energy
            for i in range(1, vehicles + 1):
                lowest_pe += (a * i) + b

            # try each path with v1. then for each option for v1, try every path for v2. and so on
            # ex with 2 vehicles and 3 paths:
                # for path 1, assign v1 to it. then try path 1, 2, and 3 for v2 and keep lowest pe
                # for path 2, assign v1 to it. then try path 1, 2, and 3 for v2 and keep lowest pe of all of them

            # for tomorrow:
                # use intertools.combinations_with_replacement(range(len(all_paths)), vehicles) to get an iterable item that picks all possible combinations for vehicles distributed over number of paths
                    # list(itertools.c...) with return a list of tuples like so: [(1,2), (1,3), (1,4)]. in this case, each tuple represents paths chosen, so (v1, v2, v3, ...) where vi will have the number of the path chosen
                    # then go through each resulting tuple and count the number of vehicles that chose each path, and store that in a tuple that is the size of the paths, not the vehicles. so (2, 1, 3) indicates 2 vehicles picked path 1, 1 picked 2, etc
                    # put all of those tuples in a list
                    # we now have a list of every possible numerical way the vehicles can be distributed across the paths
                # use the method i used above to calculate pe to calculate it for every single tuple in that list
                    # extract to a new function possibly, and do the same for intertools distribution
                    # use enumerate() to collect the location in the tuple and the value in the tuple
                # if the pe is lower than the current highest, save it and save the distribution tuple to return
                # start the pe off with float("inf"), representing infinity

    except Exception as e:
        print(f"Calculation of travel equilibrium was terminated because there was an error. Error:", e)
        return
    