from pricing import calculate_cost

# ----- Black-box tests -----
def test_basic_compute_cost():
    tiers = [0, 50, 1000, 8000]
    costs = [0.62, 0.58, 0.55, 0.52]
    assert calculate_cost("Compute", 100, tiers, costs) == 60.0

def test_zero_usage():
    tiers = [0, 50, 1000, 8000]
    costs = [0.62, 0.58, 0.55, 0.52]
    assert calculate_cost("Compute", 0, tiers, costs) == 0.0

def test_high_usage():
    tiers = [0, 50, 1000, 8000]
    costs = [0.62, 0.58, 0.55, 0.52]
    assert calculate_cost("Compute", 9000, tiers, costs) > 0

# ----- White-box tests -----
def test_tier_boundary():
    tiers = [0, 50, 1000, 8000]
    costs = [0.62, 0.58, 0.55, 0.52]
    # Edge case exactly on boundary
    assert calculate_cost("Compute", 50, tiers, costs) == round(50 * 0.62, 2)

def test_mid_tier_usage():
    tiers = [0, 50, 1000, 8000]
    costs = [0.62, 0.58, 0.55, 0.52]
    assert calculate_cost("Compute", 1050, tiers, costs) > 0
