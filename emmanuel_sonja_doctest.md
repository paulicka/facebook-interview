
>>> from EmmanuelSonja import *

>>> r = sample()

>>> DFSPrinter(r).traverse()
4
-7
--10
--2
---6
----2
-9
--6
    
>>> BFSPrinter(r).traverse()
4
-7
-9
--10
--2
--6
---6
----2
    
>>> BFSAverager(r).traverse()
{0: [4], 1: [7, 9], 2: [10, 2, 6], 3: [6], 4: [2]}

>>> [(k, sum(v) // len(v)) for (k, v) in BFSAverager(r).traverse().items()]
[(0, 4), (1, 8), (2, 6), (3, 6), (4, 2)]

>>> BFSDenser(r).traverse()
{0: (1, 4), 1: (2, 16), 2: (3, 18), 3: (1, 6), 4: (1, 2)}

>>> [(k, (s // c)) for (k, (c, s)) in BFSDenser(r).traverse().items()]
[(0, 4), (1, 8), (2, 6), (3, 6), (4, 2)]

>>> DFSAverager(r).traverse()
{0: [4], 1: [7, 9], 2: [10, 2, 6], 3: [6], 4: [2]}