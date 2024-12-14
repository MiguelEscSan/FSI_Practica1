import unittest
import search

class BranchAndBoundHeuristicTest(unittest.TestCase):


    def test_arad_to_arad(self):
        problem = search.GPSProblem('A', 'A', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'A')
        self.assertEqual(len(visited_nodes), 0)  
        self.assertEqual(last_node.path_cost, 0)

    def test_arad_to_sibiu(self):
        problem = search.GPSProblem('A', 'S', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'S')
        self.assertEqual(len(visited_nodes), 1)  
        self.assertEqual(last_node.path_cost, 140)

    def test_arad_to_bucharest(self):
        problem = search.GPSProblem('A', 'B', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'B')
        self.assertEqual(len(visited_nodes), 5)  
        self.assertEqual(last_node.path_cost, 418)
        

    def test_bucharest_to_arad(self):
        problem = search.GPSProblem('B', 'A', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'A')
        self.assertEqual(len(visited_nodes), 4)  
        self.assertEqual(last_node.path_cost, 418)

    def test_arad_to_craiova(self):
        problem = search.GPSProblem('A', 'C', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'C')
        self.assertEqual(len(visited_nodes), 6)  
        self.assertEqual(last_node.path_cost, 366)

    def test_arad_to_drobeta(self):
        problem = search.GPSProblem('A', 'D', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'D')
        self.assertEqual(len(visited_nodes), 7)  
        self.assertEqual(last_node.path_cost, 374)
    
    def test_arad_to_eforie(self):
        problem = search.GPSProblem('A', 'E', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'E')
        self.assertEqual(len(visited_nodes), 13)  
        self.assertEqual(last_node.path_cost, 687)
    
    def test_arad_to_fagaras(self):
        problem = search.GPSProblem('A', 'F', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'F')
        self.assertEqual(len(visited_nodes), 2)  
        self.assertEqual(last_node.path_cost, 239)

    def test_arad_to_neamt(self):
        problem = search.GPSProblem('A', 'N', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'N')
        self.assertEqual(len(visited_nodes), 17)  
        self.assertEqual(last_node.path_cost, 824)
    
    def test_pitesti_to_oradea(self):
        problem = search.GPSProblem('P', 'O', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'O')
        self.assertEqual(len(visited_nodes), 3)  
        self.assertEqual(last_node.path_cost, 328)
    
    def test_bucharest_to_fagaras(self):
        problem = search.GPSProblem('B', 'F', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'F')
        self.assertEqual(len(visited_nodes), 2)
        self.assertEqual(last_node.path_cost, 211)

    def test_fagaras_to_bucharest(self):
        problem = search.GPSProblem('F', 'B', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'B')
        self.assertEqual(len(visited_nodes), 1)
        self.assertEqual(last_node.path_cost, 211)

    def test_craiova_to_pitesti(self):
        problem = search.GPSProblem('C', 'P', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'P')
        self.assertEqual(len(visited_nodes), 1)
        self.assertEqual(last_node.path_cost, 138)

    def test_oradea_to_sibiu(self):
        problem = search.GPSProblem('O', 'S', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'S')
        self.assertEqual(len(visited_nodes), 1)
        self.assertEqual(last_node.path_cost, 151)

    def test_timisoara_to_fagaras(self):
        problem = search.GPSProblem('T', 'F', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'F')
        self.assertEqual(len(visited_nodes), 5)
        self.assertEqual(last_node.path_cost, 357)

    def test_bucharest_to_drobeta(self):
        problem = search.GPSProblem('B', 'D', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'D')
        self.assertEqual(len(visited_nodes), 5)
        self.assertEqual(last_node.path_cost, 359)

    def test_sibiu_to_oradea(self):
        problem = search.GPSProblem('S', 'O', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'O')
        self.assertEqual(len(visited_nodes), 1)
        self.assertEqual(last_node.path_cost, 151)

    def test_timisora_to_eforie(self):
        problem = search.GPSProblem('T', 'E', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'E')
        self.assertEqual(len(visited_nodes), 15)
        self.assertEqual(last_node.path_cost, 805)

    def test_timisoara_to_arad(self):
        problem = search.GPSProblem('T', 'A', search.romania)
        last_node, visited_nodes = search.branch_and_bound_heuristic(problem)
        self.assertEqual(last_node.state, 'A')
        self.assertEqual(len(visited_nodes), 1)
        self.assertEqual(last_node.path_cost, 118)

if __name__ == '__main__':
    unittest.main()
