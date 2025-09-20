import numpy as np

def montecarlo_from_hist(ohlc, T=252, n_paths=1000, seed=None):
    """Fit drift and vol from OHLC, simulate Monte Carlo price paths."""
    if seed: np.random.seed(seed)
    log_returns = np.log(ohlc["Close"]).diff().dropna()
    mu, sigma = log_returns.mean(), log_returns.std()

    S0 = ohlc["Close"].iloc[-1]
    dt = 1/252
    paths = np.zeros((T+1, n_paths))
    paths[0] = S0
    for t in range(1, T+1):
        z = np.random.standard_normal(n_paths)
        paths[t] = paths[t-1]*np.exp((mu - 0.5*sigma**2)*dt + sigma*np.sqrt(dt)*z)
    return paths
