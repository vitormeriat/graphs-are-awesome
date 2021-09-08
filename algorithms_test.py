
import unittest
from graph_algorithms import depth_first, breadth_first, undirected_path, graph


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


def graph_02():
    a = graph.Node('a')
    #     a

    #   -> ['a']
    return a


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


def graph_06():
    return {
        'f': ['g', 'i'],
        'g': ['h'],
        'h': [],
        'i': ['g', 'k'],
        'j': ['i'],
        'k': []
    }


def graph_07():
    return [
        ('i', 'j'),
        ('k', 'i'),
        ('m', 'k'),
        ('k', 'l'),
        ('o', 'n')
    ]


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


class TestDepthFist(unittest.TestCase):

    def test_00_iterative(self):
        graph = graph_00()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_00_recursive(self):
        graph = graph_00()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'c', 'f'])

    def test_01_iterative(self):
        graph = graph_01()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_01_recursive(self):
        graph = graph_01()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a', 'b', 'd', 'e', 'g', 'c', 'f'])

    def test_02_iterative(self):
        graph = graph_02()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a'])

    def test_02_recursive(self):
        graph = graph_02()
        path = depth_first.traversal_recursive(graph)
        self.assertEqual(path, ['a'])

    def test_03_iterative(self):
        graph = graph_03()
        path = depth_first.traversal_iterative(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e'])

    def test_03_recursive(self):
        graph = graph_03()
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
        graph = graph_00()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f'])

    def test_01(self):
        graph = graph_04()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h'])

    def test_02(self):
        graph = graph_02()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a'])

    def test_03(self):
        graph = graph_05()
        path = breadth_first.traversal(graph)
        self.assertEqual(path, ['a', 'b', 'c', 'x', 'd', 'e'])

    def test_04(self):
        graph = None
        path = breadth_first.traversal(graph)
        self.assertEqual(path, [])


class TestHasPath(unittest.TestCase):
    def test_00(self):
        graph = graph_06()
        has_path = depth_first.has_path(graph, 'f', 'k')
        self.assertEqual(has_path, True)

    def test_01(self):
        graph = graph_06()
        has_path = depth_first.has_path(graph, 'f', 'j')
        self.assertEqual(has_path, False)

    def test_02(self):
        graph = graph_06()
        has_path = depth_first.has_path(graph, 'i', 'h')
        self.assertEqual(has_path, True)


class UndirectedPath(unittest.TestCase):
    def test_00(self):
        graph = graph_07()
        has_path = undirected_path.has_path(graph, 'j', 'm')
        self.assertEqual(has_path, True)

    def test_01(self):
        graph = graph_07()
        has_path = undirected_path.has_path(graph, 'm', 'j')
        self.assertEqual(has_path, True)

    def test_02(self):
        graph = graph_07()
        has_path = undirected_path.has_path(graph, 'l', 'j')
        self.assertEqual(has_path, True)

    def test_03(self):
        graph = graph_07()
        has_path = undirected_path.has_path(graph, 'k', 'o')
        self.assertEqual(has_path, False)

    def test_04(self):
        graph = graph_07()
        has_path = undirected_path.has_path(graph, 'i', 'o')
        self.assertEqual(has_path, False)

    def test_05(self):
        graph = graph_08()
        has_path = undirected_path.has_path(graph, 'a', 'b')
        self.assertEqual(has_path, True)

    def test_06(self):
        graph = graph_08()
        has_path = undirected_path.has_path(graph, 'a', 'c')
        self.assertEqual(has_path, True)

    def test_07(self):
        graph = graph_08()
        has_path = undirected_path.has_path(graph, 'r', 't')
        self.assertEqual(has_path, True)

    def test_08(self):
        graph = graph_08()
        has_path = undirected_path.has_path(graph, 'r', 'b')
        self.assertEqual(has_path, False)


if __name__ == "__main__":
    unittest.main()
