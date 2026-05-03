# ============================================
# Newton's Backward Difference Interpolation
# ============================================
# Used when x-values are equally spaced AND
# the interpolation point is NEAR THE END of the table.
# Formula: P(x) = y_n + s*∇y_n + s(s+1)/2! * ∇²y_n + ...
# where s = (x - x_n) / h   (s is usually negative or 0 to -1)

def backward_difference_table(y):
    n = len(y)
    table = [y[:]]

    for level in range(1, n):
        prev = table[level - 1]
        curr = [prev[i] - prev[i - 1] for i in range(1, len(prev))]
        if not curr:
            break
        table.append(curr)

    return table

def print_diff_table(x_points, table):
    n = len(x_points)
    print(f"\n{'x':<12} {'y':<12}", end="")
    for i in range(1, n):
        print(f"{'∇'*i + 'y':<12}", end="")
    print()
    print("-" * (12 + 12 * (n + 1)))

    for i in range(n):
        print(f"{x_points[i]:<12.4f}", end="")
        for level in range(len(table)):
            # Backward table: level-th difference for row i is at index (i - level) in table[level]
            idx = i - level
            if 0 <= idx < len(table[level]):
                print(f"{table[level][idx + level] if level == 0 else table[level][i - level]:<12.6f}", end="")
            else:
                print(f"{'':12}", end="")
        print()

def print_backward_table(x_points, table):
    """Print backward difference table cleanly."""
    n = len(x_points)
    header = f"{'x':<12} {'y':<14}"
    for k in range(1, n):
        header += f"{'∇'*k + 'y':<14}"
    print(header)
    print("-" * len(header))

    for i in range(n):
        row = f"{x_points[i]:<12.4f} {table[0][i]:<14.6f}"
        for level in range(1, n):
            # The backward differences for row i: ∇^k y_i = table[level][i - level]
            idx = i - level
            if idx >= 0 and level < len(table) and idx < len(table[level]):
                row += f"{table[level][idx]:<14.6f}"
            else:
                row += f"{'':14}"
        print(row)

def newton_backward(x_points, y_points, x):
    n  = len(x_points)
    h  = x_points[1] - x_points[0]
    xn = x_points[-1]            # Last x value
    s  = (x - xn) / h            # s = (x - x_n) / h

    table = backward_difference_table(y_points)

    print("\nBackward Difference Table:")
    print_backward_table(x_points, table)

    # P(x) = y_n + s*∇y_n + s(s+1)/2! * ∇²y_n + ...
    # Use the LAST row values (rightmost diagonal)
    result   = table[0][-1]   # y_n
    s_term   = 1.0
    factorial = 1

    print(f"\nInterpolation steps (s = {s:.6f}):")
    print(f"  Term 0: y_n = {result:.6f}")

    for k in range(1, len(table)):
        idx = len(table[k]) - 1   # Last element of each level
        if idx < 0:
            break
        s_term   *= (s + (k - 1))
        factorial *= k
        delta_k   = table[k][idx]
        term      = (s_term / factorial) * delta_k
        result   += term
        print(f"  Term {k}: ({s_term:.4f} / {factorial}) × ∇^{k}y_n({delta_k:.6f}) = {term:.6f}")

    return result


# --- Main ---
if __name__ == "__main__":
    # Example: Population data (equally spaced years)
    x_points = [1891, 1901, 1911, 1921, 1931]
    y_points = [46,   66,   81,   93,   101]
    x = 1929   # Near the END of the table → use backward interpolation

    print("=" * 70)
    print("     NEWTON'S BACKWARD DIFFERENCE INTERPOLATION")
    print("=" * 70)
    print(f"Data (Population in thousands):")
    for xi, yi in zip(x_points, y_points):
        print(f"  Year {xi}: {yi}")
    print(f"\nInterpolating at x = {x}")
    print(f"(x is near the END of table → Backward interpolation is appropriate)")

    result = newton_backward(x_points, y_points, x)

    print(f"\n✅ P({x}) ≈ {result:.4f} thousand")

    print("\n" + "=" * 70)
    print("📌 When to use Forward vs Backward Interpolation:")
    print("   Forward  → x is near the BEGINNING of the data table")
    print("   Backward → x is near the END of the data table")
    print("=" * 70)
