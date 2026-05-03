# ============================================
# Gaussian Elimination - Solving Linear Systems
# ============================================
# Solves a system of linear equations Ax = b
# using forward elimination + back substitution.

def gaussian_elimination(A, b):
    n = len(b)
    # Augmented matrix [A | b]
    M = [A[i][:] + [b[i]] for i in range(n)]

    print("Augmented Matrix [A|b]:")
    print_matrix(M)

    # Forward Elimination
    for col in range(n):
        # Partial Pivoting
        max_row = max(range(col, n), key=lambda r: abs(M[r][col]))
        M[col], M[max_row] = M[max_row], M[col]

        for row in range(col + 1, n):
            if abs(M[col][col]) < 1e-12:
                print("Zero pivot encountered!")
                return None
            factor = M[row][col] / M[col][col]
            for j in range(col, n + 1):
                M[row][j] -= factor * M[col][j]

    print("\nAfter Forward Elimination:")
    print_matrix(M)

    # Back Substitution
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = M[i][n]
        for j in range(i + 1, n):
            x[i] -= M[i][j] * x[j]
        x[i] /= M[i][i]

    return x

def print_matrix(M):
    for row in M:
        print("  " + "  ".join(f"{val:10.4f}" for val in row))

# --- Main ---
if __name__ == "__main__":
    print("=" * 60)
    print("         GAUSSIAN ELIMINATION")
    print("=" * 60)

    # System:
    # 2x + y - z = 8
    # -3x - y + 2z = -11
    # -2x + y + 2z = -3

    A = [
        [2,  1, -1],
        [-3, -1,  2],
        [-2,  1,  2]
    ]
    b = [8, -11, -3]

    print("System of equations:")
    print("  2x  +  y  -  z =  8")
    print(" -3x  -  y  + 2z = -11")
    print(" -2x  +  y  + 2z = -3")
    print()

    solution = gaussian_elimination(A, b)

    if solution:
        print("\n✅ Solution:")
        for i, val in enumerate(solution):
            print(f"   x{i+1} = {val:.6f}")
