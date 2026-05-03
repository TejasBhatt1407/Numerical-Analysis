# ============================================
# Jacobi's Iterative Method - Solving Linear Systems
# ============================================
# Solves Ax = b iteratively.
# Unlike Gauss-Seidel, Jacobi uses ONLY values
# from the PREVIOUS iteration to compute each new x.
# Requires the matrix to be diagonally dominant.
# Formula: x_i^(k+1) = (b_i - Σ A_ij * x_j^(k)) / A_ii  (j ≠ i)

def jacobi(A, b, tol=1e-6, max_iter=100):
    n   = len(b)
    x   = [0.0] * n   # Initial guess: all zeros
    x_new = [0.0] * n

    # Check diagonal dominance (optional warning)
    for i in range(n):
        diag = abs(A[i][i])
        off  = sum(abs(A[i][j]) for j in range(n) if j != i)
        if diag <= off:
            print(f"⚠️  Warning: Row {i+1} is NOT diagonally dominant. Method may not converge.")

    print()
    print(f"{'Iter':<6}", end="")
    for i in range(n):
        print(f"{'x' + str(i+1):<18}", end="")
    print(f"{'Max Change':<15}")
    print("-" * (6 + 18 * n + 15))

    for iteration in range(1, max_iter + 1):
        for i in range(n):
            sigma   = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x_new[i] = (b[i] - sigma) / A[i][i]

        max_change = max(abs(x_new[i] - x[i]) for i in range(n))

        print(f"{iteration:<6}", end="")
        for val in x_new:
            print(f"{val:<18.8f}", end="")
        print(f"{max_change:<15.2e}")

        # Check convergence
        if max_change < tol:
            print(f"\n✅ Converged after {iteration} iterations")
            return x_new[:]

        x = x_new[:]   # Update using FULL previous iteration (key difference from Gauss-Seidel)

    print("\nMax iterations reached without convergence.")
    return x


# --- Main ---
if __name__ == "__main__":
    print("=" * 75)
    print("               JACOBI'S ITERATIVE METHOD")
    print("=" * 75)

    # Diagonally dominant system:
    # 10x + 2y + z  = 7
    #  x  + 5y + z  = -8
    #  2x + 3y + 10z = 6

    A = [
        [10, 2,  1],
        [1,  5,  1],
        [2,  3, 10]
    ]
    b = [7, -8, 6]

    print("System of equations:")
    print("  10x +  2y +   z =   7")
    print("   x  +  5y +   z =  -8")
    print("   2x +  3y + 10z =   6")
    print()
    print("Checking diagonal dominance:")

    solution = jacobi(A, b)

    print("\n✅ Final Solution:")
    for i, val in enumerate(solution):
        print(f"   x{i+1} = {val:.8f}")

    print("\n📌 Comparison — Jacobi vs Gauss-Seidel:")
    print("   Jacobi    : uses ALL values from previous iteration → slower convergence")
    print("   Gauss-Seidel: uses updated values immediately         → faster convergence")
