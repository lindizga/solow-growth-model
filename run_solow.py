import pandas as pd
import matplotlib.pyplot as plt

from solow import simulate_solow
from solow import steady_state_capital


rates = [0.1, 0.2, 0.3, 0.4]

results = []

plt.figure(figsize=(8, 6))

for s in rates:

    capital = simulate_solow(
        savings_rate=s,
        alpha=0.3,
        depreciation=0.05,
        k0=1,
        periods=100
    )

    plt.plot(capital, label=f"s={s}")

    results.append(
        {
            "savings_rate": s,
            "steady_state":
                steady_state_capital(
                    s,
                    0.3,
                    0.05
                )
        }
    )

plt.xlabel("Time")
plt.ylabel("Capital per Worker")
plt.title("Solow Growth Model")
plt.legend()

plt.savefig("growth_plot.png")

pd.DataFrame(results).to_csv(
    "steady_state.csv",
    index=False
)

print("Simulation complete.") 