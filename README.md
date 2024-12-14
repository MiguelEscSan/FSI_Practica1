<a href="https://www.eii.ulpgc.es" target="_blank"><img src="https://www.eii.ulpgc.es/sites/default/files/eii-acron-mod.png" alt="EII-ULPGC" align="right" width="516" height="150" /></a>
# PRÁCTICA 1 DE FSI
> - Ramificación y acotación
> - Realizado por Eduardo Ortega Zerpa y Miguel Escobedo Santana

Este proyecto implementa el algoritmo de **Ramificación y Acotación con Subestimación** para resolver un problema de búsqueda sobre el grafo de las ciudades de Rumanía. A partir del código base proporcionado, se implementa un método de búsqueda eficiente utilizando una heurística basada en la distancia en línea recta entre cada estado y el estado final.

## Descripción

El código presenta una solución al problema de encontrar el camino más corto entre dos ciudades en Rumanía, utilizando el algoritmo de Ramificación y Acotación con subestimación. El grafo de las ciudades de Rumanía se encuentra definido en el código, donde cada ciudad está conectada por caminos con ciertos costos. La heurística utilizada en este caso es la **distancia en línea recta** entre las ciudades (estado actual y estado final), lo que permite dirigir la búsqueda de forma eficiente.

<a href="https://www.dc.fi.udc.es/~cabalar/ai/ex1/index.html" target="_blank"><img src="https://www.dc.fi.udc.es/~cabalar/ai/ex1/romania-distances.jpg" alt="Romania" align="center" width="498" height="300" /></a>

## Funcionalidades

- **Búsqueda Ramificación y Acotación con Subestimación**: Se implementa el algoritmo para explorar los nodos del grafo buscando el camino más corto desde un nodo inicial hasta un nodo objetivo.
  
- **Heurística basada en la distancia en línea recta**: La heurística utilizada para guiar la búsqueda se calcula como la distancia recta entre las ciudades, lo que mejora la eficiencia de la búsqueda.

- **Tests**: Se incluyen una serie de pruebas unitarias para verificar la funcionalidad del algoritmo implementado. Estas pruebas aseguran que los caminos encontrados sean correctos y que el número de nodos visitados sea el esperado.


## Módulos

### Módulo `search.py`

El módulo `search.py` implementa un conjunto de clases y funciones que facilitan la resolución de problemas de búsqueda utilizando algoritmos informados y no informados. A continuación, se describen las clases y funciones principales del módulo.

#### Clases Principales

1. **Clase `Problem`**:
   - Esta clase abstracta define la estructura básica de un problema de búsqueda. Los usuarios deben heredar de esta clase y sobrescribir métodos clave como:
     - `successor(state)`: Devuelve una lista de sucesores alcanzables desde un estado dado.
     - `goal_test(state)`: Comprueba si el estado actual es el objetivo.
     - `path_cost(c, state1, action, state2)`: Calcula el costo de llegar a `state2` desde `state1` a través de una acción.
     - `value()`: Para problemas de optimización, define el valor de un estado (aunque no se utiliza en este proyecto).

2. **Clase `Node`**:
   - Representa un nodo en el árbol de búsqueda, incluyendo el estado, el nodo padre, la acción que llevó a ese estado, el costo del camino hasta ese nodo, y la profundidad.
   - Métodos importantes:
     - `expand(problem)`: Expande el nodo generando todos los nodos sucesores.
     - `path()`: Devuelve el camino desde el nodo raíz hasta este nodo.

#### Algoritmos de Búsqueda

El módulo implementa varios algoritmos de búsqueda para encontrar soluciones eficientes a los problemas:

- **Búsqueda en grafo** (`graph_search`): Función base que maneja la exploración de nodos en un grafo usando un "fringe" (estructura de datos para almacenar los nodos abiertos).

- **Búsqueda en amplitud** (`breadth_first_graph_search`): Explora primero los nodos más superficiales del árbol de búsqueda, utilizando una cola FIFO.

- **Búsqueda en profundidad** (`depth_first_graph_search`): Explora primero los nodos más profundos del árbol de búsqueda, utilizando una pila.

- **Ramificación y Acotación** (`branch_and_bound`): Explora los nodos utilizando una cola de prioridad, priorizando los nodos con los costos más bajos.

- **Ramificación y Acotación con Heurística** (`branch_and_bound_heuristic`): Implementa una versión de Ramificación y Acotación que utiliza una función heurística para guiar la búsqueda de manera más eficiente.

#### Función de Resultados

- **`print_search_resuls(node: Node, visited_nodes: list)`**: Imprime los resultados de la búsqueda, incluyendo el número de nodos visitados, el camino encontrado y el costo total del camino.

### Módulo `utils.py`
El módulo `utils.py` crea las estructuras de datos que se usarán para los distintos métodos de búsqueda. La clase implementada para esta práctica ha sido la `PriorityQueue`, la cual se explica:

#### Clase `PriorityQueue`
La clase `PriorityQueue` gestiona una cola de prioridad que mantiene los elementos ordenados según su costo de camino.

- **Métodos principales**:
  - `get_path_cost(item)`: Calcula el costo de camino de un elemento en la cola, con la opción de incluir la heurística si está configurada.
  - `append(item)`: Añade un nuevo ítem a la cola y ordena la lista por el costo de camino.
  - `pop()`: Extrae el ítem con el menor costo de camino.
  - `extend(items)`: Añade varios ítems a la cola y los ordena por su path_cost
## Ejecución de Tests

Para ejecutar las pruebas del proyecto, simplemente ejecuta el siguiente comando:

```bash
python -m unittest discover
