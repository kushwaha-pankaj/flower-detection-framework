from greenpoll.prioritize.scoring import Target, priority_score


def test_priority_score_penalizes_distance_and_occlusion() -> None:
    near_clear = Target(confidence=0.9, readiness=0.8, distance=1.0, occlusion=0.0)
    far_occluded = Target(confidence=0.9, readiness=0.8, distance=4.0, occlusion=0.5)

    assert priority_score(near_clear) > priority_score(far_occluded)
