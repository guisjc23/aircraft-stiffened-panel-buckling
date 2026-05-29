import numpy as np

# ==========================================================
# Simplified Analytical Buckling Calculation
# Aircraft Stiffened Panel
# ==========================================================

# Material Properties (Aluminum 2024-T3)
E = 73000.0      # MPa
nu = 0.33

# Geometry
t = 1.5          # mm (skin thickness)
b = 100.0        # mm (distance between stringers)

# Buckling coefficient
k = 4.0

# ----------------------------------------------------------
# Critical Buckling Stress
# ----------------------------------------------------------

sigma_cr = (
    (k * np.pi**2 * E)
    / (12 * (1 - nu**2))
    * (t / b)**2
)

# ----------------------------------------------------------
# Critical Buckling Load
# ----------------------------------------------------------

A = b * t  # mm²

P_cr = sigma_cr * A  # N
P_cr_kN = P_cr / 1000

# ----------------------------------------------------------
# FEM Results
# ----------------------------------------------------------

P_ref = 10000.0      # N
buckling_factor = 0.287608

P_cr_fem = buckling_factor * P_ref
P_cr_fem_kN = P_cr_fem / 1000

# ----------------------------------------------------------
# Comparison
# ----------------------------------------------------------

difference = (
    (P_cr - P_cr_fem)
    / P_cr_fem
    * 100
)

# ----------------------------------------------------------
# Results
# ----------------------------------------------------------

print("=" * 60)
print("SIMPLIFIED BUCKLING ANALYSIS")
print("=" * 60)

print(f"Young's Modulus (E): {E:.0f} MPa")
print(f"Poisson Ratio (ν): {nu:.2f}")
print(f"Skin Thickness (t): {t:.2f} mm")
print(f"Stringer Spacing (b): {b:.2f} mm")
print()

print(f"Critical Buckling Stress = {sigma_cr:.2f} MPa")
print(f"Critical Buckling Load   = {P_cr_kN:.2f} kN")
print()

print("=" * 60)
print("FEM RESULTS")
print("=" * 60)

print(f"Buckling Factor = {buckling_factor:.6f}")
print(f"Critical Load   = {P_cr_fem_kN:.2f} kN")
print()

print("=" * 60)
print("COMPARISON")
print("=" * 60)

print(f"Difference = {difference:.1f}%")