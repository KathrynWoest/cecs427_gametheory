# CECS 427 Project 3: Game Theory
Completed By: Kathryn Woest (030131541) and Grace Flores (030169163)


## Usage Instructions
**NOTE:** `plot.py` relies on a command that is not compatible with WSL. This command automatically opens up the graph's visualization. If you are unable to use a different terminal like Powershell, comment out `plot.py`'s line 131 and instead manually open the generated `.html` file through your file explorer.

1. Clone this repo and open it on your IDE

2. DEPENDENCIES: This program relies on two external libraries. To install them, ensure you are inside the project directory and run these commands:
    1. **NetworkX**, a library that provides `.gml` file parsing and writing, graph support, and analysis functions. To install, run: `pip install networkx[default]`
    2. **Plotly**, a library used for creating and plotting graphs. To install, run: `pip install plotly`

3. Run this program with: `python traffic_analysis.py input_file.gml vehicle_count start_node end_node --plot`
    1. All arguments MUST be provided in the order above. There is no way to check whether the numerical inputs are vehicle counts or nodes when the nodes are labeled with numbers, and there's no way to distinguish between starting and ending nodes. Thus, all these arguments must be provided in order. Additionally, since they are all in order, `--plot` must be at the end as to not cause issues reading the other arguments in. Any order of arguments other than the one above will cause the program to either terminate early or not function as expected.
    4. With the exception of `--plot`, all other commands are required. You can optionally plot the given graph, but the rest of the program requires the inclusion of all other arguments.


## Implementation Description
1. **Overall Program:** Modular program that calculates the nash equilibrium and social optimum of the given graph and displays (and optionally plots) the results.
2. **MAIN - traffic_analysis.py:** Takes a graph, number of vehicles, and where they start and are going to calculate aspects of the traffic network, namely the nash equilibrium and social optimum. Requires all inputs to be read in-order (as specified above in 3.). Conducts error checking for inputs and calls all other functions. A lot of code is reused from projects 1 and 2.
3. **file_i.py:** Reads in the directed graph from the given `.gml` file, checks that the graph is directed and not empty, and ensures all edges have `a` and `b` values, then returns the graph to the main program for analysis. A lot of code is reused from projects 1 and 2.
4. **nash_equilibrium.py:** Calculates the nash equilibrium of the given graph and vehicles by finding the distribution of vehicles that produces the lowest potential energy. First checks if a path exists between the start and end nodes to prevent the algorithm from running when it's impossible to calculate. It then calculates every possible path from start to end, and then uses statistical combinations to find every possible way vehicles can be distributed over those paths. For each distribution, the program determines the number of vehicles taking each edge and calculates their potential energies. It then performs a check, determining if it is the current lowest potential energy. If it is, it saves the energy and the distribution. Finally, once all distributions are calculated and compared, the program prints out the resulting nash equilibrium's potential energy and vehicle distribution.
5. **social_optimum.py:** 


## Example Commands and Outputs
1. Command: `python3 traffic_analysis.py traffic.gml 4 0 3 --plot`
2. Command: `python3 traffic_analysis.py traffic2.gml 5 2 4`
3. Command: `python3 traffic_analysis.py traffic2.gml 3 5 2`

Outputs for all are annotated in this PDF: 
