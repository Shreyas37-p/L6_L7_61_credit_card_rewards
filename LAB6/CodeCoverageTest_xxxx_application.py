import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# Test reward points for a valid classic card purchase
def test_reward_points_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


# Test handling of an unknown card tier
def test_reward_points_unknown_card_tier():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("silver", 100, "grocery", False)


# Test handling of an invalid purchase amount
def test_reward_points_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("gold", 0, "grocery", False)


# Test that fuel purchases do not earn reward points
def test_reward_points_fuel():
    assert reward_points("gold", 1000, "fuel", False) == 0


# Test dining rewards for a non-classic card on a weekend
def test_reward_points_dining_weekend():
    assert reward_points("gold", 300, "dining", True) == 62


# Test that no late fee applies when payment is on time
def test_late_payment_fee_paid_on_time():
    assert late_payment_fee(5000, 0) == 0


# Test the fee for an outstanding amount up to 1000
def test_late_payment_fee_small_balance():
    assert late_payment_fee(500, 5) == 100


# Test the fee for a medium balance more than 30 days late
def test_late_payment_fee_medium_balance_late():
    assert late_payment_fee(5000, 31) == 1250


# Test the fee for an outstanding amount above 10000
def test_late_payment_fee_large_balance():
    assert late_payment_fee(20000, 10) == 1000


# Test card status when the card is frozen
def test_card_status_frozen():
    assert card_status(50, 0, True) == "frozen"


# Test card status after three missed payments
def test_card_status_blocked():
    assert card_status(20, 3, False) == "blocked"


# Test card status when utilisation is above 90 percent
def test_card_status_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


# Test card status when utilisation requires monitoring
def test_card_status_watch():
    assert card_status(50, 0, False) == "watch"


# Test card status when there are no warning conditions
def test_card_status_good():
    assert card_status(20, 0, False) == "good"