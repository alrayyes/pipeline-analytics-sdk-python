"""Shared pytest config.

mutmut 3.8.1's runner reads the private ``Item._nodeid``, which pytest 9.2
removed (``nodeid`` is the public name). Alias it until mutmut catches up,
or the mutation job dies in its stats run before mutating anything.
"""

import pytest

if not hasattr(pytest.Item, "_nodeid"):
    pytest.Item._nodeid = property(lambda self: self.nodeid)  # type: ignore[attr-defined,assignment,unused-ignore]
