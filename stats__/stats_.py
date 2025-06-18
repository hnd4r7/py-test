from scipy.stats import norm  # For z-distribution
import numpy as np

# =================================================================
# Part 1: Define Parameters and Sample Data
# =================================================================
# Scenario: A vaccine trial claims 70% effectiveness (p₀ = 0.7).
# In a sample of 200 people, 150 were protected. Does this suggest
# higher effectiveness than claimed?

p_null = 0.7  # Null hypothesis proportion (H₀: p = 0.7)
n = 200  # Sample size
x_successes = 150  # Observed successes
p_hat = x_successes / n  # Sample proportion (150/200 = 0.75)

# =================================================================
# Part 2: Calculate Z-Score (Standard Normal Test Statistic)
# =================================================================
# Standard error under H₀ (uses p_null, not p_hat!)
std_error = np.sqrt(p_null * (1 - p_null) / n)

# Z-score: measures how far p_hat deviates from p_null in SE units
z_statistic = (p_hat - p_null) / std_error
print(f"Sample proportion (p̂): {p_hat:.3f}")
print(f"Z-statistic: {z_statistic:.3f}")

# =================================================================
# Part 3: Hypothesis Test (One-Tailed, Right-Tailed)
# =================================================================
alpha = 0.05  # Significance level
z_critical = norm.ppf(1 - alpha)  # Critical value for right-tailed test

print(f"\nCritical z-value (α=0.05): {z_critical:.3f}")

if z_statistic > z_critical:
    print("Result: Reject H₀ (p < 0.05)")
    print("Evidence suggests vaccine effectiveness > 70%.")
else:
    print("Result: Fail to reject H₀ (p ≥ 0.05)")
    print("No significant evidence of higher effectiveness.")

# Optional: Calculate p-value
p_value = 1 - norm.cdf(z_statistic)
print(f"\nP-value: {p_value:.4f}")
