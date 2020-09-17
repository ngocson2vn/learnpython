def mst(G):
    """
    Find a Minimum Spanning Tree using Prim's Algorithm
        - G: adjacency matrix
    """

    MST = []

    INF = 9999999

    # Number of vertices in graph
    V = G.shape[-1]

    # Create a set S to track selected vertices
    # selected vertices will become true otherwise false
    S = [False, False, False, False, False]

    # Initialize number of edge to 0
    n_edges = 0

    # The number of edges in Minimum Spanning Tree will be
    # always less than (V - 1), where V is the number of vertices in the graph

    # Choose 0th vertex and make it true
    S[0] = True

    # For every selected vertex in the set S, find all adjacent vertices 
    # that are not included in the set S.
    # Choose an adjacent vertex that is nearest to one of selected vertices.
    while (n_edges < V - 1):
        minimum = INF
        x = 0
        y = 0
        for i in range(V):
            if S[i]:
                for j in range(V):
                    if ((not S[j]) and G[i][j]):
                        if minimum > G[i][j]:
                            minimum = G[i][j]
                            x = i
                            y = j
        S[y] = True
        MST.append([x, y])
        n_edges += 1
    return MST
