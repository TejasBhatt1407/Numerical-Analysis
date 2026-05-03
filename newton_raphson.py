# ============================================
# Newton-Raphson Method - Root Finding
# ============================================
# Uses the formula: x1 = x0 - f(x0)/f'(x0)
# Requires the function and its derivative.

def f(x):
    return x**3 - x - 2   # f(x)

def df(x):
    return 3*x**2 - 1      # f'(x) — derivative of f(x)

def newton_raphson(x0, tol=1e-6, max_iter=100):
    print(f"{'Iter':<6} {'x':<20} {'f(x)':<20} {'f\\'(x)':<20}")
    print("-" * 70)

    for i in range(1, max_iter + 1):
        fx  = f(x0)
        dfx = df(x0)

        print(f"{i:<6} {x0:<20.10f} {fx:<20.10f} {dfx:<20.10f}")

        if abs(dfx) < 1e-12:
            print("Derivative near zero. Method fails.")
            return None

        x1 = x0 - fx / dfx

        if abs(x1 - x0) < tol:
            print(f"\n✅ Root found: x = {x1:.10f} after {i} iterations")
            return x1

        x0 = x1

    print("Max iterations reached.")
    return x0


# --- Main ---
if __name__ == "__main__":
    x0 = 1.5   # Initial guess
    print("=" * 70)
    print("            NEWTON-RAPHSON METHOD")
    print("=" * 70)
    print(f"Function  : f(x)  = x³ - x - 2")
    print(f"Derivative: f'(x) = 3x² - 1")
    print(f"Initial guess: x0 = {x0}")
    print()
    root = newton_raphson(x0)
