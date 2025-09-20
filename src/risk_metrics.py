import numpy as np

def value_at_risk(returns, alpha=0.05):
    """Historical VaR at confidence level (e.g., 5%)."""
    return np.percentile(returns, 100*alpha)

def cvar(returns, alpha=0.05):
    """Conditional VaR (Expected Shortfall)."""
    var = value_at_risk(returns, alpha)
    return returns[returns <= var].mean()
