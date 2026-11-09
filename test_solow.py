from solow import steady_state_capital


def test_steady_state_positive():

    k = steady_state_capital(
        0.2,
        0.3,
        0.05
    )

    assert k > 0


def test_higher_savings_means_more_capital():

    low = steady_state_capital(
        0.1,
        0.3,
        0.05
    )

    high = steady_state_capital(
        0.3,
        0.3,
        0.05
    )

    assert high > low