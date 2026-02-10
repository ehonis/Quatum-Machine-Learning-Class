# q1 - custom gate A

import numpy as np
from qiskit import QuantumCircuit
from qiskit.quantum_info import Operator

# A = (1/sqrt2)(sigma_x + sigma_y)
sqrt2 = np.sqrt(2)
top_right = (1 - 1j) / sqrt2
bottom_left = (1 + 1j) / sqrt2

mat = np.array([[0, top_right], [bottom_left, 0]], dtype=complex)
gate_A = Operator(mat)

qc = QuantumCircuit(1)
qc.append(gate_A, [0])

print("Circuit with custom gate A:")
print(qc.draw(output="text"))

# check unitary
print("\nCircuit unitary :")
print(Operator(qc).data)
