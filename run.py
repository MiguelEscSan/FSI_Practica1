# Search methods
import search
from search import print_search_results

ab = search.GPSProblem('A', 'B', search.romania)

# Breadth-First Search
print("\n====================")
print("Búsqueda en Anchura (Breadth-First Search)")
print("====================")
last_node, visited_nodes = search.breadth_first_graph_search(ab)
print_search_results(last_node, visited_nodes)
print("====================")

# Depth-First Search
print("\n====================")
print("Búsqueda en Profundidad (Depth-First Search)")
print("====================")
last_node, visited_nodes = search.depth_first_graph_search(ab)
print_search_results(last_node, visited_nodes)
print("====================")

# Shortest Path Search
print("\n====================")
print("Búsqueda del Camino más Corto")
print("====================")
last_node, visited_nodes = search.branch_and_bound(ab)
print_search_results(last_node, visited_nodes)
print("====================")

# Branch and Bound with Heuristic Search
print("\n====================")
print("Búsqueda Ramificación y Acotación con Heurística")
print("====================")
last_node, visited_nodes = search.branch_and_bound_heuristic(ab)
print_search_results(last_node, visited_nodes)
print("====================")
