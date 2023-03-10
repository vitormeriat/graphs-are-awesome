
import unittest
import algorithms as alg


class TestDepthFist(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00_iterative(self):
        graph = self.data.graph_00()
        path = alg.depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_00_recursive(self):
        graph = self.data.graph_00()
        path = alg.depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_01_iterative(self):
        graph = self.data.graph_01()
        path = alg.depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_01_recursive(self):
        graph = self.data.graph_01()
        path = alg.depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_02_iterative(self):
        graph = self.data.graph_02()
        path = alg.depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a'])

    def test_02_recursive(self):
        graph = self.data.graph_02()
        path = alg.depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a'])

    def test_03_iterative(self):
        graph = self.data.graph_03()
        path = alg.depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e'])

    def test_03_recursive(self):
        graph = self.data.graph_03()
        path = alg.depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e'])

    def test_04_iterative(self):
        graph = None
        path = alg.depth_first.traversal_iterative(graph)
        self.assertEqual(path, [])

    def test_04_recursive(self):
        graph = None
        path = alg.depth_first.traversal_recursive(graph)
        self.assertEqual(path, [])


class TestBreadthFist(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00(self):
        graph = self.data.graph_00()
        path = alg.breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_01(self):
        graph = self.data.graph_04()
        path = alg.breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_02(self):
        graph = self.data.graph_02()
        path = alg.breadth_first.traversal(graph)
        self.assertEqual(path, ['a'])

    def test_03(self):
        graph = self.data.graph_05()
        path = alg.breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'x', 'd', 'e'])

    def test_04(self):
        graph = None
        path = alg.breadth_first.traversal(graph)
        self.assertEqual(path, [])


class TestHasPath(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def _depth_first_tests_graph_06(self, arg0, arg1, arg2):
        graph = self.data.graph_06()
        has_path = alg.depth_first.has_path(graph, arg0, arg1)
        self.assertEqual(has_path, arg2)

    def test_00(self):
        self._depth_first_tests_graph_06('f', 'k', True)

    def test_01(self):
        self._depth_first_tests_graph_06('f', 'j', False)

    def test_02(self):
        self._depth_first_tests_graph_06('i', 'h', True)


class UndirectedPath(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def _undirected_path_tests_graph_07(self, arg0, arg1, arg2):
        graph = self.data.graph_07()
        has_path = alg.undirected_path.has_path(graph, arg0, arg1)
        self.assertEqual(has_path, arg2)

    def _undirected_path_tests_graph_08(self, arg0, arg1, arg2):
        graph = self.data.graph_08()
        has_path = alg.undirected_path.has_path(graph, arg0, arg1)
        self.assertEqual(has_path, arg2)

    def test_00(self):
        self._undirected_path_tests_graph_07('j', 'm', True)

    def test_01(self):
        self._undirected_path_tests_graph_07('m', 'j', True)

    def test_02(self):
        self._undirected_path_tests_graph_07('l', 'j', True)

    def test_03(self):
        self._undirected_path_tests_graph_07('k', 'o', False)

    def test_04(self):
        self._undirected_path_tests_graph_07('i', 'o', False)

    def test_05(self):
        self._undirected_path_tests_graph_08('a', 'b', True)

    def test_06(self):
        self._undirected_path_tests_graph_08('a', 'c', True)

    def test_07(self):
        self._undirected_path_tests_graph_08('r', 't', True)

    def test_08(self):
        self._undirected_path_tests_graph_08('r', 'b', False)


class ConnectedComponentsCount(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00(self):
        graph = self.data.graph_09()
        count = alg.connected_components.count(graph)
        self.assertEqual(count, 2)

    def test_01(self):
        graph = self.data.graph_10()
        count = alg.connected_components.count(graph)
        self.assertEqual(count, 1)

    def test_02(self):
        graph = self.data.graph_11()
        count = alg.connected_components.count(graph)
        self.assertEqual(count, 3)

    def test_03(self):
        graph = self.data.graph_12()
        count = alg.connected_components.count(graph)
        self.assertEqual(count, 0)

    def test_04(self):
        graph = self.data.graph_13()
        count = alg.connected_components.count(graph)
        self.assertEqual(count, 5)


class LargestComponent(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00(self):
        graph = self.data.graph_09()
        count = alg.largest_component.get_size(graph)
        self.assertEqual(count, 4)

    def test_01(self):
        graph = self.data.graph_10()
        count = alg.largest_component.get_size(graph)
        self.assertEqual(count, 6)

    def test_02(self):
        graph = self.data.graph_11()
        count = alg.largest_component.get_size(graph)
        self.assertEqual(count, 5)

    def test_03(self):
        graph = self.data.graph_12()
        count = alg.largest_component.get_size(graph)
        self.assertEqual(count, 0)

    def test_04(self):
        graph = self.data.graph_13()
        count = alg.largest_component.get_size(graph)
        self.assertEqual(count, 3)


class ShortestPath(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00(self):
        graph = self.data.graph_14()
        count = alg.shortest_path.get(graph, 'w', 'z')
        self.assertEqual(count, 2)

    def test_01(self):
        graph = self.data.graph_14()
        count = alg.shortest_path.get(graph, 'y', 'x')
        self.assertEqual(count, 1)

    def test_02(self):
        graph = self.data.graph_15()
        count = alg.shortest_path.get(graph, 'a', 'e')
        self.assertEqual(count, 3)

    def test_03(self):
        graph = self.data.graph_15()
        count = alg.shortest_path.get(graph, 'e', 'c')
        self.assertEqual(count, 2)

    def test_04(self):
        graph = self.data.graph_15()
        count = alg.shortest_path.get(graph, 'b', 'g')
        self.assertEqual(count, -1)

    def test_05(self):
        graph = self.data.graph_16()
        count = alg.shortest_path.get(graph, 'w', 'e')
        self.assertEqual(count, 1)

    def test_06(self):
        graph = self.data.graph_16()
        count = alg.shortest_path.get(graph, 'n', 'e')
        self.assertEqual(count, 2)

    def test_07(self):
        graph = self.data.graph_17()
        count = alg.shortest_path.get(graph, 'm', 's')
        self.assertEqual(count, 6)


class IslandCount(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00(self):
        graph = self.data.graph_18()
        count = alg.island_count.get(graph)
        self.assertEqual(count, 3)

    def test_01(self):
        graph = self.data.graph_19()
        count = alg.island_count.get(graph)
        self.assertEqual(count, 4)

    def test_02(self):
        graph = self.data.graph_20()
        count = alg.island_count.get(graph)
        self.assertEqual(count, 1)

    def test_03(self):
        graph = self.data.graph_21()
        count = alg.island_count.get(graph)
        self.assertEqual(count, 0)


class MinimumIsland(unittest.TestCase):

    def setUp(self):
        self.data = alg.GraphData()

    def test_00(self):
        graph = self.data.graph_18()
        count = alg.minimum_island.get(graph)
        self.assertEqual(count, 2)

    def test_01(self):
        graph = self.data.graph_19()
        count = alg.minimum_island.get(graph)
        self.assertEqual(count, 1)

    def test_02(self):
        graph = self.data.graph_20()
        count = alg.minimum_island.get(graph)
        self.assertEqual(count, 9)

    def test_03(self):
        graph = self.data.graph_22()
        count = alg.minimum_island.get(graph)
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
