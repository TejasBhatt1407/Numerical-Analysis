# ============================================
# Gauss-Seidel Method - Iterative Solver
# ============================================
# Iteratively solves Ax = b.
# Works best when matrix A is diagonally dominant.

def gauss_seidel(A, b, tol=1e-6, max_iter=100):
    n = len(b)
    x = [0.0] * n  # Initial guess: all zeros

    print(f"{'Iter':<6}", end="")
    for i in range(n):
        print(f"{'x' + str(i+1):<15}", end="")
    print()
    print("-" * (6 + 15 * n))

    for iteration in range(1, max_iter + 1):
        x_old = x[:]

        for i in range(n):
            sigma = sum(A[i][j] * x[j] for j in range(n) if j != i)
            x[i] = (b[i] - sigma) / A[i][i]

        print(f"{iteration:<6}", end="")
        for val in x:
            print(f"{val:<15.8f}", end="")
        print()

        # Check convergence
        if all(abs(x[i] - x_old[i]) < tol for i in range(n)):
            print(f"\n✅ Converged after {iteration} iterations")
            return x

    print("\nMax iterations reached without convergence.")
    return x


# --- Main ---
if __name__ == "__main__":
    print("=" * 60)
    print("           GAUSS-SEIDEL METHOD")
    print("=" * 60)

    # Diagonally dominant system:
    # 10x + 2y + z  = 7
    # x + 5y + z    = -8
    # 2x + 3y + 10z = 6

    A = [
        [10, 2,  1],
        [1,  5,  1],
        [2,  3, 10]
    ]
    b = [7, -8, 6]

    print("System:")
    print("  10x + 2y +  z =  7")
    print("   x  + 5y +  z = -8")
    print("   2x + 3y + 10z =  6")
    print()

    solution = gauss_seidel(A, b)

    print("\n✅ Final Solution:")
    for i, val in enumerate(solution):
        print(f"   x{i+1} = {val:.8f}")
