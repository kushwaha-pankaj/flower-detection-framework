from __future__ import annotations

from math import dist


def nearest_neighbor_route(points: list[tuple[float, float]], start: tuple[float, float] = (0.0, 0.0)) -> list[int]:
    """Return visit order for points using a nearest-neighbor heuristic."""
    remaining = set(range(len(points)))
    route: list[int] = []
    current = start

    while remaining:
        next_idx = min(remaining, key=lambda i: dist(current, points[i]))
        route.append(next_idx)
        current = points[next_idx]
        remaining.remove(next_idx)

    return route
