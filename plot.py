import os
import webbrowser
import networkx as nx
import plotly.graph_objects as go

def plot(graph):
    """
    Plots and visualizes the given directed graph with each edge labeled with polynomial
    and arrows to indicate direction. 
    
    Parameters:
        - graph (NetworkX graph): the graph to be visualized

    Outputs:
        - html file: visualized graph in HTML format
    """

    G = graph
    pos = nx.kamada_kawai_layout(G)

    # Creating edges
    edge_x = []
    edge_y = []

    for u, v in G.edges():
        x0, y0 = pos[u]
        x1, y1 = pos[v]
        
        edge_x += [x0, x1, None]
        edge_y += [y0, y1, None]

    edge_trace = go.Scatter(
        x=edge_x,
        y=edge_y,
        mode='lines',
        line=dict(width=1),
        hoverinfo='none'
    )
    
    # Creating edge labels for polynomials
    edge_label_x = []
    edge_label_y = []
    edge_text = []

    for u, v, data in G.edges(data=True):

        x0, y0 = pos[u]
        x1, y1 = pos[v]

        # calculating midpoint (shifting to avoid label overlap)
        mx = (x0 + x1) / 2
        my = (y0 + y1) / 2

        dx = x1 - x0
        dy = y1 - y0
        length = (dx**2 + dy**2)**0.5

        offset = 0.03
        mx += -dy/length * offset
        my +=  dx/length * offset

        # coefficients
        a = data.get('a', 0)
        b = data.get('b', 0)

        # clean formatting
        if b >= 0:
            label = f"{a}x + {b}"
        else:
            label = f"{a}x - {abs(b)}"

        edge_label_x.append(mx)
        edge_label_y.append(my)
        edge_text.append(label)

    edge_label_trace = go.Scatter(
        x=edge_label_x,
        y=edge_label_y,
        mode='text',
        text=edge_text,
        textposition="middle center",
        hoverinfo='none'
    )

    # Creating nodes
    node_x = []
    node_y = []

    for node in G.nodes():
        x, y = pos[node]
        node_x.append(x)
        node_y.append(y)

    node_trace = go.Scatter(
        x=node_x,
        y=node_y,
        mode='markers+text',
        text=list(G.nodes()),
        textposition="top center",
        marker=dict(size=20)
    )

    # Adding arrows to indicate direction
    annotations = []

    for source, target in G.edges():
        x0, y0 = pos[source]
        x1, y1 = pos[target]

        annotations.append(
            dict(
                ax=x0,
                ay=y0,
                x=x1,
                y=y1,
                xref='x',
                yref='y',
                axref='x',
                ayref='y',
                showarrow=True,
                arrowhead=3,
                arrowsize=2.5,   
                arrowwidth=1.2     
            )
        )
        

    # Plotting final directed graph with edge labels
    fig = go.Figure(
    data=[edge_trace, node_trace, edge_label_trace],
    layout=go.Layout(
        showlegend=False,
        hovermode='closest',
        annotations=annotations,
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False)
        )
    )

    # Generating figure
    fig.show()

    file_path = os.path.abspath("graph.html")
    fig.write_html("graph", auto_open=False)
    webbrowser.open("file://" + file_path)

