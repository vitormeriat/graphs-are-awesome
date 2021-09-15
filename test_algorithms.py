
import unittest
from graph_algorithms import depth_first, breadth_first, undirected_path, connected_components, \
    largest_component, shortest_path, island_count, minimum_island, graph


class TestData():

    @staticmethod
    def graph_00():
        a = graph.Node('a')
        b = graph.Node('b')
        c = graph.Node('c')
        d = graph.Node('d')
        e = graph.Node('e')
        f = graph.Node('f')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f

        #   -> ['a', 'b', 'd', 'e', 'c', 'f']
        return a

    @staticmethod
    def graph_01():
        a = graph.Node('a')
        b = graph.Node('b')
        c = graph.Node('c')
        d = graph.Node('d')
        e = graph.Node('e')
        f = graph.Node('f')
        g = graph.Node('g')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /
        #   g

        #   -> ['a', 'b', 'd', 'e', 'g', 'c', 'f']
        return a

    @staticmethod
    def graph_02():
        a = graph.Node('a')
        #     a

        #   -> ['a']
        return a

    @staticmethod
    def graph_03():
        a = graph.Node('a')
        b = graph.Node('b')
        c = graph.Node('c')
        d = graph.Node('d')
        e = graph.Node('e')
        a.right = b
        b.left = c
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #       \
        #        d
        #         \
        #          e

        #   -> ['a', 'b', 'c', 'd', 'e']
        return a

    @staticmethod
    def graph_04():
        a = graph.Node('a')
        b = graph.Node('b')
        c = graph.Node('c')
        d = graph.Node('d')
        e = graph.Node('e')
        f = graph.Node('f')
        g = graph.Node('g')
        h = graph.Node('h')
        a.left = b
        a.right = c
        b.left = d
        b.right = e
        c.right = f
        e.left = g
        f.right = h

        #      a
        #    /   \
        #   b     c
        #  / \     \
        # d   e     f
        #    /       \
        #   g         h

        #   -> ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
        return a

    @staticmethod
    def graph_05():
        a = graph.Node('a')
        b = graph.Node('b')
        c = graph.Node('c')
        d = graph.Node('d')
        e = graph.Node('e')
        x = graph.Node('x')
        a.right = b
        b.left = c
        c.left = x
        c.right = d
        d.right = e

        #      a
        #       \
        #        b
        #       /
        #      c
        #    /  \
        #   x    d
        #         \
        #          e

        #   -> ['a', 'b', 'c', 'x', 'd', 'e']
        return a

    @staticmethod
    def graph_06():
        return {
            'f': ['g', 'i'],
            'g': ['h'],
            'h': [],
            'i': ['g', 'k'],
            'j': ['i'],
            'k': []
        }

    @staticmethod
    def graph_07():
        return [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

    @staticmethod
    def graph_08():
        return [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

    @staticmethod
    def graph_09():
        return {
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        }

    @staticmethod
    def graph_10():
        return {
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        }

    @staticmethod
    def graph_11():
        return {
            3: [],
            4: [6],
            6: [4, 5, 7, 8],
            8: [6],
            7: [6],
            5: [6],
            1: [2],
            2: [1]
        }

    @staticmethod
    def graph_12():
        return {}

    @staticmethod
    def graph_13():
        return {
            0: [4, 7],
            1: [],
            2: [],
            3: [6],
            4: [0],
            6: [3],
            7: [0],
            8: []
        }

    @staticmethod
    def graph_14():
        return [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
        ]

    @staticmethod
    def graph_15():
        return [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]

    @staticmethod
    def graph_16():
        return [
            ['c', 'n'],
            ['c', 'e'],
            ['c', 's'],
            ['c', 'w'],
            ['w', 'e'],
        ]

    @staticmethod
    def graph_17():
        return [
            ['m', 'n'],
            ['n', 'o'],
            ['o', 'p'],
            ['p', 'q'],
            ['t', 'o'],
            ['r', 'q'],
            ['r', 's']
        ]

    @staticmethod
    def graph_18():
        return [
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'L', 'W'],
            ['W', 'W', 'L', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['L', 'L', 'W', 'W', 'W'],
        ]

    @staticmethod
    def graph_19():
        return [
            ['L', 'W', 'W', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['W', 'L', 'W', 'L', 'W'],
            ['W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'L', 'L', 'L'],
        ]

    @staticmethod
    def graph_20():
        return [
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
        ]

    @staticmethod
    def graph_21():
        return [
            ['W', 'W'],
            ['W', 'W'],
            ['W', 'W'],
        ]

    @staticmethod
    def graph_22():
        return [
            ['W', 'W'],
            ['L', 'L'],
            ['W', 'W'],
            ['W', 'L']
        ]


class TestDepthFist(unittest.TestCase):

    def test_00_iterative(self):
        graph = TestData.graph_00()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_00_recursive(self):
        graph = TestData.graph_00()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_01_iterative(self):
        graph = TestData.graph_01()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_01_recursive(self):
        graph = TestData.graph_01()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_02_iterative(self):
        graph = TestData.graph_02()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a'])

    def test_02_recursive(self):
        graph = TestData.graph_02()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a'])

    def test_03_iterative(self):
        graph = TestData.graph_03()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e'])

    def test_03_recursive(self):
        graph = TestData.graph_03()
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

    def test_00(self):
        graph = TestData.graph_00()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_01(self):
        graph = TestData.graph_04()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_02(self):
        graph = TestData.graph_02()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a'])

    def test_03(self):
        graph = TestData.graph_05()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'x', 'd', 'e'])

    def test_04(self):
        graph = None
        path = breadth_first.traversal(graph)
        self.assertEqual(path, [])


class TestHasPath(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_06()
        has_path = depth_first.has_path(graph, 'f', 'k')
        self.assertEqual(has_path, True)

    def test_01(self):
        graph = TestData.graph_06()
        has_path = depth_first.has_path(graph, 'f', 'j')
        self.assertEqual(has_path, False)

    def test_02(self):
        graph = TestData.graph_06()
        has_path = depth_first.has_path(graph, 'i', 'h')
        self.assertEqual(has_path, True)


class UndirectedPath(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_07()
        has_path = undirected_path.has_path(graph, 'j', 'm')
        self.assertEqual(has_path, True)

    def test_01(self):
        graph = TestData.graph_07()
        has_path = undirected_path.has_path(graph, 'm', 'j')
        self.assertEqual(has_path, True)

    def test_02(self):
        graph = TestData.graph_07()
        has_path = undirected_path.has_path(graph, 'l', 'j')
        self.assertEqual(has_path, True)

    def test_03(self):
        graph = TestData.graph_07()
        has_path = undirected_path.has_path(graph, 'k', 'o')
        self.assertEqual(has_path, False)

    def test_04(self):
        graph = TestData.graph_07()
        has_path = undirected_path.has_path(graph, 'i', 'o')
        self.assertEqual(has_path, False)

    def test_05(self):
        graph = TestData.graph_08()
        has_path = undirected_path.has_path(graph, 'a', 'b')
        self.assertEqual(has_path, True)

    def test_06(self):
        graph = TestData.graph_08()
        has_path = undirected_path.has_path(graph, 'a', 'c')
        self.assertEqual(has_path, True)

    def test_07(self):
        graph = TestData.graph_08()
        has_path = undirected_path.has_path(graph, 'r', 't')
        self.assertEqual(has_path, True)

    def test_08(self):
        graph = TestData.graph_08()
        has_path = undirected_path.has_path(graph, 'r', 'b')
        self.assertEqual(has_path, False)


class ConnectedComponentsCount(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_09()
        count = connected_components.count(graph)
        self.assertEqual(count, 2)

    def test_01(self):
        graph = TestData.graph_10()
        count = connected_components.count(graph)
        self.assertEqual(count, 1)

    def test_02(self):
        graph = TestData.graph_11()
        count = connected_components.count(graph)
        self.assertEqual(count, 3)

    def test_03(self):
        graph = TestData.graph_12()
        count = connected_components.count(graph)
        self.assertEqual(count, 0)

    def test_04(self):
        graph = TestData.graph_13()
        count = connected_components.count(graph)
        self.assertEqual(count, 5)


class LargestComponent(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_09()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 4)

    def test_01(self):
        graph = TestData.graph_10()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 6)

    def test_02(self):
        graph = TestData.graph_11()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 5)

    def test_03(self):
        graph = TestData.graph_12()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 0)

    def test_04(self):
        graph = TestData.graph_13()
        count = largest_component.get_size(graph)
        self.assertEqual(count, 3)


class ShortestPath(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_14()
        count = shortest_path.get(graph, 'w', 'z')
        self.assertEqual(count, 2)

    def test_01(self):
        graph = TestData.graph_14()
        count = shortest_path.get(graph, 'y', 'x')
        self.assertEqual(count, 1)

    def test_02(self):
        graph = TestData.graph_15()
        count = shortest_path.get(graph, 'a', 'e')
        self.assertEqual(count, 3)

    def test_03(self):
        graph = TestData.graph_15()
        count = shortest_path.get(graph, 'e', 'c')
        self.assertEqual(count, 2)

    def test_04(self):
        graph = TestData.graph_15()
        count = shortest_path.get(graph, 'b', 'g')
        self.assertEqual(count, -1)

    def test_05(self):
        graph = TestData.graph_16()
        count = shortest_path.get(graph, 'w', 'e')
        self.assertEqual(count, 1)

    def test_06(self):
        graph = TestData.graph_16()
        count = shortest_path.get(graph, 'n', 'e')
        self.assertEqual(count, 2)

    def test_07(self):
        graph = TestData.graph_17()
        count = shortest_path.get(graph, 'm', 's')
        self.assertEqual(count, 6)


class IslandCount(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_18()
        count = island_count.get(graph)
        self.assertEqual(count, 3)

    def test_01(self):
        graph = TestData.graph_19()
        count = island_count.get(graph)
        self.assertEqual(count, 4)

    def test_02(self):
        graph = TestData.graph_20()
        count = island_count.get(graph)
        self.assertEqual(count, 1)

    def test_03(self):
        graph = TestData.graph_21()
        count = island_count.get(graph)
        self.assertEqual(count, 0)


class MinimumIsland(unittest.TestCase):

    def test_00(self):
        graph = TestData.graph_18()
        count = minimum_island.get(graph)
        self.assertEqual(count, 2)

    def test_01(self):
        graph = TestData.graph_19()
        count = minimum_island.get(graph)
        self.assertEqual(count, 1)

    def test_02(self):
        graph = TestData.graph_20()
        count = minimum_island.get(graph)
        self.assertEqual(count, 9)

    def test_03(self):
        graph = TestData.graph_22()
        count = minimum_island.get(graph)
        self.assertEqual(count, 1)


if __name__ == "__main__":
    unittest.main()
