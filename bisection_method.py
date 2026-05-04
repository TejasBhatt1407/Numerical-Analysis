def f(x):
    return x**3 - x - 2  

def bisection(a, b, tol=1e-6, max_iter=100):
    if f(a) * f(b) >= 0:
        print("Bisection method fails. f(a) and f(b) must have opposite signs.")
        return None

    print(f"{'Iter':<6} {'a':<15} {'b':<15} {'c (midpoint)':<18} {'f(c)':<15}")
    print("-" * 70)

    for i in range(1, max_iter + 1):
        c = (a + b) / 2
        fc = f(c)

        print(f"{i:<6} {a:<15.8f} {b:<15.8f} {c:<18.8f} {fc:<15.8f}")

        if abs(fc) < tol or (b - a) / 2 < tol:
            print(f"\n✅ Root found: x = {c:.8f} after {i} iterations")
            return c

        if f(a) * fc < 0:
            b = c
        else:
            a = c

    print("Max iterations reached.")
    return (a + b) / 2


# --- Main ---
if __name__ == "__main__":
    a = 1.0
    b = 2.0
    print("=" * 70)
    print("            BISECTION METHOD")
    print("=" * 70)
    print(f"Function: f(x) = x³ - x - 2")
    print(f"Interval: [{a}, {b}]")
    print()
    root = bisection(a, b)
