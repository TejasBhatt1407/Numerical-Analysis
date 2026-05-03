# ============================================
# Newton's Forward Difference Interpolation
# ============================================
# Used when x-values are equally spaced.
# Formula: P(x) = y0 + s*Δy0 + s(s-1)/2! * Δ²y0 + ...
# where s = (x - x0) / h

def forward_difference_table(y):
    n = len(y)
    table = [y[:]]

    for level in range(1, n):
        prev = table[level - 1]
        curr = [prev[i+1] - prev[i] for i in range(len(prev) - 1)]
        if not curr:
            break
        table.append(curr)

    return table

def print_diff_table(x_points, table):
    n = len(x_points)
    print(f"\n{'x':<10} {'y':<12}", end="")
    for i in range(1, n):
        print(f"{'Δ'*i + 'y':<12}", end="")
    print()
    print("-" * (10 + 12 * (n + 1)))

    for i in range(n):
        print(f"{x_points[i]:<10.4f}", end="")
        for level in range(len(table)):
            if i < len(table[level]):
                print(f"{table[level][i]:<12.6f}", end="")
            else:
                print(f"{'':12}", end="")
        print()

def newton_forward(x_points, y_points, x):
    h = x_points[1] - x_points[0]
    s = (x - x_points[0]) / h
    table = forward_difference_table(y_points)

    print_diff_table(x_points, table)

    result = table[0][0]
    s_term = 1.0
    factorial = 1

    for k in range(1, len(table)):
        s_term   *= (s - (k - 1))
        factorial *= k
        result   += (s_term / factorial) * table[k][0]

    return result


# --- Main ---
if __name__ == "__main__":
    x_points = [1891, 1901, 1911, 1921, 1931]
    y_points = [46,   66,   81,   93,   101]
    x = 1895

    print("=" * 70)
    print("     NEWTON'S FORWARD DIFFERENCE INTERPOLATION")
    print("=" * 70)
    print(f"Data (Population in thousands):")
    for xi, yi in zip(x_points, y_points):
        print(f"  Year {xi}: {yi}")
    print(f"\nInterpolating at x = {x}")

    result = newton_forward(x_points, y_points, x)
    print(f"\n✅ P({x}) ≈ {result:.4f}")
