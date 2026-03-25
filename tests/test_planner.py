from greenpoll.plan.baselines import nearest_neighbor_route


def test_nearest_neighbor_route_returns_all_points() -> None:
    points = [(2.0, 0.0), (1.0, 0.0), (3.0, 0.0)]
    route = nearest_neighbor_route(points)

    assert sorted(route) == [0, 1, 2]
    assert route[0] == 1
