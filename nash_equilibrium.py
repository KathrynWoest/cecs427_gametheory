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

    except Exception as e:
        print(f"Calculation of travel equilibrium was terminated because there was an error. Error:", e)
        return
    