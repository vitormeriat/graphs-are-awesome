<div align="center">
  <img width="80" src="../docs/assets/logo.png">
  <h1 style="margin-bottom:40px; margin-top:20px">Graphs are Awesome
</h1>
</div>

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