from HP23005UNO.equation_solver.linear import gauss_elimination, gauss_jordan, cramer, lu_decomposition, jacobi, gauss_seidel
from HP23005UNO.equation_solver.nonlinear import bisection

Age = [[4, 1], [2, 3]]
bge = [9, 13]

# Ejecutar la eliminación de Gauss
try:
    result = gauss_elimination(Age, bge)
    print("Solución Gauss:", result, "\n")
except ValueError as e:
    print(e)


Agj = [[5, -1], [2, 3]]
bgj = [9, 12]

# Ejecutar Gauss-Jordan
try:
    result = gauss_jordan(Agj, bgj)
    print("Solución Gauss-Jordan:", result, "\n")
except ValueError as e:
    print(e)


Ac = [[2, 3], [1, 2]]
bc = [5, 4]

# Ejecutar la regla de Cramer
try:
    result = cramer(Ac, bc)
    print("Solución Cramer:", result, "\n")
except ValueError as e:
    print(e)


Alu = [[6, 1], [4, 3]]
blu = [15, 18]

# Ejecutar la descomposición LU
try:
    result = lu_decomposition(Alu, blu)
    print("Solución LU:", result, "\n")
except ValueError as e:
    print(e)


Aj = [[7, -2], [3, 5]]
bj = [15, 17]

# Ejecutar el método de Jacobi
try:
    result = jacobi(Aj, bj)
    print("Solución Jacobi:", result, "\n")
except RuntimeError as e:
    print(e)


Ags = [[8, 3], [2, 7]]
bgs = [20, 19]

# Ejecutar el método de Gauss-Seidel
try:
    result = gauss_seidel(Ags, bgs)
    print("Solución Gauss-Seidel:", result, "\n")
except RuntimeError as e:
    print(e)


def f(x):
    return x**3 - x - 2

a = 1
b = 2

# Ejecutar el método de bisección
try:
    result = bisection(f, a, b)
    print("Solución Bisección:", result, "\n")
except ValueError as e:
    print(e)
except RuntimeError as e:
    print(e)
