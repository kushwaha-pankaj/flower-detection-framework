from dataclasses import dataclass


@dataclass(slots=True)
class Target:
    confidence: float
    readiness: float
    distance: float
    occlusion: float = 0.0


def priority_score(
    target: Target,
    alpha: float = 1.0,
    beta: float = 1.0,
    gamma: float = 0.25,
    delta: float = 0.5,
) -> float:
    """Compute a simple target priority score.

    Higher is better.
    """
    return (
        alpha * target.readiness
        + beta * target.confidence
        - gamma * target.distance
        - delta * target.occlusion
    )
