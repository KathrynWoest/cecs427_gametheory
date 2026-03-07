## NOTE: this file reuses a lot of code from Projects 1 and 2

import sys
import file_i as fi
#import plot
#import social_optimum as so
import nash_equilibrium as ne


def main():
    # get arguments from command line
    args = sys.argv
    end = len(args)

    # if there are less than 5 arguments, then not possible to do anything. terminate program.
    if end < 5:
        raise Exception(f"Program was terminated because there is no file to upload a graph with or vehicle/node information.\n---")
    
    # parse in graph from given .gml file
    user_graph = fi.parse_graph(args[1])

    # number of vehicles
    try:
        vehicle_count = int(args[2])
    except Exception as e:
        raise Exception(f"Program was terminated because there was an error in reading in the number of vehicles, which needs to be an integer. Given value: {args[2]}. Error:", e)
    
    # initial node
    try:
        initial = args[3]
        if initial not in user_graph.nodes():
            raise Exception(f"Node '{initial}' is not in the graph.")
    except Exception as e:
        raise Exception(f"Program terminated because there was an error in reading in the initial node. Error:", e)
    
    # final node
    try:
        final = args[4]
        if final not in user_graph.nodes():
            raise Exception(f"Node '{final}' is not in the graph.")
    except Exception as e:
        raise Exception(f"Program terminated because there was an error in reading in the final node. Error:", e)
    
    # calculate social optimum
    #so.optimum(user_graph, vehicle_count, initial, final)

    # calculate nash equilibrium
    ne.equilibrium(user_graph, vehicle_count, initial, final)

    # call the visualization function
    #if "--plot" in args:
    #    plot.plot(user_graph)
    
main()