from graphlite import V


def test_find(graph):
    assert list(graph.find(V(1).knows)) == [2, 3, 4]
    assert list(graph.find(V().knows(1))) == [2, 3]


def test_union(graph):
    assert list(graph.find(V(1).knows)
                     .union(V(2).knows)) == [1, 2, 3, 4]


def test_intersection(graph):
    assert list(graph.find(V(1).knows)
                     .intersection(V().knows(1))) == [2, 3]


def test_difference(graph):
    assert list(graph.find(V(1).knows)
                     .difference(V().knows(1))) == [4]


def test_traverse(graph):
    assert list(graph.find(V(1).knows)
                     .traverse(V().knows)) == [1, 1]
    assert list(graph.find(V(1).knows)
                     .traverse(V().knows(1))) == [2, 3]


def test_nested_traverse(graph):
    query = graph.find(V(1).likes)\
                 .traverse(V().knows)\
                 .traverse(V().knows)
    assert query.to(list) == [2, 3, 4]


def test_count(graph):
    assert graph.find(V(1).knows).count() == 3
    assert graph.find(V(1).likes).count() == 2


def test_slice(graph):
    assert len(list(graph.find(V(1).knows)[:1])) == 1
    assert list(graph.find(V(1).knows)[1:]) == [3, 4]


def test_to(graph):
    assert graph.find(V(1).knows).to(list) == [2, 3, 4]
    assert graph.find(V(1).knows).to(set) == set((2, 3, 4))


def test_edge():
    assert not V(1).knows(2) == 3
    assert V(1).knows(2) == V(1).knows(2)
    assert V(1).knows(3) != V(1).knows(2)


def test_hashable():
    assert V(1).knows(2) != 2

    d = {V(1).knows(2): 5}

    assert d[V(1).knows(2)] == 5
    assert V(1).knows(3) not in d
