## NOTE: this file reuses a lot of code from Projects 1 and 2

import networkx as nx

def parse_graph(file_name):
    """Takes the input file and parses it into a NetworkX graph that can be analyzed. Checks for empty graphs, if the graph is undirected, and for edges with no int 'a' or 'b' attributes.
    Input: .gml file name of the submitted graph
    Output: NetworkX graph of the submitted graph from the file"""
    
    if ".gml" not in file_name:
        raise Exception("Input file type is not .gml, so program terminated. Provided file:", file_name)

    try:
        # reads .gml file and parses it into the graph
        submitted_graph = nx.read_gml(file_name)

        # check if the graph is undirected
        if not submitted_graph.is_directed():
            raise Exception("Program terminated because the graph is undirected.")

        # check if the graph is empty
        if submitted_graph.number_of_nodes == 0 or submitted_graph.number_of_edges == 0:
            raise Exception("Program terminated because the graph has no nodes and/or no edges.")
        
        # check if any of the edges don't have a or b values
        for node1, node2, a in submitted_graph.edges(data="a"):
            if a == None or not isinstance(a, int):
                raise Exception(f"Program terminated because edge ({node1}, {node2}) doesn't have an 'a' attribute or 'a' is not an integer.")
        for node1, node2, b in submitted_graph.edges(data="b"):
            if b == None or not isinstance(b, int):
                raise Exception(f"Program terminated because edge ({node1}, {node2}) doesn't have a 'b' attribute or 'b' is not an integer.")
        
        return submitted_graph
    
    except Exception as e:
        raise Exception("Program quit due to an error in reading and parsing the graph from the provided .gml file. Provided error:", e)
    