import numpy as np

# Definir o valor das matrizes A e B
A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
B = np.array([[9, 8, 7], [6, 5, 4], [3, 2, 1]])

# 1. A soma das duas matrizes C = A + B
C = A + B
print("Matriz C (A +B):\n", C)

# 2. O produto elemento a elemento D = A * B
D = A * B
print("Matriz D (A * B  elemento a elemento):\n", D)

# 3. Produto matricial E = A x B
E = np.dot(A, B)
print("Matriz E (A * B produto matricial):\n", E)

# 4. A soma de todos os elementos da matriz C.
soma_C = np.sum(C)
print("Soma de todos os elementos de C:", soma_C)

# 5. A transposta da matriz D.
D_transposta = D.T
print("Transposta da matriz D):\n", D_transposta)

# 6. O valor máximo e mínimo da matriz E.
max_E = np.max(E)
min_E = np.min(E)
print("Valor máximo de E:", max_E)
print("Valor mínimo de E:", min_E)

# link do github:
# https://github.com/oEmailou02/atividade-estrmate-py/blob/master/atividade_6_(matriz_com_python).py