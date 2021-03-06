# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
ab2 = search.GPSProblem('A', 'B', search.romania.locations)


print search.breadth_first_graph_search(ab).path()
#print search.depth_first_graph_search(ab).path()
#print search.iterative_deepening_search(ab).path()
#print search.depth_limited_search(ab).path()
print search.branch_and_bound_graph_search(ab).path()

print search.branch_and_bound_graph_search_With_Heuristica(ab).path()

#print search.astar_search(ab).path()

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
