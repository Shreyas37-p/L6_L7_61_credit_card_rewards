import pytest
from hypothesis import given, strategies as st

from credit_cards_reward import (
    reward_points,
    late_payment_fee,
    card_status,
)


any_value = st.one_of(
    st.none(),
    st.integers(),
    st.floats(allow_nan=True, allow_infinity=True),
    st.text(),
    st.lists(st.integers()),
    st.dictionaries(st.text(), st.integers()),
)


def allow_only_expected_errors(function, *args):
    try:
        return function(*args)
    except ValueError:
        return None
    except Exception as error:
        pytest.fail(
            f"Unexpected {type(error).__name__}: {error}"
        )


@given(any_value, any_value, any_value, any_value)
def test_reward_points_does_not_crash(card, amount, category, weekend):
    result = allow_only_expected_errors(
        reward_points,
        card,
        amount,
        category,
        weekend,
    )

    if result is not None:
        assert result >= 0


@given(any_value, any_value)
def test_late_payment_fee_does_not_crash(balance, days_late):
    result = allow_only_expected_errors(
        late_payment_fee,
        balance,
        days_late,
    )

    if result is not None:
        assert result >= 0


@given(any_value, any_value, any_value)
def test_card_status_does_not_crash(
    utilisation,
    missed_payments,
    frozen,
):
    result = allow_only_expected_errors(
        card_status,
        utilisation,
        missed_payments,
        frozen,
    )

    if result is not None:
        assert result in {
            "frozen",
            "blocked",
            "over limit risk",
            "watch",
            "good",
        }
