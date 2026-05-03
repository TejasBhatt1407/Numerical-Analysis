# ============================================
# Regula Falsi Method (False Position)
# ============================================
# Similar to Bisection but uses a weighted midpoint
# (linear interpolation) instead of the simple midpoint.
# Formula: c = a - f(a) * (b - a) / (f(b) - f(a))
# Converges faster than Bisection in most cases.

def f(x):
    return x**3 - x - 2   # Change this function as needed

def regula_falsi(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Regula Falsi fails: f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iter':<6} {'a':<18} {'b':<18} {'c (false pos)':<20} {'f(c)':<15}")
    print("-" * 80)

    c = a  # initialize
    for i in range(1, max_iter + 1):
        fa = f(a)
        fb = f(b)

        # False position formula
        c  = a - fa * (b - a) / (fb - fa)
        fc = f(c)

        print(f"{i:<6} {a:<18.10f} {b:<18.10f} {c:<20.10f} {fc:<15.10f}")

        if abs(fc) < tol:
            print(f"\n✅ Root found: x = {c:.10f} after {i} iterations")
            return c

        if fa * fc < 0:
            b = c
        else:
            a = c

    print(f"\nMax iterations reached. Best estimate: x = {c:.10f}")
    return c


# --- Main ---
if __name__ == "__main__":
    a = 1.0
    b = 2.0

    print("=" * 80)
    print("             REGULA FALSI METHOD (FALSE POSITION)")
    print("=" * 80)
    print(f"Function : f(x) = x³ - x - 2")
    print(f"Interval : [{a}, {b}]")
    print(f"f({a}) = {f(a)},  f({b}) = {f(b)}")
    print()

    root = regula_falsi(a, b)
