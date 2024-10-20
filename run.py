# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)

# Breadth-First Search
print("\n====================")
print("Búsqueda en Anchura (Breadth-First Search)")
print("====================")
print("Ruta:", search.breadth_first_graph_search(ab).path())
print("====================")

# Depth-First Search
print("\n====================")
print("Búsqueda en Profundidad (Depth-First Search)")
print("====================")
print("Ruta:", search.depth_first_graph_search(ab).path())
print("====================")

# Shortest Path Search
print("\n====================")
print("Búsqueda del Camino más Corto")
print("====================")
print("Ruta:", search.shortest_path(ab).path())
print("====================")

# Branch and Bound with Heuristic Search
print("\n====================")
print("Búsqueda Ramificación y Acotación con Heurística")
print("====================")
print("Ruta:", search.branch_and_bound_with_heuristic(ab).path())
print("====================")
