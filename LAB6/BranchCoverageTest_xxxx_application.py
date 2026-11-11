import pytest
from credit_card_rewards import reward_points, late_payment_fee, card_status


# REWARD POINTS: card tier validation
def test_unknown_card_tier():
    with pytest.raises(ValueError, match="unknown card tier"):
        reward_points("silver", 100, "grocery", False)


# REWARD POINTS: amount validation
def test_invalid_amount():
    with pytest.raises(ValueError, match="invalid amount"):
        reward_points("gold", 0, "grocery", False)


# REWARD POINTS: fuel category returns zero points
def test_fuel_category():
    assert reward_points("gold", 1000, "fuel", False) == 0


# REWARD POINTS: ordinary grocery purchase
def test_classic_grocery():
    assert reward_points("classic", 1000, "grocery", False) == 10


# REWARD POINTS: dining category doubles the points
def test_dining_category():
    assert reward_points("gold", 300, "dining", False) == 12


# REWARD POINTS: travel category doubles the points
def test_travel_category():
    assert reward_points("platinum", 200, "travel", False) == 16


# REWARD POINTS: weekend bonus for a non-classic card
def test_weekend_bonus():
    assert reward_points("gold", 100, "grocery", True) == 52


# REWARD POINTS: classic card gets no weekend bonus
def test_classic_weekend_no_bonus():
    assert reward_points("classic", 100, "grocery", True) == 1


# REWARD POINTS: non-weekend purchase gets no weekend bonus
def test_weekday_no_bonus():
    assert reward_points("gold", 100, "grocery", False) == 2


# LATE PAYMENT FEE: payment is on time
def test_payment_on_time():
    assert late_payment_fee(5000, 0) == 0


# LATE PAYMENT FEE: no outstanding balance
def test_no_outstanding_balance():
    assert late_payment_fee(0, 5) == 0


# LATE PAYMENT FEE: small outstanding balance
def test_small_balance_fee():
    assert late_payment_fee(500, 10) == 100


# LATE PAYMENT FEE: exact lower fee boundary
def test_balance_exactly_1000():
    assert late_payment_fee(1000, 10) == 100


# LATE PAYMENT FEE: medium outstanding balance
def test_medium_balance_fee():
    assert late_payment_fee(5000, 10) == 500


# LATE PAYMENT FEE: just above the lower fee boundary
def test_balance_just_above_1000():
    assert late_payment_fee(1001, 10) == 500


# LATE PAYMENT FEE: exact upper medium-fee boundary
def test_balance_exactly_10000():
    assert late_payment_fee(10000, 10) == 500


# LATE PAYMENT FEE: large outstanding balance
def test_large_balance_fee():
    assert late_payment_fee(20000, 10) == 1000


# LATE PAYMENT FEE: additional fee after more than 30 days
def test_fee_after_30_days():
    assert late_payment_fee(5000, 31) == 1250


# CARD STATUS: frozen card
def test_frozen_card():
    assert card_status(50, 0, True) == "frozen"


# CARD STATUS: three missed payments
def test_blocked_card():
    assert card_status(20, 3, False) == "blocked"


# CARD STATUS: utilisation above 90 percent
def test_over_limit_risk():
    assert card_status(95, 0, False) == "over limit risk"


# CARD STATUS: utilisation triggers watch status
def test_watch_due_to_utilisation():
    assert card_status(50, 0, False) == "watch"


# CARD STATUS: missed payment triggers watch status
def test_watch_due_to_missed_payment():
    assert card_status(20, 1, False) == "watch"


# CARD STATUS: no warning conditions
def test_good_card_status():
    assert card_status(20, 0, False) == "good"