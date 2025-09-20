from src.data_loader import get_ohlc
from src.mc_simulator import montecarlo_from_hist
from src.risk_metrics import value_at_risk, cvar
import numpy as np

if __name__ == "__main__":
    tickers = ["NFLX", "DIS"]  # Netflix vs Disney
    for t in tickers:
        ohlc = get_ohlc(t)
        paths = montecarlo_from_hist(ohlc, n_paths=5000)
        sim_returns = (paths[-1] - paths[0]) / paths[0]
        print(f"\n{t} Monte Carlo results:")
        print(f"Mean return: {sim_returns.mean():.4f}")
        print(f"VaR(5%): {value_at_risk(sim_returns):.4f}")
        print(f"CVaR(5%): {cvar(sim_returns):.4f}")
