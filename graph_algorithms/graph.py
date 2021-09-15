class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class GraphData():

    def graph_00(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
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

    def graph_01(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
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

    def graph_02(self):
        a = Node('a')
        #     a

        #   -> ['a']
        return a

    def graph_03(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
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

    def graph_04(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        f = Node('f')
        g = Node('g')
        h = Node('h')
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

    def graph_05(self):
        a = Node('a')
        b = Node('b')
        c = Node('c')
        d = Node('d')
        e = Node('e')
        x = Node('x')
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

    def graph_06(self):
        return {
            'f': ['g', 'i'],
            'g': ['h'],
            'h': [],
            'i': ['g', 'k'],
            'j': ['i'],
            'k': []
        }

    def graph_07(self):
        return [
            ('i', 'j'),
            ('k', 'i'),
            ('m', 'k'),
            ('k', 'l'),
            ('o', 'n')
        ]

    def graph_08(self):
        return [
            ('b', 'a'),
            ('c', 'a'),
            ('b', 'c'),
            ('q', 'r'),
            ('q', 's'),
            ('q', 'u'),
            ('q', 't'),
        ]

    def graph_09(self):
        return {
            0: [8, 1, 5],
            1: [0],
            5: [0, 8],
            8: [0, 5],
            2: [3, 4],
            3: [2, 4],
            4: [3, 2]
        }

    def graph_10(self):
        return {
            1: [2],
            2: [1, 8],
            6: [7],
            9: [8],
            7: [6, 8],
            8: [9, 7, 2]
        }

    def graph_11(self):
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

    def graph_12(self):
        return {}

    def graph_13(self):
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

    def graph_14(self):
        return [
            ['w', 'x'],
            ['x', 'y'],
            ['z', 'y'],
            ['z', 'v'],
            ['w', 'v']
        ]

    def graph_15(self):
        return [
            ['a', 'c'],
            ['a', 'b'],
            ['c', 'b'],
            ['c', 'd'],
            ['b', 'd'],
            ['e', 'd'],
            ['g', 'f']
        ]

    def graph_16(self):
        return [
            ['c', 'n'],
            ['c', 'e'],
            ['c', 's'],
            ['c', 'w'],
            ['w', 'e'],
        ]

    def graph_17(self):
        return [
            ['m', 'n'],
            ['n', 'o'],
            ['o', 'p'],
            ['p', 'q'],
            ['t', 'o'],
            ['r', 'q'],
            ['r', 's']
        ]

    def graph_18(self):
        return [
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'L', 'W', 'W', 'W'],
            ['W', 'W', 'W', 'L', 'W'],
            ['W', 'W', 'L', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['L', 'L', 'W', 'W', 'W'],
        ]

    def graph_19(self):
        return [
            ['L', 'W', 'W', 'L', 'W'],
            ['L', 'W', 'W', 'L', 'L'],
            ['W', 'L', 'W', 'L', 'W'],
            ['W', 'W', 'W', 'W', 'W'],
            ['W', 'W', 'L', 'L', 'L'],
        ]

    def graph_20(self):
        return [
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
            ['L', 'L', 'L'],
        ]

    def graph_21(self):
        return [
            ['W', 'W'],
            ['W', 'W'],
            ['W', 'W'],
        ]

    def graph_22(self):
        return [
            ['W', 'W'],
            ['L', 'L'],
            ['W', 'W'],
            ['W', 'L']
        ]
