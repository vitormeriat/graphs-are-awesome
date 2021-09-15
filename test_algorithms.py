
import unittest
from graph_algorithms import depth_first, breadth_first, undirected_path, connected_components, \
    largest_component, shortest_path, island_count, minimum_island, graph


class TestDepthFist(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00_iterative(self):
        graph = self.data.graph_00()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_00_recursive(self):
        graph = self.data.graph_00()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_01_iterative(self):
        graph = self.data.graph_01()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_01_recursive(self):
        graph = self.data.graph_01()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_02_iterative(self):
        graph = self.data.graph_02()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a'])

    def test_02_recursive(self):
        graph = self.data.graph_02()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a'])

    def test_03_iterative(self):
        graph = self.data.graph_03()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e'])

    def test_03_recursive(self):
        graph = self.data.graph_03()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e'])

    def test_04_iterative(self):
        graph = None
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, [])

    def test_04_recursive(self):
        graph = None
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, [])


class TestBreadthFist(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_00()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_01(self):
        graph = self.data.graph_04()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_02(self):
        graph = self.data.graph_02()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a'])

    def test_03(self):
        graph = self.data.graph_05()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'x', 'd', 'e'])

    def test_04(self):
        graph = None
        path = breadth_first.traversal(graph)
        self.assertEqual(path, [])


class TestHasPath(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_06()
        has_path = depth_first.has_path(graph, 'f', 'k')
        self.assertEqual(has_path, True)

    def test_01(self):
        graph = self.data.graph_06()
        has_path = depth_first.has_path(graph, 'f', 'j')
        self.assertEqual(has_path, False)

    def test_02(self):
        graph = self.data.graph_06()
        has_path = depth_first.has_path(graph, 'i', 'h')
        self.assertEqual(has_path, True)


class UndirectedPath(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_07()
        has_path = undirected_path.has_path(graph, 'j', 'm')
        self.assertEqual(has_path, True)

    def test_01(self):
        graph = self.data.graph_07()
        has_path = undirected_path.has_path(graph, 'm', 'j')
        self.assertEqual(has_path, True)

    def test_02(self):
        graph = self.data.graph_07()
        has_path = undirected_path.has_path(graph, 'l', 'j')
        self.assertEqual(has_path, True)

    def test_03(self):
        graph = self.data.graph_07()
        has_path = undirected_path.has_path(graph, 'k', 'o')
        self.assertEqual(has_path, False)

    def test_04(self):
        graph = self.data.graph_07()
        has_path = undirected_path.has_path(graph, 'i', 'o')
        self.assertEqual(has_path, False)

    def test_05(self):
        graph = self.data.graph_08()
        has_path = undirected_path.has_path(graph, 'a', 'b')
        self.assertEqual(has_path, True)

    def test_06(self):
        graph = self.data.graph_08()
        has_path = undirected_path.has_path(graph, 'a', 'c')
        self.assertEqual(has_path, True)

    def test_07(self):
        graph = self.data.graph_08()
        has_path = undirected_path.has_path(graph, 'r', 't')
        self.assertEqual(has_path, True)

    def test_08(self):
        graph = self.data.graph_08()
        has_path = undirected_path.has_path(graph, 'r', 'b')
        self.assertEqual(has_path, False)


class ConnectedComponentsCount(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_09()
        count = connected_components.count(graph)
        self.assertEqual(count, 2)

    def test_01(self):
        graph = self.data.graph_10()
        count = connected_components.count(graph)
        self.assertEqual(count, 1)

    def test_02(self):
        graph = self.data.graph_11()
        count = connected_components.count(graph)
        self.assertEqual(count, 3)

    def test_03(self):
        graph = self.data.graph_12()
        count = connected_components.count(graph)
        self.assertEqual(count, 0)

    def test_04(self):
        graph = self.data.graph_13()
        count = connected_components.count(graph)
        self.assertEqual(count, 5)


class LargestComponent(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_09()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 4)

    def test_01(self):
        graph = self.data.graph_10()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 6)

    def test_02(self):
        graph = self.data.graph_11()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 5)

    def test_03(self):
        graph = self.data.graph_12()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 0)

    def test_04(self):
        graph = self.data.graph_13()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 3)


class ShortestPath(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_14()
        count = shortest_path.get(graph, 'w', 'z')
        self.assertEqual(count, 2)

    def test_01(self):
        graph = self.data.graph_14()
        count = shortest_path.get(graph, 'y', 'x')
        self.assertEqual(count, 1)

    def test_02(self):
        graph = self.data.graph_15()
        count = shortest_path.get(graph, 'a', 'e')
        self.assertEqual(count, 3)

    def test_03(self):
        graph = self.data.graph_15()
        count = shortest_path.get(graph, 'e', 'c')
        self.assertEqual(count, 2)

    def test_04(self):
        graph = self.data.graph_15()
        count = shortest_path.get(graph, 'b', 'g')
        self.assertEqual(count, -1)

    def test_05(self):
        graph = self.data.graph_16()
        count = shortest_path.get(graph, 'w', 'e')
        self.assertEqual(count, 1)

    def test_06(self):
        graph = self.data.graph_16()
        count = shortest_path.get(graph, 'n', 'e')
        self.assertEqual(count, 2)

    def test_07(self):
        graph = self.data.graph_17()
        count = shortest_path.get(graph, 'm', 's')
        self.assertEqual(count, 6)


class IslandCount(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_18()
        count = island_count.get(graph)
        self.assertEqual(count, 3)

    def test_01(self):
        graph = self.data.graph_19()
        count = island_count.get(graph)
        self.assertEqual(count, 4)

    def test_02(self):
        graph = self.data.graph_20()
        count = island_count.get(graph)
        self.assertEqual(count, 1)

    def test_03(self):
        graph = self.data.graph_21()
        count = island_count.get(graph)
        self.assertEqual(count, 0)


class MinimumIsland(unittest.TestCase):

    def setUp(self):
        self.data = graph.GraphData()

    def test_00(self):
        graph = self.data.graph_18()
        count = minimum_island.get(graph)
        self.assertEqual(count, 2)

    def test_01(self):
        graph = self.data.graph_19()
        count = minimum_island.get(graph)
        self.assertEqual(count, 1)

    def test_02(self):
        graph = self.data.graph_20()
        count = minimum_island.get(graph)
        self.assertEqual(count, 9)

    def test_03(self):
        graph = self.data.graph_22()
        count = minimum_island.get(graph)
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
