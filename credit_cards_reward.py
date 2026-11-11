POINTS_PER_100 = {
    "classic": 1,
    "gold": 2,
    "platinum": 4
}


def is_number(value):
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def reward_points(card_tier, amount, category, is_weekend):
    if not isinstance(card_tier, str) or card_tier not in POINTS_PER_100:
        raise ValueError("unknown card tier")

    if not is_number(amount) or amount <= 0:
        raise ValueError("invalid amount")

    if not isinstance(category, str):
        raise ValueError("invalid category")

    if not isinstance(is_weekend, bool):
        raise ValueError("invalid weekend flag")

    if category == "fuel":
        return 0

    points = amount // 100 * POINTS_PER_100[card_tier]

    if category == "dining" or category == "travel":
        points = points * 2

    if is_weekend and card_tier != "classic":
        points += 50

    return points


def late_payment_fee(outstanding, days_late):
    if not is_number(outstanding) or not is_number(days_late):
        raise ValueError("invalid payment values")

    if outstanding < 0 or days_late < 0:
        raise ValueError("invalid payment values")

    if days_late <= 0 or outstanding <= 0:
        return 0

    if outstanding <= 1000:
        fee = 100
    elif outstanding <= 10000:
        fee = 500
    else:
        fee = 1000

    if days_late > 30:
        fee += 750

    return fee


def card_status(utilisation_percent, missed_payments, is_frozen):
    if not is_number(utilisation_percent):
        raise ValueError("invalid account values")

    if not is_number(missed_payments):
        raise ValueError("invalid account values")

    if utilisation_percent < 0 or missed_payments < 0:
        raise ValueError("invalid account values")

    if not isinstance(is_frozen, bool):
        raise ValueError("invalid frozen flag")

    if is_frozen:
        return "frozen"

    if missed_payments >= 3:
        return "blocked"

    if utilisation_percent > 90:
        return "over limit risk"

    elif utilisation_percent > 30 or missed_payments > 0:
        return "watch"

    return "good"
