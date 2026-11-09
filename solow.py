import numpy as np


def simulate_solow(
    savings_rate,
    alpha,
    depreciation,
    k0,
    periods
):
    """
    Simulate Solow growth model.

    Returns capital per worker over time.
    """

    k = np.zeros(periods)
    k[0] = k0

    for t in range(periods - 1):
        k[t + 1] = (
            savings_rate * k[t] ** alpha
            + (1 - depreciation) * k[t]
        )

    return k


def steady_state_capital(
    savings_rate,
    alpha,
    depreciation
):
    """
    Analytical steady state.
    """

    return (savings_rate / depreciation) ** (
        1 / (1 - alpha)
    ) 