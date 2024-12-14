# Search methods

import search
from search import print_search_resuls

ab = search.GPSProblem('A', 'B'
                       , search.romania)

# last_node, visited_nodes = search.breadth_first_graph_search(ab)
# last_node, visited_nodes = search.depth_first_graph_search(ab)
# last_node, visited_nodes = search.branch_and_bound(ab)
last_node, visited_nodes = search.branch_and_bound_heuristic(ab)

print_search_resuls(last_node, visited_nodes)


# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
