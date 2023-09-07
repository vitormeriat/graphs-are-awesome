<div align="center">
  <img width="80" src="../docs/assets/logo.png">
  <h1 style="margin-bottom:40px; margin-top:20px">Graphs are Awesome
</h1>
</div>

Graph theory goes back to the XVIII century, when Euler introduced its basic ideas to solve the famous problem of the Kronigsberg’s bridges. However, in the last few decades, graph theory has been established, by its own right, as an important mathematical tool in a wide variety of areas of knowledge, such as operational research, engineering, genetics, sociology, geography, ecology, numerical analysis, parallel computation, telecommunications and chemistry. Besides, it is usual to say that a considerable number of problems in a wide variety of sciences can be modeled by a graph and solved using graph theory. For example, it is possible to calculate the different combinations of flights between two cities, to determinate if it is possible or not to walk in every street of a city without walking in a street twice and to know the number of colours we need to colour a map.

---

<h2 style="margin-top:40px"><a href="../algorithms/README.md">Blog Content</a></h2>

1. Graph Theory Intro
2. Graph Neural Networks

---

<h2 style="margin-top:40px"><a href="../algorithms/README.md">Basic Graph Algorithms</a></h2>

* Breadth First
* Depth First
* Has Path
* Undirected Path
* Connected Components Count
* Largest Component
* Shortest Path
* Island Count
* Minimum Island



```
> python -m unittest discover

----------------------------------------------------------------------
Ran 53 tests in 0.009s

OK
```

```
> pytest

==================== test session starts ==================== 
platform win32 -- Python 3.8.8, pytest-6.2.3, py-1.10.0, pluggy-0.13.1
rootdir: C:\repos\basic_graph_algorithms
plugins: anyio-2.2.0
collected 53 items

test_algorithms.py ............................................ [100%] 

==================== warnings summary ======================= 
..\..\Users\vitor.pereira\Anaconda3\lib\site-packages\pyreadline\py3k_compat.py:8
  C:\Users\vitor.pereira\Anaconda3\lib\site-packages\pyreadline\py3k_compat.py:8: DeprecationWarning: Using or importing the ABCs from 'collections' instead of from 'collections.abc' is deprecated 
since Python 3.3, and in 3.9 it will stop working
    return isinstance(x, collections.Callable)

-- Docs: https://docs.pytest.org/en/stable/warnings.html
==================== 53 passed, 1 warning in 0.52s ==========
```

![](../docs/assets/tests.png)