import numpy as np

# column vectors
u = np.array([[-2], [-1], [0], [1]])
v = np.array([[1], [2], [3]])

# tensor product (result is column vector)
uv = np.kron(u, v)
vu = np.kron(v, u)

print("u =\n", u)
print("v =\n", v)
print()
print("u ⊗ v =\n", uv)
print("shape:", uv.shape)
print()
print("v ⊗ u =\n", vu)
print("shape:", vu.shape)
